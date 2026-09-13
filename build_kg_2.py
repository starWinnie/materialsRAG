import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


DEFAULT_INPUT = Path("outputs/all_results.json")
DEFAULT_OUTPUT_DIR = Path("kg_outputs")


def stable_id(prefix: str, *parts: str) -> str:
    raw = "||".join((part or "").strip().lower() for part in parts)
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]
    return f"{prefix}_{digest}"


def clean_text(value) -> str:
    if value is None:
        return ""
    text = str(value).replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def paper_title_from_file(paper_file: str) -> str:
    title = Path(paper_file).stem
    title = title.replace("_", " ")
    title = re.sub(r"\s+", " ", title)
    return title.strip()


def normalize_link(link: str) -> str:
    link = clean_text(link)
    if not link or link.lower() == "none":
        return "None"
    return link


def canonical_dataset_title(title: str) -> str:
    title = clean_text(title)
    normalized = title.lower()
    normalized = normalized.replace("&", " and ")
    normalized = re.sub(r"[\u2010-\u2015]", "-", normalized)
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    normalized = re.sub(r"\bthe\b", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()

    if re.fullmatch(r"qm9", normalized):
        return "QM9"
    if re.fullmatch(r"matbench(?: v0 1)?", normalized):
        return "Matbench"
    if re.fullmatch(r"matbench dielectric(?: task)?", normalized):
        return "matbench_dielectric"
    if re.fullmatch(r"computational 2d materials database c2db|c2db computational 2d materials database|c2db", normalized):
        return "C2DB"
    if re.fullmatch(r"wang botti marques wbm dataset|wang botti marques dataset|wbm dataset", normalized):
        return "Wang-Botti-Marques (WBM) dataset"
    if re.fullmatch(r"hybrid organic inorganic perovskite hoip dataset|hybrid organic inorganic perovskite dataset|hoip dataset|hoip dataset hybrid organic inorganic perovskite dataset", normalized):
        return "HOIP Dataset"
    if re.fullmatch(r"jarvis dft(?: dataset)?(?: 3d 2021| 2021 8 18)?|jarvis dft 3d 2021", normalized):
        return "JARVIS-DFT"
    if re.fullmatch(r"jarvis 3d", normalized):
        return "JARVIS-DFT"

    known_aliases = [
        (
            "Materials Project",
            [
                "materials project",
                "materials project database",
                "materials project dataset",
                "materials project mp",
                "materials project mp database",
                "materials project mp dataset",
                "materials project mp 2018 6 1",
                "materials project 2018 6 1",
                "materials project 2021 snapshot",
                "materials project mp 2022 10 28",
                "materials project mp v 2022 10 28",
                "materials project mp 2023 6 23",
                "materials project mp database 2023 6 23",
                "materials project megnet",
                "materials project 2021",
                "materials project 2021 mp21",
                "materials project mp21",
            ],
        ),
        (
            "Open Quantum Materials Database",
            [
                "oqmd",
                "oqmd exp",
                "open quantum materials database",
                "open quantum materials database oqmd",
                "oqmd open quantum materials database",
                "open quantum materials database oqmd 2021 snapshot",
            ],
        ),
        (
            "Inorganic Crystal Structure Database",
            [
                "icsd",
                "icsd inorganic crystal structure database",
                "inorganic crystal structure database",
                "inorganic crystal structure database icsd",
                "icsd database",
            ],
        ),
        (
            "JARVIS Database",
            [
                "jarvis",
                "jarvis database",
                "jarvis dataset",
                "jarvis tools datasets",
                "joint automated repository for various integrated simulations",
                "jarvis joint automated repository for various integrated simulations",
                "joint automated repository for various integrated simulations jarvis",
            ],
        ),
    ]

    for canonical, aliases in known_aliases:
        if normalized in aliases:
            return canonical

    title = re.sub(r"^\s*the\s+", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def dataset_key(title: str, link: str) -> tuple[str, str]:
    normalized_title = canonical_dataset_title(title).lower()
    return normalized_title, ""


def add_node(nodes: dict, node_id: str, label: str, **properties):
    if node_id not in nodes:
        nodes[node_id] = {
            "id": node_id,
            "label": label,
            **{key: clean_text(value) for key, value in properties.items()},
        }
        return

    # Keep the first non-empty value, but fill missing properties if later records have them.
    for key, value in properties.items():
        value = clean_text(value)
        if key == "aliases":
            current = {item.strip() for item in nodes[node_id].get(key, "").split(";") if item.strip()}
            incoming = {item.strip() for item in value.split(";") if item.strip()}
            nodes[node_id][key] = "; ".join(sorted(current | incoming))
            continue
        if value and not nodes[node_id].get(key):
            nodes[node_id][key] = value


def add_edge(edges: dict, source: str, target: str, relation: str, **properties):
    edge_id = stable_id("edge", source, relation, target)
    if edge_id not in edges:
        edges[edge_id] = {
            "id": edge_id,
            "source": source,
            "target": target,
            "relation": relation,
            **{key: clean_text(value) for key, value in properties.items()},
        }


def build_graph(records: list[dict]) -> tuple[dict, dict]:
    nodes = {}
    edges = {}
    dataset_ids = {}

    for paper_index, paper_record in enumerate(records, start=1):
        paper_file = clean_text(paper_record.get("paper_file"))
        if not paper_file:
            continue

        paper_id = stable_id("paper", paper_file)
        add_node(
            nodes,
            paper_id,
            "Paper",
            paper_file=paper_file,
            title=paper_title_from_file(paper_file),
        )

        tasks = paper_record.get("result", [])
        if not isinstance(tasks, list):
            continue

        for task_index, task in enumerate(tasks, start=1):
            if not isinstance(task, dict):
                continue

            task_description = clean_text(task.get("task_description"))
            if not task_description:
                continue

            task_id = stable_id("task", paper_file, str(task_index), task_description)
            task_tags = task.get("task_tags", [])
            if not isinstance(task_tags, list):
                task_tags = []

            add_node(
                nodes,
                task_id,
                "Task",
                task_description=task_description,
                task_tags="; ".join(clean_text(tag) for tag in task_tags if clean_text(tag)),
                paper_file=paper_file,
            )
            add_edge(edges, paper_id, task_id, "HAS_TASK")

            for tag in task_tags:
                tag_name = clean_text(tag)
                if not tag_name:
                    continue

                tag_id = stable_id("tag", tag_name)
                add_node(nodes, tag_id, "Tag", name=tag_name)
                add_edge(edges, task_id, tag_id, "HAS_TAG")

            datasets = task.get("datasets", [])
            if not isinstance(datasets, list):
                continue

            for dataset in datasets:
                if not isinstance(dataset, dict):
                    continue

                db_title = clean_text(dataset.get("db_title"))
                if not db_title:
                    continue

                db_link = normalize_link(dataset.get("db_link"))
                db_description = clean_text(dataset.get("db_description"))
                canonical_title = canonical_dataset_title(db_title)

                key = dataset_key(db_title, db_link)
                if key not in dataset_ids:
                    dataset_ids[key] = stable_id("dataset", canonical_title, key[1])

                dataset_id = dataset_ids[key]
                add_node(
                    nodes,
                    dataset_id,
                    "Dataset",
                    db_title=canonical_title,
                    db_description=db_description,
                    db_link=db_link,
                    aliases=db_title,
                )
                add_edge(edges, task_id, dataset_id, "USES_DATASET")
                add_edge(edges, paper_id, dataset_id, "PAPER_USES_DATASET")

    return nodes, edges


def write_csv(path: Path, rows: list[dict], preferred_fields: list[str]):
    fieldnames = list(preferred_fields)
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)

    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(nodes: dict, edges: dict, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)

    node_rows = list(nodes.values())
    edge_rows = list(edges.values())

    write_csv(
        output_dir / "kg_nodes.csv",
        node_rows,
        ["id", "label", "title", "paper_file", "task_description", "task_tags", "db_title", "db_description", "db_link", "aliases", "name"],
    )
    write_csv(
        output_dir / "kg_edges.csv",
        edge_rows,
        ["id", "source", "target", "relation"],
    )

    graph = {
        "nodes": node_rows,
        "edges": edge_rows,
    }
    with (output_dir / "kg_graph.json").open("w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)


def parse_args():
    parser = argparse.ArgumentParser(description="Build a paper-task-dataset knowledge graph from all_results.json.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Path to all_results.json.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directory for graph outputs.")
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.input.exists():
        raise FileNotFoundError(f"Input JSON not found: {args.input}")

    with args.input.open("r", encoding="utf-8") as f:
        records = json.load(f)

    if not isinstance(records, list):
        raise ValueError("Input JSON must be a list of paper records.")

    nodes, edges = build_graph(records)
    write_outputs(nodes, edges, args.output_dir)

    label_counts = {}
    relation_counts = {}
    for node in nodes.values():
        label_counts[node["label"]] = label_counts.get(node["label"], 0) + 1
    for edge in edges.values():
        relation_counts[edge["relation"]] = relation_counts.get(edge["relation"], 0) + 1

    print(f"Knowledge graph built from: {args.input}")
    print(f"Output directory: {args.output_dir}")
    print(f"Nodes: {len(nodes)} {label_counts}")
    print(f"Edges: {len(edges)} {relation_counts}")
    print(f"CSV nodes: {args.output_dir / 'kg_nodes.csv'}")
    print(f"CSV edges: {args.output_dir / 'kg_edges.csv'}")
    print(f"JSON graph: {args.output_dir / 'kg_graph.json'}")


if __name__ == "__main__":
    main()
