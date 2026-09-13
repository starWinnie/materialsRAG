#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
对 LLM Wiki 数据集推荐实验建立逐阶段诊断基线。

本脚本同时检查两类结果：

1. DOCX 最终结果基线：
   直接复用 evaluate_llm_dataset_recommendations.py 的解析与规范化规则。
2. 检索链路基线：
   将 DOCX 中的测试案例与 retrieval_runs 中的轨迹对齐，检查 gold 数据集
   在 Dense、BM25、RRF、DatasetCandidate、确定性重排、LLM 重排和最终结果
   中是否仍然存在。

重要限制：
DOCX 当前没有保存 run_id。必须通过 --trace-manifest 显式提供 case -> trace
映射。若轨迹中的 selected_dataset_ids 与 DOCX 推荐列表不一致，脚本会将该
案例标记为 trace_aligned=false；其链路诊断只能作为暂定结果，不能作为严格
的因果结论。
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import math
import sys
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Any, Callable, Iterable


STAGES = (
    "dense",
    "bm25",
    "hybrid_union",
    "rrf_top40",
    "candidate",
    "deterministic_top30",
    "deterministic_top5",
    "llm_top30",
    "llm_top5",
    "trace_selected",
    "docx_final",
)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number} 不是合法 JSONL：{exc}") from exc
    return rows


