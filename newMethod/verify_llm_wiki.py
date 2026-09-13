from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

import extract_llm_wiki as pipeline


ROOT = Path(__file__).resolve().parent / "newLLMWiki"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    papers = load_jsonl(ROOT / "raw/papers.jsonl")
    tasks = load_jsonl(ROOT / "raw/tasks.jsonl")
    stages = load_jsonl(ROOT / "raw/stages.jsonl")
    datasets = load_jsonl(ROOT / "raw/datasets.jsonl")
    uses = load_jsonl(ROOT / "raw/dataset_uses.jsonl")
    edges = load_jsonl(ROOT / "relations/edges.jsonl")
    manifest = json.loads((ROOT / "raw/manifest.json").read_text(encoding="utf-8"))
    errors: list[dict[str, Any]] = []

    def error(check: str, record_id: str, detail: str) -> None:
        errors.append({"check": check, "record_id": record_id, "detail": detail})

    paper_ids = {row["paper_id"] for row in papers}
    task_ids = {row["task_id"] for row in tasks}
    stage_ids = {row["stage_id"] for row in stages}
    dataset_ids = {row["dataset_id"] for row in datasets}
    use_ids = {row["dataset_use_id"] for row in uses}
    expected_ids = {row["paper_id"] for row in manifest["selected_papers"]}
    if paper_ids != expected_ids:
        error("paper_selection", "manifest", f"expected={sorted(expected_ids)} actual={sorted(paper_ids)}")

    pages_by_paper = {}
    required_artifacts = ["pages.json", "stage1_candidate_pages.json", "stage1_final.json",
                          "stage2_candidate_pages.json", "stage2_final.json", "normalized.json", "status.json"]
    for paper in papers:
        artifact_dir = ROOT / "raw/extractions" / paper["paper_id"]
        for name in required_artifacts:
            if not (artifact_dir / name).is_file():
                error("intermediate_artifact", paper["paper_id"], f"missing {name}")
        pages_path = artifact_dir / "pages.json"
        if pages_path.is_file():
            pages_by_paper[paper["paper_id"]] = {
                row["page"]: row for row in json.loads(pages_path.read_text(encoding="utf-8"))
            }
        status_path = artifact_dir / "status.json"
        if status_path.is_file():
            status = json.loads(status_path.read_text(encoding="utf-8"))
            if status.get("status") != "completed":
                error("extraction_status", paper["paper_id"], str(status.get("status")))

    def check_evidence(kind: str, record_id: str, paper_id: str, evidence: Any) -> None:
        if not isinstance(evidence, list) or not evidence:
            error("evidence_presence", record_id, f"{kind} has no evidence")
            return
        for item in evidence:
            page = item.get("page") if isinstance(item, dict) else None
            excerpt = item.get("text", "") if isinstance(item, dict) else ""
            page_record = pages_by_paper.get(paper_id, {}).get(page)
            if page_record is None:
                error("evidence_page", record_id, f"{paper_id}:{page} does not exist")
            elif not pipeline.evidence_matches(excerpt, page_record["text"])[0]:
                error("evidence_match", record_id, f"unmatched at {paper_id}:{page}")

    for task in tasks:
        if task["paper_id"] not in paper_ids:
            error("task_reference", task["task_id"], "paper does not exist")
        check_evidence("Task", task["task_id"], task["paper_id"], task.get("evidence"))
    for stage in stages:
        if stage["task_id"] not in task_ids:
            error("stage_reference", stage["stage_id"], "task does not exist")
        check_evidence("Stage", stage["stage_id"], stage["paper_id"], stage.get("evidence"))
    for dataset in datasets:
        source = dataset.get("source_dataset_id")
        if source and source not in dataset_ids:
            error("dataset_source", dataset["dataset_id"], f"missing {source}")
        if dataset["availability"] not in {"public", "restricted", "not_directly_available", "unknown"}:
            error("availability_enum", dataset["dataset_id"], dataset["availability"])
        if dataset["dataset_type"] in {"paper_specific", "derived_subset"} and dataset["recommendable"]:
            error("recommendability", dataset["dataset_id"], "private/derived dataset is recommendable")
        for evidence in dataset.get("evidence", []):
            check_evidence("Dataset", dataset["dataset_id"], evidence.get("paper_id", ""), [evidence])
    use_pairs = Counter((row["paper_id"], row["stage_id"], row["dataset_id"]) for row in uses)
    for pair, count in use_pairs.items():
        if count > 1:
            error("duplicate_dataset_use", ":".join(pair), str(count))
    for use in uses:
        for field, valid in (("task_id", task_ids), ("stage_id", stage_ids), ("dataset_id", dataset_ids)):
            if use[field] not in valid:
                error("dataset_use_reference", use["dataset_use_id"], f"missing {field}={use[field]}")
        check_evidence("DatasetUse", use["dataset_use_id"], use["paper_id"], use.get("evidence"))
        if use.get("sample_count") is not None:
            evidence_text = " ".join(item["text"] for item in use["evidence"])
            evidence_text = evidence_text.replace(",", "")
            if str(use["sample_count"]) not in evidence_text:
                error("sample_count_evidence", use["dataset_use_id"], str(use["sample_count"]))

    node_ids = {"Paper": paper_ids, "Task": task_ids, "Stage": stage_ids,
                "Dataset": dataset_ids, "DatasetUse": use_ids}
    for edge in edges:
        if edge["source_id"] not in node_ids.get(edge["source_type"], set()):
            error("edge_source", edge["edge_id"], edge["source_id"])
        if edge["target_id"] not in node_ids.get(edge["target_type"], set()):
            error("edge_target", edge["edge_id"], edge["target_id"])

    node_rows = {"papers": papers, "tasks": tasks, "stages": stages,
                 "datasets": datasets, "dataset_uses": uses}
    page_counts = {}
    for directory, rows in node_rows.items():
        count = len(list((ROOT / "pages" / directory).glob("*.md")))
        page_counts[directory] = count
        if count != len(rows):
            error("page_count", directory, f"pages={count} nodes={len(rows)}")

    report = {
        "valid": not errors,
        "counts": {"papers": len(papers), "tasks": len(tasks), "stages": len(stages),
                   "datasets": len(datasets), "dataset_uses": len(uses), "edges": len(edges)},
        "page_counts": page_counts,
        "evidence_records_checked": len(tasks) + len(stages) + len(uses) +
            sum(len(row.get("evidence", [])) for row in datasets),
        "duplicate_dataset_use_pairs": sum(1 for count in use_pairs.values() if count > 1),
        "errors": errors,
    }
    pipeline.write_json(ROOT / "reports/independent_audit.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
