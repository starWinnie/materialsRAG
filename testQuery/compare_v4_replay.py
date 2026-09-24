"""Compare a completed batch and selector replay on identical query cases."""
import argparse
import ast
import json
import re
import unicodedata
from pathlib import Path
from typing import Sequence


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline", type=Path)
    parser.add_argument("replay", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    tree = ast.parse((root / "evaluate_llm_dataset_recommendations.py").read_text(encoding="utf-8"))
    needed = {"CANONICAL_RULES", "basic_normalize", "canonicalize", "safe_div", "set_metrics"}
    nodes = [n for n in tree.body if getattr(n, "name", None) in needed or
             isinstance(n, ast.AnnAssign) and getattr(n.target, "id", None) in needed]
    scope = dict(re=re, unicodedata=unicodedata, Sequence=Sequence)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), "existing_evaluation_rules", "exec"), scope)
    canonical = scope["canonicalize"]
    registry = [json.loads(s) for s in (root / "newMethod/newLLMWiki/registry/dataset_registry.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
    names = {d["dataset_id"]: d["canonical_name"] for d in registry}
    gold, number = {}, None
    for line in (root / "goldres.md").read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*(\d+)\.\s+", line)
        if match:
            number = int(match[1]); gold[number] = []
        elif line.strip() and number is not None:
            name = line.strip().removeprefix("使用的数据集：").strip()
            if name:
                gold[number].append(name)
    old = {r["number"]: r for r in json.loads(args.baseline.read_text(encoding="utf-8")) if r["status"] == "success"}
    replay = json.loads(args.replay.read_text(encoding="utf-8"))["records"]
    rows = []
    for r in replay:
        n = int(r["case_id"][1:])
        if n not in old:
            continue
        row = {"case": r["case_id"]}
        for mode, ids in (("before", old[n]["selected_dataset_ids"]), ("after", r["v4_selected"])):
            row[mode] = {"names": [names.get(i, i) for i in ids],
                         **scope["set_metrics"]([canonical(g) for g in gold[n]], [canonical(names.get(i, i)) for i in ids])}
        rows.append(row)
    summary = {"cases": len(rows), "type": "selector replay on frozen candidates; not full end-to-end V4",
               "gold": "paper-used goldres.md, unchanged", "normalization": "existing canonical rules"}
    for mode in ("before", "after"):
        data = [r[mode] for r in rows]
        tp, fp, fn = (sum(r[k] for r in data) for k in ("tp", "fp", "fn"))
        summary[mode] = {"macro_" + k: sum(r[k] for r in data) / len(data) if data else 0 for k in ("precision", "recall", "f1")}
        summary[mode].update(empty=sum(not r["names"] for r in data),
                             mean_count=sum(len(r["names"]) for r in data) / len(data) if data else 0,
                             micro_precision=tp/(tp+fp) if tp+fp else 0,
                             micro_recall=tp/(tp+fn) if tp+fn else 0,
                             micro_f1=2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else 0)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"summary": summary, "rows": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