def load_evaluator(script_path: Path) -> Any:
    """动态加载现有评估器，保证最终基线与原 Strict/Canonical/Family 规则一致。"""
    spec = importlib.util.spec_from_file_location("llm_wiki_evaluator", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载评估脚本：{script_path}")
    module = importlib.util.module_from_spec(spec)
    # dataclass 在装饰时会读取 sys.modules，因此执行前必须注册模块。
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            output.append(value)
    return output


def safe_recall(gold: set[str], candidates: set[str]) -> float:
    return len(gold & candidates) / len(gold) if gold else 0.0


def safe_precision(gold: set[str], candidates: set[str]) -> float:
    return len(gold & candidates) / len(candidates) if candidates else 0.0


def jaccard(left: set[str], right: set[str]) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 1.0


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


class WikiMapper:
    """复现生产检索中的页面 -> DatasetUse -> 可推荐 Dataset 映射。"""

    def __init__(self, wiki_root: Path, canonicalize: Callable[[str], str]):
        raw_root = wiki_root / "raw"
        self.datasets = {
            row["dataset_id"]: row for row in load_jsonl(raw_root / "datasets.jsonl")
        }
        self.uses = load_jsonl(raw_root / "dataset_uses.jsonl")
        self.use_by_id = {row["dataset_use_id"]: row for row in self.uses}
        self.uses_by_task: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.uses_by_stage: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.uses_by_dataset: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for use in self.uses:
            self.uses_by_task[use["task_id"]].append(use)
            self.uses_by_stage[use["stage_id"]].append(use)
            self.uses_by_dataset[use["dataset_id"]].append(use)

        self.dataset_canonical: dict[str, str] = {}
        for dataset_id, row in self.datasets.items():
            canonical_name = row.get("canonical_name") or dataset_id.removeprefix("D_")
            self.dataset_canonical[dataset_id] = canonicalize(str(canonical_name))
        # evaluator 中的通用 JARVIS-DFT 正则会先匹配 JARVIS-DFT-2D；
        # 对 Wiki 的明确实体 ID 做更具体的修正，防止 2D 子集被并入通用 JARVIS。
        self.dataset_canonical["D_jarvis_dft_2d"] = "jarvis_2d"

        self.wiki_canonicals = set(self.dataset_canonical.values())
        self.retrievable_canonicals: set[str] = set()
        for use in self.uses:
            target = self.target_dataset_id(str(use["dataset_id"]))
            if target:
                self.retrievable_canonicals.add(self.canonical_for_dataset_id(target))

    def target_dataset_id(self, dataset_id: str) -> str | None:
        """使用与 aggregate_dataset_candidates() 相同的一跳公共源映射。"""
        dataset = self.datasets.get(dataset_id)
        if dataset is None:
            return dataset_id
        if dataset.get("recommendable"):
            return dataset_id
        source_id = dataset.get("source_dataset_id")
        return str(source_id) if source_id else None

    def document_uses(self, doc_id: str) -> list[dict[str, Any]]:
        if doc_id in self.use_by_id:
            return [self.use_by_id[doc_id]]
        if doc_id in self.uses_by_task:
            return self.uses_by_task[doc_id]
        if doc_id in self.uses_by_stage:
            return self.uses_by_stage[doc_id]
        if doc_id in self.datasets:
            return self.uses_by_dataset.get(doc_id, [])
        return []

    def map_documents(self, doc_ids: Iterable[str]) -> set[str]:
        """把页面集合映射为生产流程实际能够聚合出的 canonical 数据集集合。"""
        result: set[str] = set()
        for doc_id in doc_ids:
            for use in self.document_uses(doc_id):
                target = self.target_dataset_id(str(use["dataset_id"]))
                if target:
                    result.add(self.canonical_for_dataset_id(target))
        return result

    def canonical_for_dataset_id(self, dataset_id: str) -> str:
        if dataset_id in self.dataset_canonical:
            return self.dataset_canonical[dataset_id]
        # 对轨迹中已不存在于 Wiki 的旧 ID，保留可读的后备规范化形式。
        return dataset_id.removeprefix("D_").casefold()

    def map_dataset_ids(self, dataset_ids: Iterable[str]) -> set[str]:
        return {self.canonical_for_dataset_id(value) for value in dataset_ids}


def raw_channel_documents(trace: dict[str, Any], prefix: str) -> list[str]:
    """合并某一检索通道全部查询的 Top-K 页面，保持首次出现顺序。"""
    doc_ids: list[str] = []
    for ranking in trace.get("raw_rankings", []):
        channel = str(ranking.get("channel", ""))
        if not channel.startswith(prefix):
            continue
        doc_ids.extend(
            str(item["doc_id"])
            for item in ranking.get("results", [])
            if item.get("doc_id")
        )
    return unique(doc_ids)


def trace_stage_sets(trace: dict[str, Any], mapper: WikiMapper) -> dict[str, set[str]]:
    dense_docs = raw_channel_documents(trace, "dense:")
    bm25_docs = raw_channel_documents(trace, "bm25:")
    rrf_docs = [
        str(item["doc_id"])
        for item in trace.get("rrf_results", [])[:40]
        if item.get("doc_id")
    ]

    ranked = list(trace.get("ranked_candidates", []))
    candidate_ids = [str(item["dataset_id"]) for item in ranked if item.get("dataset_id")]

    # 轨迹中的 ranked_candidates 已是 LLM 重排后的顺序；通过 deterministic_score
    # 重新排序可以恢复确定性 Top-30。
    deterministic = sorted(
        ranked,
        key=lambda item: float(item.get("deterministic_score") or 0.0),
        reverse=True,
    )
    deterministic_ids = [
        str(item["dataset_id"]) for item in deterministic[:30] if item.get("dataset_id")
    ]
    deterministic_top5_ids = [
        str(item["dataset_id"]) for item in deterministic[:5] if item.get("dataset_id")
    ]
    llm_top30_ids = [
        str(item["dataset_id"]) for item in ranked[:30] if item.get("dataset_id")
    ]
    llm_ids = [str(item["dataset_id"]) for item in ranked[:5] if item.get("dataset_id")]
    selected_ids = [str(value) for value in trace.get("selected_dataset_ids", [])]

    dense_set = mapper.map_documents(dense_docs)
    bm25_set = mapper.map_documents(bm25_docs)
    return {
        "dense": dense_set,
        "bm25": bm25_set,
        "hybrid_union": dense_set | bm25_set,
        "rrf_top40": mapper.map_documents(rrf_docs),
        "candidate": mapper.map_dataset_ids(candidate_ids),
        "deterministic_top30": mapper.map_dataset_ids(deterministic_ids),
        "deterministic_top5": mapper.map_dataset_ids(deterministic_top5_ids),
        "llm_top30": mapper.map_dataset_ids(llm_top30_ids),
        "llm_top5": mapper.map_dataset_ids(llm_ids),
        "trace_selected": mapper.map_dataset_ids(selected_ids),
    }


def first_loss_stage(gold: str, stage_sets: dict[str, set[str]]) -> str:
    """
    返回 gold 在主链路中第一次消失的位置。

    Dense 和 BM25 是并行通道，因此以 hybrid_union 作为主链路起点。
    llm_top5 是排名截断，不保证最终集合一定只能从 Top-5 中选择，所以单独标记。
    """
    ordered = (
        "hybrid_union",
        "rrf_top40",
        "candidate",
        "deterministic_top30",
        "llm_top5",
        "docx_final",
    )
    for stage in ordered:
        if gold not in stage_sets.get(stage, set()):
            return stage
    return "survived_all"


def pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def main() -> int:
    workspace = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="建立 LLM Wiki 检索链路诊断基线")
    parser.add_argument("docx", type=Path)
    parser.add_argument("--trace-manifest", required=True, type=Path)
    parser.add_argument(
        "--retrieval-runs",
        type=Path,
        default=Path(__file__).resolve().parent / "retrieval_runs",
    )
    parser.add_argument(
        "--wiki-root",
        type=Path,
        default=Path(__file__).resolve().parent / "newLLMWiki",
    )
    parser.add_argument(
        "--evaluator",
        type=Path,
        default=workspace / "evaluate_llm_dataset_recommendations.py",
    )
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    evaluator = load_evaluator(args.evaluator.resolve())
    records = evaluator.parse_docx(args.docx.resolve())
    record_by_case = {record.paper: record for record in records}
    manifest = load_json(args.trace_manifest.resolve())
    manifest_entries = manifest.get("cases", manifest)
    manifest_by_case = {entry["case_id"]: entry for entry in manifest_entries}
    mapper = WikiMapper(args.wiki_root.resolve(), evaluator.canonicalize)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    # 把原评估器的最终 Strict/Canonical/Family 指标一并保存，使本目录成为
    # 自包含的基线产物，而不必依赖此前手工运行的评估目录。
    evaluator.evaluate(records, args.output_dir / "final_metrics")
    stage_rows: list[dict[str, Any]] = []
    survival_rows: list[dict[str, Any]] = []
    alignment_rows: list[dict[str, Any]] = []
    stage_accumulator: dict[tuple[str, str, str], list[float]] = defaultdict(list)
    warning_lines: list[str] = []

    for case_id, record in record_by_case.items():
        entry = manifest_by_case.get(case_id)
        if not entry:
            warning_lines.append(f"{case_id}: trace manifest 中没有对应轨迹。")
            continue

        trace_path = args.retrieval_runs / entry["trace_file"]
        try:
            trace = load_json(trace_path)
        except (OSError, json.JSONDecodeError) as exc:
            warning_lines.append(f"{case_id}: 无法读取 {trace_path.name}: {exc}")
            continue

        canonical_gold = set(evaluator.transform_names(record.ground_truth, "canonical"))
        family_gold = set(evaluator.transform_names(record.ground_truth, "family"))
        canonical_final = set(evaluator.transform_names(record.recommended, "canonical"))
        family_final = set(evaluator.transform_names(record.recommended, "family"))
        canonical_stages = trace_stage_sets(trace, mapper)
        canonical_stages["docx_final"] = canonical_final
        family_stages = {
            stage: {evaluator.family_name(value) for value in values}
            for stage, values in canonical_stages.items()
        }
        family_stages["docx_final"] = family_final

        trace_selected = canonical_stages["trace_selected"]
        alignment_jaccard = jaccard(canonical_final, trace_selected)
        trace_aligned = canonical_final == trace_selected
        alignment_rows.append({
            "case_id": case_id,
            "trace_file": trace_path.name,
            "mapping_confidence": entry.get("mapping_confidence", "unknown"),
            "trace_aligned": trace_aligned,
            "alignment_jaccard": round(alignment_jaccard, 6),
            "docx_recommended": " | ".join(sorted(canonical_final)),
            "trace_selected": " | ".join(sorted(trace_selected)),
            "note": entry.get("note", ""),
        })

        row: dict[str, Any] = {
            "case_id": case_id,
            "trace_file": trace_path.name,
            "trace_aligned": trace_aligned,
            "gold_count_canonical": len(canonical_gold),
        }
        for level, gold, stages in (
            ("canonical", canonical_gold, canonical_stages),
            ("family", family_gold, family_stages),
        ):
            if level == "canonical":
                retrievable_gold = gold & mapper.retrievable_canonicals
            else:
                retrievable_gold = gold & {
                    evaluator.family_name(value)
                    for value in mapper.retrievable_canonicals
                }
            for stage in STAGES:
                value = safe_recall(gold, stages.get(stage, set()))
                row[f"{level}_{stage}_recall"] = round(value, 6)
                stage_accumulator[(level, "all_gold", stage)].append(value)
                if retrievable_gold:
                    covered_value = safe_recall(
                        retrievable_gold, stages.get(stage, set())
                    )
                    stage_accumulator[
                        (level, "retrievable_gold", stage)
                    ].append(covered_value)
        stage_rows.append(row)

        for raw_gold in record.ground_truth:
            canonical_gold_item = evaluator.canonicalize(raw_gold)
            family_gold_item = evaluator.family_name(canonical_gold_item)
            survival_row: dict[str, Any] = {
                "case_id": case_id,
                "trace_file": trace_path.name,
                "gold_raw": raw_gold,
                "gold_canonical": canonical_gold_item,
                "gold_family": family_gold_item,
                "exists_in_wiki": canonical_gold_item in mapper.wiki_canonicals,
                "retrievable_by_production_mapping": (
                    canonical_gold_item in mapper.retrievable_canonicals
                ),
                "first_loss_stage": first_loss_stage(canonical_gold_item, canonical_stages),
                "trace_aligned": trace_aligned,
            }
            for stage in STAGES:
                survival_row[stage] = canonical_gold_item in canonical_stages.get(stage, set())
            survival_rows.append(survival_row)

    summary_rows: list[dict[str, Any]] = []
    for level in ("canonical", "family"):
        for scope in ("all_gold", "retrievable_gold"):
            for stage in STAGES:
                values = stage_accumulator.get((level, scope, stage), [])
                summary_rows.append({
                    "match_level": level,
                    "scope": scope,
                    "stage": stage,
                    "case_count": len(values),
                    "macro_recall": (
                        round(sum(values) / len(values), 6) if values else ""
                    ),
                })

    stage_fields = [
        "case_id", "trace_file", "trace_aligned", "gold_count_canonical",
        *[
            f"{level}_{stage}_recall"
            for level in ("canonical", "family")
            for stage in STAGES
        ],
    ]
    write_csv(args.output_dir / "stage_metrics.csv", stage_rows, stage_fields)
    write_csv(
        args.output_dir / "gold_survival.csv",
        survival_rows,
        [
            "case_id", "trace_file", "gold_raw", "gold_canonical", "gold_family",
            "exists_in_wiki", "retrievable_by_production_mapping",
            *STAGES, "first_loss_stage", "trace_aligned",
        ],
    )
    write_csv(
        args.output_dir / "trace_alignment.csv",
        alignment_rows,
        [
            "case_id", "trace_file", "mapping_confidence", "trace_aligned",
            "alignment_jaccard", "docx_recommended", "trace_selected", "note",
        ],
    )
    write_csv(
        args.output_dir / "stage_summary.csv",
        summary_rows,
        ["match_level", "scope", "stage", "case_count", "macro_recall"],
    )

    aligned_count = sum(1 for row in alignment_rows if row["trace_aligned"])
    canonical_summary = {
        row["stage"]: row["macro_recall"]
        for row in summary_rows
        if row["match_level"] == "canonical" and row["scope"] == "all_gold"
    }
    covered_canonical_summary = {
        row["stage"]: row["macro_recall"]
        for row in summary_rows
        if (
            row["match_level"] == "canonical"
            and row["scope"] == "retrievable_gold"
        )
    }
    gold_total = len(survival_rows)
    missing_wiki_rows = [
        row for row in survival_rows if not row["exists_in_wiki"]
    ]
    retrievable_total = sum(
        1 for row in survival_rows if row["retrievable_by_production_mapping"]
    )
    report_lines = [
        "# LLM Wiki 0729 检索诊断基线",
        "",
        f"- DOCX 测试案例：{len(records)}",
        f"- 成功匹配轨迹：{len(stage_rows)}",
        f"- 轨迹 selected 与 DOCX 推荐完全一致：{aligned_count}/{len(alignment_rows)}",
        "- 主评测口径：Canonical；Family 用于判断同一家族的宽松命中。",
        "",
        "## 逐阶段 Macro Recall",
        "",
        "| 阶段 | 全部 gold | 生产流程可召回 gold |",
        "|---|---:|---:|",
    ]
    stage_labels = {
        "dense": "Dense（全部查询 Top-30 并集）",
        "bm25": "BM25（全部查询 Top-30 并集）",
        "hybrid_union": "Dense∪BM25",
        "rrf_top40": "RRF Top-40",
        "candidate": "图扩展后的 DatasetCandidate",
        "deterministic_top30": "确定性重排 Top-30",
        "deterministic_top5": "确定性重排 Top-5",
        "llm_top30": "LLM 重排 Top-30",
        "llm_top5": "LLM 重排 Top-5",
        "trace_selected": "轨迹 selected_dataset_ids",
        "docx_final": "DOCX 最终推荐",
    }
    for stage in STAGES:
        value = canonical_summary.get(stage, "")
        display = pct(float(value)) if value != "" else "N/A"
        covered_value = covered_canonical_summary.get(stage, "")
        covered_display = (
            pct(float(covered_value)) if covered_value != "" else "N/A"
        )
        report_lines.append(
            f"| {stage_labels[stage]} | {display} | {covered_display} |"
        )

    union_recall = float(canonical_summary.get("hybrid_union") or 0.0)
    rrf_recall = float(canonical_summary.get("rrf_top40") or 0.0)
    candidate_recall = float(canonical_summary.get("candidate") or 0.0)
    det5_recall = float(canonical_summary.get("deterministic_top5") or 0.0)
    llm5_recall = float(canonical_summary.get("llm_top5") or 0.0)
    report_lines.extend([
        "",
        "## 基线结论",
        "",
        f"- 共有 {gold_total} 个 canonical gold，其中 {gold_total - len(missing_wiki_rows)} 个存在于 Wiki，{retrievable_total} 个能够按生产映射形成候选。",
        f"- Dense∪BM25 到 RRF Top-40 的 Macro Recall 变化为 {pct(union_recall)} → {pct(rrf_recall)}，损失 {pct(max(0.0, union_recall - rrf_recall))}。",
        f"- 图扩展将 Macro Recall 从 {pct(rrf_recall)} 提升到 {pct(candidate_recall)}，说明图扩展总体有效，但仍需控制噪声。",
        f"- 同为 Top-5 时，确定性重排为 {pct(det5_recall)}，LLM 重排为 {pct(llm5_recall)}；LLM 在本组暂定轨迹上净变化 {pct(llm5_recall - det5_recall)}。",
        f"- 只有 {aligned_count}/{len(alignment_rows)} 条轨迹的 selected_dataset_ids 与 DOCX 完全一致，因此最终选择阶段的因果分析必须等补充 run_id 后复核。",
    ])
    if missing_wiki_rows:
        report_lines.extend(["", "### Wiki 中缺失的 gold", ""])
        report_lines.extend(
            f"- {row['case_id']}：{row['gold_raw']}"
            for row in missing_wiki_rows
        )

    report_lines.extend([
        "",
        "## 解释限制",
        "",
        "DOCX 没有保存 run_id，且部分最相近轨迹的 selected_dataset_ids 与 DOCX",
        "推荐列表不一致。因此，最终结果指标是严格基线；逐阶段指标在轨迹未完全",
        "对齐的案例上属于暂定诊断。后续运行必须把 run_id 写入 DOCX 或实验清单。",
        "",
        "## 输出文件",
        "",
        "- `stage_metrics.csv`：每个案例、每个阶段的 Canonical/Family Recall。",
        "- `gold_survival.csv`：每个 gold 在各阶段是否存在，以及首次消失位置。",
        "- `trace_alignment.csv`：DOCX 与轨迹的一致性检查。",
        "- `stage_summary.csv`：逐阶段 Macro Recall 汇总。",
        "- `final_metrics/`：DOCX 最终 Strict/Canonical/Family 基线。",
    ])
    if warning_lines:
        report_lines.extend(["", "## 警告", ""])
        report_lines.extend(f"- {line}" for line in warning_lines)
    (args.output_dir / "baseline_report.md").write_text(
        "\n".join(report_lines) + "\n", encoding="utf-8"
    )

    print(f"Parsed cases: {len(records)}")
    print(f"Traced cases: {len(stage_rows)}")
    print(f"Exactly aligned traces: {aligned_count}/{len(alignment_rows)}")
    print(f"Outputs: {args.output_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
