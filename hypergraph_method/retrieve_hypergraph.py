import argparse
import sys
from pathlib import Path

from hypergraph_common import PROJECT_ROOT, infer_nodes, read_json, weighted_coverage, write_json


DEFAULT_GRAPH_DIR = PROJECT_ROOT / "hypergraph_method" / "outputs" / "hypergraph_30"
CORE_NODE_TYPES = {"material_system", "target_property", "data_source_type"}


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def node_type(node: str) -> str:
    return node.split(":", 1)[0]


def core_nodes(query_nodes: set[str]) -> set[str]:
    return {node for node in query_nodes if node_type(node) in CORE_NODE_TYPES}


def edge_core_coverage(edge: dict, query_core_nodes: set[str]) -> set[str]:
    return set(edge["nodes"]) & query_core_nodes


def edge_gain(edge: dict, uncovered_nodes: set[str], selected_datasets: set[str] | None = None) -> tuple[float, set[str]]:
    covered = set(edge["nodes"]) & uncovered_nodes
    if edge.get("edge_type") == "DatasetCapabilityEdge" and edge.get("node_frequencies"):
        use_count = max(1, len(edge.get("dataset_use_edge_ids") or []))
        gain = 0.0
        for node in covered:
            confidence = edge["node_frequencies"].get(node, 1) / use_count
            gain += weighted_coverage([node]) * confidence
    else:
        gain = weighted_coverage(covered)
    if selected_datasets and edge.get("dataset_id") in selected_datasets:
        gain *= 0.35
    return gain, covered


def is_better_edge(edge: dict, gain: float, covered: set[str], best_edge: dict | None, best_gain: float, best_covered: set[str], query_core_nodes: set[str]) -> bool:
    core_covered = edge_core_coverage(edge, query_core_nodes)
    best_core_covered = edge_core_coverage(best_edge, query_core_nodes) if best_edge else set()
    return (
        weighted_coverage(core_covered),
        len(core_covered),
        gain,
        len(covered),
        edge.get("dataset_name", ""),
    ) > (
        weighted_coverage(best_core_covered),
        len(best_core_covered),
        best_gain,
        len(best_covered),
        best_edge.get("dataset_name", "") if best_edge else "",
    )


def greedy_select_edges(
    query_nodes: set[str],
    candidate_edges: list[dict],
    max_edges: int,
    avoid_duplicate_datasets: bool = True,
    query_core_nodes: set[str] | None = None,
) -> tuple[list[dict], set[str]]:
    uncovered = set(query_nodes)
    remaining = {edge["edge_id"]: edge for edge in candidate_edges}
    selected = []
    selected_datasets = set()
    query_core_nodes = query_core_nodes or set()

    while uncovered and len(selected) < max_edges and remaining:
        best_edge = None
        best_gain = 0.0
        best_covered = set()
        for edge in remaining.values():
            gain, covered = edge_gain(edge, uncovered, selected_datasets if avoid_duplicate_datasets else None)
            if is_better_edge(edge, gain, covered, best_edge, best_gain, best_covered, query_core_nodes):
                best_edge = edge
                best_gain = gain
                best_covered = covered

        if best_edge is None or best_gain <= 0:
            break

        selected_item = dict(best_edge)
        selected_item["covered_query_nodes"] = sorted(best_covered)
        selected_item["covered_core_nodes"] = sorted(edge_core_coverage(best_edge, query_core_nodes))
        selected_item["gain"] = best_gain
        selected.append(selected_item)
        uncovered.difference_update(best_covered)
        selected_datasets.add(best_edge.get("dataset_id"))
        remaining.pop(best_edge["edge_id"], None)

    return selected, uncovered


def collect_candidates(query_nodes: set[str], node_to_edges: dict, edges_by_id: dict, edge_type: str) -> list[dict]:
    candidate_ids = set()
    for node in query_nodes:
        candidate_ids.update(node_to_edges.get(node, []))
    candidates = [edges_by_id[edge_id] for edge_id in candidate_ids if edges_by_id[edge_id]["edge_type"] == edge_type]
    if candidates:
        return candidates
    return [edge for edge in edges_by_id.values() if edge["edge_type"] == edge_type]


def filter_by_core_nodes(candidates: list[dict], query_nodes: set[str]) -> list[dict]:
    query_core = core_nodes(query_nodes)
    if not query_core:
        return candidates

    # Material system is the strongest domain constraint. If present, avoid returning
    # datasets that only match generic properties such as band gap or stability.
    material_nodes = {node for node in query_core if node_type(node) == "material_system"}
    strict_core = material_nodes or query_core
    strict = [edge for edge in candidates if edge_core_coverage(edge, strict_core)]
    if strict:
        return strict

    loose = [edge for edge in candidates if edge_core_coverage(edge, query_core)]
    return loose or candidates


