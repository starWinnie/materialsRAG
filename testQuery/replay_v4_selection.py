"""Offline V4 selection replay; does not evaluate expanded V4 retrieval."""
import argparse
import json
import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "newMethod"))
import retrieve_llm_wiki as base
from v4_scoped_selection import select_scoped


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("trace_dir", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    store = base.WikiStore(ROOT / "newMethod/newLLMWiki")
    records = []
    for path in sorted(args.trace_dir.glob("q*.json")):
        trace = json.loads(path.read_text(encoding="utf-8"))
        pool = []
        candidates = {c["dataset_id"]: c for c in trace.get("selection_candidates", trace["ranked_candidates"])}
        adjustments = {c["dataset_id"]: c for c in trace.get("intent_calibration_diagnostics", {}).get("adjustments", [])}
        for dataset_id in trace.get("evidence_selection_candidate_ids", list(candidates)):
            item = candidates.get(dataset_id)
            if item is None:
                adjustment = adjustments[dataset_id]
                item = {"dataset_id": dataset_id, "final_score": adjustment["calibrated_score"], "supporting_use_ids": []}
            # Match V4 evidence retention using all uses of already reranked
            # pairs. Restore pre-family-dedup candidates from calibration trace.
            uses = {u for p in trace.get("ranked_task_dataset_pairs", [])
                    if p["dataset_id"] == item["dataset_id"] for u in p["supporting_use_ids"]}
            pool.append(SimpleNamespace(dataset_id=item["dataset_id"], final_score=item["final_score"],
                                        supporting_use_ids=uses or set(item["supporting_use_ids"])))
        plan = SimpleNamespace(**trace["query_plan"])
        selected, diag = select_scoped(store=store, plan=plan, question=trace["question"],
                                       ranked=pool, max_results=6, candidate_top_k=30)
        records.append({"case_id": path.stem, "original_selected": trace["selected_dataset_ids"],
                        "v4_selected": [c.dataset_id for c in selected],
                        "v4_names": [store.dataset_by_id[c.dataset_id]["canonical_name"] for c in selected],
                        "diagnostics": diag})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"mode": "offline_selection_replay",
                                      "limitation": "old reranked candidates only; not a full V4 retrieval experiment",
                                      "records": records}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps([{ "case": r["case_id"], "selected": r["v4_names"],
                      "covered": len(r["diagnostics"]["covered_needs"]),
                      "needs": len(r["diagnostics"]["needs"]),
                      "provisional": len(r["diagnostics"]["provisional_dataset_ids"])} for r in records], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
