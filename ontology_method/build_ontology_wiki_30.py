import argparse
import json
import os
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(PROJECT_ROOT))

from build_ontology_layer import build_ontology
from build_llm_wiki import build_entities, read_records, write_raw_layer


DEFAULT_INPUT = PROJECT_ROOT / "outputs" / "30results.json"
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "ontology_wiki_30"
SCHEMA_PATH = SCRIPT_DIR / "ontology_schema.yaml"


ENTITY_PAGE_DIRS = {
    "Paper": "papers",
    "Task": "tasks",
    "Dataset": "datasets",
    "DatasetUse": "dataset_uses",
    "MaterialSystem": "material_systems",
    "TargetProperty": "target_properties",
    "Representation": "representations",
    "Method": "methods",
    "RDStage": "stages",
}


def slug(text: str) -> str:
    text = str(text or "unknown").strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "unknown"


def md_text(value) -> str:
    return str(value or "").replace("\r\n", "\n").strip()


def as_list(value) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    if value in (None, ""):
        return []
    return [str(value)]


def bullet(items: list[str], empty="None") -> str:
    clean = [md_text(item) for item in items if md_text(item)]
    if not clean:
        return empty
    return "\n".join(f"- {item}" for item in clean)


def write_page(path: Path, title: str, sections: list[tuple[str, str]]):
    lines = [f"# {title}", ""]
    for heading, body in sections:
        body = md_text(body)
        if body:
            lines.extend([f"## {heading}", body, ""])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def entity_label(entity: dict) -> str:
    for key in ["canonical_name", "name", "title", "paper_file", "dataset_name"]:
        if entity.get(key):
            return str(entity[key])
    if entity.get("task_description"):
        return str(entity["task_description"])[:90]
    return entity.get("id", "unknown")


def build_page_map(entities: list[dict], pages_dir: Path) -> dict[tuple[str, str], Path]:
    counters = defaultdict(int)
    page_map = {}
    for entity in entities:
        page_dir = ENTITY_PAGE_DIRS.get(entity["type"])
        if not page_dir:
            continue
        base = slug(entity_label(entity) or entity["id"])
        counters[(entity["type"], base)] += 1
        suffix = "" if counters[(entity["type"], base)] == 1 else f"_{counters[(entity['type'], base)]}"
        page_map[(entity["type"], entity["id"])] = pages_dir / page_dir / f"{base}{suffix}.md"
    return page_map


def link_for(entity: dict, page_map: dict[tuple[str, str], Path], current_path: Path) -> str:
    label = entity_label(entity)
    target = page_map.get((entity["type"], entity["id"]))
    if not target:
        return label
    rel = os.path.relpath(target, current_path.parent).replace("\\", "/")
    return f"[{label}]({rel})"


def relation_index(relations: list[dict]):
    outgoing = defaultdict(list)
    incoming = defaultdict(list)
    for rel in relations:
        outgoing[(rel["source_type"], rel["source_id"])].append(rel)
        incoming[(rel["target_type"], rel["target_id"])].append(rel)
    return outgoing, incoming


def targets(entity: dict, relation_name: str, outgoing: dict, entities_by_key: dict) -> list[dict]:
    result = []
    for rel in outgoing.get((entity["type"], entity["id"]), []):
        if rel["relation"] == relation_name:
            target = entities_by_key.get((rel["target_type"], rel["target_id"]))
            if target:
                result.append(target)
    return result


def sources(entity: dict, relation_name: str, incoming: dict, entities_by_key: dict) -> list[dict]:
    result = []
    for rel in incoming.get((entity["type"], entity["id"]), []):
        if rel["relation"] == relation_name:
            source = entities_by_key.get((rel["source_type"], rel["source_id"]))
            if source:
                result.append(source)
    return result


def generic_page(entity: dict, page_path: Path, page_map: dict, outgoing: dict, incoming: dict, entities_by_key: dict):
    props = []
    for key, value in entity.items():
        if key in {"id", "type"}:
            continue
        if isinstance(value, list):
            value = "; ".join(str(item) for item in value)
        props.append(f"{key}: {value}")
    out_lines = []
    for rel in outgoing.get((entity["type"], entity["id"]), []):
        target = entities_by_key.get((rel["target_type"], rel["target_id"]))
        if target:
            out_lines.append(f"{rel['relation']} -> {link_for(target, page_map, page_path)}")
    in_lines = []
    for rel in incoming.get((entity["type"], entity["id"]), []):
        source = entities_by_key.get((rel["source_type"], rel["source_id"]))
        if source:
            in_lines.append(f"{link_for(source, page_map, page_path)} -> {rel['relation']}")
    write_page(
        page_path,
        entity_label(entity),
        [
            ("Ontology Type", entity["type"]),
            ("Properties", bullet(props)),
            ("Outgoing Relations", bullet(out_lines)),
            ("Incoming Relations", bullet(in_lines)),
        ],
    )