def rank_by_weighted_overlap(query_nodes: set[str], edges: list[dict]) -> list[dict]:
    query_core = core_nodes(query_nodes)
    ranked = []
    for edge in edges:
        covered = set(edge["nodes"]) & query_nodes
        if not covered:
            continue
        item = dict(edge)
        item["covered_query_nodes"] = sorted(covered)
        item["covered_core_nodes"] = sorted(edge_core_coverage(edge, query_core))
        item["overlap_score"] = weighted_coverage(covered)
        ranked.append(item)
    ranked.sort(
        key=lambda item: (
            weighted_coverage(item["covered_core_nodes"]),
            len(item["covered_core_nodes"]),
            item["overlap_score"],
            len(item["covered_query_nodes"]),
        ),
        reverse=True,
    )
    return ranked


def retrieve(query: str, graph_dir: Path, max_capability_edges: int, max_use_edges: int) -> dict:
    edges = read_json(graph_dir / "hyperedges.json")
    node_to_edges = read_json(graph_dir / "node_to_edges.json")
    edges_by_id = {edge["edge_id"]: edge for edge in edges}
    query_nodes = infer_nodes(query, include_dataset_family=True)
    query_core = core_nodes(query_nodes)

    capability_candidates = collect_candidates(query_nodes, node_to_edges, edges_by_id, "DatasetCapabilityEdge")
    capability_candidates = filter_by_core_nodes(capability_candidates, query_nodes)
    selected_capabilities, capability_uncovered = greedy_select_edges(
        query_nodes=query_nodes,
        candidate_edges=capability_candidates,
        max_edges=max_capability_edges,
        avoid_duplicate_datasets=True,
        query_core_nodes=query_core,
    )

    candidate_dataset_ids = {edge["dataset_id"] for edge in selected_capabilities}
    use_candidates = collect_candidates(query_nodes, node_to_edges, edges_by_id, "DatasetUseEdge")
    use_candidates = filter_by_core_nodes(use_candidates, query_nodes)
    if candidate_dataset_ids:
        dataset_scoped = [edge for edge in use_candidates if edge["dataset_id"] in candidate_dataset_ids]
        if dataset_scoped:
            use_candidates = dataset_scoped

    selected_uses, use_uncovered = greedy_select_edges(
        query_nodes=query_nodes,
        candidate_edges=use_candidates,
        max_edges=max_use_edges,
        avoid_duplicate_datasets=False,
        query_core_nodes=query_core,
    )

    if not selected_uses:
        selected_uses = rank_by_weighted_overlap(query_nodes, use_candidates)[:max_use_edges]
        use_uncovered = query_nodes - set().union(*(set(edge.get("covered_query_nodes", [])) for edge in selected_uses)) if selected_uses else query_nodes

    return {
        "query": query,
        "query_nodes": sorted(query_nodes),
        "query_core_nodes": sorted(query_core),
        "selected_capability_edges": selected_capabilities,
        "capability_uncovered_nodes": sorted(capability_uncovered),
        "selected_dataset_use_edges": selected_uses,
        "dataset_use_uncovered_nodes": sorted(use_uncovered),
    }


def print_result(result: dict):
    print("Query nodes:")
    for node in result["query_nodes"]:
        print(f"- {node}")
    if result.get("query_core_nodes"):
        print("\nCore query nodes:")
        for node in result["query_core_nodes"]:
            print(f"- {node}")

    print("\nSelected dataset capability edges:")
    for index, edge in enumerate(result["selected_capability_edges"], start=1):
        print(f"{index}. {edge['dataset_name']}  gain={edge.get('gain', edge.get('overlap_score', 0)):.2f}")
        print(f"   covered: {', '.join(edge.get('covered_query_nodes', [])) or 'None'}")
        print(f"   core: {', '.join(edge.get('covered_core_nodes', [])) or 'None'}")
        print(f"   papers: {', '.join(edge.get('paper_files', [])[:5])}")

    print("\nSelected dataset-use evidence edges:")
    for index, edge in enumerate(result["selected_dataset_use_edges"], start=1):
        print(f"{index}. {edge['dataset_name']}  gain={edge.get('gain', edge.get('overlap_score', 0)):.2f}")
        print(f"   paper: {edge.get('paper_file', '')}")
        print(f"   covered: {', '.join(edge.get('covered_query_nodes', [])) or 'None'}")
        print(f"   core: {', '.join(edge.get('covered_core_nodes', [])) or 'None'}")
        print(f"   task: {edge.get('task_description', '')[:240]}")
        print(f"   evidence: {edge.get('usage_description', '')[:300]}")

    if result["dataset_use_uncovered_nodes"]:
        print("\nUncovered query nodes:")
        for node in result["dataset_use_uncovered_nodes"]:
            print(f"- {node}")


def parse_args():
    parser = argparse.ArgumentParser(description="Retrieve materials datasets with ontology-hypergraph greedy coverage.")
    parser.add_argument("query", nargs="+")
    parser.add_argument("--graph-dir", type=Path, default=DEFAULT_GRAPH_DIR)
    parser.add_argument("--max-capability-edges", type=int, default=5)
    parser.add_argument("--max-use-edges", type=int, default=5)
    parser.add_argument("--json-output", type=Path)
    return parser.parse_args()


def main():
    args = parse_args()
    query = " ".join(args.query)
    result = retrieve(query, args.graph_dir, args.max_capability_edges, args.max_use_edges)
    print_result(result)
    if args.json_output:
        write_json(args.json_output, result)


if __name__ == "__main__":
    main()

