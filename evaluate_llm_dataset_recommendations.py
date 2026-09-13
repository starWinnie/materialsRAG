#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluate LLM dataset recommendations against datasets actually used in papers.

Input: a DOCX with sections like:
    33_DenseGNN
    使用的数据集：JARVIS-DFT
    Materials Project
    推荐的数据集：Materials Project（MP）
    JARVIS-DFT

Outputs:
    1) per_paper_metrics.csv
    2) summary_metrics.csv
    3) parsed_records.csv

Metrics:
    - Precision / Recall / F1 for set-valued recommendations
    - macro and micro averages
    - Recall@K when recommendation order is treated as ranking
    - optional negative-selection rate for entries under “不推荐...”

Important:
    - "canonical" metrics use an explicit alias map.
    - "family" metrics are more lenient and merge derived/versioned datasets
      into the same source family (e.g. MPtrj -> Materials Project family).
    - Extend CANONICAL_RULES and FAMILY_MAP for your own corpus.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import pandas as pd
from docx import Document


# -----------------------------
# 1. Name normalization rules
# -----------------------------
# Rules are evaluated from top to bottom. Put more specific rules first.
CANONICAL_RULES: list[tuple[str, str]] = [
    # Materials Project derived datasets before generic Materials Project
    (r"\bmaterials project trajectory dataset\b|\bmptraj\b|\bmptrj\b|材料项目.*弛豫轨迹|materials project.*弛豫轨迹|materials project.*trajectory", "materials_project_trajectory"),
    (r"\bmpf\s*[._-]?\s*2021|\bmpf\.2021\.2\.8\b", "materials_project_force_2021"),
    (r"materials project phonon database", "materials_project_phonon"),
    (r"\bmaterials project\b|\bthe materials project\b|\bmp database\b", "materials_project"),

    # OQMD variants
    (r"\boqmd[-_ ]?exp\b", "oqmd_exp"),
    (r"\bopen quantum materials database\b|\boqmd\b", "oqmd"),

    # JARVIS variants
    (r"\bjarvis[-_ ]?2d\b", "jarvis_2d"),
    (r"\bjarvis[-_ ]?dft\b|joint automated repository for various integrated simulations|^jarvis$", "jarvis_dft"),

    # Other common materials datasets
    (r"\binorganic crystal structure database\b|\bicsd\b", "icsd"),
    (r"\bwang[-–— ]?botti[-–— ]?marques\b|\bwbm\b", "wbm"),
    (r"\bmatbench\s*v?0\.1\b|^matbench$", "matbench"),
    (r"\bqm9\b", "qm9"),
    (r"\boc22\b", "oc22"),
    (r"\bmd17[-_ ]?ccsd\s*\(?t\)?\b", "md17_ccsdt"),
    (r"\bmd17\b", "md17"),
    (r"\bc2db\b", "c2db"),
    (r"\b2dmatpedia\b", "2dmatpedia"),
    (r"\baflow\b", "aflow"),
    (r"\bopenkim\b", "openkim"),
    (r"\bphonondb\b", "phonondb"),
    (r"\bharvard hopv\b|\bhopv\b", "harvard_hopv"),
    (r"\bdielectric constant\b|\bdc database\b", "dielectric_constant_database"),
    (r"\bpiezoelectric tensor\b|\bpt database\b", "piezoelectric_tensor_database"),
    (r"\bflla\b", "flla"),

    # Paper-specific datasets must precede generic property datasets.
    (r"\bperovskite solar cell\b|\bpsc database\b", "perovskite_solar_cell_database"),
    (r"\bliu et al\.? experimental bandgap dataset\b", "liu_bandgap_dataset"),
    (r"\byang et al\.? experimental bandgap dataset\b", "yang_bandgap_dataset"),

    # Experimental property datasets. These aliases may need domain review.
    (r"\bexperimental formation energy(?: dataset)?\b|\befe\b|\bkefe\b", "experimental_formation_energy"),
    # Kingsbury Experimental Bandgap (KEB) and the separately named
    # Experimental Band Gap Dataset are distinct datasets. Keep the specific
    # Kingsbury rule first and never merge the two at canonical level.
    (r"\bkingsbury experimental band\s*gap\b|\bkeb\b", "kingsbury_experimental_bandgap"),
    (r"\bexperimental band\s*gap(?: dataset)?\b", "experimental_bandgap"),
    (r"\bdft[- ]calculated bandgap dataset\b", "dft_pbe_bandgap_dataset"),
    (r"\bhoip dataset\b", "hoip_dataset"),
    (r"\bperovskite halides dataset\b|^perovskite halides$", "perovskite_halides"),
    (r"\blipopdataset\b|\blipophilicity\b", "lipophilicity"),
    (r"\bfreesolvdataset\b|\bfreesolv\b", "freesolv"),
    (r"\besoldataset\b|\besol\b", "esol"),
    (r"\bzuo et al\.? dft dataset\b", "zuo_dft"),
    (r"\bcrysgnn curated dataset\b", "crysgnn_curated"),
    (r"\bsynthesizability dataset\b", "synthesizability_curated"),
    (r"\b380,?743 unlabeled (?:crystal )?structures\b", "merchant_380743_unlabeled_structures"),
    (r"\bin[- ]house dft[- ]relaxed novel structures\b", "inhouse_dft_relaxed_structures"),
    (r"\bmat(?:scholar)? embeddings\b", "matscholar_embeddings"),
    (r"\bmendeleev metrics\b", "mendeleev_metrics"),
    (r"\bli[- ]oxides\b", "li_oxides"),
    (r"\bdouble perovskites\b", "double_perovskites"),
]

