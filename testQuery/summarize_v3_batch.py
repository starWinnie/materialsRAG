"""Summarize V3 traces against paper-used gold, with existing alias rules.

The top-k comparison shares the same updated retrieval trace; it is NOT a
before/after experiment against the old V3 implementation.
"""
import argparse
import ast
import csv
import json
import re
import unicodedata
from pathlib import Path
from typing import Sequence


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("results", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    # Reuse the project's normalization unchanged without loading DOCX/pandas.
    tree = ast.parse((root / "evaluate_llm_dataset_recommendations.py").read_text(encoding="utf-8"))
    names = {"CANONICAL_RULES", "basic_normalize", "canonicalize", "safe_div", "set_metrics"}
    nodes = [n for n in tree.body if getattr(n, "name", None) in names or
             isinstance(n, ast.AnnAssign) and getattr(n.target, "id", None) in names]
    scope = {"re": re, "unicodedata": unicodedata, "Sequence": Sequence}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), "project_alias_rules", "exec"), scope)
    canonicalize, metrics = scope["canonicalize"], scope["set_metrics"]
    datasets = [json.loads(s) for s in (root / "newMethod/newLLMWiki/registry/dataset_registry.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
    labels = {d["dataset_id"]: d["canonical_name"] for d in datasets}
    gold = {}
    for line in (root / "goldres.md").read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*(\d+)\.\s+", line)
        if match:
            number = int(match[1])
            gold[number] = []
        elif line.strip():
            name = line.strip().removeprefix("使用的数据集：").strip()
            if name:
                gold[number].append(name)
    results = json.loads(args.results.read_text(encoding="utf-8"))
    rows = []
    for record in results:
        if record["status"] != "success":
            continue
        trace = json.loads(Path(record["trace_file"]).read_text(encoding="utf-8"))
        for mode, ids in [("evidence_top1", trace["selected_dataset_ids"]),
                          ("same_trace_top6", trace["retrieval_top_k_dataset_ids"][:6])]:
            pred_names = [labels.get(i, i) for i in ids]
            row = {"number": record["number"], "label": record["label"], "mode": mode,
                   "datasets": " | ".join(pred_names), "count": len(ids)}
            row.update(metrics([canonicalize(s) for s in gold[record["number"]]],
                               [canonicalize(s) for s in pred_names]))
            rows.append(row)
        record["datasets"] = [labels.get(i, i) for i in trace["selected_dataset_ids"]]
    summary = {"successful": sum(r["status"] == "success" for r in results),
               "total": len(results), "gold": "goldres.md: paper-used datasets",
               "comparison": "same updated retrieval, different selection; not old V3"}
    for mode in ("evidence_top1", "same_trace_top6"):
        group = [r for r in rows if r["mode"] == mode]
        tp, fp, fn = (sum(r[k] for r in group) for k in ("tp", "fp", "fn"))
        summary[mode] = {"macro_" + k: sum(r[k] for r in group) / len(group) if group else 0 for k in ("precision", "recall", "f1")}
        summary[mode].update({"tp": tp, "fp": fp, "fn": fn,
                             "micro_precision": tp / (tp + fp) if tp + fp else 0,
                             "micro_recall": tp / (tp + fn) if tp + fn else 0,
                             "mean_dataset_count": sum(r["count"] for r in group) / len(group) if group else 0})
    out = args.results.parent
    (out / "named_results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "metrics_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    if rows:
        with (out / "per_query_metrics.csv").open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    lines = ["# V3 13-query results", "", "Gold: paper-used dataset names; not adjudicated task-need gold.",
             "Comparison: same updated retrieval + Top-6, not an old-V3 baseline.", "",
             "| Query | Recommended datasets | P | R | F1 |", "|---|---|---:|---:|---:|"]
    for row in rows:
        if row["mode"] == "evidence_top1":
            lines.append(f"| {row['label']} | {row['datasets'].replace(' | ', '<br>')} | {row['precision']:.3f} | {row['recall']:.3f} | {row['f1']:.3f} |")
    (out / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
