from __future__ import annotations

import argparse
import json
import os
import re
import time
import unicodedata
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date, datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable

import fitz
from dotenv import load_dotenv
from openai import OpenAI


STAGE_TYPES = [
    "data_acquisition",
    "data_preparation",
    "label_generation",
    "model_training",
    "model_evaluation",
    "candidate_generation",
    "candidate_screening",
    "computational_validation",
    "experimental_validation",
    "other",
]

USAGE_ROLES = [
    "source",
    "training",
    "validation",
    "test",
    "pretraining",
    "label_source",
    "candidate_pool",
    "screening",
    "benchmark",
    "computational_validation",
    "experimental_validation",
]

DATASET_TYPES = [
    "public_database",
    "public_subset",
    "derived_subset",
    "paper_specific",
]

DATASET_ALIAS_GROUPS = {
    "2dmatpedia_database": ("2dmatpedia", "2DMatPedia"),
    "materials_project_2021": ("materials_project", "Materials Project"),
    "materials_project_2023_6_23_version": ("materials_project", "Materials Project"),
    "materials_project_database": ("materials_project", "Materials Project"),
    "materials_project_megnet": ("materials_project", "Materials Project"),
    "materials_project_v2023_11_1": ("materials_project", "Materials Project"),
    "materials_project_v_2022_10_28": ("materials_project", "Materials Project"),
    "open_quantum_materials_database": ("oqmd", "Open Quantum Materials Database (OQMD)"),
    "jarvis_2d": ("jarvis_dft_2d", "JARVIS-DFT 2D"),
    "jarvis_3d": ("jarvis_dft_3d", "JARVIS-DFT 3D"),
    "jarvis_dft_3d_2021": ("jarvis_dft_3d", "JARVIS-DFT 3D"),
    "jarvis": ("jarvis_dft", "JARVIS-DFT"),
    "jarvis_database": ("jarvis_dft", "JARVIS-DFT"),
    "jarvis_dataset": ("jarvis_dft", "JARVIS-DFT"),
    "joint_automated_repository_for_various_integrated_simulations": ("jarvis_dft", "JARVIS-DFT"),
}

DATASET_CANONICAL_DISPLAY = {
    "2dmatpedia": "2DMatPedia",
    "computational_2d_materials_database": "Computational 2D Materials Database (C2DB)",
    "inorganic_crystal_structure_database_icsd": "Inorganic Crystal Structure Database (ICSD)",
    "jarvis_dft": "JARVIS-DFT",
    "jarvis_dft_2d": "JARVIS-DFT 2D",
    "jarvis_dft_3d": "JARVIS-DFT 3D",
    "materials_project": "Materials Project",
    "matbench": "Matbench",
    "openkim_repository": "OpenKIM Repository",
    "oqmd": "Open Quantum Materials Database (OQMD)",
}

STAGE_TAXONOMY = {
    "version": "1.0",
    "stage_types": [
        {"stage_type": "data_acquisition", "description": "Acquiring source records or measurements."},
        {"stage_type": "data_preparation", "description": "Cleaning, filtering, transforming, or splitting data."},
        {"stage_type": "label_generation", "description": "Generating target labels by calculation, annotation, or experiment."},
        {"stage_type": "model_training", "description": "Fitting or pretraining a model."},
        {"stage_type": "model_evaluation", "description": "Evaluating or benchmarking model performance."},
        {"stage_type": "candidate_generation", "description": "Generating a material candidate space."},
        {"stage_type": "candidate_screening", "description": "Ranking or filtering material candidates."},
        {"stage_type": "computational_validation", "description": "Validating candidates with computation or simulation."},
        {"stage_type": "experimental_validation", "description": "Validating candidates experimentally."},
        {"stage_type": "other", "description": "A paper-specific R&D stage not represented above."},
    ],
}

DATA_KEYWORDS = (
    "data",
    "dataset",
    "database",
    "training",
    "validation",
    "test set",
    "benchmark",
    "supplement",
    "availability",
    "materials project",
    "jarvis",
    "oqmd",
    "aflow",
    "icsd",
    "cod",
    "calculated",
    "collected",
    "samples",
    "structures",
    "candidate",
    "screen",
    "experiment",
)

TASK_KEYWORDS = (
    "abstract",
    "introduction",
    "method",
    "approach",
    "workflow",
    "results",
    "predict",
    "discover",
    "design",
    "screen",
    "generate",
    "validate",
    "train",
    "dataset",
    "experiment",
    "calculation",
)


STAGE1_SYSTEM = """
You extract a paper's single main materials R&D Task and its actual R&D Stages.
Use only the supplied page text. Preserve the paper's original language for all
descriptive fields and copy evidence verbatim. Never fill a missing fact from
general knowledge.

The user requires exactly one main Task per paper. Model/algorithm names are not
Tasks. Other activities (data construction, training, evaluation, candidate
screening, computation, experiment) are Stages of that one Task.

Allowed stage_type values:
data_acquisition, data_preparation, label_generation, model_training,
model_evaluation, candidate_generation, candidate_screening,
computational_validation, experimental_validation, other.

Return one JSON object only:
{
  "paper": {
    "title": string|null,
    "year": integer|null,
    "doi": string|null,
    "research_summary": string
  },
  "task": {
    "task_name_raw": string,
    "task_name_canonical": "lowercase_snake_case",
    "objective": string,
    "material_scope": [string],
    "target_properties": [string],
    "constraints": [string],
    "input_requirements": [string],
    "output_goal": [string],
    "evidence": [
      {"text": "verbatim excerpt", "page": integer, "section": string|null, "inferred": false}
    ]
  },
  "stages": [
    {
      "stage_type": "allowed enum",
      "stage_name_raw": string,
      "stage_order": integer,
      "stage_goal": string,
      "stage_input": [string],
      "stage_output": [string],
      "evidence": [
        {"text": "verbatim excerpt", "page": integer, "section": string|null, "inferred": boolean}
      ]
    }
  ]
}

Rules:
- Every Task and Stage needs at least one evidence excerpt and a 1-based PDF page.
- Evidence must be copied exactly from the supplied page, not paraphrased.
- A Stage is an actual step in the paper's R&D workflow, not merely a section title.
- Do not create label_generation merely because a retrieved dataset already has
  labels. Use label_generation only when this paper's authors calculate,
  experimentally measure, or annotate labels as an actual workflow step.
- Put stages in workflow order and number stage_order from 1 without gaps.
- Use [] or null when the paper does not state a field.
- Mark inferred=true only for a relationship directly implied by context; do not
  invent an unsupported stage.
""".strip()


STAGE2_SYSTEM = """
You extract Dataset nodes and DatasetUse relationship events from a paper,
conditioned on the already established single Task and Stages. Use only the
supplied page text. Preserve the original language in descriptions and copy all
evidence verbatim.

A DatasetUse means that this paper actually used this dataset in one specified
stage. A dataset merely cited, compared in related work, or mentioned as
background must not be extracted. Models, algorithms, metrics, software,
instruments, and characterization methods are not datasets.

Candidate material tables/pools may be paper_specific or derived_subset datasets
when the paper actually constructs and uses them, but never label them as public
databases merely because they contain candidates.

Allowed dataset_type:
public_database, public_subset, derived_subset, paper_specific.

Allowed usage_role:
source, training, validation, test, pretraining, label_source, candidate_pool,
screening, benchmark, computational_validation, experimental_validation.

Return one JSON object only:
{
  "datasets": [
    {
      "dataset_key": "short unique key within this response",
      "canonical_name": string,
      "raw_names": [string],
      "dataset_type": "allowed enum",
      "source_dataset_key": string|null,
      "material_scope": [string],
      "available_properties": [string],
      "available_fields": [string],
      "availability": "public|restricted|not_directly_available|unknown",
      "recommendable": boolean,
      "evidence": [
        {"text": "verbatim excerpt", "page": integer, "section": string|null, "inferred": boolean}
      ],
      "confidence": number
    }
  ],
  "dataset_uses": [
    {
      "stage_order": integer,
      "dataset_key": string,
      "usage_role": "allowed enum",
      "purpose": string,
      "used_fields": [string],
      "is_derived": boolean,
      "construction_method": string|null,
      "filter_conditions": [string],
      "sample_count": integer|null,
      "evidence": [
        {"text": "verbatim excerpt", "page": integer, "section": string|null, "inferred": boolean}
      ],
      "confidence": number
    }
  ]
}

Rules:
- Each Dataset and DatasetUse needs verbatim evidence and a 1-based PDF page.
- Evidence must be copied exactly, not paraphrased.
- Every DatasetUse must reference an existing dataset_key and stage_order.
- Create a separate DatasetUse when one dataset is used in different stages.
- Create separate DatasetUse records for multiple datasets in one stage.
- Create exactly one DatasetUse for a given dataset in a given stage. If several
  roles apply there, choose the dominant role and combine the purpose/used_fields.
- Split a public source database from a paper-created derived subset. A
  derived_subset must reference its source_dataset_key, and that public source
  must also be present in datasets.
- paper_specific and derived_subset are normally not directly recommendable.
- sample_count must be a number explicitly printed for that exact dataset or
  subset in the evidence. Never add counts from several benchmark tasks.
- Do not infer fields, counts, construction methods, or availability.
- confidence must be between 0 and 1 and lower when inferred=true.
""".strip()