# A lenient family-level map. Useful for reporting, but should not replace
# exact/canonical results because a generic parent database may not satisfy
# a task requiring a specific trajectory/phonon/versioned subset.
FAMILY_MAP: dict[str, str] = {
    "materials_project": "materials_project_family",
    "materials_project_trajectory": "materials_project_family",
    "materials_project_force_2021": "materials_project_family",
    "materials_project_phonon": "materials_project_family",
    "oqmd": "oqmd_family",
    "oqmd_exp": "oqmd_family",
    "jarvis_dft": "jarvis_family",
    "jarvis_2d": "jarvis_family",
    "matbench": "matbench_family",
    "md17": "md17_family",
    "md17_ccsdt": "md17_family",
}


@dataclass
class PaperRecord:
    paper: str
    ground_truth: list[str]
    recommended: list[str]
    not_recommended: list[str]


def basic_normalize(text: str) -> str:
    """Unicode/punctuation/case normalization without semantic alias merging."""
    text = unicodedata.normalize("NFKC", text)
    text = text.strip().lower()
    text = text.replace("–", "-").replace("—", "-")
    text = re.sub(r"[，,;；。]+$", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def canonicalize(text: str) -> str:
    """Map a dataset mention to a canonical dataset ID."""
    normalized = basic_normalize(text)
    for pattern, canonical_name in CANONICAL_RULES:
        if re.search(pattern, normalized, flags=re.IGNORECASE):
            return canonical_name

    # Fallback: remove parenthetical descriptions and non-alphanumeric symbols.
    fallback = re.sub(r"\([^)]*\)|（[^）]*）", " ", normalized)
    fallback = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "_", fallback)
    return fallback.strip("_")


def family_name(canonical_name: str) -> str:
    return FAMILY_MAP.get(canonical_name, canonical_name)


def split_outside_parentheses(text: str, separators: Sequence[str]) -> list[str]:
    """Split at separators only when not inside () or Chinese （）."""
    result: list[str] = []
    buffer: list[str] = []
    depth = 0
    i = 0
    ordered_seps = sorted(separators, key=len, reverse=True)

    while i < len(text):
        ch = text[i]
        if ch in "(（":
            depth += 1
        elif ch in ")）" and depth > 0:
            depth -= 1

        matched = None
        if depth == 0:
            for sep in ordered_seps:
                if text.startswith(sep, i):
                    matched = sep
                    break

        if matched is not None:
            item = "".join(buffer).strip()
            if item:
                result.append(item)
            buffer = []
            i += len(matched)
        else:
            buffer.append(ch)
            i += 1

    item = "".join(buffer).strip()
    if item:
        result.append(item)
    return result


def split_dataset_mentions(text: str) -> list[str]:
    """Split a paragraph that may contain several dataset names."""
    text = text.strip()
    if not text:
        return []

    # Keep contextual qualifiers because they may distinguish a generic source
    # from a task-specific version, e.g. “Materials Project，尤其是弛豫轨迹版本”.

    parts: list[str] = []
    for line in re.split(r"[\r\n]+", text):
        line = line.strip(" •\t")
        if not line:
            continue
        # Separators used in the uploaded record to list multiple datasets.
        subparts = split_outside_parentheses(
            line,
            separators=[" + ", " & ", " / ", " 或 ", " and "],
        )
        parts.extend(subparts)

    cleaned: list[str] = []
    for item in parts:
        item = item.strip(" ：:;；,，。")
        if item:
            cleaned.append(item)
    return cleaned