def paper_page(entity, page_path, page_map, outgoing, incoming, entities_by_key):
    paper_tasks = targets(entity, "HAS_TASK", outgoing, entities_by_key)
    paper_datasets = targets(entity, "USES_DATASET", outgoing, entities_by_key)
    write_page(
        page_path,
        entity_label(entity),
        [
            ("Ontology Type", "Paper"),
            ("Paper File", entity.get("paper_file", "")),
            ("Tasks", bullet([link_for(item, page_map, page_path) for item in paper_tasks])),
            ("Datasets Used", bullet([link_for(item, page_map, page_path) for item in paper_datasets])),
            ("Metadata", f"paper_id: `{entity.get('id')}`"),
        ],
    )


def task_page(entity, page_path, page_map, outgoing, incoming, entities_by_key):
    use_entities = targets(entity, "HAS_DATASET_USE", outgoing, entities_by_key)
    dataset_entities = []
    for use in use_entities:
        dataset_entities.extend(targets(use, "DESCRIBES_DATASET", outgoing, entities_by_key))
    write_page(
        page_path,
        entity_label(entity),
        [
            ("Ontology Type", "Task"),
            ("Task Description", entity.get("task_description", "")),
            ("Material Systems", bullet([link_for(item, page_map, page_path) for item in targets(entity, "STUDIES_MATERIAL_SYSTEM", outgoing, entities_by_key)])),
            ("Target Properties", bullet([link_for(item, page_map, page_path) for item in targets(entity, "TARGETS_PROPERTY", outgoing, entities_by_key)])),
            ("Representations", bullet([link_for(item, page_map, page_path) for item in targets(entity, "REQUIRES_REPRESENTATION", outgoing, entities_by_key)])),
            ("Methods", bullet([link_for(item, page_map, page_path) for item in targets(entity, "USES_METHOD", outgoing, entities_by_key)])),
            ("Supporting Dataset Uses", bullet([link_for(item, page_map, page_path) for item in use_entities])),
            ("Datasets", bullet([link_for(item, page_map, page_path) for item in dataset_entities])),
            ("Source Papers", bullet([link_for(item, page_map, page_path) for item in sources(entity, "HAS_TASK", incoming, entities_by_key)])),
            ("Metadata", f"task_id: `{entity.get('id')}`\ntags: {'; '.join(as_list(entity.get('task_tags')))}"),
        ],
    )


def dataset_page(entity, page_path, page_map, outgoing, incoming, entities_by_key):
    write_page(
        page_path,
        entity_label(entity),
        [
            ("Ontology Type", "Dataset"),
            ("Aliases", bullet(as_list(entity.get("aliases")))),
            ("Links", bullet(as_list(entity.get("links")))),
            ("Dataset Uses", bullet([link_for(item, page_map, page_path) for item in sources(entity, "DESCRIBES_DATASET", incoming, entities_by_key)])),
            ("Supported Tasks", bullet([link_for(item, page_map, page_path) for item in targets(entity, "SUPPORTS_TASK", outgoing, entities_by_key)])),
            ("Source Papers", bullet([link_for(item, page_map, page_path) for item in sources(entity, "USES_DATASET", incoming, entities_by_key)])),
            ("Metadata", f"dataset_id: `{entity.get('id')}`\ndataset_use_count: {entity.get('dataset_use_count', '')}"),
        ],
    )