@dataclass(frozen=True)
class Config:
    project_root: Path
    input_dir: Path
    output_root: Path
    model: str
    base_url: str
    limit: int
    max_chars: int
    retries: int
    resume: bool


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def natural_pdf_key(path: Path) -> tuple[int, str]:
    match = re.match(r"(\d+)", path.stem)
    return (int(match.group(1)) if match else 10**9, path.name.casefold())


def paper_id_from_path(path: Path) -> str:
    match = re.match(r"(\d+)", path.stem)
    if not match:
        raise ValueError(f"PDF has no numeric prefix: {path.name}")
    return f"P{int(match.group(1)):03d}"


def clean_page_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = text.replace("\u00ad", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def guess_section(text: str) -> str | None:
    patterns = [
        r"(?im)^\s*(abstract|introduction|methods?|materials and methods|data(?:set)?(?: availability)?|"
        r"experimental(?: setup| methods?)?|results(?: and discussion)?|supporting information|conclusion)\s*$",
        r"(?im)^\s*\d+(?:\.\d+)*\.?\s+([A-Z][A-Za-z \-/]{2,60})\s*$",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
    return None


def extract_pages(pdf_path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    pages: list[dict[str, Any]] = []
    with fitz.open(pdf_path) as document:
        metadata = dict(document.metadata or {})
        for page_number, page in enumerate(document, start=1):
            text = clean_page_text(page.get_text("text"))
            blocks = []
            for block in page.get_text("blocks"):
                if len(block) >= 5:
                    block_text = clean_page_text(str(block[4]))
                    if block_text:
                        blocks.append(block_text)
            pages.append(
                {
                    "page": page_number,
                    "text": text,
                    "blocks": blocks,
                    "section_hint": guess_section(text),
                    "char_count": len(text),
                }
            )
    return pages, metadata


def page_score(page: dict[str, Any], keywords: tuple[str, ...], first_page_bonus: bool = True) -> int:
    lowered = page["text"].casefold()
    score = sum(lowered.count(keyword) for keyword in keywords)
    if first_page_bonus and page["page"] <= 4:
        score += 40 - page["page"]
    if page.get("section_hint"):
        score += 5
    return score


def select_pages(
    pages: list[dict[str, Any]],
    keywords: tuple[str, ...],
    max_chars: int,
    required_pages: Iterable[int] = (),
) -> list[dict[str, Any]]:
    selected_numbers = {page["page"] for page in pages[:4]}
    selected_numbers.update(int(number) for number in required_pages)
    ranked = sorted(pages, key=lambda page: (-page_score(page, keywords), page["page"]))
    used = sum(len(page["text"]) for page in pages if page["page"] in selected_numbers)
    for page in ranked:
        if page["page"] in selected_numbers:
            continue
        length = len(page["text"])
        if used + length > max_chars and selected_numbers:
            continue
        selected_numbers.add(page["page"])
        used += length
    return [page for page in pages if page["page"] in selected_numbers]


def render_pages(pages: list[dict[str, Any]]) -> str:
    chunks = []
    for page in pages:
        section = page.get("section_hint") or "unknown"
        chunks.append(f"\n===== PDF PAGE {page['page']} | SECTION HINT: {section} =====\n{page['text']}")
    return "\n".join(chunks).strip()


def normalize_for_match(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u00ad", "")
    text = re.sub(r"(?<=\w)-\s+(?=\w)", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().casefold()


def evidence_matches(excerpt: str, page_text: str) -> tuple[bool, float]:
    needle = normalize_for_match(excerpt)
    haystack = normalize_for_match(page_text)
    if not needle or len(needle) < 12:
        return False, 0.0
    if needle in haystack:
        return True, 1.0
    matcher = SequenceMatcher(None, needle, haystack, autojunk=False)
    match = matcher.find_longest_match(0, len(needle), 0, len(haystack))
    sequence_score = match.size / max(1, len(needle))
    excerpt_tokens = re.findall(r"[a-z0-9]+", needle)
    page_tokens = set(re.findall(r"[a-z0-9]+", haystack))
    token_score = (
        sum(1 for token in excerpt_tokens if token in page_tokens) / len(excerpt_tokens)
        if excerpt_tokens else 0.0
    )
    score = max(sequence_score, token_score)
    matched = sequence_score >= 0.88 or (len(excerpt_tokens) >= 8 and token_score >= 0.9)
    return matched, round(score, 4)


def validate_evidence(
    evidence: Any,
    pages_by_number: dict[int, dict[str, Any]],
    location: str,
) -> list[str]:
    errors: list[str] = []
    if not isinstance(evidence, list) or not evidence:
        return [f"{location}.evidence must be a non-empty list"]
    valid_count = 0
    for index, item in enumerate(evidence):
        prefix = f"{location}.evidence[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        page = item.get("page")
        text = item.get("text")
        if not isinstance(page, int) or page not in pages_by_number:
            item["_evidence_valid"] = False
            continue
        if not isinstance(text, str):
            item["_evidence_valid"] = False
            continue
        matched, score = evidence_matches(text, pages_by_number[page]["text"])
        if not matched:
            best_page, best_score = None, 0.0
            for candidate_page, candidate in pages_by_number.items():
                candidate_matched, candidate_score = evidence_matches(text, candidate["text"])
                if candidate_matched and candidate_score > best_score:
                    best_page, best_score = candidate_page, candidate_score
            if best_page is not None:
                item["page"] = best_page
                matched, score = True, best_score
        item["_match_score"] = score
        item["_evidence_valid"] = matched
        if matched:
            valid_count += 1
    if valid_count == 0:
        errors.append(f"{location}.evidence has no excerpt matching its stated PDF page")
    return errors


def validate_string_list(value: Any, location: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        return [f"{location} must be a list of strings"]
    return []


def sanitize_stage2_result(result: Any) -> None:
    if not isinstance(result, dict) or not isinstance(result.get("datasets"), list):
        return
    datasets = [item for item in result["datasets"] if isinstance(item, dict)]
    key_by_name = {}
    for dataset in datasets:
        key = dataset.get("dataset_key")
        if not isinstance(key, str):
            continue
        for name in [dataset.get("canonical_name"), *(dataset.get("raw_names") or [])]:
            if isinstance(name, str) and name.strip():
                key_by_name[name.strip().casefold()] = key
    keys = {item.get("dataset_key") for item in datasets}
    for dataset in datasets:
        source = dataset.get("source_dataset_key")
        if isinstance(source, str) and source not in keys:
            resolved = key_by_name.get(source.strip().casefold())
            if resolved:
                dataset["source_dataset_key"] = resolved
        if dataset.get("dataset_type") == "derived_subset" and dataset.get("source_dataset_key") not in keys:
            dataset["dataset_type"] = "paper_specific"
            dataset["source_dataset_key"] = None
            dataset["recommendable"] = False
    uses = result.get("dataset_uses")
    if not isinstance(uses, list):
        return
    merged = {}
    order = []
    for use in uses:
        if not isinstance(use, dict):
            continue
        pair = (use.get("stage_order"), use.get("dataset_key"))
        if pair not in merged:
            merged[pair] = use
            order.append(pair)
            continue
        target = merged[pair]
        target["used_fields"] = unique_strings(target.get("used_fields", []), use.get("used_fields", []))
        target["filter_conditions"] = unique_strings(target.get("filter_conditions", []), use.get("filter_conditions", []))
        target["evidence"] = list(target.get("evidence", [])) + list(use.get("evidence", []))
        target["is_derived"] = bool(target.get("is_derived") or use.get("is_derived"))
        purposes = unique_strings([target.get("purpose")], [use.get("purpose")])
        target["purpose"] = " / ".join(purposes)
        methods = unique_strings([target.get("construction_method")], [use.get("construction_method")])
        target["construction_method"] = " / ".join(methods) if methods else None
        if target.get("sample_count") != use.get("sample_count"):
            target["sample_count"] = None
        try:
            target["confidence"] = min(float(target.get("confidence", 0.5)), float(use.get("confidence", 0.5)))
        except (TypeError, ValueError):
            target["confidence"] = 0.5
    result["dataset_uses"] = [merged[pair] for pair in order]


def validate_stage1(result: Any, pages: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    if not isinstance(result, dict):
        return ["root must be an object"]
    pages_by_number = {page["page"]: page for page in pages}
    paper = result.get("paper")
    task = result.get("task")
    stages = result.get("stages")
    if not isinstance(paper, dict):
        errors.append("paper must be an object")
    if not isinstance(task, dict):
        errors.append("task must be an object")
    else:
        for key in ("task_name_raw", "task_name_canonical", "objective"):
            if not isinstance(task.get(key), str) or not task[key].strip():
                errors.append(f"task.{key} must be a non-empty string")
        for key in ("material_scope", "target_properties", "constraints", "input_requirements", "output_goal"):
            errors.extend(validate_string_list(task.get(key), f"task.{key}"))
        errors.extend(validate_evidence(task.get("evidence"), pages_by_number, "task"))
    if not isinstance(stages, list) or not stages:
        errors.append("stages must be a non-empty list")
    else:
        seen_orders = set()
        for index, stage in enumerate(stages):
            location = f"stages[{index}]"
            if not isinstance(stage, dict):
                errors.append(f"{location} must be an object")
                continue
            if stage.get("stage_type") not in STAGE_TYPES:
                errors.append(f"{location}.stage_type is not allowed")
            order = stage.get("stage_order")
            if not isinstance(order, int) or order < 1:
                errors.append(f"{location}.stage_order must be a positive integer")
            elif order in seen_orders:
                errors.append(f"{location}.stage_order is duplicated")
            seen_orders.add(order)
            for key in ("stage_name_raw", "stage_goal"):
                if not isinstance(stage.get(key), str) or not stage[key].strip():
                    errors.append(f"{location}.{key} must be a non-empty string")
            for key in ("stage_input", "stage_output"):
                errors.extend(validate_string_list(stage.get(key), f"{location}.{key}"))
            errors.extend(validate_evidence(stage.get("evidence"), pages_by_number, location))
        if seen_orders and seen_orders != set(range(1, len(stages) + 1)):
            errors.append("stage_order must be consecutive from 1")
    return errors


def validate_stage2(
    result: Any,
    pages: list[dict[str, Any]],
    valid_stage_orders: set[int],
) -> list[str]:
    errors: list[str] = []
    if not isinstance(result, dict):
        return ["root must be an object"]
    sanitize_stage2_result(result)
    pages_by_number = {page["page"]: page for page in pages}
    datasets = result.get("datasets")
    uses = result.get("dataset_uses")
    if not isinstance(datasets, list):
        return ["datasets must be a list"]
    if not isinstance(uses, list):
        return ["dataset_uses must be a list"]
    keys: set[str] = set()
    dataset_by_key: dict[str, dict[str, Any]] = {}
    for index, dataset in enumerate(datasets):
        location = f"datasets[{index}]"
        if not isinstance(dataset, dict):
            errors.append(f"{location} must be an object")
            continue
        key = dataset.get("dataset_key")
        if not isinstance(key, str) or not key.strip():
            errors.append(f"{location}.dataset_key must be a non-empty string")
        elif key in keys:
            errors.append(f"{location}.dataset_key is duplicated")
        else:
            keys.add(key)
            dataset_by_key[key] = dataset
        if not isinstance(dataset.get("canonical_name"), str) or not dataset["canonical_name"].strip():
            errors.append(f"{location}.canonical_name must be a non-empty string")
        if dataset.get("dataset_type") not in DATASET_TYPES:
            errors.append(f"{location}.dataset_type is not allowed")
        for field in ("raw_names", "material_scope", "available_properties", "available_fields"):
            errors.extend(validate_string_list(dataset.get(field), f"{location}.{field}"))
        if not isinstance(dataset.get("recommendable"), bool):
            errors.append(f"{location}.recommendable must be boolean")
        confidence = dataset.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            errors.append(f"{location}.confidence must be between 0 and 1")
        errors.extend(validate_evidence(dataset.get("evidence"), pages_by_number, location))
    for index, dataset in enumerate(datasets):
        if not isinstance(dataset, dict):
            continue
        source = dataset.get("source_dataset_key")
        if dataset.get("dataset_type") == "derived_subset":
            if not isinstance(source, str) or source not in keys:
                errors.append(f"datasets[{index}] derived_subset must reference an existing source_dataset_key")
        elif source is not None and source not in keys:
            errors.append(f"datasets[{index}].source_dataset_key does not exist")
    seen_use_pairs: set[tuple[int, str]] = set()
    evidence_valid_uses = []
    for index, use in enumerate(uses):
        location = f"dataset_uses[{index}]"
        if not isinstance(use, dict):
            errors.append(f"{location} must be an object")
            continue
        if use.get("dataset_key") not in keys:
            errors.append(f"{location}.dataset_key does not exist")
        if use.get("stage_order") not in valid_stage_orders:
            errors.append(f"{location}.stage_order does not exist")
        pair = (use.get("stage_order"), use.get("dataset_key"))
        if pair in seen_use_pairs:
            errors.append(f"{location} duplicates a dataset use in the same stage")
        seen_use_pairs.add(pair)
        if use.get("usage_role") not in USAGE_ROLES:
            errors.append(f"{location}.usage_role is not allowed")
        if not isinstance(use.get("purpose"), str) or not use["purpose"].strip():
            errors.append(f"{location}.purpose must be a non-empty string")
        for field in ("used_fields", "filter_conditions"):
            errors.extend(validate_string_list(use.get(field), f"{location}.{field}"))
        if not isinstance(use.get("is_derived"), bool):
            errors.append(f"{location}.is_derived must be boolean")
        sample_count = use.get("sample_count")
        if sample_count is not None and (not isinstance(sample_count, int) or sample_count < 0):
            errors.append(f"{location}.sample_count must be null or a non-negative integer")
        elif isinstance(sample_count, int):
            evidence_text = " ".join(
                str(item.get("text") or "") for item in use.get("evidence", []) if isinstance(item, dict)
            )
            evidence_text = re.sub(r"(?<=\d),(?=\d)", "", evidence_text)
            if str(sample_count) not in evidence_text:
                use["sample_count"] = None
        confidence = use.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            errors.append(f"{location}.confidence must be between 0 and 1")
        use_evidence_errors = validate_evidence(use.get("evidence"), pages_by_number, location)
        if not use_evidence_errors:
            evidence_valid_uses.append(use)
    if len(evidence_valid_uses) != len(uses):
        result["dataset_uses"] = evidence_valid_uses
        uses = evidence_valid_uses
    if uses and not datasets:
        errors.append("dataset_uses cannot exist without datasets")
    return errors


def strip_internal_match_fields(value: Any) -> Any:
    if isinstance(value, dict):
        cleaned = {}
        for key, item in value.items():
            if key in {"_match_score", "_evidence_valid"}:
                continue
            if key == "evidence" and isinstance(item, list):
                item = [entry for entry in item if isinstance(entry, dict) and entry.get("_evidence_valid") is True]
            cleaned[key] = strip_internal_match_fields(item)
        return cleaned
    if isinstance(value, list):
        return [strip_internal_match_fields(item) for item in value]
    return value


def extract_json_object(raw: str) -> dict[str, Any]:
    text = (raw or "").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)
    try:
        parsed = json.loads(text, strict=False)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end <= start:
            raise
        parsed = json.loads(text[start : end + 1], strict=False)
    if not isinstance(parsed, dict):
        raise ValueError("Model response is not a JSON object")
    return parsed


def call_model(
    client: OpenAI,
    model: str,
    system_prompt: str,
    user_prompt: str,
) -> tuple[str, dict[str, Any]]:
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        max_tokens=12000,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    raw = response.choices[0].message.content or ""
    return raw, extract_json_object(raw)


def call_with_validation(
    *,
    client: OpenAI,
    config: Config,
    artifact_dir: Path,
    phase: str,
    system_prompt: str,
    base_user_prompt: str,
    validator: Any,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    attempts: list[dict[str, Any]] = []
    prior_raw = ""
    prior_errors: list[str] = []
    last_exception: Exception | None = None
    for attempt in range(1, config.retries + 2):
        if attempt == 1:
            user_prompt = base_user_prompt
        else:
            user_prompt = (
                base_user_prompt
                + "\n\nYOUR PREVIOUS RESPONSE FAILED VALIDATION.\n"
                + "\n".join(f"- {error}" for error in prior_errors[:80])
                + "\nReturn a complete corrected JSON object. Copy evidence exactly from the pages."
                + f"\n\nPrevious response:\n{prior_raw[:50000]}"
            )
        try:
            raw, parsed = call_model(client, config.model, system_prompt, user_prompt)
            write_text(artifact_dir / f"{phase}_attempt_{attempt}_raw.txt", raw)
            write_json(artifact_dir / f"{phase}_attempt_{attempt}_parsed.json", parsed)
            errors = validator(parsed)
            attempts.append({"attempt": attempt, "errors": errors, "exception": None})
            write_json(artifact_dir / f"{phase}_attempt_{attempt}_validation.json", attempts[-1])
            if not errors:
                return strip_internal_match_fields(parsed), attempts
            prior_raw = raw
            prior_errors = errors
        except Exception as exc:
            last_exception = exc
            prior_errors = [f"{type(exc).__name__}: {exc}"]
            attempts.append({"attempt": attempt, "errors": prior_errors, "exception": repr(exc)})
            write_json(artifact_dir / f"{phase}_attempt_{attempt}_validation.json", attempts[-1])
        if attempt <= config.retries:
            time.sleep(min(2**attempt, 8))
    message = f"{phase} failed after {config.retries + 1} attempts"
    if last_exception:
        message += f": {last_exception}"
    elif prior_errors:
        message += ": " + "; ".join(prior_errors[:5])
    raise RuntimeError(message)


def load_valid_cached_attempt(artifact_dir: Path, phase: str, validator: Any) -> dict[str, Any] | None:
    for raw_path in reversed(sorted(artifact_dir.glob(f"{phase}_attempt_*_raw.txt"))):
        try:
            parsed = extract_json_object(raw_path.read_text(encoding="utf-8"))
            errors = validator(parsed)
            if not errors:
                return strip_internal_match_fields(parsed)
        except Exception:
            continue
    return None


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", ascii_value).strip("_").casefold()
    if not slug:
        slug = "unnamed"
    return slug[:100]


def unique_strings(*values: Iterable[Any]) -> list[str]:
    result: list[str] = []
    seen = set()
    for collection in values:
        for value in collection or []:
            if value is None:
                continue
            text = str(value).strip()
            key = text.casefold()
            if text and key not in seen:
                seen.add(key)
                result.append(text)
    return result


def clamp_confidence(value: Any, evidence: list[dict[str, Any]]) -> float:
    try:
        confidence = float(value)
    except (TypeError, ValueError):
        confidence = 0.5
    confidence = min(1.0, max(0.0, confidence))
    if any(item.get("inferred") is True for item in evidence):
        confidence = min(confidence, 0.79)
    return round(confidence, 4)

# Normalization and wiki generation are defined below.


def paper_metadata_fallback(pdf_path: Path, pages: list[dict[str, Any]], pdf_metadata: dict[str, Any]) -> dict[str, Any]:
    first_text = "\n".join(page["text"] for page in pages[:3])
    title = clean_page_text(str(pdf_metadata.get("title") or ""))
    if not title or title.casefold() in {"untitled", "none"}:
        title = re.sub(r"^\d+_", "", pdf_path.stem).replace("_", " ")
    year_match = re.search(r"\b(19[89]\d|20[0-2]\d)\b", first_text)
    doi_match = re.search(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", first_text, flags=re.IGNORECASE)
    return {
        "title": title,
        "year": int(year_match.group(1)) if year_match else None,
        "doi": doi_match.group(0).rstrip(".,;)") if doi_match else None,
    }


def normalize_evidence(evidence: Any, paper_id: str | None = None) -> list[dict[str, Any]]:
    result = []
    for item in evidence or []:
        if not isinstance(item, dict):
            continue
        row = {
            "text": str(item.get("text") or "").strip(),
            "page": item.get("page"),
            "section": item.get("section"),
            "inferred": bool(item.get("inferred", False)),
        }
        if paper_id is not None:
            row["paper_id"] = paper_id
        result.append(row)
    return result


def dataset_local_identity(dataset: dict[str, Any], paper_id: str) -> str:
    if dataset["dataset_type"] in {"derived_subset", "paper_specific"}:
        return f"{paper_id}:{dataset['dataset_type']}:{slugify(dataset['canonical_name'])}"
    raw_slug = slugify(dataset["canonical_name"])
    canonical_slug = DATASET_ALIAS_GROUPS.get(raw_slug, (raw_slug, dataset["canonical_name"]))[0]
    return f"shared:{canonical_slug}"


def dataset_id_from_identity(identity: str, dataset: dict[str, Any], paper_id: str) -> str:
    name_slug = slugify(dataset["canonical_name"])
    if identity.startswith("shared:"):
        return f"D_{identity.split(':', 1)[1]}"
    return f"D_{paper_id}_{name_slug}"


def normalize_paper_result(
    *, pdf_path: Path, paper_id: str, stage1: dict[str, Any], stage2: dict[str, Any],
    pages: list[dict[str, Any]], pdf_metadata: dict[str, Any],
) -> dict[str, Any]:
    fallback = paper_metadata_fallback(pdf_path, pages, pdf_metadata)
    model_paper = stage1.get("paper") or {}
    paper = {
        "paper_id": paper_id,
        "title": model_paper.get("title") or fallback["title"],
        "year": model_paper.get("year") or fallback["year"],
        "doi": model_paper.get("doi") or fallback["doi"],
        "file_name": pdf_path.name,
        "research_summary": str(model_paper.get("research_summary") or "").strip(),
        "extraction_status": "completed",
    }
    raw_task = stage1["task"]
    task_id = f"T_{paper_id}_01"
    task = {
        "task_id": task_id, "paper_id": paper_id,
        "task_name_raw": raw_task["task_name_raw"].strip(),
        "task_name_canonical": slugify(raw_task["task_name_canonical"]),
        "objective": raw_task["objective"].strip(),
        "material_scope": unique_strings(raw_task.get("material_scope", [])),
        "target_properties": unique_strings(raw_task.get("target_properties", [])),
        "constraints": unique_strings(raw_task.get("constraints", [])),
        "input_requirements": unique_strings(raw_task.get("input_requirements", [])),
        "output_goal": unique_strings(raw_task.get("output_goal", [])),
        "parent_task_id": None, "task_level": "main_task",
        "evidence": normalize_evidence(raw_task.get("evidence")),
    }
    stages = []
    stage_id_by_order = {}
    ordered_stages = sorted(stage1["stages"], key=lambda item: item["stage_order"])
    for sequence, raw_stage in enumerate(ordered_stages, start=1):
        stage_id = f"S_{paper_id}_{sequence:02d}"
        stage_id_by_order[raw_stage["stage_order"]] = stage_id
        stages.append({
            "stage_id": stage_id, "paper_id": paper_id, "task_id": task_id,
            "stage_type": raw_stage["stage_type"],
            "stage_name_raw": raw_stage["stage_name_raw"].strip(),
            "stage_order": sequence, "stage_goal": raw_stage["stage_goal"].strip(),
            "stage_input": unique_strings(raw_stage.get("stage_input", [])),
            "stage_output": unique_strings(raw_stage.get("stage_output", [])),
            "evidence": normalize_evidence(raw_stage.get("evidence")),
        })
    raw_datasets = stage2.get("datasets", [])
    identity_by_key, dataset_id_by_key = {}, {}
    dataset_raw_by_key = {item["dataset_key"]: item for item in raw_datasets}
    for raw_dataset in raw_datasets:
        identity = dataset_local_identity(raw_dataset, paper_id)
        identity_by_key[raw_dataset["dataset_key"]] = identity
        dataset_id_by_key[raw_dataset["dataset_key"]] = dataset_id_from_identity(identity, raw_dataset, paper_id)
    datasets = []
    for raw_dataset in raw_datasets:
        source_key = raw_dataset.get("source_dataset_key")
        evidence = normalize_evidence(raw_dataset.get("evidence"), paper_id=paper_id)
        datasets.append({
            "dataset_id": dataset_id_by_key[raw_dataset["dataset_key"]],
            "canonical_name": raw_dataset["canonical_name"].strip(),
            "raw_names": unique_strings([raw_dataset["canonical_name"]], raw_dataset.get("raw_names", [])),
            "dataset_type": raw_dataset["dataset_type"],
            "source_dataset_id": dataset_id_by_key.get(source_key),
            "material_scope": unique_strings(raw_dataset.get("material_scope", [])),
            "available_properties": unique_strings(raw_dataset.get("available_properties", [])),
            "available_fields": unique_strings(raw_dataset.get("available_fields", [])),
            "availability": raw_dataset.get("availability") or "unknown",
            "recommendable": bool(raw_dataset.get("recommendable", False)),
            "evidence": evidence,
            "confidence": clamp_confidence(raw_dataset.get("confidence"), evidence),
            "_identity": identity_by_key[raw_dataset["dataset_key"]],
        })
    dataset_uses = []
    for sequence, raw_use in enumerate(stage2.get("dataset_uses", []), start=1):
        evidence = normalize_evidence(raw_use.get("evidence"))
        raw_dataset = dataset_raw_by_key[raw_use["dataset_key"]]
        is_derived = bool(raw_use.get("is_derived") or raw_dataset.get("dataset_type") == "derived_subset" or raw_dataset.get("source_dataset_key"))
        dataset_uses.append({
            "dataset_use_id": f"DU_{paper_id}_{sequence:03d}",
            "paper_id": paper_id, "task_id": task_id,
            "stage_id": stage_id_by_order[raw_use["stage_order"]],
            "dataset_id": dataset_id_by_key[raw_use["dataset_key"]],
            "usage_role": raw_use["usage_role"], "purpose": raw_use["purpose"].strip(),
            "used_fields": unique_strings(raw_use.get("used_fields", [])),
            "is_derived": is_derived,
            "construction_method": str(raw_use["construction_method"]).strip() if raw_use.get("construction_method") is not None else None,
            "filter_conditions": unique_strings(raw_use.get("filter_conditions", [])),
            "sample_count": raw_use.get("sample_count"), "evidence": evidence,
            "confidence": clamp_confidence(raw_use.get("confidence"), evidence),
        })
    return {"paper": paper, "tasks": [task], "stages": stages, "datasets": datasets, "dataset_uses": dataset_uses}


def merge_dataset(existing: dict[str, Any], incoming: dict[str, Any]) -> None:
    for field in ("raw_names", "material_scope", "available_properties", "available_fields"):
        existing[field] = unique_strings(existing.get(field, []), incoming.get(field, []))
    existing["evidence"] = list(existing.get("evidence", [])) + list(incoming.get("evidence", []))
    rank = {"unknown": 0, "not_directly_available": 1, "restricted": 2, "public": 3}
    if rank.get(incoming.get("availability"), 0) > rank.get(existing.get("availability"), 0):
        existing["availability"] = incoming["availability"]
    existing["recommendable"] = bool(existing.get("recommendable") or incoming.get("recommendable"))
    existing["confidence"] = max(float(existing.get("confidence", 0)), float(incoming.get("confidence", 0)))
    if existing.get("source_dataset_id") is None and incoming.get("source_dataset_id") is not None:
        existing["source_dataset_id"] = incoming["source_dataset_id"]


def consolidate_results(normalized_results: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], ...]:
    papers, tasks, stages, dataset_uses = [], [], [], []
    dataset_by_identity, canonical_id_by_old_id = {}, {}
    for result in normalized_results:
        papers.append(result["paper"])
        tasks.extend(result["tasks"])
        stages.extend(result["stages"])
        for dataset in result["datasets"]:
            identity = dataset_local_identity(dataset, result["paper"]["paper_id"])
            clean_dataset = {key: value for key, value in dataset.items() if not key.startswith("_")}
            old_dataset_id = clean_dataset["dataset_id"]
            clean_dataset["dataset_id"] = dataset_id_from_identity(
                identity, clean_dataset, result["paper"]["paper_id"]
            )
            if identity not in dataset_by_identity:
                dataset_by_identity[identity] = clean_dataset
            else:
                merge_dataset(dataset_by_identity[identity], clean_dataset)
            canonical_id_by_old_id[old_dataset_id] = dataset_by_identity[identity]["dataset_id"]
        dataset_uses.extend(result["dataset_uses"])
    for use in dataset_uses:
        use["dataset_id"] = canonical_id_by_old_id.get(use["dataset_id"], use["dataset_id"])
    merged_uses: dict[tuple[str, str, str], dict[str, Any]] = {}
    merged_order: list[tuple[str, str, str]] = []
    for use in dataset_uses:
        pair = (use["paper_id"], use["stage_id"], use["dataset_id"])
        if pair not in merged_uses:
            merged_uses[pair] = use
            merged_order.append(pair)
            continue
        target = merged_uses[pair]
        target["used_fields"] = unique_strings(target.get("used_fields", []), use.get("used_fields", []))
        target["filter_conditions"] = unique_strings(target.get("filter_conditions", []), use.get("filter_conditions", []))
        target["evidence"] = list(target.get("evidence", [])) + list(use.get("evidence", []))
        target["purpose"] = " / ".join(unique_strings([target.get("purpose")], [use.get("purpose")]))
        methods = unique_strings([target.get("construction_method")], [use.get("construction_method")])
        target["construction_method"] = " / ".join(methods) if methods else None
        target["is_derived"] = bool(target.get("is_derived") or use.get("is_derived"))
        target["confidence"] = min(float(target.get("confidence", 0.5)), float(use.get("confidence", 0.5)))
        if target.get("sample_count") != use.get("sample_count"):
            target["sample_count"] = None
    dataset_uses = [merged_uses[pair] for pair in merged_order]
    for use in dataset_uses:
        if use.get("sample_count") is None:
            continue
        evidence_text = " ".join(str(item.get("text") or "") for item in use.get("evidence", []))
        evidence_digits = re.sub(r"(?<=\d)[,\s](?=\d)", "", evidence_text)
        if str(use["sample_count"]) not in evidence_digits:
            use["sample_count"] = None
    for dataset in dataset_by_identity.values():
        source = dataset.get("source_dataset_id")
        if source:
            dataset["source_dataset_id"] = canonical_id_by_old_id.get(source, source)
        slug = dataset["dataset_id"].removeprefix("D_")
        if slug in DATASET_CANONICAL_DISPLAY:
            dataset["canonical_name"] = DATASET_CANONICAL_DISPLAY[slug]
        if dataset.get("source_dataset_id") and dataset["dataset_type"] == "paper_specific":
            dataset["dataset_type"] = "derived_subset"
            dataset["recommendable"] = False
        if dataset["dataset_id"] in {"D_jarvis_dft_2d", "D_jarvis_dft_3d"}:
            dataset["dataset_type"] = "public_subset"
            dataset["source_dataset_id"] = "D_jarvis_dft"
        if dataset["dataset_id"] in {
            "D_matbench_dielectric", "D_matbench_log_gvrh", "D_matbench_perovskites"
        }:
            dataset["dataset_type"] = "public_subset"
            dataset["source_dataset_id"] = "D_matbench"
        if dataset["dataset_id"] == "D_materials_project_oqmd_matgen_and_icsd_pre_training_pool":
            dataset["dataset_type"] = "paper_specific"
            dataset["availability"] = "not_directly_available"
            dataset["recommendable"] = False
    datasets = sorted(dataset_by_identity.values(), key=lambda item: item["dataset_id"])
    return papers, tasks, stages, datasets, dataset_uses


def make_edge(edge_id: str, source_type: str, source_id: str, relation_type: str,
              target_type: str, target_id: str, confidence: float, paper_id: str) -> dict[str, Any]:
    return {
        "edge_id": edge_id, "source_type": source_type, "source_id": source_id,
        "relation_type": relation_type, "target_type": target_type, "target_id": target_id,
        "confidence": round(float(confidence), 4), "paper_id": paper_id,
    }


def build_edges(papers: list[dict[str, Any]], tasks: list[dict[str, Any]],
                stages: list[dict[str, Any]], datasets: list[dict[str, Any]],
                dataset_uses: list[dict[str, Any]]) -> list[dict[str, Any]]:
    del papers
    edges, sequence_by_paper = [], defaultdict(int)
    def add(paper_id: str, source_type: str, source_id: str, relation_type: str,
            target_type: str, target_id: str, confidence: float) -> None:
        sequence_by_paper[paper_id] += 1
        edge_id = f"E_{paper_id}_{sequence_by_paper[paper_id]:04d}"
        edges.append(make_edge(edge_id, source_type, source_id, relation_type,
                               target_type, target_id, confidence, paper_id))
    for task in tasks:
        add(task["paper_id"], "Paper", task["paper_id"], "REPORTS_TASK", "Task", task["task_id"], 1.0)
    stages_by_task = defaultdict(list)
    for stage in stages:
        stages_by_task[stage["task_id"]].append(stage)
        add(stage["paper_id"], "Task", stage["task_id"], "HAS_STAGE", "Stage", stage["stage_id"], 1.0)
    for task_stages in stages_by_task.values():
        ordered = sorted(task_stages, key=lambda item: item["stage_order"])
        for current, following in zip(ordered, ordered[1:]):
            add(current["paper_id"], "Stage", current["stage_id"], "NEXT_STAGE", "Stage", following["stage_id"], 1.0)
    for use in dataset_uses:
        confidence = use["confidence"]
        add(use["paper_id"], "Task", use["task_id"], "HAS_DATASET_USE", "DatasetUse", use["dataset_use_id"], confidence)
        add(use["paper_id"], "DatasetUse", use["dataset_use_id"], "AT_STAGE", "Stage", use["stage_id"], confidence)
        add(use["paper_id"], "DatasetUse", use["dataset_use_id"], "USES_DATASET", "Dataset", use["dataset_id"], confidence)
        add(use["paper_id"], "DatasetUse", use["dataset_use_id"], "EVIDENCED_BY", "Paper", use["paper_id"], confidence)
    for dataset in datasets:
        if dataset.get("source_dataset_id"):
            paper_ids = sorted({e.get("paper_id") for e in dataset.get("evidence", []) if e.get("paper_id")})
            paper_id = paper_ids[0] if paper_ids else "P000"
            add(paper_id, "Dataset", dataset["dataset_id"], "DERIVED_FROM", "Dataset",
                dataset["source_dataset_id"], dataset["confidence"])
    return edges


def md_list(values: Iterable[Any], empty: str = "- None stated") -> str:
    rows = [f"- {value}" for value in values if value is not None and str(value).strip()]
    return "\n".join(rows) if rows else empty


def md_evidence(evidence: list[dict[str, Any]], default_paper_id: str) -> str:
    chunks = []
    for item in evidence:
        paper_id = item.get("paper_id") or default_paper_id
        section = f", {item['section']}" if item.get("section") else ""
        inferred = " (inferred)" if item.get("inferred") else ""
        excerpt = str(item.get("text") or "").replace("\n", " ").strip()
        chunks.append(f'- {paper_id}, PDF page {item.get("page")}{section}{inferred}: "{excerpt}"')
    return "\n".join(chunks) if chunks else "- None"


def safe_page_name(node_id: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "_", node_id) + ".md"


def build_pages(root: Path, papers: list[dict[str, Any]], tasks: list[dict[str, Any]],
                stages: list[dict[str, Any]], datasets: list[dict[str, Any]],
                uses: list[dict[str, Any]]) -> None:
    paper_by_id = {item["paper_id"]: item for item in papers}
    task_by_id = {item["task_id"]: item for item in tasks}
    stage_by_id = {item["stage_id"]: item for item in stages}
    dataset_by_id = {item["dataset_id"]: item for item in datasets}
    stages_by_task, uses_by_task, uses_by_stage, uses_by_dataset = (defaultdict(list) for _ in range(4))
    for stage in stages:
        stages_by_task[stage["task_id"]].append(stage)
    for use in uses:
        uses_by_task[use["task_id"]].append(use)
        uses_by_stage[use["stage_id"]].append(use)
        uses_by_dataset[use["dataset_id"]].append(use)
    expected_pages = {
        "papers": {item["paper_id"] for item in papers},
        "tasks": {item["task_id"] for item in tasks},
        "stages": {item["stage_id"] for item in stages},
        "datasets": {item["dataset_id"] for item in datasets},
        "dataset_uses": {item["dataset_use_id"] for item in uses},
    }
    for directory, expected_ids in expected_pages.items():
        page_dir = root / "pages" / directory
        for page_path in page_dir.glob("*.md"):
            if page_path.stem not in expected_ids:
                page_path.unlink()
    for paper in papers:
        paper_tasks = [task for task in tasks if task["paper_id"] == paper["paper_id"]]
        body = [
            f"# Paper: {paper['title']}", "", f"- Paper ID: `{paper['paper_id']}`",
            f"- Year: {paper.get('year') or 'Not stated'}", f"- DOI: {paper.get('doi') or 'Not stated'}",
            f"- File: `{paper['file_name']}`", f"- Extraction status: {paper['extraction_status']}",
            "", "## Research summary", "", paper.get("research_summary") or "Not stated.",
            "", "## Tasks", "", md_list(f"{t['task_id']}: {t['task_name_raw']}" for t in paper_tasks), "",
        ]
        write_text(root / "pages/papers" / safe_page_name(paper["paper_id"]), "\n".join(body))
    for task in tasks:
        task_stages = sorted(stages_by_task[task["task_id"]], key=lambda item: item["stage_order"])
        use_lines = []
        for use in uses_by_task[task["task_id"]]:
            stage, dataset = stage_by_id[use["stage_id"]], dataset_by_id[use["dataset_id"]]
            use_lines.append(f"{stage['stage_name_raw']}: {dataset['canonical_name']} ({use['usage_role']}, {use['dataset_use_id']})")
        stage_lines = [f"{s['stage_order']}. {s['stage_name_raw']} (`{s['stage_type']}`)" for s in task_stages]
        body = [
            f"# Task: {task['task_name_raw']}", "", f"- Task ID: `{task['task_id']}`",
            f"- Canonical name: `{task['task_name_canonical']}`", f"- Paper: `{task['paper_id']}`",
            "", "## Objective", "", task["objective"], "", "## Material scope", "", md_list(task["material_scope"]),
            "", "## Target properties", "", md_list(task["target_properties"]), "", "## Constraints", "", md_list(task["constraints"]),
            "", "## Input requirements", "", md_list(task["input_requirements"]), "", "## Output goal", "", md_list(task["output_goal"]),
            "", "## Research stages", "", "\n".join(stage_lines), "", "## Dataset uses", "", md_list(use_lines),
            "", "## Evidence", "", md_evidence(task["evidence"], task["paper_id"]), "",
        ]
        write_text(root / "pages/tasks" / safe_page_name(task["task_id"]), "\n".join(body))
    for stage in stages:
        task = task_by_id[stage["task_id"]]
        dataset_lines = []
        for use in uses_by_stage[stage["stage_id"]]:
            dataset_lines.append(f"{dataset_by_id[use['dataset_id']]['canonical_name']} — {use['usage_role']}: {use['purpose']}")
        body = [
            f"# Stage: {stage['stage_name_raw']}", "", f"- Stage ID: `{stage['stage_id']}`",
            f"- Stage type: `{stage['stage_type']}`", f"- Stage order: {stage['stage_order']}",
            f"- Task: `{task['task_id']}` — {task['task_name_raw']}", "", "## Goal", "", stage["stage_goal"],
            "", "## Input", "", md_list(stage["stage_input"]), "", "## Output", "", md_list(stage["stage_output"]),
            "", "## Datasets used", "", md_list(dataset_lines), "", "## Evidence", "",
            md_evidence(stage["evidence"], stage["paper_id"]), "",
        ]
        write_text(root / "pages/stages" / safe_page_name(stage["stage_id"]), "\n".join(body))
    for use in uses:
        task, stage, dataset = task_by_id[use["task_id"]], stage_by_id[use["stage_id"]], dataset_by_id[use["dataset_id"]]
        body = [
            f"# Dataset Use: {dataset['canonical_name']} in {stage['stage_name_raw']}", "",
            f"- DatasetUse ID: `{use['dataset_use_id']}`", f"- Paper: `{use['paper_id']}`",
            "", "## Research task", "", f"{task['task_name_raw']} (`{task['task_id']}`)",
            "", "## Research stage", "", f"{stage['stage_name_raw']} (`{stage['stage_type']}`, `{stage['stage_id']}`)",
            "", "## Dataset", "", f"{dataset['canonical_name']} (`{dataset['dataset_id']}`)",
            "", "## Usage role", "", use["usage_role"], "", "## Purpose", "", use["purpose"],
            "", "## Used fields", "", md_list(use["used_fields"]), "", "## Construction method", "", use.get("construction_method") or "Not stated.",
            "", "## Filter conditions", "", md_list(use["filter_conditions"]), "", "## Sample count", "", str(use["sample_count"]) if use.get("sample_count") is not None else "Not stated.",
            "", "## Availability", "", f"- Dataset: {dataset['availability']}", f"- Recommendable: {str(dataset['recommendable']).lower()}",
            "", "## Confidence", "", str(use["confidence"]), "", "## Evidence", "", md_evidence(use["evidence"], use["paper_id"]), "",
        ]
        write_text(root / "pages/dataset_uses" / safe_page_name(use["dataset_use_id"]), "\n".join(body))
    for dataset in datasets:
        dataset_uses = uses_by_dataset[dataset["dataset_id"]]
        observed_tasks = unique_strings([task_by_id[u["task_id"]]["task_name_raw"] for u in dataset_uses])
        observed_stages = unique_strings([stage_by_id[u["stage_id"]]["stage_type"] for u in dataset_uses])
        usage_lines = []
        for use in dataset_uses:
            paper, stage = paper_by_id[use["paper_id"]], stage_by_id[use["stage_id"]]
            usage_lines.append(f"{paper['paper_id']} ({paper['title']}): {use['usage_role']} in {stage['stage_name_raw']} — {use['purpose']}")
        source_line = f"- Source dataset: `{dataset['source_dataset_id']}`" if dataset.get("source_dataset_id") else "- Source dataset: None"
        body = [
            f"# Dataset: {dataset['canonical_name']}", "", f"- Dataset ID: `{dataset['dataset_id']}`",
            f"- Dataset type: `{dataset['dataset_type']}`", source_line, f"- Availability: {dataset['availability']}",
            f"- Recommendable: {str(dataset['recommendable']).lower()}", f"- Confidence: {dataset['confidence']}",
            "", "## Raw names", "", md_list(dataset["raw_names"]), "", "## Observed material scopes", "", md_list(dataset["material_scope"]),
            "", "## Observed research tasks", "", md_list(observed_tasks), "", "## Observed research stages", "", md_list(observed_stages),
            "", "## Observed properties", "", md_list(dataset["available_properties"]), "", "## Observed fields", "", md_list(dataset["available_fields"]),
            "", "## Usage evidence", "", md_list(usage_lines), "", "## Dataset evidence", "", md_evidence(dataset["evidence"], ""), "",
        ]
        write_text(root / "pages/datasets" / safe_page_name(dataset["dataset_id"]), "\n".join(body))


def build_registries(root: Path, tasks: list[dict[str, Any]], datasets: list[dict[str, Any]],
                     uses: list[dict[str, Any]]) -> None:
    tasks_by_canonical = defaultdict(list)
    for task in tasks:
        tasks_by_canonical[task["task_name_canonical"]].append(task)
    task_registry = []
    for canonical, members in sorted(tasks_by_canonical.items()):
        task_registry.append({
            "canonical_name": canonical,
            "raw_names": unique_strings([member["task_name_raw"] for member in members]),
            "task_ids": [member["task_id"] for member in members],
            "paper_ids": sorted({member["paper_id"] for member in members}),
        })
    use_count, papers_by_dataset = defaultdict(int), defaultdict(set)
    for use in uses:
        use_count[use["dataset_id"]] += 1
        papers_by_dataset[use["dataset_id"]].add(use["paper_id"])
    dataset_registry = [{
        **dataset,
        "observed_use_count": use_count[dataset["dataset_id"]],
        "paper_ids": sorted(papers_by_dataset[dataset["dataset_id"]]),
    } for dataset in datasets]
    write_jsonl(root / "registry/task_registry.jsonl", task_registry)
    write_jsonl(root / "registry/dataset_registry.jsonl", dataset_registry)
    write_json(root / "registry/stage_taxonomy.json", STAGE_TAXONOMY)


def validate_graph(papers: list[dict[str, Any]], tasks: list[dict[str, Any]],
                   stages: list[dict[str, Any]], datasets: list[dict[str, Any]],
                   uses: list[dict[str, Any]], edges: list[dict[str, Any]]) -> dict[str, Any]:
    errors = []
    paper_ids = {item["paper_id"] for item in papers}
    task_ids = {item["task_id"] for item in tasks}
    stage_ids = {item["stage_id"] for item in stages}
    dataset_ids = {item["dataset_id"] for item in datasets}
    use_ids = {item["dataset_use_id"] for item in uses}
    for task in tasks:
        if task["paper_id"] not in paper_ids:
            errors.append({"type": "missing_paper", "record_id": task["task_id"]})
    for stage in stages:
        if stage["task_id"] not in task_ids:
            errors.append({"type": "missing_task", "record_id": stage["stage_id"]})
    for use in uses:
        for field, valid, kind in (("task_id", task_ids, "task"), ("stage_id", stage_ids, "stage"), ("dataset_id", dataset_ids, "dataset")):
            if use[field] not in valid:
                errors.append({"type": f"missing_{kind}", "record_id": use["dataset_use_id"]})
        if not use.get("evidence"):
            errors.append({"type": "missing_evidence", "record_id": use["dataset_use_id"]})
    for dataset in datasets:
        if dataset.get("source_dataset_id") and dataset["source_dataset_id"] not in dataset_ids:
            errors.append({"type": "missing_source_dataset", "record_id": dataset["dataset_id"]})
    expected = {"Paper": paper_ids, "Task": task_ids, "Stage": stage_ids, "Dataset": dataset_ids, "DatasetUse": use_ids}
    for edge in edges:
        if edge["source_id"] not in expected.get(edge["source_type"], set()):
            errors.append({"type": "invalid_edge_source", "record_id": edge["edge_id"]})
        if edge["target_id"] not in expected.get(edge["target_type"], set()):
            errors.append({"type": "invalid_edge_target", "record_id": edge["edge_id"]})
    return {
        "generated_at": utc_now(), "valid": not errors,
        "counts": {"papers": len(papers), "tasks": len(tasks), "stages": len(stages),
                   "datasets": len(datasets), "dataset_uses": len(uses), "edges": len(edges)},
        "errors": errors,
    }


def prepare_tree(root: Path) -> None:
    directories = ["raw/extractions", "registry", "relations", "pages/papers", "pages/tasks",
                   "pages/stages", "pages/datasets", "pages/dataset_uses", "reports"]
    for directory in directories:
        (root / directory).mkdir(parents=True, exist_ok=True)


def process_paper(*, client: OpenAI, config: Config, pdf_path: Path) -> dict[str, Any]:
    paper_id = paper_id_from_path(pdf_path)
    artifact_dir = config.output_root / "raw/extractions" / paper_id
    normalized_path = artifact_dir / "normalized.json"
    if config.resume and normalized_path.exists():
        print(f"[{paper_id}] resume: using validated normalized extraction", flush=True)
        return read_json(normalized_path)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    print(f"[{paper_id}] extracting page text: {pdf_path.name}", flush=True)
    pages, pdf_metadata = extract_pages(pdf_path)
    write_json(artifact_dir / "pages.json", pages)
    write_json(artifact_dir / "pdf_metadata.json", pdf_metadata)
    if not pages or sum(page["char_count"] for page in pages) < 500:
        raise RuntimeError(f"{paper_id} has insufficient extractable PDF text")
    stage1_pages = select_pages(pages, TASK_KEYWORDS, config.max_chars)
    write_json(artifact_dir / "stage1_candidate_pages.json", {
        "selected_pages": [page["page"] for page in stage1_pages], "total_pages": len(pages),
        "selected_chars": sum(page["char_count"] for page in stage1_pages),
    })
    print(f"[{paper_id}] phase 1/2: Task + Stage", flush=True)
    stage1_prompt = f"Paper file: {pdf_path.name}\nPDF page count: {len(pages)}\n\n{render_pages(stage1_pages)}"
    stage1_validator = lambda result: validate_stage1(result, pages)
    stage1 = load_valid_cached_attempt(artifact_dir, "stage1", stage1_validator) if config.resume else None
    if stage1 is not None:
        stage1_attempts = [{"attempt": "cached", "errors": [], "exception": None}]
        print(f"[{paper_id}] phase 1 recovered from cached validated response", flush=True)
    else:
        stage1, stage1_attempts = call_with_validation(
            client=client, config=config, artifact_dir=artifact_dir, phase="stage1",
            system_prompt=STAGE1_SYSTEM, base_user_prompt=stage1_prompt, validator=stage1_validator,
        )
    write_json(artifact_dir / "stage1_final.json", stage1)
    evidence_pages = {item["page"] for item in stage1["task"].get("evidence", []) if isinstance(item.get("page"), int)}
    for stage in stage1["stages"]:
        evidence_pages.update(item["page"] for item in stage.get("evidence", []) if isinstance(item.get("page"), int))
    stage2_pages = select_pages(pages, DATA_KEYWORDS, config.max_chars, required_pages=evidence_pages)
    write_json(artifact_dir / "stage2_candidate_pages.json", {
        "selected_pages": [page["page"] for page in stage2_pages], "required_from_stage1": sorted(evidence_pages),
        "total_pages": len(pages), "selected_chars": sum(page["char_count"] for page in stage2_pages),
    })
    context = {"task": stage1["task"], "stages": stage1["stages"]}
    print(f"[{paper_id}] phase 2/2: Dataset + DatasetUse", flush=True)
    stage2_prompt = "Validated Task and Stages:\n" + json.dumps(context, ensure_ascii=False, indent=2)
    stage2_prompt += f"\n\nPaper file: {pdf_path.name}\nPDF page count: {len(pages)}\n\n{render_pages(stage2_pages)}"
    valid_orders = {stage["stage_order"] for stage in stage1["stages"]}
    stage2_validator = lambda result: validate_stage2(result, pages, valid_orders)
    stage2 = load_valid_cached_attempt(artifact_dir, "stage2", stage2_validator) if config.resume else None
    if stage2 is not None:
        stage2_attempts = [{"attempt": "cached", "errors": [], "exception": None}]
        print(f"[{paper_id}] phase 2 recovered from cached validated response", flush=True)
    else:
        stage2, stage2_attempts = call_with_validation(
            client=client, config=config, artifact_dir=artifact_dir, phase="stage2",
            system_prompt=STAGE2_SYSTEM, base_user_prompt=stage2_prompt, validator=stage2_validator,
        )
    write_json(artifact_dir / "stage2_final.json", stage2)
    normalized = normalize_paper_result(pdf_path=pdf_path, paper_id=paper_id, stage1=stage1,
                                        stage2=stage2, pages=pages, pdf_metadata=pdf_metadata)
    write_json(normalized_path, normalized)
    write_json(artifact_dir / "status.json", {
        "paper_id": paper_id, "file_name": pdf_path.name, "status": "completed",
        "completed_at": utc_now(), "model": config.model,
        "stage1_attempts": stage1_attempts, "stage2_attempts": stage2_attempts,
        "counts": {key: len(normalized[key]) for key in ("tasks", "stages", "datasets", "dataset_uses")},
    })
    return normalized


def build_wiki(root: Path, results: list[dict[str, Any]], extraction_errors: list[dict[str, Any]],
               manifest: dict[str, Any]) -> dict[str, Any]:
    papers, tasks, stages, datasets, uses = consolidate_results(results)
    edges = build_edges(papers, tasks, stages, datasets, uses)
    write_jsonl(root / "raw/papers.jsonl", papers)
    write_jsonl(root / "raw/tasks.jsonl", tasks)
    write_jsonl(root / "raw/stages.jsonl", stages)
    write_jsonl(root / "raw/datasets.jsonl", datasets)
    write_jsonl(root / "raw/dataset_uses.jsonl", uses)
    build_registries(root, tasks, datasets, uses)
    write_jsonl(root / "relations/edges.jsonl", edges)
    build_pages(root, papers, tasks, stages, datasets, uses)
    report = validate_graph(papers, tasks, stages, datasets, uses, edges)
    report["extraction_error_count"] = len(extraction_errors)
    report["processed_paper_ids"] = [paper["paper_id"] for paper in papers]
    write_json(root / "reports/validation_report.json", report)
    write_jsonl(root / "reports/extraction_errors.jsonl", extraction_errors)
    manifest.update({
        "updated_at": utc_now(), "completed_paper_ids": [paper["paper_id"] for paper in papers],
        "failed_paper_ids": [error["paper_id"] for error in extraction_errors],
        "counts": report["counts"], "validation_valid": report["valid"],
    })
    write_json(root / "raw/manifest.json", manifest)
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a new evidence-grounded LLM Wiki.")
    parser.add_argument("--limit", type=int, default=42)
    parser.add_argument("--max-chars", type=int, default=120_000)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--input-dir", type=Path)
    parser.add_argument("--output-root", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent
    load_dotenv(project_root / ".env")
    input_dir = args.input_dir or (project_root / "数据集论文/无机晶体材料论文语料_公开全文/papers/构建")
    output_root = args.output_root or script_path.parent / "LLMWiki_new"
    input_dir, output_root = input_dir.resolve(), output_root.resolve()
    if not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")
    if args.limit < 1 or args.retries < 0 or args.workers < 1:
        raise ValueError("--limit and --workers must be positive; --retries cannot be negative")
    api_key = os.getenv("QWEN_API_KEY")
    if not api_key:
        raise ValueError("QWEN_API_KEY is not configured in the environment or project .env")
    base_url = os.getenv("QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    model = os.getenv("QWEN_MODEL", "qwen-plus")
    config = Config(project_root, input_dir, output_root, model, base_url, args.limit,
                    args.max_chars, args.retries, args.resume)
    prepare_tree(output_root)
    pdfs = sorted(input_dir.glob("*.pdf"), key=natural_pdf_key)[:config.limit]
    if len(pdfs) < config.limit:
        raise RuntimeError(f"Requested {config.limit} PDFs, but only found {len(pdfs)}")
    selected = [{"paper_id": paper_id_from_path(path), "file_name": path.name, "path": str(path)} for path in pdfs]
    manifest = {
        "schema_version": "1.0", "created_at": utc_now(),
        "standard_source": "材料论文抽取与LLM_Wiki构建规范.md",
        "input_directory": str(input_dir), "output_directory": str(output_root),
        "selection_rule": "First N PDFs by natural numeric filename prefix; original paper numbers retained.",
        "requested_limit": config.limit, "selected_papers": selected, "model": model,
        "base_url": base_url, "page_numbering": "1-based physical PDF page",
        "descriptive_language": "paper original language",
    }
    write_json(output_root / "raw/manifest.json", manifest)
    results, extraction_errors = [], []

    def run_one(pdf_path: Path) -> dict[str, Any]:
        client = OpenAI(api_key=api_key, base_url=base_url, timeout=240.0, max_retries=2)
        return process_paper(client=client, config=config, pdf_path=pdf_path)

    def record_failure(pdf_path: Path, exc: Exception) -> None:
        paper_id = paper_id_from_path(pdf_path)
        error = {"paper_id": paper_id, "file_name": pdf_path.name, "phase": "paper_extraction",
                 "error_type": type(exc).__name__, "error": str(exc), "occurred_at": utc_now()}
        extraction_errors.append(error)
        write_json(output_root / "raw/extractions" / paper_id / "status.json",
                   {"paper_id": paper_id, "file_name": pdf_path.name, "status": "failed", "error": error})
        print(f"[{paper_id}] FAILED: {exc}", flush=True)

    if args.workers == 1:
        work_items = [(path, None) for path in pdfs]
        for index, (pdf_path, _) in enumerate(work_items, start=1):
            print(f"\n=== {index}/{len(pdfs)} {paper_id_from_path(pdf_path)} {pdf_path.name} ===", flush=True)
            try:
                results.append(run_one(pdf_path))
            except Exception as exc:
                record_failure(pdf_path, exc)
            results.sort(key=lambda item: item["paper"]["paper_id"])
            report = build_wiki(output_root, results, extraction_errors, manifest)
            print(f"[aggregate] papers={report['counts']['papers']} datasets={report['counts']['datasets']} "
                  f"uses={report['counts']['dataset_uses']} valid={report['valid']}", flush=True)
    else:
        print(f"Running {len(pdfs)} papers with {args.workers} workers.", flush=True)
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(run_one, path): path for path in pdfs}
            for completed, future in enumerate(as_completed(futures), start=1):
                pdf_path = futures[future]
                try:
                    results.append(future.result())
                except Exception as exc:
                    record_failure(pdf_path, exc)
                results.sort(key=lambda item: item["paper"]["paper_id"])
                extraction_errors.sort(key=lambda item: item["paper_id"])
                report = build_wiki(output_root, results, extraction_errors, manifest)
                print(f"[aggregate {completed}/{len(pdfs)}] papers={report['counts']['papers']} "
                      f"datasets={report['counts']['datasets']} uses={report['counts']['dataset_uses']} "
                      f"valid={report['valid']}", flush=True)
    report = build_wiki(output_root, results, extraction_errors, manifest)
    print("\nCompleted.", flush=True)
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
    return 0 if len(results) == len(pdfs) and report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
