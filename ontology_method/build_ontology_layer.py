import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WIKI_RAW_DIR = PROJECT_ROOT / "llm_wiki_all" / "raw"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


PROPERTY_PATTERNS = {
    "band gap": [r"band\s*gap", r"bandgap"],
    "formation energy": [r"formation\s+energy"],
    "energy above hull": [r"energy\s+above\s+hull", r"ehull", r"hull\s+distance"],
    "total energy": [r"total\s+energy"],
    "bulk modulus": [r"bulk\s+modulus"],
    "shear modulus": [r"shear\s+modulus"],
    "young's modulus": [r"young'?s\s+modulus"],
    "dielectric property": [r"dielectric", r"refractive\s+index"],
    "adsorption energy": [r"adsorption\s+energy"],
    "conductivity": [r"conductivity", r"ionic\s+conduct"],
    "stability": [r"stability", r"stable", r"thermodynamic"],
    "synthesis condition": [r"synthesis", r"reaction\s+condition"],
}

MATERIAL_PATTERNS = {
    "perovskite": [r"perovskite", r"abx\s*3"],
    "inorganic crystal": [r"inorganic", r"crystalline", r"crystal\s+structure"],
    "2D material": [r"2d\s+material", r"layered"],
    "catalyst": [r"catalyst", r"catalytic", r"catalysis"],
    "battery material": [r"battery", r"electrode", r"electrolyte"],
    "alloy": [r"alloy"],
    "organic material": [r"organic"],
    "hybrid material": [r"hybrid"],
    "MOF": [r"metal[- ]organic\s+framework", r"\bmof\b"],
}

REPRESENTATION_PATTERNS = {
    "composition": [r"composition", r"chemical\s+formula", r"stoichiometry"],
    "crystal structure": [r"crystal\s+structure", r"structure"],
    "atomic coordinates": [r"atomic\s+coordinates", r"fractional\s+coordinates", r"cartesian\s+coordinates"],
    "lattice vectors": [r"lattice\s+vectors", r"lattice\s+parameters"],
    "crystal graph": [r"crystal\s+graph", r"graph"],
    "space group": [r"space\s+group"],
    "CIF": [r"\bcif\b"],
    "SMILES": [r"smiles", r"selfies"],
    "descriptor": [r"descriptor", r"feature", r"featur"],
    "spectrum or tensor": [r"spectrum", r"spectra", r"tensor"],
}

METHOD_PATTERNS = {
    "DFT": [r"\bdft\b", r"density\s+functional"],
    "machine learning": [r"machine\s+learning", r"\bml\b"],
    "graph neural network": [r"graph\s+neural", r"\bgnn\b"],
    "transformer": [r"transformer"],
    "equivariant neural network": [r"equivariant", r"equivariance"],
    "benchmarking": [r"benchmark", r"baseline"],
    "high-throughput screening": [r"high[- ]throughput", r"screening"],
}

STAGE_PATTERNS = {
    "Problem Definition": [r"problem\s+definition"],
    "Candidate Space Construction": [r"candidate\s+space", r"hypothetical"],
    "Dataset Selection": [r"dataset", r"database", r"benchmark"],
    "Representation / Feature Construction": [r"representation", r"feature", r"descriptor", r"graph"],
    "Model Training": [r"train", r"training"],
    "Screening / Prediction": [r"predict", r"prediction", r"screening"],
    "Validation": [r"validation", r"validate", r"experimental"],
    "Optimization / Iteration": [r"optimization", r"iteration"],
    "Benchmarking / Evaluation": [r"benchmark", r"evaluation", r"compare"],
}


def slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return value or "unknown"


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def find_terms(text: str, patterns: dict[str, list[str]]) -> list[str]:
    text = text or ""
    found = []
    for name, exprs in patterns.items():
        if any(re.search(expr, text, flags=re.IGNORECASE) for expr in exprs):
            found.append(name)
    return found


def add_entity(store: dict, entity_type: str, entity_id: str, **props):
    key = f"{entity_type}:{entity_id}"
    if key not in store:
        store[key] = {"id": entity_id, "type": entity_type}
    for name, value in props.items():
        if value in (None, ""):
            continue
        if isinstance(value, list):
            old = store[key].setdefault(name, [])
            for item in value:
                if item not in old:
                    old.append(item)
        else:
            store[key][name] = value
    return key


def add_relation(relations: list[dict], source_type: str, source_id: str, relation: str, target_type: str, target_id: str, **props):
    item = {
        "source_type": source_type,
        "source_id": source_id,
        "relation": relation,
        "target_type": target_type,
        "target_id": target_id,
    }
    item.update({k: v for k, v in props.items() if v not in (None, "")})
    if item not in relations:
        relations.append(item)