def dataset_use_page(entity, page_path, page_map, outgoing, incoming, entities_by_key):
    task_entities = sources(entity, "HAS_DATASET_USE", incoming, entities_by_key)
    paper_entities = []
    for task in task_entities:
        paper_entities.extend(sources(task, "HAS_TASK", incoming, entities_by_key))
    evidence_texts = [item.get("text", "") for item in targets(entity, "SUPPORTED_BY_EVIDENCE", outgoing, entities_by_key)]
    write_page(
        page_path,
        entity_label(entity),
        [
            ("Ontology Type", "DatasetUse"),
            ("Usage Description", entity.get("usage_description", "")),
            ("Dataset", bullet([link_for(item, page_map, page_path) for item in targets(entity, "DESCRIBES_DATASET", outgoing, entities_by_key)])),
            ("Task", bullet([link_for(item, page_map, page_path) for item in task_entities])),
            ("Paper", bullet([link_for(item, page_map, page_path) for item in paper_entities])),
            ("Provided Representations", bullet([link_for(item, page_map, page_path) for item in targets(entity, "PROVIDES_REPRESENTATION", outgoing, entities_by_key)])),
            ("Supported R&D Stages", bullet([link_for(item, page_map, page_path) for item in targets(entity, "SUPPORTS_RD_STAGE", outgoing, entities_by_key)])),
            ("Evidence", bullet(evidence_texts)),
            ("Metadata", f"dataset_use_id: `{entity.get('id')}`\nlink: {entity.get('link', '')}"),
        ],
    )


def create_source_raw(input_path: Path, output_dir: Path) -> Path:
    records = read_records(input_path)
    entities = build_entities(records)
    source_root = output_dir / "_source_llm_wiki"
    (source_root / "raw").mkdir(parents=True, exist_ok=True)
    write_raw_layer(source_root, input_path, entities)
    return source_root / "raw"


def build_ontology_wiki(input_path: Path, output_dir: Path, clean: bool = True):
    if clean and output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    source_raw_dir = create_source_raw(input_path, output_dir)
    entities, relations, summary = build_ontology(source_raw_dir)

    raw_out = output_dir / "raw"
    pages_dir = output_dir / "pages"
    schema_dir = output_dir / "schema"
    raw_out.mkdir(parents=True, exist_ok=True)
    schema_dir.mkdir(parents=True, exist_ok=True)
    for subdir in ENTITY_PAGE_DIRS.values():
        (pages_dir / subdir).mkdir(parents=True, exist_ok=True)

    entities_by_key = {(item["type"], item["id"]): item for item in entities}
    outgoing, incoming = relation_index(relations)
    page_map = build_page_map(entities, pages_dir)

    (raw_out / "ontology_entities.json").write_text(json.dumps(entities, ensure_ascii=False, indent=2), encoding="utf-8")
    (raw_out / "ontology_relations.json").write_text(json.dumps(relations, ensure_ascii=False, indent=2), encoding="utf-8")
    (raw_out / "ontology_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    if SCHEMA_PATH.exists():
        shutil.copy2(SCHEMA_PATH, schema_dir / "ontology_schema.yaml")

    for entity in entities:
        page_path = page_map.get((entity["type"], entity["id"]))
        if not page_path:
            continue
        if entity["type"] == "Paper":
            paper_page(entity, page_path, page_map, outgoing, incoming, entities_by_key)
        elif entity["type"] == "Task":
            task_page(entity, page_path, page_map, outgoing, incoming, entities_by_key)
        elif entity["type"] == "Dataset":
            dataset_page(entity, page_path, page_map, outgoing, incoming, entities_by_key)
        elif entity["type"] == "DatasetUse":
            dataset_use_page(entity, page_path, page_map, outgoing, incoming, entities_by_key)
        else:
            generic_page(entity, page_path, page_map, outgoing, incoming, entities_by_key)

    entity_counts = defaultdict(int)
    for entity in entities:
        entity_counts[entity["type"]] += 1
    write_page(
        pages_dir / "index.md",
        "Ontology Wiki 30",
        [
            ("Purpose", "Ontology-organized LLM Wiki generated from `outputs/30results.json`."),
            ("Source", str(input_path)),
            ("Entity Counts", bullet([f"{name}: {count}" for name, count in sorted(entity_counts.items())])),
            ("Page Directories", bullet([f"{entity_type}: pages/{directory}" for entity_type, directory in ENTITY_PAGE_DIRS.items()])),
            ("Retrieval Use", "Build an index over this folder, then query it with the existing LLM Wiki retrieval chain."),
        ],
    )
    return {"source_json": str(input_path), "output_dir": str(output_dir), **summary}


def parse_args():
    parser = argparse.ArgumentParser(description="Build a 30-paper ontology-organized LLM Wiki without modifying the original wiki.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--no-clean", action="store_true", help="Do not remove the existing output directory before rebuilding.")
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.input.exists():
        raise FileNotFoundError(f"Input JSON not found: {args.input}")
    summary = build_ontology_wiki(args.input, args.output_dir, clean=not args.no_clean)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