def parse_docx(path: Path) -> list[PaperRecord]:
    doc = Document(path)
    raw_lines: list[str] = []
    for paragraph in doc.paragraphs:
        # A Word paragraph may itself contain line breaks.
        raw_lines.extend(x.strip() for x in re.split(r"[\r\n]+", paragraph.text) if x.strip())

    records: list[PaperRecord] = []
    current: PaperRecord | None = None
    state: str | None = None

    paper_pattern = re.compile(r"^\d+[_、.\s-].+")

    for line in raw_lines:
        if paper_pattern.match(line):
            if current is not None:
                records.append(current)
            current = PaperRecord(line, [], [], [])
            state = None
            continue

        if current is None:
            continue

        if line.startswith("使用的数据集"):
            state = "ground_truth"
            tail = re.split(r"[：:]", line, maxsplit=1)
            if len(tail) == 2:
                current.ground_truth.extend(split_dataset_mentions(tail[1]))
            continue

        if line.startswith("推荐的数据集"):
            state = "recommended"
            tail = re.split(r"[：:]", line, maxsplit=1)
            if len(tail) == 2:
                current.recommended.extend(split_dataset_mentions(tail[1]))
            continue

        if line.startswith("不推荐"):
            state = "not_recommended"
            tail = re.split(r"[：:]", line, maxsplit=1)
            if len(tail) == 2:
                current.not_recommended.extend(split_dataset_mentions(tail[1]))
            continue

        if state == "ground_truth":
            current.ground_truth.extend(split_dataset_mentions(line))
        elif state == "recommended":
            current.recommended.extend(split_dataset_mentions(line))
        elif state == "not_recommended":
            current.not_recommended.extend(split_dataset_mentions(line))

    if current is not None:
        records.append(current)

    return records


