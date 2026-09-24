"""Audit batch JSON with explicit provenance and existing project name rules.

Does not read generated prose, change gold, or merge subsets beyond the existing
canonical/family evaluator. Failed runs are rejected instead of scored as empty.
"""
import argparse
import ast
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[1]


def rules():
    names = {"CANONICAL_RULES", "FAMILY_MAP", "basic_normalize", "canonicalize",
             "family_name", "transform_names", "deduplicate_keep_order", "safe_div", "set_metrics", "recall_at_k"}
    tree = ast.parse((ROOT / "evaluate_llm_dataset_recommendations.py").read_text(encoding="utf-8"))
    nodes = [n for n in tree.body if getattr(n, "name", None) in names or
             isinstance(n, ast.AnnAssign) and getattr(n.target, "id", None) in names]
    scope = dict(re=re, unicodedata=unicodedata, Sequence=Sequence, Iterable=Iterable)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), "existing_project_rules", "exec"), scope)
    return scope


def evaluate(results, gold_path, prediction_field="selected"):
    scope = rules()
    records = json.loads(results.read_text(encoding="utf-8"))
    gold = {}
    for line in gold_path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*(\d+)\.\s+", line)
        if match:
            number = int(match[1]); gold[number] = []
        elif line.strip():
            name = line.strip().rsplit("\uff1a", 1)[-1].strip()
            if name:
                gold[number].append(name)
    if len({r["number"] for r in records}) != len(records):
        raise ValueError("Duplicate query numbers")
    registry = ROOT / "newMethod/newLLMWiki/registry/dataset_registry.jsonl"
    names = {d["dataset_id"]: d["canonical_name"] for d in
             (json.loads(s) for s in registry.read_text(encoding="utf-8").splitlines() if s.strip())}
    rows, backends = [], set()
    for r in records:
        if r.get("status", "success") != "success":
            raise ValueError(f"Query {r['number']} failed; retry it before reporting complete metrics")
        backend = r.get("backend", "legacy_unversioned" if "evidence" in r and "datasets" in r else "unknown")
        backends.add(backend)
        pred = r.get("datasets") if prediction_field == "selected" else None
        if pred is None:
            pred = [names[i] for i in r[prediction_field + "_dataset_ids"]]
        for mode in ("strict", "canonical", "family"):
            gt = scope["transform_names"](gold[r["number"]], mode)
            ranked = scope["transform_names"](pred, mode)
            row = dict(number=r["number"], label=r["label"], mode=mode,
                       gold=gt, predictions=ranked, **scope["set_metrics"](gt, ranked))
            row.update({f"recall_at_{k}": scope["recall_at_k"](gt, ranked, k) for k in (1, 3, 5)})
            rows.append(row)
    if len(backends) != 1:
        raise ValueError(f"Mixed backends: {backends}")
    aggregate = []
    for mode in ("strict", "canonical", "family"):
        subset = [r for r in rows if r["mode"] == mode]
        aggregate.append(dict(mode=mode, average="macro", **{
            k: sum(r[k] for r in subset)/len(subset) for k in
            ("precision", "recall", "f1", "recall_at_1", "recall_at_3", "recall_at_5")}))
        tp, fp, fn = (sum(r[k] for r in subset) for k in ("tp", "fp", "fn"))
        div = scope["safe_div"]
        aggregate.append(dict(mode=mode, average="micro", precision=div(tp,tp+fp), recall=div(tp,tp+fn),
                              f1=div(2*tp,2*tp+fp+fn), tp=tp, fp=fp, fn=fn))
    return {"results_path": str(results.resolve()), "results_sha256": hashlib.sha256(results.read_bytes()).hexdigest(),
            "gold_path": str(gold_path.resolve()), "gold_sha256": hashlib.sha256(gold_path.read_bytes()).hexdigest(),
            "backend": next(iter(backends)), "prediction_field": prediction_field,
            "cases": len(records), "metrics": aggregate, "per_query": rows,
            "code_fingerprints": sorted({r.get("code_fingerprint", "unversioned") for r in records}),
            "gold_interpretation": "paper-used datasets, not adjudicated task-need gold"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("results", type=Path)
    parser.add_argument("--gold", type=Path, default=ROOT / "goldres.md")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--prediction-field", choices=("selected", "portfolio"), default="selected")
    args = parser.parse_args()
    report = evaluate(args.results, args.gold, args.prediction_field)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k != "per_query"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