def build_ontology(raw_dir: Path):
    papers = read_csv(raw_dir / "papers.csv")
    tasks = read_csv(raw_dir / "tasks.csv")
    datasets = read_csv(raw_dir / "datasets.csv")
    dataset_uses = read_csv(raw_dir / "dataset_uses.csv")

    entities = {}
    relations = []
    task_by_id = {row.get("task_id"): row for row in tasks}

    for paper in papers:
        paper_id = paper.get("paper_id")
        if paper_id:
            add_entity(entities, "Paper", paper_id, paper_file=paper.get("paper_file"), title=paper.get("title"))

    for dataset in datasets:
        dataset_id = dataset.get("dataset_id")
        aliases = [x.strip() for x in (dataset.get("aliases") or "").split(";") if x.strip()]
        links = [x.strip() for x in (dataset.get("links") or "").split(";") if x.strip()]
        if dataset_id:
            add_entity(
                entities,
                "Dataset",
                dataset_id,
                canonical_name=dataset.get("db_title"),
                aliases=aliases,
                links=links,
                paper_count=dataset.get("paper_count"),
                task_count=dataset.get("task_count"),
                dataset_use_count=dataset.get("dataset_use_count"),
            )

    for task in tasks:
        task_id = task.get("task_id")
        paper_id = task.get("paper_id")
        text = " ".join([task.get("task_description") or "", task.get("task_tags") or ""])
        properties = find_terms(text, PROPERTY_PATTERNS)
        materials = find_terms(text, MATERIAL_PATTERNS)
        representations = find_terms(text, REPRESENTATION_PATTERNS)
        methods = find_terms(text, METHOD_PATTERNS)

        if not task_id:
            continue

        add_entity(
            entities,
            "Task",
            task_id,
            paper_id=paper_id,
            paper_file=task.get("paper_file"),
            task_description=task.get("task_description"),
            task_tags=[x.strip() for x in (task.get("task_tags") or "").split(";") if x.strip()],
            target_properties=properties,
            material_systems=materials,
            representations=representations,
            methods=methods,
        )
        if paper_id:
            add_relation(relations, "Paper", paper_id, "HAS_TASK", "Task", task_id)

        for name in properties:
            prop_id = slug(name)
            add_entity(entities, "TargetProperty", prop_id, name=name)
            add_relation(relations, "Task", task_id, "TARGETS_PROPERTY", "TargetProperty", prop_id)
        for name in materials:
            material_id = slug(name)
            add_entity(entities, "MaterialSystem", material_id, name=name)
            add_relation(relations, "Task", task_id, "STUDIES_MATERIAL_SYSTEM", "MaterialSystem", material_id)
        for name in representations:
            rep_id = slug(name)
            add_entity(entities, "Representation", rep_id, name=name)
            add_relation(relations, "Task", task_id, "REQUIRES_REPRESENTATION", "Representation", rep_id)
        for name in methods:
            method_id = slug(name)
            add_entity(entities, "Method", method_id, name=name)
            add_relation(relations, "Task", task_id, "USES_METHOD", "Method", method_id)

    for use in dataset_uses:
        use_id = use.get("dataset_use_id")
        paper_id = use.get("paper_id")
        task_id = use.get("task_id")
        dataset_id = use.get("dataset_id")
        text = " ".join([use.get("db_title") or "", use.get("db_description") or "", task_by_id.get(task_id, {}).get("task_description") or ""])
        representations = find_terms(text, REPRESENTATION_PATTERNS)
        stages = find_terms(text, STAGE_PATTERNS)

        if not use_id:
            continue
        add_entity(
            entities,
            "DatasetUse",
            use_id,
            paper_id=paper_id,
            task_id=task_id,
            dataset_id=dataset_id,
            dataset_name=use.get("db_title"),
            usage_description=use.get("db_description"),
            link=use.get("db_link"),
            representations=representations,
            rd_stages=stages,
        )
        add_entity(
            entities,
            "Evidence",
            f"evidence_{use_id}",
            source_type="DatasetUse",
            source_id=use_id,
            text=use.get("db_description"),
        )

        if paper_id and dataset_id:
            add_relation(relations, "Paper", paper_id, "USES_DATASET", "Dataset", dataset_id)
        if task_id:
            add_relation(relations, "Task", task_id, "HAS_DATASET_USE", "DatasetUse", use_id)
        if dataset_id:
            add_relation(relations, "DatasetUse", use_id, "DESCRIBES_DATASET", "Dataset", dataset_id)
        if dataset_id and task_id:
            add_relation(relations, "Dataset", dataset_id, "SUPPORTS_TASK", "Task", task_id)
        add_relation(relations, "DatasetUse", use_id, "SUPPORTED_BY_EVIDENCE", "Evidence", f"evidence_{use_id}")

        for name in representations:
            rep_id = slug(name)
            add_entity(entities, "Representation", rep_id, name=name)
            add_relation(relations, "DatasetUse", use_id, "PROVIDES_REPRESENTATION", "Representation", rep_id)
        for name in stages:
            stage_id = slug(name)
            add_entity(entities, "RDStage", stage_id, name=name)
            add_relation(relations, "DatasetUse", use_id, "SUPPORTS_RD_STAGE", "RDStage", stage_id)

    summary = defaultdict(int)
    for entity in entities.values():
        summary[entity["type"]] += 1
    relation_summary = defaultdict(int)
    for rel in relations:
        relation_summary[rel["relation"]] += 1

    return list(entities.values()), relations, {
        "entity_counts": dict(sorted(summary.items())),
        "relation_counts": dict(sorted(relation_summary.items())),
        "source_raw_dir": str(raw_dir),
    }


def parse_args():
    parser = argparse.ArgumentParser(description="Build an ontology layer from the existing LLM Wiki raw tables.")
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_WIKI_RAW_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main():
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    entities, relations, summary = build_ontology(args.raw_dir)

    (args.output_dir / "ontology_entities.json").write_text(json.dumps(entities, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output_dir / "ontology_relations.json").write_text(json.dumps(relations, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output_dir / "ontology_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