def deduplicate_keep_order(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def transform_names(items: Sequence[str], level: str) -> list[str]:
    if level == "strict":
        transformed = [basic_normalize(x) for x in items]
    elif level == "canonical":
        transformed = [canonicalize(x) for x in items]
    elif level == "family":
        transformed = [family_name(canonicalize(x)) for x in items]
    else:
        raise ValueError(f"Unknown level: {level}")
    return deduplicate_keep_order(x for x in transformed if x)


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def set_metrics(gt: Sequence[str], pred: Sequence[str]) -> dict[str, float | int | str]:
    gt_set, pred_set = set(gt), set(pred)
    correct = gt_set & pred_set
    false_positive = pred_set - gt_set
    false_negative = gt_set - pred_set

    precision = safe_div(len(correct), len(pred_set))
    recall = safe_div(len(correct), len(gt_set))
    f1 = safe_div(2 * precision * recall, precision + recall)

    return {
        "tp": len(correct),
        "fp": len(false_positive),
        "fn": len(false_negative),
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "correct": " | ".join(sorted(correct)),
        "false_positive": " | ".join(sorted(false_positive)),
        "false_negative": " | ".join(sorted(false_negative)),
    }


def recall_at_k(gt: Sequence[str], ranked_pred: Sequence[str], k: int) -> float:
    gt_set = set(gt)
    return safe_div(len(gt_set & set(ranked_pred[:k])), len(gt_set))


def evaluate(records: Sequence[PaperRecord], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    detail_rows: list[dict[str, object]] = []
    parsed_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    for rec in records:
        parsed_rows.append(
            {
                "paper": rec.paper,
                "ground_truth_raw": " | ".join(rec.ground_truth),
                "recommended_raw": " | ".join(rec.recommended),
                "not_recommended_raw": " | ".join(rec.not_recommended),
            }
        )

    for level in ("strict", "canonical", "family"):
        level_rows: list[dict[str, object]] = []

        for rec in records:
            gt = transform_names(rec.ground_truth, level)
            pred = transform_names(rec.recommended, level)
            negative = transform_names(rec.not_recommended, level)
            metrics = set_metrics(gt, pred)

            selected_negative = set(pred) & set(negative)
            row: dict[str, object] = {
                "paper": rec.paper,
                "match_level": level,
                "ground_truth_count": len(set(gt)),
                "recommended_count": len(set(pred)),
                **metrics,
                "recall@1": recall_at_k(gt, pred, 1),
                "recall@3": recall_at_k(gt, pred, 3),
                "recall@5": recall_at_k(gt, pred, 5),
                "any_hit": int(metrics["tp"] > 0),
                "perfect_set_match": int(set(gt) == set(pred)),
                "selected_negative_count": len(selected_negative),
                "selected_negative": " | ".join(sorted(selected_negative)),
                "ground_truth_normalized": " | ".join(gt),
                "recommended_normalized": " | ".join(pred),
            }
            level_rows.append(row)
            detail_rows.append(row)

        df_level = pd.DataFrame(level_rows)
        tp = int(df_level["tp"].sum())
        fp = int(df_level["fp"].sum())
        fn = int(df_level["fn"].sum())
        micro_precision = safe_div(tp, tp + fp)
        micro_recall = safe_div(tp, tp + fn)
        micro_f1 = safe_div(2 * micro_precision * micro_recall, micro_precision + micro_recall)

        summary_rows.extend(
            [
                {"match_level": level, "aggregation": "macro", "metric": "precision", "value": df_level["precision"].mean()},
                {"match_level": level, "aggregation": "macro", "metric": "recall", "value": df_level["recall"].mean()},
                {"match_level": level, "aggregation": "macro", "metric": "f1", "value": df_level["f1"].mean()},
                {"match_level": level, "aggregation": "micro", "metric": "precision", "value": micro_precision},
                {"match_level": level, "aggregation": "micro", "metric": "recall", "value": micro_recall},
                {"match_level": level, "aggregation": "micro", "metric": "f1", "value": micro_f1},
                {"match_level": level, "aggregation": "macro", "metric": "recall@1", "value": df_level["recall@1"].mean()},
                {"match_level": level, "aggregation": "macro", "metric": "recall@3", "value": df_level["recall@3"].mean()},
                {"match_level": level, "aggregation": "macro", "metric": "recall@5", "value": df_level["recall@5"].mean()},
                {"match_level": level, "aggregation": "macro", "metric": "any_hit_rate", "value": df_level["any_hit"].mean()},
                {"match_level": level, "aggregation": "macro", "metric": "perfect_set_match_rate", "value": df_level["perfect_set_match"].mean()},
                {
                    "match_level": level,
                    "aggregation": "micro",
                    "metric": "negative_selection_rate",
                    "value": safe_div(int(df_level["selected_negative_count"].sum()), int(df_level["recommended_count"].sum())),
                },
            ]
        )

    parsed_df = pd.DataFrame(parsed_rows)
    detail_df = pd.DataFrame(detail_rows)
    summary_df = pd.DataFrame(summary_rows)

    parsed_df.to_csv(output_dir / "parsed_records.csv", index=False, encoding="utf-8-sig")
    detail_df.to_csv(output_dir / "per_paper_metrics.csv", index=False, encoding="utf-8-sig")
    summary_df.to_csv(output_dir / "summary_metrics.csv", index=False, encoding="utf-8-sig")

    # Print the most useful report to the terminal.
    print(f"Parsed {len(records)} papers.\n")
    print("=== Summary metrics ===")
    pivot = summary_df.pivot_table(
        index=["match_level", "aggregation"], columns="metric", values="value", aggfunc="first"
    )
    with pd.option_context("display.max_columns", None, "display.width", 180):
        print((pivot * 100).round(2).to_string())

    print("\n=== Canonical per-paper metrics ===")
    canonical = detail_df[detail_df["match_level"] == "canonical"][
        ["paper", "precision", "recall", "f1", "correct", "false_positive", "false_negative"]
    ].copy()
    for col in ["precision", "recall", "f1"]:
        canonical[col] = (canonical[col] * 100).round(2)
    with pd.option_context("display.max_colwidth", 55, "display.width", 220):
        print(canonical.to_string(index=False))

    print(f"\nCSV files written to: {output_dir.resolve()}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path, help="Path to the experiment DOCX")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("evaluation_output/80papers"),
        help="Directory for CSV outputs",
    )
    args = parser.parse_args()

    if not args.docx.exists():
        raise FileNotFoundError(args.docx)

    records = parse_docx(args.docx)
    if not records:
        raise ValueError("No paper records were parsed. Check the DOCX headings and section labels.")

    evaluate(records, args.output_dir)


if __name__ == "__main__":
    main()
