import argparse
import csv
import re
from pathlib import Path

from hypergraph_common import PROJECT_ROOT, canonical_dataset_key, read_json, write_json
from retrieve_hypergraph import DEFAULT_GRAPH_DIR, retrieve


DEFAULT_QUERIES = PROJECT_ROOT / "hypergraph_method" / "outputs" / "heldout_queries.json"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "hypergraph_method" / "outputs" / "heldout_eval"


FAMILY_RULES = [
    (r"materials project|mptraj|mptrj|mpf", "materials_project_family"),
    (r"jarvis", "jarvis_family"),
    (r"oqmd|open quantum materials database", "oqmd_family"),
    (r"matbench", "matbench_family"),
    (r"icsd|inorganic crystal structure database", "icsd_family"),
    (r"qm9", "qm9_family"),
    (r"perovskite|bandgap|band gap|keb|hoip", "perovskite_bandgap_family"),
]


def family_key(name: str) -> str:
    text = str(name or "").lower()
    for pattern, family in FAMILY_RULES:
        if re.search(pattern, text):
            return family
    return canonical_dataset_key(name)


def dataset_names_from_result(result: dict) -> list[str]:
    names = []
    for edge in result.get("selected_capability_edges", []):
        if edge.get("dataset_name") and edge["dataset_name"] not in names:
            names.append(edge["dataset_name"])
    for edge in result.get("selected_dataset_use_edges", []):
        if edge.get("dataset_name") and edge["dataset_name"] not in names:
            names.append(edge["dataset_name"])
    return names


def coverage_ratio(result: dict) -> float:
    query_nodes = set(result.get("query_nodes") or [])
    if not query_nodes:
        return 0.0
    covered = set()
    for edge in result.get("selected_dataset_use_edges", []):
        covered.update(edge.get("covered_query_nodes") or [])
    return len(covered & query_nodes) / len(query_nodes)


def evaluate(queries: list[dict], graph_dir: Path, max_capability_edges: int, max_use_edges: int) -> tuple[list[dict], dict]:
    rows = []
    for item in queries:
        result = retrieve(item["query"], graph_dir, max_capability_edges, max_use_edges)
        recommended = dataset_names_from_result(result)
        truth = item["heldout_dataset"]
        truth_canonical = canonical_dataset_key(truth)
        truth_family = family_key(truth)
        recommended_canonical = [canonical_dataset_key(name) for name in recommended]
        recommended_family = [family_key(name) for name in recommended]
        rows.append(
            {
                "query_id": item["query_id"],
                "paper_file": item["paper_file"],
                "heldout_dataset": truth,
                "recommended_datasets": " | ".join(recommended),
                "query_node_count": len(result.get("query_nodes") or []),
                "coverage_ratio": coverage_ratio(result),
                "strict_hit": int(str(truth).lower() in [str(name).lower() for name in recommended]),
                "canonical_hit": int(truth_canonical in recommended_canonical),
                "family_hit": int(truth_family in recommended_family),
                "query_nodes": " | ".join(result.get("query_nodes") or []),
            }
        )

    summary = {
        "query_count": len(rows),
        "avg_coverage_ratio": sum(row["coverage_ratio"] for row in rows) / max(1, len(rows)),
        "strict_hit_rate": sum(row["strict_hit"] for row in rows) / max(1, len(rows)),
        "canonical_hit_rate": sum(row["canonical_hit"] for row in rows) / max(1, len(rows)),
        "family_hit_rate": sum(row["family_hit"] for row in rows) / max(1, len(rows)),
    }
    return rows, summary


def write_csv(path: Path, rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8-sig")
        return
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate held-out hypergraph retrieval with 30-paper graph.")
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    parser.add_argument("--graph-dir", type=Path, default=DEFAULT_GRAPH_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--max-capability-edges", type=int, default=5)
    parser.add_argument("--max-use-edges", type=int, default=5)
    return parser.parse_args()


def main():
    args = parse_args()
    queries = read_json(args.queries)
    rows, summary = evaluate(queries, args.graph_dir, args.max_capability_edges, args.max_use_edges)
    write_csv(args.output_dir / "heldout_hypergraph_results.csv", rows)
    write_json(args.output_dir / "heldout_hypergraph_summary.json", summary)
    print(summary)


if __name__ == "__main__":
    main()
