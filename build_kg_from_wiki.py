import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


DEFAULT_WIKI_DIR = Path("llm_wiki")
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


def read_csv_rows(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def split_semicolon(value: str) -> list[str]:
    return [item.strip() for item in clean_text(value).split(";") if item.strip()]


def add_node(nodes: dict, node_id: str, label: str, **properties):
    if not node_id:
        return
    if node_id not in nodes:
        nodes[node_id] = {
            "id": node_id,
            "label": label,
            **{key: clean_text(value) for key, value in properties.items()},
        }
        return

    for key, value in properties.items():
        value = clean_text(value)
        if value and not nodes[node_id].get(key):
            nodes[node_id][key] = value


def add_edge(edges: dict, source: str, target: str, relation: str, **properties):
    if not source or not target:
        return
    edge_id = stable_id("edge", source, relation, target)
    if edge_id not in edges:
        edges[edge_id] = {
            "id": edge_id,
            "source": source,
            "target": target,
            "relation": relation,
            **{key: clean_text(value) for key, value in properties.items()},
        }


def build_graph_from_wiki(wiki_dir: Path) -> tuple[dict, dict]:
    raw_dir = wiki_dir / "raw"
    required = ["papers.csv", "tasks.csv", "datasets.csv", "dataset_uses.csv"]
    missing = [name for name in required if not (raw_dir / name).exists()]
    if missing:
        raise FileNotFoundError(f"Missing LLM Wiki raw files in {raw_dir}: {', '.join(missing)}")

    papers = read_csv_rows(raw_dir / "papers.csv")
    tasks = read_csv_rows(raw_dir / "tasks.csv")
    datasets = read_csv_rows(raw_dir / "datasets.csv")
    dataset_uses = read_csv_rows(raw_dir / "dataset_uses.csv")

    nodes = {}
    edges = {}

    for paper in papers:
        paper_id = clean_text(paper.get("paper_id"))
        add_node(
            nodes,
            paper_id,
            "Paper",
            paper_file=paper.get("paper_file", ""),
            title=paper.get("title", ""),
            task_count=paper.get("task_count", ""),
            dataset_count=paper.get("dataset_count", ""),
        )

    for task in tasks:
        task_id = clean_text(task.get("task_id"))
        paper_id = clean_text(task.get("paper_id"))
        add_node(
            nodes,
            task_id,
            "Task",
            task_description=task.get("task_description", ""),
            task_tags=task.get("task_tags", ""),
            paper_file=task.get("paper_file", ""),
            task_index=task.get("task_index", ""),
        )
        add_edge(edges, paper_id, task_id, "HAS_TASK")

        for tag_name in split_semicolon(task.get("task_tags", "")):
            tag_id = stable_id("tag", tag_name)
            add_node(nodes, tag_id, "Tag", name=tag_name)
            add_edge(edges, task_id, tag_id, "HAS_TAG")

    for dataset in datasets:
        dataset_id = clean_text(dataset.get("dataset_id"))
        add_node(
            nodes,
            dataset_id,
            "Dataset",
            db_title=dataset.get("db_title", ""),
            aliases=dataset.get("aliases", ""),
            db_link=dataset.get("links", ""),
            paper_count=dataset.get("paper_count", ""),
            task_count=dataset.get("task_count", ""),
            dataset_use_count=dataset.get("dataset_use_count", ""),
        )

    for dataset_use in dataset_uses:
        dataset_use_id = clean_text(dataset_use.get("dataset_use_id"))
        paper_id = clean_text(dataset_use.get("paper_id"))
        task_id = clean_text(dataset_use.get("task_id"))
        dataset_id = clean_text(dataset_use.get("dataset_id"))

        add_node(
            nodes,
            dataset_use_id,
            "DatasetUse",
            paper_file=dataset_use.get("paper_file", ""),
            db_title=dataset_use.get("db_title", ""),
            original_db_title=dataset_use.get("original_db_title", ""),
            db_description=dataset_use.get("db_description", ""),
            db_link=dataset_use.get("db_link", ""),
        )
        add_edge(edges, task_id, dataset_use_id, "HAS_DATASET_USE")
        add_edge(edges, dataset_use_id, dataset_id, "DESCRIBES_DATASET")
        add_edge(edges, task_id, dataset_id, "USES_DATASET")
        add_edge(edges, paper_id, dataset_id, "PAPER_USES_DATASET")
        add_edge(edges, paper_id, dataset_use_id, "HAS_DATASET_USE")

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
        [
            "id",
            "label",
            "title",
            "paper_file",
            "task_description",
            "task_tags",
            "db_title",
            "db_description",
            "db_link",
            "aliases",
            "name",
            "original_db_title",
            "task_count",
            "dataset_count",
            "paper_count",
            "dataset_use_count",
        ],
    )
    write_csv(output_dir / "kg_edges.csv", edge_rows, ["id", "source", "target", "relation"])

    with (output_dir / "kg_graph.json").open("w", encoding="utf-8") as f:
        json.dump({"nodes": node_rows, "edges": edge_rows}, f, ensure_ascii=False, indent=2)


def parse_args():
    parser = argparse.ArgumentParser(description="Build a knowledge graph from the standard LLM Wiki raw layer.")
    parser.add_argument("--wiki-dir", type=Path, default=DEFAULT_WIKI_DIR, help="Path to the generated llm_wiki directory.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directory for graph outputs.")
    return parser.parse_args()


def main():
    args = parse_args()
    nodes, edges = build_graph_from_wiki(args.wiki_dir)
    write_outputs(nodes, edges, args.output_dir)

    label_counts = {}
    relation_counts = {}
    for node in nodes.values():
        label_counts[node["label"]] = label_counts.get(node["label"], 0) + 1
    for edge in edges.values():
        relation_counts[edge["relation"]] = relation_counts.get(edge["relation"], 0) + 1

    print(f"Knowledge graph built from: {args.wiki_dir / 'raw'}")
    print("Source type: llm_wiki_raw")
    print(f"Output directory: {args.output_dir}")
    print(f"Nodes: {len(nodes)} {label_counts}")
    print(f"Edges: {len(edges)} {relation_counts}")
    print(f"CSV nodes: {args.output_dir / 'kg_nodes.csv'}")
    print(f"CSV edges: {args.output_dir / 'kg_edges.csv'}")
    print(f"JSON graph: {args.output_dir / 'kg_graph.json'}")


if __name__ == "__main__":
    main()
