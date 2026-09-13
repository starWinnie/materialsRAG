import argparse
from collections import Counter, defaultdict
from pathlib import Path

from hypergraph_common import (
    PROJECT_ROOT,
    find_dataset_families,
    find_values,
    load_entities_from_extraction,
    node_id,
    read_json,
    weighted_coverage,
    write_json,
)


DEFAULT_INPUT = PROJECT_ROOT / "outputs" / "30results.json"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "hypergraph_method" / "outputs" / "hypergraph_30"


def build_dataset_use_edge(use: dict) -> dict:
    dataset_text = " ".join(
        [
            use.get("db_title", ""),
            use.get("original_db_title", ""),
            use.get("db_description", ""),
        ]
    )
    task_text = " ".join(
        [
            use.get("task_description", ""),
            " ".join(use.get("task_tags") or []),
            use.get("db_description", ""),
        ]
    )
    nodes = set()
    for category in ["material_system", "target_property", "data_source_type", "representation"]:
        for value in find_values(dataset_text, category):
            nodes.add(node_id(category, value))
    for category in ["task_type", "rd_stage"]:
        for value in find_values(task_text, category):
            nodes.add(node_id(category, value))
    for value in find_dataset_families(dataset_text):
        nodes.add(node_id("dataset_family", value))
    nodes.add(node_id("dataset_family", use.get("db_title", "")))
    return {
        "edge_id": f"use::{use['dataset_use_id']}",
        "edge_type": "DatasetUseEdge",
        "dataset_use_id": use["dataset_use_id"],
        "dataset_id": use["dataset_id"],
        "dataset_name": use["db_title"],
        "original_dataset_name": use.get("original_db_title", ""),
        "paper_id": use["paper_id"],
        "paper_file": use["paper_file"],
        "task_id": use["task_id"],
        "task_description": use.get("task_description", ""),
        "task_tags": use.get("task_tags") or [],
        "usage_description": use.get("db_description", ""),
        "link": use.get("db_link", ""),
        "nodes": sorted(nodes),
        "coverage_weight": weighted_coverage(nodes),
    }


def build_capability_edges(dataset_use_edges: list[dict], datasets: dict) -> list[dict]:
    by_dataset = defaultdict(list)
    for edge in dataset_use_edges:
        by_dataset[edge["dataset_id"]].append(edge)

    capability_edges = []
    for dataset_id, edges in by_dataset.items():
        dataset = datasets[dataset_id]
        node_counter = Counter()
        for edge in edges:
            node_counter.update(edge["nodes"])
        nodes = set(node_counter)
        nodes.add(node_id("dataset_family", dataset["db_title"]))
        capability_edges.append(
            {
                "edge_id": f"capability::{dataset_id}",
                "edge_type": "DatasetCapabilityEdge",
                "dataset_id": dataset_id,
                "dataset_name": dataset["db_title"],
                "aliases": dataset.get("aliases") or [],
                "links": dataset.get("links") or [],
                "dataset_use_edge_ids": [edge["edge_id"] for edge in edges],
                "paper_files": sorted({edge["paper_file"] for edge in edges}),
                "nodes": sorted(nodes),
                "node_frequencies": dict(sorted(node_counter.items())),
                "coverage_weight": weighted_coverage(nodes),
                "description_examples": dataset.get("description_examples") or [],
            }
        )
    return sorted(capability_edges, key=lambda item: item["dataset_name"].lower())


def build_hypernodes(edges: list[dict]) -> list[dict]:
    counter = Counter()
    edge_types = defaultdict(set)
    for edge in edges:
        for node in edge["nodes"]:
            counter[node] += 1
            edge_types[node].add(edge["edge_type"])

    nodes = []
    for node, count in sorted(counter.items()):
        node_type, value = node.split(":", 1)
        nodes.append(
            {
                "node_id": node,
                "node_type": node_type,
                "value": value,
                "edge_count": count,
                "edge_types": sorted(edge_types[node]),
            }
        )
    return nodes


def build_node_to_edges(edges: list[dict]) -> dict:
    node_to_edges = defaultdict(list)
    for edge in edges:
        for node in edge["nodes"]:
            node_to_edges[node].append(edge["edge_id"])
    return {node: sorted(edge_ids) for node, edge_ids in sorted(node_to_edges.items())}


def build_hypergraph(input_path: Path, output_dir: Path) -> dict:
    entities = load_entities_from_extraction(input_path)
    dataset_use_edges = [
        build_dataset_use_edge(use)
        for use in sorted(entities["dataset_uses"].values(), key=lambda item: (item["paper_file"], item["db_title"]))
    ]
    capability_edges = build_capability_edges(dataset_use_edges, entities["datasets"])
    all_edges = dataset_use_edges + capability_edges
    hypernodes = build_hypernodes(all_edges)
    node_to_edges = build_node_to_edges(all_edges)

    summary = {
        "source_json": str(input_path),
        "paper_count": len(entities["papers"]),
        "task_count": len(entities["tasks"]),
        "dataset_count": len(entities["datasets"]),
        "dataset_use_count": len(entities["dataset_uses"]),
        "hypernode_count": len(hypernodes),
        "hyperedge_count": len(all_edges),
        "dataset_use_edge_count": len(dataset_use_edges),
        "dataset_capability_edge_count": len(capability_edges),
        "node_type_counts": dict(Counter(node["node_type"] for node in hypernodes)),
        "edge_type_counts": dict(Counter(edge["edge_type"] for edge in all_edges)),
    }

    write_json(output_dir / "hypernodes.json", hypernodes)
    write_json(output_dir / "hyperedges.json", all_edges)
    write_json(output_dir / "dataset_use_edges.json", dataset_use_edges)
    write_json(output_dir / "dataset_capability_edges.json", capability_edges)
    write_json(output_dir / "node_to_edges.json", node_to_edges)
    write_json(output_dir / "summary.json", summary)
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description="Build a 30-paper ontology hypergraph for materials dataset recommendation.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main():
    args = parse_args()
    summary = build_hypergraph(args.input, args.output_dir)
    write_json(args.output_dir / "summary.json", summary)
    print(read_json(args.output_dir / "summary.json"))


if __name__ == "__main__":
    main()


