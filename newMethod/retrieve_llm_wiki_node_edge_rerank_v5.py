#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V5: V4 retrieval plus evidence-backed dataset-family expansion and
single-use scoped evidence matching followed by bounded portfolio search.

Default selection mode is scoped. Unknown evidence is reported separately;
the answer is rendered from the support matrix, not unioned registry fields.
The inherited retrieval architecture below is retained for controlled tests.

V3 changes the candidate granularity after graph expansion:

1. Node retrieval:
   only Task / Stage / Dataset pages participate in Dense + BM25 retrieval.
2. Relation completion:
   retrieved Task/Dataset nodes are expanded one hop to incident DatasetUse facts,
   but DatasetUse is treated as supporting evidence rather than as an independent
   ranking candidate.
3. Task-Dataset pair aggregation:
   all DatasetUse facts sharing the same (Task, Dataset) endpoints are merged into
   one relation candidate. A retrieved endpoint may contribute to a pair at most
   once, so a Task-Dataset relation is not rewarded merely for having many
   duplicated/phase-specific DatasetUse records.
4. Pair ranking:
   each Task-Dataset pair receives endpoint RRF evidence, degree-specificity
   attenuation computed on the pair graph, a pair-local semantic score, diversity
   control, and one expensive rerank over only Top-K pair candidates.
5. Dataset ranking:
   reranked Task-Dataset pairs are aggregated to Dataset scores using a decayed
   Top-M evidence score. DatasetUse IDs remain attached as provenance for evidence
   packages and answer generation.

The node index serialization is unchanged from V2, so V3 intentionally keeps the
same NODE_EDGE_INDEX_VERSION and can reuse a V2 4.0 node index built from the same
Wiki fingerprint and embedding model.

This script still reuses retrieve_llm_wiki.py for common data structures,
embedding, BM25, evidence-package generation and legacy set-selection routines.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit, urlunsplit

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

import retrieve_llm_wiki as base
from v5_scoped_selection import select_scoped, scoped_answer, reserve_need_pairs, calibrate_bounded_score, add_domain_routes
from v5_family_evidence import expand_candidates, load_family_overrides, annotate_family_output


NODE_EDGE_INDEX_VERSION = "node-only-hyperedge-rrf-4.0"
DEFAULT_RERANK_MODEL = "qwen3-rerank"
DEFAULT_RERANK_DOCUMENT_CHARS = 8_000

DEFAULT_TASK_SEED_TOP_K = 20
DEFAULT_DATASET_SEED_TOP_K = 20
DEFAULT_STAGE_SEED_TOP_K = 5
DEFAULT_EDGE_TOP_K = 30
DEFAULT_RETRIEVAL_TOP_K = 6

DEFAULT_TASK_NODE_WEIGHT = 0.50
DEFAULT_DATASET_NODE_WEIGHT = 0.35
DEFAULT_STAGE_NODE_WEIGHT = 0.15
DEFAULT_SPECIFICITY_FLOOR = 0.10

# V3 pair-level diversity controls. DatasetUse facts are evidence only; the
# irreversible Top-K cutoff is applied to unique (Task, Dataset) pairs.
DEFAULT_PAIR_TOP_K = 60
DEFAULT_MAX_PAIRS_PER_TASK = 0
DEFAULT_MAX_PAIRS_PER_DATASET = 5
DEFAULT_SUPPORTING_USES_PER_PAIR = 3
DEFAULT_SUPPORTING_PAIRS_PER_DATASET = 3

# Pair-local semantic match is an auxiliary score computed from Dataset facts,
# concise Task context, and aggregated DatasetUse-local facts.
DEFAULT_PAIR_LOCAL_WEIGHT = 0.25

# A Dataset score is based on its strongest few query-relevant Task-Dataset pairs.
DEFAULT_DATASET_PAIR_DECAY_WEIGHTS = (0.70, 0.20, 0.10)


DEFAULT_RERANK_INSTRUCT = (
    "Rank each Task-Dataset relation candidate by how useful it is as historical "
    "evidence for selecting datasets needed to complete the materials R&D query. "
    "Judge the Dataset identity/capabilities and the DatasetUse evidence first: "
    "available properties, available/used fields, usage roles, purposes, filters, "
    "construction method, and explicit constraints. Treat the Task context as a "
    "routing/support signal, not as proof that every Dataset used by that Task is "
    "relevant. A highly similar Task must not make a Dataset relevant when the "
    "Dataset or its actual uses conflict with the requested property/data need. "
    "Multiple DatasetUse facts under the same Task-Dataset pair are corroborating "
    "evidence, not independent candidates. Treat each relation as one possible role "
    "in a multi-dataset workflow. For cross-property transfer learning, a pretraining "
    "source may have labels different from the target properties; do not reject it "
    "only for that reason. Prefer explicit evidence and penalize explicit conflicts."
)


HYPEREDGE_QUERY_REWRITE_SYSTEM = """
You rewrite a user's materials R&D dataset request into a structured retrieval
plan. Return one JSON object only. All extracted material, property, constraint,
task mechanism, input representation, and dataset-role needs must include an
exact support_text substring copied from the user question.

Schema:
{
  "objective": string,
  "material_scope": [{"value": string, "support_text": string}],
  "target_properties": [{"value": string, "support_text": string}],
  "constraints": [{"value": string, "support_text": string}],
  "required_stages": [string],
  "preferred_usage_roles": [string],
  "task_mechanisms": [{"value": string, "support_text": string}],
  "input_representations": [{"value": string, "support_text": string}],
  "dataset_role_needs": [
    {
      "role": "pretraining_source|fine_tuning_target|evaluation_target|label_source|candidate_pool",
      "scale": "large|small|unspecified",
      "property_relation": "same_as_target|different_or_unrelated|unspecified",
      "support_text": string
    }
  ],
  "subtasks": [],
  "dense_queries": [],
  "bm25_queries": []
}

Allowed required_stages:
data_acquisition, data_preparation, label_generation, model_training,
model_evaluation, candidate_generation, candidate_screening,
computational_validation, experimental_validation, other.

Allowed preferred_usage_roles:
source, training, validation, test, pretraining, label_source, candidate_pool,
screening, benchmark, computational_validation, experimental_validation.

Rules:
- The objective must be exactly the original user question. Do not rewrite,
  broaden, specialize, professionalize, or infer the user's need.
- Use concise professional canonical English values.
- support_text must be copied exactly from the question.
- Do not invent a material, property, dataset name, role, scale, constraint,
  numerical range, chemistry, or experimental requirement.
- Extract only what is explicit enough to affect dataset retrieval. Keep a
  field empty when the question does not state it.
- If a phrase is ambiguous, choose the most literal field. If still unsure,
  leave it empty.
- A material_scope item must denote a material class or system. Composition,
  elemental fractions, chemical formula, stoichiometry, crystal/atomic/
  molecular structure and other feature representations belong only in
  input_representations.
- "composition", "chemical formula", "elemental fractions", "structure",
  "graph", "SMILES", and similar model inputs are not material scopes unless
  the phrase also names a material class such as inorganic crystals,
  perovskites, molecules, polymers, or catalysts.
- Site definitions and allowed species such as "A = ...; B = ...; X = ..."
  are constraints on one material system, not separate material scopes.
- target_properties must contain only properties explicitly named by the user.
  Never specialize broad phrases such as "physical properties", "chemical
  properties", "materials properties", or "multiple properties" into a list of
  unstated concrete properties.
- Do not infer required_stages or preferred_usage_roles merely because a model
  is mentioned. Emit them only when training, evaluation, screening, validation
  or another stage/role is explicitly requested.
- Distinguish a pretraining source dataset from a small target dataset.
- If the query explicitly permits source properties to differ from target
  properties, record different_or_unrelated instead of treating them as direct
  target-property requirements.
- Extract an input representation such as elemental fractions only when it is
  explicit in the question.
- dense_queries and bm25_queries are generated deterministically by code; return
  empty arrays for them.
""".strip()



@dataclass
class HyperedgeQueryPlan(base.QueryPlan):
    task_mechanisms: list[str] = field(default_factory=list)
    input_representations: list[str] = field(default_factory=list)
    dataset_role_needs: list[dict[str, str]] = field(default_factory=list)
    dense_query_lanes: dict[str, str] = field(default_factory=dict)
    bm25_query_lanes: dict[str, str] = field(default_factory=dict)


@dataclass
class TaskDatasetPairDiscovery:
    """One unique (Task, Dataset) relation supported by one or more DatasetUse facts."""

    task_id: str
    dataset_id: str
    supporting_use_ids: set[str] = field(default_factory=set)
    node_hits: list[dict[str, Any]] = field(default_factory=list)
    supporting_node_ids: set[str] = field(default_factory=set)
    pair_rrf_score: float = 0.0
    normalized_pair_rrf_score: float = 0.0
    pair_local_score: float = 0.0
    pair_seed_score: float = 0.0
    rerank_score: float = 0.0
    rerank_position: int | None = None

    @property
    def pair_id(self) -> str:
        return f"{self.task_id}::{self.dataset_id}"


@dataclass
class NodeEdgeDatasetCandidate(base.DatasetCandidate):
    """Dataset candidate aggregated from a few top reranked Task-Dataset pairs."""

    aggregated_pair_score: float = 0.0
    supporting_pair_scores: dict[str, float] = field(default_factory=dict)
    supporting_use_scores: dict[str, float] = field(default_factory=dict)


_CURRENT_USE_SCORES: dict[str, float] = {}



def _values(values: Iterable[Any] | Any, limit: int | None = None) -> str:
    """把列表字段稳定序列化；None 和空列表使用明确的 unknown 标记。"""

    if isinstance(values, (str, int, float)):
        items = [str(values)]
    elif isinstance(values, Iterable):
        items = [str(value).strip() for value in values if str(value).strip()]
    else:
        items = []
    if limit is not None:
        items = items[:limit]
    return "; ".join(items) if items else "unknown"


def serialize_task_node(task: dict[str, Any]) -> str:
    """Task 超节点只保留任务核心字段，不重复写入 DatasetUse 列表。"""

    return "\n".join([
        "[NODE TYPE] Task",
        f"[TASK ID] {task['task_id']}",
        f"[TASK NAME] {task.get('task_name_raw') or task.get('task_name_canonical')}",
        f"[OBJECTIVE] {task.get('objective') or 'unknown'}",
        f"[MATERIAL SCOPE] {_values(task.get('material_scope', []))}",
        f"[TARGET PROPERTIES] {_values(task.get('target_properties', []))}",
        f"[CONSTRAINTS] {_values(task.get('constraints', []))}",
        f"[INPUT REQUIREMENTS] {_values(task.get('input_requirements', []))}",
        f"[OUTPUT GOAL] {task.get('output_goal') or 'unknown'}",
    ])


def serialize_stage_node(stage: dict[str, Any]) -> str:
    """Stage 超节点不包含“Datasets used”，避免节点检索提前混入边事实。"""

    return "\n".join([
        "[NODE TYPE] Stage",
        f"[STAGE ID] {stage['stage_id']}",
        f"[STAGE NAME] {stage.get('stage_name_raw') or 'unknown'}",
        f"[STAGE TYPE] {stage.get('stage_type') or 'unknown'}",
        f"[GOAL] {stage.get('stage_goal') or 'unknown'}",
        f"[INPUT] {_values(stage.get('stage_input', []))}",
        f"[OUTPUT] {_values(stage.get('stage_output', []))}",
    ])


def serialize_dataset_node(dataset: dict[str, Any]) -> str:
    """Dataset 超节点只描述数据能力，不写入全部历史 Task/Stage/Usage。"""

    return "\n".join([
        "[NODE TYPE] Dataset",
        f"[DATASET ID] {dataset['dataset_id']}",
        f"[NAME] {dataset.get('canonical_name') or 'unknown'}",
        f"[ALIASES] {_values(dataset.get('raw_names', []))}",
        f"[TYPE] {dataset.get('dataset_type') or 'unknown'}",
        f"[MATERIAL SCOPE] {_values(dataset.get('material_scope', []))}",
        f"[AVAILABLE PROPERTIES] {_values(dataset.get('available_properties', []))}",
        f"[AVAILABLE FIELDS] {_values(dataset.get('available_fields', []))}",
        f"[AVAILABILITY] {dataset.get('availability') or 'unknown'}",
        f"[RECOMMENDABLE] {bool(dataset.get('recommendable', False))}",
    ])


def serialize_dataset_use_hyperedge(
    store: base.WikiStore,
    use: dict[str, Any],
    max_chars: int = DEFAULT_RERANK_DOCUMENT_CHARS,
) -> str:
    """把一条 DatasetUse 与其四个端点组成一个完整、不可拆分的事实文本。"""

    task = store.task_by_id[use["task_id"]]
    stage = store.stage_by_id[use["stage_id"]]
    dataset = store.dataset_by_id[use["dataset_id"]]
    paper = store.paper_by_id[use["paper_id"]]
    evidence = []
    for item in use.get("evidence", [])[:2]:
        if not isinstance(item, dict):
            continue
        text = str(item.get("text") or "").replace("\n", " ").strip()
        evidence.append(
            f"PDF page {item.get('page', 'unknown')}, "
            f"section {item.get('section') or 'unknown'}: {text}"
        )

    # DatasetUse 自身的角色、用途和原文证据放在前面，避免长 Dataset 属性截断
    # 后把最关键的本轮事实丢在文档尾部。
    text = "\n".join([
        "[FACT TYPE] DatasetUse hyperedge",
        f"[DATASET USE ID] {use['dataset_use_id']}",
        f"[USAGE ROLE] {use.get('usage_role') or 'unknown'}",
        f"[PURPOSE] {use.get('purpose') or 'unknown'}",
        f"[USED FIELDS] {_values(use.get('used_fields', []))}",
        f"[FILTER CONDITIONS] {_values(use.get('filter_conditions', []))}",
        f"[CONSTRUCTION METHOD] {use.get('construction_method') or 'unknown'}",
        f"[SAMPLE COUNT] {use.get('sample_count') or 'unknown'}",
        f"[DERIVED DATASET] {bool(use.get('is_derived', False))}",
        "",
        f"[TASK ID] {task['task_id']}",
        f"[TASK] {task.get('task_name_raw') or task.get('task_name_canonical')}",
        f"[TASK OBJECTIVE] {task.get('objective') or 'unknown'}",
        f"[TASK MATERIAL SCOPE] {_values(task.get('material_scope', []))}",
        f"[TASK TARGET PROPERTIES] {_values(task.get('target_properties', []))}",
        f"[TASK CONSTRAINTS] {_values(task.get('constraints', []))}",
        "",
        f"[STAGE ID] {stage['stage_id']}",
        f"[STAGE NAME] {stage.get('stage_name_raw') or 'unknown'}",
        f"[STAGE TYPE] {stage.get('stage_type') or 'unknown'}",
        f"[STAGE GOAL] {stage.get('stage_goal') or 'unknown'}",
        "",
        f"[DATASET ID] {dataset['dataset_id']}",
        f"[DATASET] {dataset.get('canonical_name') or 'unknown'}",
        f"[DATASET TYPE] {dataset.get('dataset_type') or 'unknown'}",
        f"[DATASET MATERIAL SCOPE] {_values(dataset.get('material_scope', []))}",
        f"[DATASET PROPERTIES] {_values(dataset.get('available_properties', []))}",
        f"[DATASET FIELDS] {_values(dataset.get('available_fields', []))}",
        f"[AVAILABILITY] {dataset.get('availability') or 'unknown'}",
        f"[RECOMMENDABLE] {bool(dataset.get('recommendable', False))}",
        "",
        f"[PAPER ID] {paper['paper_id']}",
        f"[PAPER TITLE] {paper.get('title') or 'unknown'}",
        f"[EVIDENCE] {_values(evidence)}",
        f"[CONFIDENCE] {use.get('confidence', 'unknown')}",
    ])
    return text[:max_chars]


def _exact_support_present(support: str, question: str) -> bool:
    normalized_support = re.sub(r"\s+", "", support).casefold()
    normalized_question = re.sub(r"\s+", "", question).casefold()
    return bool(normalized_support) and normalized_support in normalized_question


def _first_support(pattern: str, question: str) -> str:
    match = re.search(pattern, question, flags=re.IGNORECASE)
    return match.group(0) if match else ""


def supported_raw_values(items: Any, question: str) -> list[str]:
    """Keep exact user-supported specific values in addition to canonical values."""

    result: list[str] = []
    for item in items if isinstance(items, list) else []:
        if not isinstance(item, dict):
            continue
        value = str(item.get("value") or "").strip()
        support = str(item.get("support_text") or "").strip()
        if value and support and _exact_support_present(support, question):
            result.append(value)
    return base.unique_strings(result)


def conservative_material_scope(values: list[str]) -> list[str]:
    """Keep only explicit material classes/systems in material_scope.

    Query rewrite models sometimes put inputs such as composition or structure
    into material_scope. That makes later retrieval over-generalize the task, so
    we keep a value only when it names a material domain rather than a feature.
    """

    representation_terms = (
        "composition", "compositions", "chemical formula", "formula",
        "elemental fraction", "elemental fractions", "stoichiometry",
        "stoichiometric", "atomic structure", "crystal structure",
        "molecular structure", "structure", "structures", "graph", "graphs",
        "smiles", "feature", "features", "input", "inputs",
    )
    material_terms = (
        "material", "materials", "crystal", "crystalline", "inorganic",
        "organic", "molecule", "molecular", "polymer", "perovskite",
        "abx", "catalyst", "catalytic", "compound", "compounds", "alloy",
        "oxide", "halide", "solid", "solid-state", "2d", "二维", "晶体",
        "无机", "分子", "催化", "材料", "化合物", "钙钛矿",
    )
    result: list[str] = []
    for value in values:
        text = re.sub(r"\s+", " ", str(value).casefold()).strip()
        if not text:
            continue
        has_material_signal = any(term in text for term in material_terms)
        is_representation_only = (
            any(term in text for term in representation_terms)
            and not has_material_signal
        )
        if is_representation_only:
            continue
        if has_material_signal:
            result.append(value)
    return base.unique_strings(result)


def conservative_target_properties(values: list[str]) -> list[str]:
    """Drop broad property placeholders that cannot identify a dataset."""

    broad_terms = {
        "property", "properties", "material property", "materials property",
        "material properties", "materials properties", "physical property",
        "physical properties", "chemical property", "chemical properties",
        "multiple properties", "diverse properties", "various properties",
        "many properties", "multi property", "multi-property",
        "多种性质", "材料性质", "物理性质", "化学性质",
    }
    result: list[str] = []
    for value in values:
        text = re.sub(r"[_\-]+", " ", str(value).casefold())
        text = re.sub(r"\s+", " ", text).strip()
        if not text or text in broad_terms:
            continue
        if text.endswith(" properties") and len(text.split()) <= 3:
            continue
        result.append(value)
    return base.unique_strings(result)


def conservative_input_representations(values: list[str]) -> list[str]:
    """Remove duplicated canonical/raw representation labels after grounding."""

    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        text = re.sub(r"[_\-]+", " ", str(value).casefold())
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        key = text
        if text in {"elemental fractions", "element fractions"}:
            key = "elemental_fractions"
        if key in seen:
            continue
        seen.add(key)
        result.append(value)
    return result


def explicit_stages_and_roles(question: str) -> tuple[list[str], list[str]]:
    """Deterministically keep only workflow stages/roles explicitly stated by user."""

    q = question.casefold()
    stage_patterns = {
        "data_acquisition": r"data acquisition|collect(?:ion)?|采集|收集",
        "data_preparation": r"data preparation|preprocess|clean(?:ing)?|数据准备|预处理|清洗",
        "label_generation": r"label generation|annotation|标注|标签生成",
        "model_training": r"\btrain(?:ing)?\b|训练",
        "model_evaluation": r"\bevaluat(?:e|ion)\b|\btest(?:ing)?\b|评估|测试",
        "candidate_generation": r"candidate generation|候选生成",
        "candidate_screening": r"\bscreen(?:ing)?\b|筛选",
        "computational_validation": r"computational validation|计算验证",
        "experimental_validation": r"experimental validation|实验验证",
    }
    role_patterns = {
        "source": r"source dataset|source data|源数据集|源数据",
        "training": r"training dataset|training data|训练数据",
        "validation": r"validation dataset|validation data|验证数据",
        "test": r"test dataset|test data|测试数据",
        "pretraining": r"pre[- ]?train|预训练",
        "label_source": r"label source|annotation source|标签来源|标注来源",
        "candidate_pool": r"candidate pool|候选池|候选数据",
        "screening": r"screening dataset|screening data|筛选数据",
        "benchmark": r"benchmark dataset|benchmark data|基准数据",
        "computational_validation": r"computational validation|计算验证",
        "experimental_validation": r"experimental validation|实验验证",
    }
    stages = [name for name, pattern in stage_patterns.items() if re.search(pattern, q, flags=re.I)]
    roles = [name for name, pattern in role_patterns.items() if re.search(pattern, q, flags=re.I)]
    return stages, roles


def specific_task_mechanisms(values: list[str]) -> list[str]:
    """Remove generic mechanism words from independent retrieval lanes."""

    generic = {
        "prediction", "predict", "modeling", "modelling", "machine learning",
        "deep learning", "regression",
    }
    return [value for value in values if value.casefold().strip() not in generic]


def normalize_dataset_role_needs(items: Any, question: str) -> list[dict[str, str]]:
    """Validate online source/target role needs against exact user evidence."""

    allowed_roles = {
        "pretraining_source", "fine_tuning_target", "evaluation_target",
        "label_source", "candidate_pool",
    }
    allowed_scales = {"large", "small", "unspecified"}
    allowed_relations = {
        "same_as_target", "different_or_unrelated", "unspecified",
    }
    result: list[dict[str, str]] = []
    for item in items if isinstance(items, list) else []:
        if not isinstance(item, dict):
            continue
        role = str(item.get("role") or "").strip()
        scale = str(item.get("scale") or "unspecified").strip()
        relation = str(item.get("property_relation") or "unspecified").strip()
        support = str(item.get("support_text") or "").strip()
        if role not in allowed_roles or not _exact_support_present(support, question):
            continue
        support_lower = support.casefold()
        question_lower = question.casefold()
        role_is_explicit = {
            "pretraining_source": bool(
                re.search(r"pre[- ]?train|source datasets?|预训练|源数据集", support_lower)
                or (
                    re.search(r"source datasets?|源数据集", support_lower)
                    and re.search(r"pre[- ]?train|transfer learning|预训练|迁移学习", question_lower)
                )
            ),
            "fine_tuning_target": bool(
                re.search(r"fine[- ]?tun|target datasets?|微调|目标数据集", support_lower)
                and re.search(r"fine[- ]?tun|transfer|pre[- ]?train|微调|迁移|预训练", question_lower)
            ),
            "evaluation_target": bool(
                re.search(r"evaluat|test|benchmark|validat|评估|测试|基准|验证", support_lower)
            ),
            "label_source": bool(
                re.search(r"label|annotation|标签|标注", support_lower)
            ),
            "candidate_pool": bool(
                re.search(r"candidate|screen|候选|筛选", support_lower)
            ),
        }[role]
        if not role_is_explicit:
            continue
        # Scale and property relation are derived only from explicit wording,
        # rather than trusting a possibly over-specific LLM value.
        if re.search(r"\blarge\b|大规模|大型", support_lower):
            scale = "large"
        elif re.search(r"\bsmall\b|小规模|小样本", support_lower):
            scale = "small"
        else:
            scale = "unspecified"
        if role == "pretraining_source" and re.search(
            r"different|unrelated|不同|无关", question_lower
        ):
            relation = "different_or_unrelated"
        elif role in {"fine_tuning_target", "evaluation_target"}:
            relation = "same_as_target"
        else:
            relation = "unspecified"
        if scale not in allowed_scales:
            scale = "unspecified"
        if relation not in allowed_relations:
            relation = "unspecified"
        row = {
            "role": role,
            "scale": scale,
            "property_relation": relation,
            "support_text": support,
        }
        if row not in result:
            result.append(row)
    return result


def add_grounded_semantic_fallbacks(
    question: str,
    mechanisms: list[str],
    inputs: list[str],
    role_needs: list[dict[str, str]],
) -> tuple[list[str], list[str], list[dict[str, str]]]:
    """Recover explicit workflow signals if the rewrite model omits them."""

    transfer_support = _first_support(
        r"knowledge transferred|transfer learning|transferred|\u8fc1\u79fb\u5b66\u4e60",
        question,
    )
    pretrain_support = _first_support(r"pre[- ]?trained|pretraining|\u9884\u8bad\u7ec3", question)
    different_support = _first_support(
        r"different(?:/unrelated)?|unrelated|\u4e0d\u540c|\u65e0\u5173",
        question,
    )
    if transfer_support and pretrain_support:
        mechanism = (
            "cross_property_transfer_learning"
            if different_support else "transfer_learning"
        )
        mechanisms = base.unique_strings([*mechanisms, mechanism])

    elemental_support = _first_support(
        r"elemental fractions?|element fractions?|\u5143\u7d20\u5206\u6570|\u5143\u7d20\u6bd4\u4f8b",
        question,
    )
    if elemental_support:
        inputs = base.unique_strings([*inputs, "elemental_fractions"])

    source_support = _first_support(r"(?:large )?source datasets?", question)
    target_support = _first_support(r"(?:small )?target datasets?", question)
    if source_support and not any(x["role"] == "pretraining_source" for x in role_needs):
        role_needs.append({
            "role": "pretraining_source",
            "scale": "large" if "large" in source_support.casefold() else "unspecified",
            "property_relation": (
                "different_or_unrelated" if different_support else "unspecified"
            ),
            "support_text": source_support,
        })
    if target_support and not any(x["role"] == "fine_tuning_target" for x in role_needs):
        role_needs.append({
            "role": "fine_tuning_target",
            "scale": "small" if "small" in target_support.casefold() else "unspecified",
            "property_relation": "same_as_target",
            "support_text": target_support,
        })
    return mechanisms, inputs, role_needs


def controlled_property_aliases(prop: str) -> list[str]:
    """Controlled aliases are retrieval-only and never change the user target."""

    text = re.sub(r"[_-]+", " ", prop.casefold()).strip()
    aliases = [prop]
    if "band" in text and "gap" in text:
        aliases.extend(["band gap", "bandgap", "Bg"])
    if "exfoli" in text:
        aliases.extend(["exfoliation energy", "Exfoli"])
    if "dielectric" in text or "permittivity" in text:
        aliases.extend([
            "dielectric constant", "dielectric tensor", "permittivity",
            "PolyTotal", "Poly Elec",
        ])
    if "thermoelectric" in text:
        aliases.extend(["thermoelectric coefficient", "ETC"])
    return base.unique_strings(aliases)


def build_stratified_queries(
    plan: HyperedgeQueryPlan,
) -> tuple[list[str], list[str], list[str], dict[str, str], dict[str, str]]:
    """Build a small number of semantically distinct retrieval lanes.

    Multiple rewrites from the same intent lane are allowed, but node-level RRF
    later keeps only the strongest vote per (node, retrieval-mode, lane). This
    prevents correlated query rewrites from repeatedly rewarding the same node.
    """

    # The first material is intentionally the most specific user-supported form
    # inserted by rewrite_hyperedge_query. If the user did not name a material
    # domain, keep the lane unanchored instead of inventing "materials", which
    # otherwise over-rewards broad public databases.
    material = plan.material_scope[0] if plan.material_scope else ""
    properties = " ".join(plan.target_properties)
    mechanisms = " ".join(
        value.replace("_", " ")
        for value in specific_task_mechanisms(plan.task_mechanisms)
    )
    stages = " ".join(plan.required_stages)
    roles = " ".join(plan.preferred_usage_roles)

    dense: list[str] = []
    bm25: list[str] = []
    subtasks: list[str] = []
    dense_lanes: dict[str, str] = {}
    bm25_lanes: dict[str, str] = {}

    def add(target: list[str], lane_map: dict[str, str], query: str, lane: str) -> None:
        value = re.sub(r"\s+", " ", query).strip()
        if not value or value in target:
            return
        target.append(value)
        lane_map[value] = lane

    def phrase(*parts: str) -> str:
        return re.sub(r"\s+", " ", " ".join(part for part in parts if part)).strip()

    add(dense, dense_lanes, plan.objective, "objective")

    if properties:
        add(
            dense,
            dense_lanes,
            phrase(material, properties, "dataset"),
            "material_property",
        )
        for prop in plan.target_properties[:2]:
            add(
                bm25,
                bm25_lanes,
                phrase(material, " ".join(controlled_property_aliases(prop)), "dataset"),
                "material_property",
            )

    if mechanisms:
        mechanism_query = phrase(material, mechanisms, "dataset")
        add(dense, dense_lanes, mechanism_query, "mechanism")
        add(bm25, bm25_lanes, mechanism_query, "mechanism")
        subtasks.append(mechanism_query)

    if "elemental_fractions" in plan.input_representations:
        input_query = phrase(
            material,
            "elemental fractions composition chemical formula "
            "stoichiometric composition dataset",
        )
        add(dense, dense_lanes, input_query, "input")
        add(bm25, bm25_lanes, input_query, "input")
        subtasks.append(input_query)
    elif plan.input_representations:
        input_query = phrase(material, " ".join(plan.input_representations), "dataset")
        add(dense, dense_lanes, input_query, "input")
        add(bm25, bm25_lanes, input_query, "input")
        subtasks.append(input_query)

    source_queries: list[str] = []
    target_queries: list[str] = []
    for need in plan.dataset_role_needs:
        if need["role"] == "pretraining_source":
            relation = need["property_relation"].replace("_", " ")
            query = phrase(
                material,
                need["scale"],
                "source dataset pretraining",
                relation,
                "properties",
            )
            source_queries.append(query)
            add(dense, dense_lanes, query, "source_target")
            add(bm25, bm25_lanes, query, "source_target")
        elif need["role"] in {"fine_tuning_target", "evaluation_target"}:
            source_role = need["role"].replace("_", " ")
            query = phrase(material, need["scale"], source_role, "dataset", properties)
            target_queries.append(query)
            add(dense, dense_lanes, query, "source_target")
            add(bm25, bm25_lanes, query, "source_target")

    # Workflow queries are emitted only after deterministic explicit-evidence
    # filtering in rewrite_hyperedge_query.
    if stages:
        stage_query = phrase(material, stages, "dataset")
        add(dense, dense_lanes, stage_query, "workflow")
        add(bm25, bm25_lanes, stage_query, "workflow")
        subtasks.append(stage_query)
    if roles:
        role_query = phrase(material, roles, "dataset")
        add(dense, dense_lanes, role_query, "workflow")
        subtasks.append(role_query)

    subtasks.extend(source_queries)
    subtasks.extend(target_queries)
    subtasks.extend(
        phrase("dataset for", material, prop) for prop in plan.target_properties
    )

    dense = dense[:8]
    bm25 = bm25[:10]
    dense_lanes = {q: dense_lanes[q] for q in dense}
    bm25_lanes = {q: bm25_lanes[q] for q in bm25}
    subtasks = base.unique_strings(subtasks)[:12]
    return dense, bm25, subtasks, dense_lanes, bm25_lanes


def rewrite_hyperedge_query(
    client: OpenAI,
    model: str,
    question: str,
) -> tuple[HyperedgeQueryPlan, str]:
    """Extract workflow semantics while retaining exact user-specific details."""

    response = client.chat.completions.create(
        model=model,
        temperature=0,
        max_tokens=3200,
        messages=[
            {"role": "system", "content": HYPEREDGE_QUERY_REWRITE_SYSTEM},
            {"role": "user", "content": question},
        ],
    )
    raw = response.choices[0].message.content or ""
    value = base.parse_json_object(raw)
    core = base.normalize_query_plan(value, question)

    # Preserve exact user-supported specific concepts *before* canonical parents.
    # E.g. "mixed ABX3 perovskites" + "perovskite" instead of losing ABX3.
    specific_materials = supported_raw_values(value.get("material_scope"), question)
    specific_properties = supported_raw_values(value.get("target_properties"), question)
    core.material_scope = conservative_material_scope(
        base.unique_strings([*specific_materials, *core.material_scope])
    )
    core.target_properties = conservative_target_properties(
        base.unique_strings([*specific_properties, *core.target_properties])
    )

    # Never trust the LLM alone for workflow stages/roles: keep only terms that
    # are explicitly present in the original user question.
    explicit_stages, explicit_roles = explicit_stages_and_roles(question)
    core.required_stages = explicit_stages
    core.preferred_usage_roles = explicit_roles

    mechanisms = base.normalize_supported_items(
        value.get("task_mechanisms"), question
    )
    inputs = base.normalize_supported_items(
        value.get("input_representations"), question
    )
    role_needs = normalize_dataset_role_needs(
        value.get("dataset_role_needs"), question
    )
    mechanisms, inputs, role_needs = add_grounded_semantic_fallbacks(
        question, mechanisms, inputs, role_needs
    )
    inputs = conservative_input_representations(inputs)

    plan = HyperedgeQueryPlan(
        **asdict(core),
        task_mechanisms=mechanisms,
        input_representations=inputs,
        dataset_role_needs=role_needs,
    )
    dense, bm25, subtasks, dense_lanes, bm25_lanes = build_stratified_queries(plan)
    plan.dense_queries = dense
    plan.bm25_queries = bm25
    plan.subtasks = subtasks
    plan.dense_query_lanes = dense_lanes
    plan.bm25_query_lanes = bm25_lanes
    return plan, raw


def serialize_query_for_rerank(question: str, plan: base.QueryPlan) -> str:
    """把原问题和经过校验的 QueryPlan 组合为专用 rerank 查询。"""

    return "\n".join([
        "[USER QUESTION]",
        question,
        "",
        "[OBJECTIVE]",
        plan.objective,
        "",
        f"[MATERIAL SCOPE] {_values(plan.material_scope)}",
        f"[TARGET PROPERTIES] {_values(plan.target_properties)}",
        f"[CONSTRAINTS] {_values(plan.constraints)}",
        f"[REQUIRED STAGES] {_values(plan.required_stages)}",
        f"[PREFERRED DATASET ROLES] {_values(plan.preferred_usage_roles)}",
        f"[TASK MECHANISMS] {_values(getattr(plan, 'task_mechanisms', []))}",
        f"[INPUT REPRESENTATIONS] {_values(getattr(plan, 'input_representations', []))}",
        (
            "[SOURCE/TARGET DATASET NEEDS] "
            f"{json.dumps(getattr(plan, 'dataset_role_needs', []), ensure_ascii=False)}"
        ),
        f"[SUBTASKS] {_values(plan.subtasks)}",
    ])


# ---------------------------------------------------------------------------
# 1. Node-only index
# ---------------------------------------------------------------------------

def build_node_documents(
    store: base.WikiStore,
    max_chars: int = DEFAULT_RERANK_DOCUMENT_CHARS,
) -> list[base.SearchDocument]:
    """Index only Task, Stage and Dataset nodes. DatasetUse is never indexed."""

    documents: list[base.SearchDocument] = []

    for task in store.tasks:
        documents.append(base.SearchDocument(
            doc_id=task["task_id"],
            entity_id=task["task_id"],
            node_type="Task",
            text=serialize_task_node(task)[:max_chars],
            paper_id=task["paper_id"],
            task_id=task["task_id"],
            source_path=str(store.root / "pages/tasks" / f"{task['task_id']}.md"),
        ))

    for stage in store.stages:
        documents.append(base.SearchDocument(
            doc_id=stage["stage_id"],
            entity_id=stage["stage_id"],
            node_type="Stage",
            text=serialize_stage_node(stage)[:max_chars],
            paper_id=stage["paper_id"],
            task_id=stage["task_id"],
            stage_id=stage["stage_id"],
            stage_type=stage["stage_type"],
            source_path=str(store.root / "pages/stages" / f"{stage['stage_id']}.md"),
        ))

    # All Dataset nodes are indexed. recommendable/availability are evidence
    # attributes, not retrieval gates. This keeps retrieval evaluation separate
    # from downstream usability preferences.
    for dataset in store.datasets:
        documents.append(base.SearchDocument(
            doc_id=dataset["dataset_id"],
            entity_id=dataset["dataset_id"],
            node_type="Dataset",
            text=serialize_dataset_node(dataset)[:max_chars],
            dataset_id=dataset["dataset_id"],
            availability=dataset.get("availability"),
            recommendable=dataset.get("recommendable", False),
            source_path=str(
                store.root / "pages/datasets" / f"{dataset['dataset_id']}.md"
            ),
        ))

    return documents


def build_node_index(
    store: base.WikiStore,
    client: OpenAI,
    index_dir: Path,
    embedding_model: str,
    batch_size: int,
    max_chars: int,
) -> tuple[list[base.SearchDocument], np.ndarray, dict[str, Any]]:
    documents = build_node_documents(store, max_chars)
    print(f"Building node-only embeddings for {len(documents)} nodes...", flush=True)
    embeddings = base.embed_texts(
        client,
        embedding_model,
        [document.text for document in documents],
        batch_size,
    )
    index_dir.mkdir(parents=True, exist_ok=True)
    base.write_json(index_dir / "documents.json", [asdict(item) for item in documents])
    np.save(index_dir / "embeddings.npy", embeddings)
    meta = {
        "index_version": NODE_EDGE_INDEX_VERSION,
        "created_at": base.utc_now(),
        "wiki_fingerprint": store.fingerprint(),
        "embedding_model": embedding_model,
        "document_count": len(documents),
        "embedding_dimension": int(embeddings.shape[1]),
        "node_types": ["Task", "Stage", "Dataset"],
        "dataset_use_indexed": False,
        "max_document_chars": max_chars,
    }
    base.write_json(index_dir / "index_meta.json", meta)
    return documents, embeddings, meta


def load_node_index(
    store: base.WikiStore,
    index_dir: Path,
) -> tuple[list[base.SearchDocument], np.ndarray, dict[str, Any]]:
    meta = json.loads((index_dir / "index_meta.json").read_text(encoding="utf-8"))
    if meta.get("index_version") != NODE_EDGE_INDEX_VERSION:
        raise RuntimeError(
            "索引版本不是 node-only hyperedge RRF 版本，请使用 --build-index 重建"
        )
    if meta.get("wiki_fingerprint") != store.fingerprint():
        raise RuntimeError("索引与当前 Wiki 不一致，请使用 --build-index 重建")

    documents = [
        base.SearchDocument(**row)
        for row in json.loads(
            (index_dir / "documents.json").read_text(encoding="utf-8")
        )
    ]
    embeddings = np.load(index_dir / "embeddings.npy")
    if len(documents) != len(embeddings):
        raise RuntimeError("documents.json 与 embeddings.npy 数量不一致")
    return documents, embeddings, meta



# ---------------------------------------------------------------------------
# 2. Node-level Dense/BM25 retrieval + RRF
# ---------------------------------------------------------------------------

def fuse_node_rrf(
    documents: list[base.SearchDocument],
    channel_rankings: list[tuple[str, str, str, list[int], np.ndarray]],
    rrf_k: int,
) -> list[dict[str, Any]]:
    """Intent-lane RRF for individual nodes.

    A node receives at most one vote from each (retrieval mode, intent lane).
    If several correlated rewrites belong to the same lane, only the strongest
    rank contribution is counted. Dense and BM25 remain independent modes.
    """

    best_vote: dict[tuple[int, str, str], dict[str, Any]] = {}

    for mode, lane, query, ranking, scores in channel_rankings:
        for rank, document_index in enumerate(ranking, start=1):
            contribution = 1.0 / (rrf_k + rank)
            key = (document_index, mode, lane)
            hit = {
                "channel": f"{mode}:{query}",
                "mode": mode,
                "lane": lane,
                "query": query,
                "rank": rank,
                "raw_score": float(scores[document_index]),
                "rrf": contribution,
            }
            previous = best_vote.get(key)
            if previous is None or contribution > float(previous["rrf"]):
                best_vote[key] = hit

    fused: dict[int, float] = defaultdict(float)
    channels_by_index: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for (document_index, _mode, _lane), hit in best_vote.items():
        fused[document_index] += float(hit["rrf"])
        channels_by_index[document_index].append(hit)

    for hits in channels_by_index.values():
        hits.sort(key=lambda row: (row["mode"], row["lane"], row["rank"]))

    ordered = sorted(
        fused,
        key=lambda index: (fused[index], documents[index].doc_id),
        reverse=True,
    )
    maximum = max(fused.values(), default=1.0)

    results: list[dict[str, Any]] = []
    for overall_rank, index in enumerate(ordered, start=1):
        document = documents[index]
        results.append({
            "rank": overall_rank,
            "doc_index": index,
            "doc_id": document.doc_id,
            "node_type": document.node_type,
            "task_id": document.task_id,
            "stage_id": document.stage_id,
            "dataset_id": document.dataset_id,
            "rrf_score": fused[index],
            "normalized_rrf_score": fused[index] / maximum if maximum > 0 else 0.0,
            "channels": channels_by_index[index],
        })
    return results


def node_only_hybrid_retrieve(
    client: OpenAI,
    embedding_model: str,
    documents: list[base.SearchDocument],
    embeddings: np.ndarray,
    bm25: base.BM25Index,
    plan: HyperedgeQueryPlan,
    dense_top_k: int,
    bm25_top_k: int,
    rrf_k: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    query_vectors = base.embed_texts(
        client, embedding_model, plan.dense_queries, batch_size=16
    )

    channels: list[tuple[str, str, str, list[int], np.ndarray]] = []
    raw_rankings: list[dict[str, Any]] = []

    for query, vector in zip(plan.dense_queries, query_vectors):
        scores = embeddings @ vector
        ranking = base.ranked_indices(scores, dense_top_k)
        lane = plan.dense_query_lanes.get(query, "other")
        channels.append(("dense", lane, query, ranking, scores))
        raw_rankings.append({
            "channel": f"dense:{query}",
            "mode": "dense",
            "lane": lane,
            "results": [
                {
                    "doc_id": documents[index].doc_id,
                    "node_type": documents[index].node_type,
                    "score": float(scores[index]),
                }
                for index in ranking
            ],
        })

    for query in plan.bm25_queries:
        scores = bm25.scores(query)
        ranking = base.ranked_indices(
            scores, bm25_top_k, require_positive=True
        )
        lane = plan.bm25_query_lanes.get(query, "other")
        channels.append(("bm25", lane, query, ranking, scores))
        raw_rankings.append({
            "channel": f"bm25:{query}",
            "mode": "bm25",
            "lane": lane,
            "results": [
                {
                    "doc_id": documents[index].doc_id,
                    "node_type": documents[index].node_type,
                    "score": float(scores[index]),
                }
                for index in ranking
            ],
        })

    return fuse_node_rrf(documents, channels, rrf_k), raw_rankings


def select_node_seeds(
    node_results: list[dict[str, Any]],
    task_top_k: int,
    dataset_top_k: int,
    stage_top_k: int,
) -> tuple[list[dict[str, Any]], dict[str, list[str]]]:
    """Use typed seed quotas so generic Stage nodes cannot consume all anchors."""

    limits = {
        "Task": max(0, task_top_k),
        "Dataset": max(0, dataset_top_k),
        "Stage": max(0, stage_top_k),
    }
    counts = defaultdict(int)
    seeds: list[dict[str, Any]] = []
    selected_by_type: dict[str, list[str]] = {
        "Task": [], "Dataset": [], "Stage": []
    }

    for result in node_results:
        node_type = result["node_type"]
        if node_type not in limits:
            continue
        if counts[node_type] >= limits[node_type]:
            continue
        seeds.append(result)
        counts[node_type] += 1
        selected_by_type[node_type].append(result["doc_id"])

    # Use existing channel ranks to reserve two Dataset anchors per explicit
    # domain, within the same Dataset quota. No fabricated node scores.
    lanes = sorted({c.get("lane", "") for r in node_results for c in r.get("channels", [])
                    if c.get("lane", "").startswith("domain_rescue:")})
    reserved = []
    for lane in lanes:
        domain_nodes = [r for r in node_results if r["node_type"] == "Dataset" and
                        any(c.get("lane") == lane for c in r.get("channels", []))]
        domain_nodes.sort(key=lambda r: min(c["rank"] for c in r["channels"] if c.get("lane") == lane))
        for r in domain_nodes[:2]:
            if r["doc_id"] not in {n["doc_id"] for n in reserved}:
                reserved.append(r)
    if reserved:
        originals = [r for r in seeds if r["node_type"] == "Dataset"]
        combined = {r["doc_id"]: r for r in reserved}
        for r in originals:
            combined.setdefault(r["doc_id"], r)
        kept = list(combined.values())[:limits["Dataset"]]
        seeds = [r for r in seeds if r["node_type"] != "Dataset"] + kept
        selected_by_type["Dataset"] = [r["doc_id"] for r in kept]

    return seeds, selected_by_type



# ---------------------------------------------------------------------------
# 3. Controlled one-hop expansion + Task-Dataset pair ranking
# ---------------------------------------------------------------------------

def node_specificity(
    total_edges: int,
    degree: int,
    floor: float = DEFAULT_SPECIFICITY_FLOOR,
) -> float:
    """IDF-like attenuation for high-degree generic nodes.

    floor prevents a ubiquitous Stage from becoming exactly zero, while still
    ensuring a highly specific Task/Dataset contributes substantially more.
    """

    if degree <= 0 or total_edges <= 0:
        return 0.0
    denominator = math.log(total_edges + 1.0)
    if denominator <= 0:
        return 1.0
    raw = math.log((total_edges + 1.0) / (degree + 1.0)) / denominator
    raw = min(1.0, max(0.0, raw))
    floor = min(1.0, max(0.0, floor))
    return floor + (1.0 - floor) * raw


def expand_nodes_to_task_dataset_pairs(
    store: base.WikiStore,
    documents: list[base.SearchDocument],
    node_seeds: list[dict[str, Any]],
    rrf_k: int,
    task_weight: float,
    dataset_weight: float,
    stage_weight: float,
    specificity_floor: float,
) -> tuple[dict[tuple[str, str], TaskDatasetPairDiscovery], list[dict[str, Any]]]:
    """Controlled one-hop completion from node seeds to unique Task-Dataset pairs.

    Task and Dataset seeds may create pair candidates. DatasetUse facts are grouped
    by (task_id, dataset_id) immediately and become provenance only. One endpoint
    node contributes to one pair at most once, so repeated DatasetUse records cannot
    multiply the same Task/Dataset node score. Stage seeds remain support-only and
    cannot create new pairs.
    """

    document_by_id = {document.doc_id: document for document in documents}
    type_weights = {
        "Task": max(0.0, task_weight),
        "Dataset": max(0.0, dataset_weight),
        "Stage": max(0.0, stage_weight),
    }

    # Pair-level graph degree is used in V3. For a Task this is effectively the
    # number of distinct datasets it connects to; for a Dataset it is the number
    # of distinct tasks; for a Stage it is the number of distinct Task-Dataset
    # relations represented under that stage.
    all_pair_keys = {
        (str(use["task_id"]), str(use["dataset_id"]))
        for use in store.uses
    }
    total_pairs = max(1, len(all_pair_keys))
    degree_cache: dict[str, int] = {}
    discovered: dict[tuple[str, str], TaskDatasetPairDiscovery] = {}
    expansion_trace: list[dict[str, Any]] = []

    def make_node_hit(
        seed: dict[str, Any],
        document: base.SearchDocument,
    ) -> tuple[list[dict[str, Any]], dict[str, Any]]:
        uses = base.document_dataset_uses(store, document)
        pair_degree = degree_cache.setdefault(
            document.doc_id,
            len({
                (str(use["task_id"]), str(use["dataset_id"]))
                for use in uses
            }),
        )
        specificity = node_specificity(
            total_pairs,
            pair_degree,
            floor=specificity_floor,
        )
        type_weight = type_weights.get(document.node_type, 0.0)
        endpoint_rrf = sum(
            type_weight * specificity * float(channel_hit["rrf"])
            for channel_hit in seed.get("channels", [])
        )
        hit = {
            "node_id": document.doc_id,
            "node_type": document.node_type,
            "node_rrf_score": float(seed["rrf_score"]),
            "node_normalized_rrf_score": float(seed["normalized_rrf_score"]),
            "node_global_rank": int(seed["rank"]),
            "pair_degree": pair_degree,
            "specificity": specificity,
            "type_weight": type_weight,
            "pair_rrf_contribution": endpoint_rrf,
            "channels": seed.get("channels", []),
        }
        return uses, hit

    primary_seeds = [
        seed for seed in node_seeds
        if seed.get("node_type") in {"Task", "Dataset"}
    ]
    stage_seeds = [
        seed for seed in node_seeds
        if seed.get("node_type") == "Stage"
    ]

    # Task/Dataset endpoints create pair candidates.
    for seed in primary_seeds:
        document = document_by_id.get(seed["doc_id"])
        if document is None:
            continue
        uses, node_hit = make_node_hit(seed, document)
        if node_hit["type_weight"] <= 0.0 or not uses:
            continue

        grouped_uses: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for use in uses:
            key = (str(use["task_id"]), str(use["dataset_id"]))
            grouped_uses[key].append(use)

        for (task_id, dataset_id), pair_uses in grouped_uses.items():
            key = (task_id, dataset_id)
            item = discovered.setdefault(
                key,
                TaskDatasetPairDiscovery(task_id=task_id, dataset_id=dataset_id),
            )
            item.supporting_use_ids.update(
                str(use["dataset_use_id"]) for use in pair_uses
            )

            # Critical V3 rule: a node can vote only once for this pair, regardless
            # of how many DatasetUse records happen to encode that same relation.
            if node_hit["node_id"] not in item.supporting_node_ids:
                item.supporting_node_ids.add(str(node_hit["node_id"]))
                item.node_hits.append(node_hit)
                item.pair_rrf_score += float(node_hit["pair_rrf_contribution"])

            expansion_trace.append({
                "pair_id": item.pair_id,
                "task_id": task_id,
                "dataset_id": dataset_id,
                "supporting_use_ids": sorted(
                    str(use["dataset_use_id"]) for use in pair_uses
                ),
                "discovery_mode": "primary_pair_create",
                **node_hit,
            })

    # Stage endpoints only reinforce pairs that Task/Dataset retrieval already found.
    for seed in stage_seeds:
        document = document_by_id.get(seed["doc_id"])
        if document is None:
            continue
        uses, node_hit = make_node_hit(seed, document)
        if node_hit["type_weight"] <= 0.0 or not uses:
            continue

        grouped_uses: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for use in uses:
            key = (str(use["task_id"]), str(use["dataset_id"]))
            grouped_uses[key].append(use)

        for key, pair_uses in grouped_uses.items():
            item = discovered.get(key)
            if item is None:
                continue
            item.supporting_use_ids.update(
                str(use["dataset_use_id"]) for use in pair_uses
            )
            if node_hit["node_id"] not in item.supporting_node_ids:
                item.supporting_node_ids.add(str(node_hit["node_id"]))
                item.node_hits.append(node_hit)
                item.pair_rrf_score += float(node_hit["pair_rrf_contribution"])

            expansion_trace.append({
                "pair_id": item.pair_id,
                "task_id": item.task_id,
                "dataset_id": item.dataset_id,
                "supporting_use_ids": sorted(
                    str(use["dataset_use_id"]) for use in pair_uses
                ),
                "discovery_mode": "stage_pair_boost_only",
                **node_hit,
            })

    maximum = max(
        (item.pair_rrf_score for item in discovered.values()),
        default=1.0,
    )
    for item in discovered.values():
        item.normalized_pair_rrf_score = (
            item.pair_rrf_score / maximum if maximum > 0 else 0.0
        )
        item.pair_seed_score = item.normalized_pair_rrf_score

    return discovered, expansion_trace


def _use_information_score(use: dict[str, Any]) -> tuple[int, int, str]:
    """Deterministic quality proxy used only to pick representative provenance facts."""

    populated = 0
    for key in (
        "usage_role", "purpose", "construction_method", "sample_count",
    ):
        if use.get(key) not in (None, "", [], {}):
            populated += 1
    populated += int(bool(use.get("used_fields")))
    populated += int(bool(use.get("filter_conditions")))
    populated += int(bool(use.get("evidence")))
    evidence_count = len(use.get("evidence", [])) if isinstance(use.get("evidence"), list) else 0
    return populated, evidence_count, str(use.get("dataset_use_id") or "")


def representative_pair_uses(
    store: base.WikiStore,
    pair: TaskDatasetPairDiscovery,
    limit: int = DEFAULT_SUPPORTING_USES_PER_PAIR,
) -> list[dict[str, Any]]:
    uses = [
        store.use_by_id[use_id]
        for use_id in pair.supporting_use_ids
        if use_id in store.use_by_id
    ]
    uses.sort(key=_use_information_score, reverse=True)
    return uses[:max(1, limit)]


def serialize_task_dataset_pair_local(
    store: base.WikiStore,
    pair: TaskDatasetPairDiscovery,
) -> str:
    """Compact pair-local text for the auxiliary embedding score.

    Full Task objective/paper text is intentionally excluded. Dataset capability
    and aggregated DatasetUse-local facts dominate this representation.
    """

    task = store.task_by_id[pair.task_id]
    dataset = store.dataset_by_id[pair.dataset_id]
    uses = [
        store.use_by_id[use_id]
        for use_id in pair.supporting_use_ids
        if use_id in store.use_by_id
    ]

    roles: list[str] = []
    purposes: list[str] = []
    used_fields: list[str] = []
    filters: list[str] = []
    methods: list[str] = []
    for use in uses:
        if use.get("usage_role"):
            roles.append(str(use["usage_role"]))
        if use.get("purpose"):
            purposes.append(str(use["purpose"]))
        used_fields.extend(str(x) for x in use.get("used_fields", []) if str(x).strip())
        filters.extend(str(x) for x in use.get("filter_conditions", []) if str(x).strip())
        if use.get("construction_method"):
            methods.append(str(use["construction_method"]))

    return "\n".join([
        f"Dataset: {dataset.get('canonical_name') or 'unknown'}",
        f"Dataset aliases: {_values(dataset.get('raw_names', []), limit=12)}",
        f"Dataset type: {dataset.get('dataset_type') or 'unknown'}",
        f"Dataset material scope: {_values(dataset.get('material_scope', []), limit=12)}",
        f"Dataset properties: {_values(dataset.get('available_properties', []), limit=20)}",
        f"Dataset fields: {_values(dataset.get('available_fields', []), limit=30)}",
        f"Historical usage roles: {_values(base.unique_strings(roles), limit=12)}",
        f"Historical purposes: {_values(base.unique_strings(purposes), limit=16)}",
        f"Historical used fields: {_values(base.unique_strings(used_fields), limit=30)}",
        f"Historical filters: {_values(base.unique_strings(filters), limit=20)}",
        f"Construction methods: {_values(base.unique_strings(methods), limit=12)}",
        f"Task: {task.get('task_name_raw') or task.get('task_name_canonical') or 'unknown'}",
        f"Task material scope: {_values(task.get('material_scope', []), limit=12)}",
        f"Task target properties: {_values(task.get('target_properties', []), limit=16)}",
    ])


def score_pair_local_semantics(
    client: OpenAI,
    embedding_model: str,
    store: base.WikiStore,
    question: str,
    discovered: dict[tuple[str, str], TaskDatasetPairDiscovery],
    local_weight: float,
) -> dict[str, Any]:
    """Add an auxiliary semantic score to unique Task-Dataset pair candidates."""

    weight = min(1.0, max(0.0, local_weight))
    if not discovered:
        return {"enabled": False, "weight": weight, "count": 0}
    if weight <= 0.0:
        for item in discovered.values():
            item.pair_local_score = 0.0
            item.pair_seed_score = item.normalized_pair_rrf_score
        return {"enabled": False, "weight": 0.0, "count": len(discovered)}

    pair_keys = sorted(discovered)
    texts = [question]
    texts.extend(
        serialize_task_dataset_pair_local(store, discovered[key])
        for key in pair_keys
    )
    vectors = base.embed_texts(client, embedding_model, texts, batch_size=16)
    query_vector = np.asarray(vectors[0], dtype=np.float32)
    doc_vectors = np.asarray(vectors[1:], dtype=np.float32)

    q_norm = float(np.linalg.norm(query_vector)) or 1.0
    d_norms = np.linalg.norm(doc_vectors, axis=1)
    d_norms[d_norms == 0.0] = 1.0
    similarities = (doc_vectors @ query_vector) / (d_norms * q_norm)

    local_values: list[float] = []
    for key, similarity in zip(pair_keys, similarities):
        item = discovered[key]
        local = min(1.0, max(0.0, float(similarity)))
        local_values.append(local)
        item.pair_local_score = local
        item.pair_seed_score = (
            (1.0 - weight) * item.normalized_pair_rrf_score
            + weight * local
        )

    return {
        "enabled": True,
        "weight": weight,
        "count": len(pair_keys),
        "min_local_score": min(local_values) if local_values else 0.0,
        "max_local_score": max(local_values) if local_values else 0.0,
    }


def rank_task_dataset_pairs(
    discovered: dict[tuple[str, str], TaskDatasetPairDiscovery],
    pair_top_k: int,
    max_per_task: int,
    max_per_dataset: int,
) -> tuple[
    list[TaskDatasetPairDiscovery],
    list[TaskDatasetPairDiscovery],
    dict[str, Any],
]:
    """Rank unique Task-Dataset relations and enforce pair-level diversity."""

    ranked = sorted(
        discovered.values(),
        key=lambda item: (
            item.pair_seed_score,
            item.pair_rrf_score,
            len({hit["node_type"] for hit in item.node_hits}),
            item.pair_id,
        ),
        reverse=True,
    )

    task_counts: dict[str, int] = defaultdict(int)
    dataset_counts: dict[str, int] = defaultdict(int)
    selected: list[TaskDatasetPairDiscovery] = []
    dropped: list[TaskDatasetPairDiscovery] = []
    drop_reasons: dict[str, str] = {}

    task_limit = max(0, max_per_task)
    dataset_limit = max(0, max_per_dataset)
    limit = max(1, pair_top_k)

    for item in ranked:
        reason = ""
        if task_limit and task_counts[item.task_id] >= task_limit:
            reason = "task_pair_cap"
        elif dataset_limit and dataset_counts[item.dataset_id] >= dataset_limit:
            reason = "dataset_pair_cap"

        if reason:
            dropped.append(item)
            drop_reasons[item.pair_id] = reason
            continue

        if len(selected) < limit:
            selected.append(item)
            task_counts[item.task_id] += 1
            dataset_counts[item.dataset_id] += 1
        else:
            dropped.append(item)
            drop_reasons[item.pair_id] = "outside_pair_top_k"

    diagnostics = {
        "max_pairs_per_task": task_limit,
        "max_pairs_per_dataset": dataset_limit,
        "selected_count": len(selected),
        "drop_reasons": drop_reasons,
        "selected_task_counts": dict(task_counts),
        "selected_dataset_counts": dict(dataset_counts),
    }
    return selected, dropped, diagnostics


def derive_rerank_url(chat_base_url: str, explicit_url: str | None) -> str:
    """从聊天端点推导rerank端点；显式QWEN_RERANK_URL优先。"""

    if explicit_url and ("<" in explicit_url or ">" in explicit_url):
        raise ValueError("QWEN_RERANK_URL包含未替换的占位符，请设置实际地址或通过 --rerank-url 指定标准端点")
    if explicit_url:
        return explicit_url.rstrip("/")
    parsed = urlsplit(chat_base_url)
    host = parsed.netloc.casefold()
    if host == "dashscope.aliyuncs.com":
        # 兼容现有项目使用的非Workspace DashScope地址。
        return (
            "https://dashscope.aliyuncs.com/api/v1/services/"
            "rerank/text-rerank/text-rerank"
        )
    path = parsed.path.rstrip("/")
    if path.endswith("/compatible-mode/v1"):
        path = path[: -len("/compatible-mode/v1")] + "/compatible-api/v1/reranks"
    elif path.endswith("/compatible-api/v1"):
        path += "/reranks"
    else:
        path += "/reranks"
    return urlunsplit((parsed.scheme, parsed.netloc, path, "", ""))


def call_text_rerank(
    *,
    api_key: str,
    url: str,
    model: str,
    query: str,
    documents: list[str],
    instruct: str,
    timeout: float,
) -> tuple[list[float], dict[str, Any]]:
    """调用qwen3-rerank或兼容的DashScope文本排序接口。"""

    if not documents:
        return [], {"results": []}

    # qwen3-rerank使用顶层query/documents；保留gte-rerank-v2兼容分支，方便
    # 用户已有旧端点时做对照实验。
    # Select the request schema by endpoint. The compatible rerank endpoint
    # accepts top-level fields, while the legacy DashScope service endpoint
    # requires input.query/input.documents and a parameters object.
    compatible_rerank_endpoint = "/compatible-api/" in url
    if compatible_rerank_endpoint:
        payload: dict[str, Any] = {
            "model": model,
            "query": query,
            "documents": documents,
            "top_n": len(documents),
            "instruct": instruct,
        }
    else:
        payload = {
            "model": model,
            "input": {"query": query, "documents": documents},
            "parameters": {
                "top_n": len(documents),
                "return_documents": False,
                "instruct": instruct,
            },
        }

    request = urllib.request.Request(
        url=url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            value = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"rerank API HTTP {exc.code}: {body[:2000]}"
        ) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"无法连接rerank API：{exc}") from exc

    rows = value.get("results")
    if not isinstance(rows, list):
        rows = (value.get("output") or {}).get("results")
    if not isinstance(rows, list):
        raise RuntimeError(
            "rerank API响应缺少results：" +
            json.dumps(value, ensure_ascii=False)[:2000]
        )

    scores = [0.0] * len(documents)
    seen: set[int] = set()
    for row in rows:
        if not isinstance(row, dict):
            continue
        try:
            index = int(row["index"])
            score = min(1.0, max(0.0, float(row["relevance_score"])))
        except (KeyError, TypeError, ValueError):
            continue
        if 0 <= index < len(scores):
            scores[index] = score
            seen.add(index)
    if len(seen) != len(documents):
        missing = sorted(set(range(len(documents))) - seen)
        raise RuntimeError(
            "rerank API未返回全部候选；缺失原始索引：" +
            ", ".join(str(index) for index in missing[:30])
        )
    return scores, value


def serialize_task_dataset_pair_for_rerank(
    store: base.WikiStore,
    pair: TaskDatasetPairDiscovery,
    max_chars: int = DEFAULT_RERANK_DOCUMENT_CHARS,
    supporting_uses_per_pair: int = DEFAULT_SUPPORTING_USES_PER_PAIR,
) -> str:
    """Serialize one Task-Dataset relation with a few representative DatasetUse facts."""

    task = store.task_by_id[pair.task_id]
    dataset = store.dataset_by_id[pair.dataset_id]
    uses = representative_pair_uses(store, pair, supporting_uses_per_pair)

    rows = [
        "[CANDIDATE TYPE] Task-Dataset relation",
        f"[PAIR ID] {pair.pair_id}",
        "",
        f"[DATASET ID] {dataset['dataset_id']}",
        f"[DATASET] {dataset.get('canonical_name') or 'unknown'}",
        f"[DATASET TYPE] {dataset.get('dataset_type') or 'unknown'}",
        f"[DATASET MATERIAL SCOPE] {_values(dataset.get('material_scope', []))}",
        f"[DATASET PROPERTIES] {_values(dataset.get('available_properties', []))}",
        f"[DATASET FIELDS] {_values(dataset.get('available_fields', []))}",
        f"[AVAILABILITY] {dataset.get('availability') or 'unknown'}",
        f"[RECOMMENDABLE] {bool(dataset.get('recommendable', False))}",
        "",
        f"[TASK ID] {task['task_id']}",
        f"[TASK] {task.get('task_name_raw') or task.get('task_name_canonical') or 'unknown'}",
        f"[TASK MATERIAL SCOPE] {_values(task.get('material_scope', []))}",
        f"[TASK TARGET PROPERTIES] {_values(task.get('target_properties', []))}",
        f"[TASK CONSTRAINTS] {_values(task.get('constraints', []))}",
        "",
        f"[SUPPORTING DATASET USE COUNT] {len(pair.supporting_use_ids)}",
    ]

    for index, use in enumerate(uses, start=1):
        evidence_parts: list[str] = []
        for evidence in use.get("evidence", [])[:1]:
            if not isinstance(evidence, dict):
                continue
            text = str(evidence.get("text") or "").replace("\n", " ").strip()
            if text:
                evidence_parts.append(text[:600])
        rows.extend([
            "",
            f"[USE {index} ID] {use['dataset_use_id']}",
            f"[USE {index} ROLE] {use.get('usage_role') or 'unknown'}",
            f"[USE {index} PURPOSE] {use.get('purpose') or 'unknown'}",
            f"[USE {index} USED FIELDS] {_values(use.get('used_fields', []))}",
            f"[USE {index} FILTERS] {_values(use.get('filter_conditions', []))}",
            f"[USE {index} CONSTRUCTION] {use.get('construction_method') or 'unknown'}",
            f"[USE {index} SAMPLE COUNT] {use.get('sample_count') or 'unknown'}",
            f"[USE {index} EVIDENCE] {_values(evidence_parts)}",
        ])

    return "\n".join(rows)[:max_chars]


def rerank_task_dataset_pairs(
    *,
    store: base.WikiStore,
    question: str,
    plan: base.QueryPlan,
    pool: list[TaskDatasetPairDiscovery],
    api_key: str,
    rerank_url: str,
    rerank_model: str,
    rerank_instruct: str,
    max_document_chars: int,
    timeout: float,
    supporting_uses_per_pair: int,
) -> tuple[list[TaskDatasetPairDiscovery], dict[str, Any]]:
    """One expensive semantic rerank over only Top-K Task-Dataset pairs."""

    query = serialize_query_for_rerank(question, plan)
    documents = [
        serialize_task_dataset_pair_for_rerank(
            store,
            item,
            max_document_chars,
            supporting_uses_per_pair,
        )
        for item in pool
    ]
    scores, raw = call_text_rerank(
        api_key=api_key,
        url=rerank_url,
        model=rerank_model,
        query=query,
        documents=documents,
        instruct=rerank_instruct,
        timeout=timeout,
    )

    for item, score in zip(pool, scores):
        item.rerank_score = score

    ranked = sorted(
        pool,
        key=lambda item: (
            item.rerank_score,
            item.pair_seed_score,
            item.normalized_pair_rrf_score,
            item.pair_id,
        ),
        reverse=True,
    )
    for position, item in enumerate(ranked, start=1):
        item.rerank_position = position
    return ranked, raw


def _normalized_decay_score(
    scores: list[float],
    weights: tuple[float, ...] = DEFAULT_DATASET_PAIR_DECAY_WEIGHTS,
) -> float:
    usable = min(len(scores), len(weights))
    if usable <= 0:
        return 0.0
    local_weights = list(weights[:usable])
    denominator = sum(local_weights)
    if denominator <= 0:
        return max(scores[:usable])
    return sum(
        local_weights[index] * scores[index]
        for index in range(usable)
    ) / denominator


def _derivation_note(
    dataset: dict[str, Any],
    target_dataset_id: str,
    use: dict[str, Any],
) -> dict[str, Any]:
    return {
        "derived_dataset_id": dataset["dataset_id"],
        "derived_dataset_name": dataset.get("canonical_name"),
        "source_dataset_id": target_dataset_id,
        "construction_method": use.get("construction_method"),
        "filter_conditions": use.get("filter_conditions", []),
        "paper_id": use["paper_id"],
        "dataset_use_id": use["dataset_use_id"],
    }


def aggregate_reranked_pairs_to_datasets(
    *,
    store: base.WikiStore,
    ranked_pairs: list[TaskDatasetPairDiscovery],
    supporting_pairs_per_dataset: int,
    supporting_uses_per_pair: int,
    map_derived_to_source: bool,
) -> tuple[list[NodeEdgeDatasetCandidate], list[dict[str, Any]]]:
    """Aggregate independent Task-Dataset relation evidence into Dataset scores.

    A Dataset is rewarded by its strongest few query-relevant Task-Dataset pairs,
    not by the raw number of DatasetUse records. DatasetUse IDs are retained only
    as provenance/evidence for the selected pairs.
    """

    grouped: dict[str, list[TaskDatasetPairDiscovery]] = defaultdict(list)
    derivations: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for pair in ranked_pairs:
        dataset = store.dataset_by_id[pair.dataset_id]
        target_dataset_id = dataset["dataset_id"]

        if map_derived_to_source:
            source_id = dataset.get("source_dataset_id")
            if (
                not dataset.get("recommendable", False)
                and source_id
                and source_id in store.dataset_by_id
            ):
                target_dataset_id = source_id
                for use in representative_pair_uses(
                    store, pair, supporting_uses_per_pair
                ):
                    derivations[target_dataset_id].append(
                        _derivation_note(dataset, target_dataset_id, use)
                    )

        grouped[target_dataset_id].append(pair)

    candidates: list[NodeEdgeDatasetCandidate] = []
    global _CURRENT_USE_SCORES
    _CURRENT_USE_SCORES = {}

    pair_limit = max(1, supporting_pairs_per_dataset)
    for dataset_id, pairs in grouped.items():
        pairs.sort(
            key=lambda item: (
                item.rerank_score,
                item.pair_seed_score,
                item.normalized_pair_rrf_score,
                item.pair_id,
            ),
            reverse=True,
        )
        kept_pairs = pairs[:pair_limit]
        kept_scores = [item.rerank_score for item in kept_pairs]
        aggregate_score = _normalized_decay_score(
            kept_scores,
            weights=DEFAULT_DATASET_PAIR_DECAY_WEIGHTS,
        )

        candidate = NodeEdgeDatasetCandidate(dataset_id=dataset_id)
        candidate.aggregated_pair_score = aggregate_score
        candidate.final_score = aggregate_score
        candidate.retrieval_score = max(
            item.pair_seed_score for item in pairs
        )
        candidate.supporting_pair_scores = {
            item.pair_id: item.rerank_score
            for item in kept_pairs
        }

        use_scores: dict[str, float] = {}
        # Preserve every use from reranked pairs for scope checking. A display
        # limit must not discard the only use proving a required label bundle.
        for pair in pairs:
            for use_id in sorted(pair.supporting_use_ids):
                use = store.use_by_id[use_id]
                use_id = str(use["dataset_use_id"])
                use_scores[use_id] = max(
                    use_scores.get(use_id, 0.0),
                    pair.rerank_score,
                )

        candidate.supporting_use_scores = use_scores
        candidate.supporting_use_ids = set(use_scores)
        candidate.supporting_doc_ids = set(candidate.supporting_use_ids)
        for pair in kept_pairs:
            candidate.supporting_doc_ids.update(
                str(hit["node_id"]) for hit in pair.node_hits
            )

        candidate.derivation_notes = derivations.get(dataset_id, [])
        candidate.rerank_reason = (
            "Dataset score uses normalized decayed Top Task-Dataset pair evidence: "
            + ", ".join(
                f"{item.pair_id}={item.rerank_score:.6f}"
                for item in kept_pairs
            )
            + f"; aggregate={aggregate_score:.6f}"
        )
        _CURRENT_USE_SCORES.update(use_scores)
        candidates.append(candidate)

    return sorted(
        candidates,
        key=lambda item: (
            item.final_score,
            item.retrieval_score,
            item.dataset_id,
        ),
        reverse=True,
    ), []


def _text_blob(*values: Any) -> str:
    parts: list[str] = []
    for value in values:
        if isinstance(value, dict):
            parts.extend(str(item) for item in value.values())
        elif isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
            parts.extend(str(item) for item in value)
        else:
            parts.append(str(value))
    return " ".join(parts).casefold()


def query_intent_needs(plan: HyperedgeQueryPlan) -> set[tuple[str, str]]:
    """Explicit coverage needs used by V3 adaptive recommendation.

    These are not extra rewrite facts. They are conservative buckets derived
    from already-grounded query fields and the original objective.
    """

    text = _text_blob(
        plan.objective,
        plan.material_scope,
        plan.target_properties,
        plan.input_representations,
        plan.task_mechanisms,
        plan.dataset_role_needs,
    )
    needs: set[tuple[str, str]] = set()

    if re.search(r"crystal|crystalline|inorganic|solid[- ]?state|晶体|无机|固体", text):
        needs.add(("domain", "crystal"))
    if re.search(r"molecule|molecular|homo|lumo|qm9|smiles|分子", text):
        needs.add(("domain", "molecule"))
    if re.search(r"catalyst|catalytic|catalysis|oc22|催化", text):
        needs.add(("domain", "catalysis"))
    if re.search(r"benchmark|standardized|fair|reproducible|bias[- ]?mitigated|comparison", text):
        needs.add(("role", "benchmark"))
    if re.search(r"synthesizability|synthesi[sz]able|experimentally realizable|synthetic capabilities", text):
        needs.add(("intent", "synthesizability"))
        needs.add(("role", "experimental_reference"))
    if re.search(r"potential energy surface|\bpes\b|forces|stresses|molecular dynamics|interatomic potential", text):
        needs.add(("intent", "trajectory_or_pes"))
    if re.search(r"pre[- ]?train|source dataset|source datasets|transfer learning|knowledge transfer", text):
        needs.add(("role", "source"))
    if re.search(r"fine[- ]?tun|target dataset|target datasets|small target", text):
        needs.add(("role", "target"))

    for prop in base.property_concepts(plan.target_properties):
        needs.add(("property", prop))
    return needs


def candidate_intent_coverage(
    store: base.WikiStore,
    candidate: NodeEdgeDatasetCandidate,
) -> set[tuple[str, str]]:
    """Map a Dataset candidate to coarse needs using DatasetUse evidence only.

    A historical Task can be about a property without every Dataset used by that
    Task actually containing that property's label.  Consequently, Task and
    Stage text must not be used as a Dataset capability claim here.
    """

    context = node_edge_candidate_context(store, candidate)
    dataset = context["dataset"]
    uses = context["uses"]
    text = _text_blob(
        dataset.get("canonical_name"),
        dataset.get("raw_names", []),
        dataset.get("dataset_type"),
        dataset.get("material_scope", []),
        dataset.get("available_properties", []),
        dataset.get("available_fields", []),
        [use.get("usage_role") for use in uses],
        [use.get("purpose") for use in uses],
        [field for use in uses for field in use.get("used_fields", [])],
    )
    coverage: set[tuple[str, str]] = set()

    if re.search(r"crystal|crystalline|inorganic|solid[- ]?state|jarvis|materials project|oqmd|icsd|晶体|无机", text):
        coverage.add(("domain", "crystal"))
    if re.search(r"molecule|molecular|qm9|lipophilicity|freesolv|esol|homo|lumo|smiles|分子", text):
        coverage.add(("domain", "molecule"))
    if re.search(r"catalyst|catalytic|catalysis|oc22|open catalyst|催化", text):
        coverage.add(("domain", "catalysis"))
    if re.search(r"matbench|benchmark|standardized|evaluation|test set|validation", text):
        coverage.add(("role", "benchmark"))
    if re.search(r"icsd|experimental|experimentally|synthesi|known synthes", text):
        coverage.add(("role", "experimental_reference"))
    if re.search(r"m?ptrj|trajectory|forces|stresses|molecular dynamics|potential energy surface|\bpes\b", text):
        coverage.add(("intent", "trajectory_or_pes"))
    if re.search(r"pretrain|pre-training|source dataset|source data|unlabeled", text):
        coverage.add(("role", "source"))
    if re.search(r"fine[- ]?tun|target dataset|test set|evaluation|experimental", text):
        coverage.add(("role", "target"))
    if re.search(r"synthesizability|synthesi[sz]able|experimentally realizable", text):
        coverage.add(("intent", "synthesizability"))

    property_values = [
        *dataset.get("available_properties", []),
        *dataset.get("available_fields", []),
        *[field for use in uses for field in use.get("used_fields", [])],
    ]
    for prop in base.property_concepts(property_values):
        coverage.add(("property", prop))
    return coverage


def recalibrate_dataset_candidates(
    store: base.WikiStore,
    plan: HyperedgeQueryPlan,
    candidates: list[NodeEdgeDatasetCandidate],
) -> tuple[list[NodeEdgeDatasetCandidate], dict[str, Any]]:
    """Apply a small intent-aware score calibration after pair rerank.

    The rerank model ranks relation evidence. This step nudges Dataset-level
    ranking toward explicit workflow needs such as benchmark suites, molecular
    side datasets, synthesizability references, and PES/trajectory datasets.
    """

    required = query_intent_needs(plan)
    if not candidates:
        return candidates, {"enabled": False, "reason": "empty_candidates"}

    diagnostics: list[dict[str, Any]] = []
    for candidate in candidates:
        coverage = candidate_intent_coverage(store, candidate)
        matched = coverage & required
        domain_required = {need for need in required if need[0] == "domain"}
        domain_matched = {need for need in matched if need[0] == "domain"}
        role_required = {need for need in required if need[0] == "role"}
        role_matched = {need for need in matched if need[0] == "role"}
        property_required = {need for need in required if need[0] == "property"}
        property_matched = {need for need in matched if need[0] == "property"}
        intent_matched = {need for need in matched if need[0] == "intent"}

        bonus = 0.0
        if domain_required:
            bonus += 0.10 * len(domain_matched) / len(domain_required)
        if role_required:
            bonus += 0.08 * len(role_matched) / len(role_required)
        if property_required:
            bonus += 0.08 * len(property_matched) / len(property_required)
        if intent_matched:
            bonus += 0.06

        # Penalize off-domain public databases only when the query explicitly
        # names more than one material domain and this candidate covers none.
        penalty = 0.0
        if len(domain_required) >= 2 and not domain_matched:
            penalty += 0.08

        original = candidate.final_score
        candidate.final_score = calibrate_bounded_score(original, bonus, penalty)
        if bonus or penalty:
            candidate.rerank_reason += (
                f"; intent_calibration original={original:.6f} "
                f"bonus={bonus:.6f} penalty={penalty:.6f} "
                f"matched={sorted(matched)}"
            )
        diagnostics.append({
            "dataset_id": candidate.dataset_id,
            "original_score": original,
            "calibrated_score": candidate.final_score,
            "matched_needs": sorted(matched),
            "bonus": bonus,
            "penalty": penalty,
        })

    ranked = sorted(
        candidates,
        key=lambda item: (item.final_score, item.retrieval_score, item.dataset_id),
        reverse=True,
    )
    return ranked, {
        "enabled": True,
        "required_needs": sorted(required),
        "candidate_count": len(candidates),
        "adjustments": diagnostics,
    }


def node_edge_candidate_context(
    store: base.WikiStore,
    candidate: base.DatasetCandidate,
) -> dict[str, Any]:
    dataset = store.dataset_by_id[candidate.dataset_id]
    uses = [
        store.use_by_id[use_id]
        for use_id in candidate.supporting_use_ids
        if use_id in store.use_by_id
    ]
    uses.sort(
        key=lambda use: _CURRENT_USE_SCORES.get(use["dataset_use_id"], 0.0),
        reverse=True,
    )
    tasks = [
        store.task_by_id[use["task_id"]]
        for use in uses
        if use["task_id"] in store.task_by_id
    ]
    stages = [
        store.stage_by_id[use["stage_id"]]
        for use in uses
        if use["stage_id"] in store.stage_by_id
    ]
    return {
        "dataset": dataset,
        "uses": uses,
        "tasks": tasks,
        "stages": stages,
    }


def deduplicate_dataset_families(
    store: base.WikiStore,
    ranked: list[NodeEdgeDatasetCandidate],
    enabled: bool,
) -> tuple[list[NodeEdgeDatasetCandidate], list[dict[str, Any]]]:
    if not enabled:
        return ranked, []

    selected: list[NodeEdgeDatasetCandidate] = []
    seen_families: dict[str, str] = {}
    removed: list[dict[str, Any]] = []

    for candidate in ranked:
        family = base.dataset_family_id(store, candidate.dataset_id)
        if family in seen_families:
            removed.append({
                "dataset_id": candidate.dataset_id,
                "family_id": family,
                "kept_dataset_id": seen_families[family],
                "reason": "same_dataset_family_as_higher_ranked_candidate",
            })
            continue
        seen_families[family] = candidate.dataset_id
        selected.append(candidate)

    return selected, removed



# ---------------------------------------------------------------------------
# 5. Retrieval ranking vs optional set recommendation
# ---------------------------------------------------------------------------

ROLE_TRIGGER_TERMS: dict[str, tuple[str, ...]] = {
    "training": ("train", "training", "训练", "微调", "fine-tun"),
    "fine_tuning": ("fine-tun", "微调"),
    "fine_tuning_target": ("fine-tun", "微调"),
    "pretraining": ("pretrain", "预训练", "迁移学习", "transfer learning"),
    "pretraining_source": ("pretrain", "预训练", "迁移学习", "transfer learning"),
    "source": ("pretrain", "预训练", "迁移学习", "transfer learning"),
    "validation": ("validat", "验证", "外部测试", "holdout"),
    "test": ("test set", "测试集", "测试", "外部测试"),
    "evaluation": ("evaluat", "评估", "验证", "test set", "测试集"),
    "evaluation_target": ("evaluat", "评估", "验证", "test set", "测试集"),
    "benchmark": ("benchmark", "baseline", "基准", "对比", "比较"),
    "reference": ("reference", "基准", "对比", "比较"),
}


def role_is_explicit_in_question(role: str, question: str) -> bool:
    """Require user wording before making an auxiliary role a hard need."""

    normalized_role = role.strip().casefold()
    question_text = question.casefold()
    return any(
        term.casefold() in question_text
        for term in ROLE_TRIGGER_TERMS.get(normalized_role, ())
    )


def explicit_evidence_needs(
    plan: base.QueryPlan,
    question: str,
) -> set[tuple[str, str]]:
    """Return only needs that the user explicitly supplied to the QueryPlan.

    This deliberately differs from ``query_intent_needs``.  It does not infer
    a benchmark, validation, source, or target need from a broadly similar
    Task.  A dataset such as an evaluation set is selected only when the user
    asks for that role in the original question.  A query rewrite is useful for
    finding candidates, but it is not sufficient evidence that the user asked
    for a benchmark, validation, or pretraining dataset.
    """

    needs = {
        ("property", value)
        for value in base.property_concepts(plan.target_properties)
    }
    needs.update(
        ("role", str(role))
        for role in plan.preferred_usage_roles
        if role_is_explicit_in_question(str(role), question)
    )
    for item in getattr(plan, "dataset_role_needs", []):
        if not isinstance(item, dict):
            continue
        role = str(item.get("role") or "").strip()
        if role and role_is_explicit_in_question(role, question):
            needs.add(("role", role))
    return needs


def candidate_evidence_coverage(
    store: base.WikiStore,
    candidate: NodeEdgeDatasetCandidate,
) -> set[tuple[str, str]]:
    """Return explicit needs supported by Dataset and DatasetUse fields.

    Unlike semantic reranking, this is an eligibility check: the fields come
    from the Dataset profile or current query's DatasetUse records, never from
    the parent Task's target properties.
    """

    context = node_edge_candidate_context(store, candidate)
    dataset = context["dataset"]
    uses = context["uses"]
    property_values = [
        *dataset.get("available_properties", []),
        *dataset.get("available_fields", []),
        *[field for use in uses for field in use.get("used_fields", [])],
    ]
    coverage = {
        ("property", value)
        for value in base.property_concepts(property_values)
    }

    role_aliases = {
        "source": {"source", "pretraining"},
        "pretraining": {"source", "pretraining"},
        "pretraining_source": {"source", "pretraining"},
        "training": {"training", "fine_tuning"},
        "fine_tuning_target": {"fine_tuning", "training", "target"},
        "validation": {"validation", "evaluation", "test"},
        "test": {"test", "evaluation", "validation"},
        "evaluation_target": {"evaluation", "validation", "test", "target"},
    }
    observed_roles = {
        str(use.get("usage_role") or "").strip().casefold()
        for use in uses
    }
    observed_roles.discard("")
    for role in observed_roles:
        coverage.add(("role", role))
    for canonical, aliases in role_aliases.items():
        if observed_roles & aliases:
            coverage.add(("role", canonical))
    return coverage


def select_evidence_top1_datasets(
    *,
    store: base.WikiStore,
    plan: base.QueryPlan,
    question: str,
    ranked: list[NodeEdgeDatasetCandidate],
    max_results: int,
    candidate_top_k: int,
) -> tuple[list[NodeEdgeDatasetCandidate], dict[str, Any]]:
    """Pick the best evidenced candidate for each explicit data need.

    With one explicit need, this is exactly an evidence-gated Top-1.  With
    multiple needs, it selects a small non-redundant portfolio: a candidate is
    eligible for a need only when its own Dataset/DatasetUse evidence supports
    it, and the next candidate must cover an as-yet-uncovered need.
    """

    pool = ranked[:max(0, candidate_top_k)]
    required = explicit_evidence_needs(plan, question)
    if not pool or max_results <= 0:
        return [], {
            "mode": "evidence_top1",
            "selection_reason": "empty_candidate_pool",
            "required_needs": sorted(required),
            "selected_size": 0,
        }

    coverage_by_id = {
        candidate.dataset_id: candidate_evidence_coverage(store, candidate)
        for candidate in pool
    }
    winners: dict[str, str] = {}
    for need in sorted(required):
        eligible = [
            candidate for candidate in pool
            if need in coverage_by_id[candidate.dataset_id]
        ]
        if eligible:
            winners[f"{need[0]}:{need[1]}"] = eligible[0].dataset_id

    if not required:
        return [pool[0]], {
            "mode": "evidence_top1",
            "selection_reason": "no_explicit_data_need_keep_ranked_top1",
            "required_needs": [],
            "need_winners": {},
            "selected_size": 1,
        }

    selected: list[NodeEdgeDatasetCandidate] = []
    covered: set[tuple[str, str]] = set()
    available = list(pool)
    while available and len(selected) < max_results:
        best = max(
            available,
            key=lambda candidate: (
                len((coverage_by_id[candidate.dataset_id] & required) - covered),
                candidate.final_score,
                candidate.retrieval_score,
                candidate.dataset_id,
            ),
        )
        new_needs = (coverage_by_id[best.dataset_id] & required) - covered
        if not new_needs:
            break
        selected.append(best)
        covered.update(new_needs)
        available.remove(best)
        if covered >= required:
            break

    return selected, {
        "mode": "evidence_top1",
        "selection_reason": (
            "all_explicit_needs_covered_by_evidenced_candidates"
            if covered >= required else "some_explicit_needs_have_no_evidenced_candidate"
        ),
        "required_needs": sorted(required),
        "covered_needs": sorted(covered),
        "uncovered_needs": sorted(required - covered),
        "need_winners": winners,
        "candidate_evidence_coverage": {
            candidate.dataset_id: sorted(coverage_by_id[candidate.dataset_id] & required)
            for candidate in pool
        },
        "selected_size": len(selected),
        "candidate_pool_size": len(pool),
    }

def select_final_datasets(
    *,
    store: base.WikiStore,
    plan: base.QueryPlan,
    question: str,
    ranked: list[NodeEdgeDatasetCandidate],
    selection_mode: str,
    max_results: int,
    minimum_score: float,
    candidate_top_k: int,
    family_overrides: dict[str, str] | None = None,
) -> tuple[list[NodeEdgeDatasetCandidate], dict[str, Any]]:
    """Keep retrieval Top-K separate from the downstream recommendation policy."""

    if selection_mode == "scoped":
        return select_scoped(store=store, plan=plan, question=question,
                             ranked=ranked, max_results=max_results,
                             candidate_top_k=candidate_top_k,
                             family_overrides=family_overrides)

    if selection_mode == "topk":
        selected = ranked[:max(0, max_results)]
        return selected, {
            "mode": "topk",
            "selection_reason": "top_ranked_datasets_after_family_dedup",
            "selected_size": len(selected),
        }

    if selection_mode == "evidence_top1":
        return select_evidence_top1_datasets(
            store=store,
            plan=plan,
            question=question,
            ranked=ranked,
            max_results=max_results,
            candidate_top_k=candidate_top_k,
        )

    # Legacy base selectors are reused only as the optional recommendation layer.
    # They see only current-query DatasetUse evidence through candidate_context.
    if selection_mode == "minimum":
        selected = base.select_minimum_dataset_set(
            store,
            plan,
            ranked,
            max_results,
            minimum_score,
            candidate_pool_size=candidate_top_k,
        )
        return selected, {
            "mode": "minimum",
            "selection_reason": "optional_minimum_dataset_recommendation_layer",
            "selected_size": len(selected),
        }

    selected = base.select_dataset_combination(
        store,
        plan,
        ranked,
        max_results,
        minimum_score,
    )
    return selected, {
        "mode": "recommend",
        "selection_reason": "legacy_recommendation_layer",
        "selected_size": len(selected),
    }


def select_adaptive_minimum_datasets(
    *,
    store: base.WikiStore,
    plan: base.QueryPlan,
    ranked: list[NodeEdgeDatasetCandidate],
    max_results: int,
    minimum_score: float,
    candidate_top_k: int,
) -> tuple[list[NodeEdgeDatasetCandidate], dict[str, Any]]:
    """Trace-only adaptive selection for the real recommendation use case.

    The frozen retrieval Top-K remains unchanged for evaluation. This selector
    answers a separate question: if a small set already covers the explicit data
    needs, stop there; otherwise fall back to the legacy coverage selector.
    """

    if not ranked or max_results <= 0:
        return [], {
            "mode": "adaptive_minimum",
            "selection_reason": "empty_ranked_candidates",
            "selected_size": 0,
        }

    pool_size = max(1, candidate_top_k)
    pool = [
        candidate for index, candidate in enumerate(ranked[:pool_size])
        if index < 2 or candidate.final_score >= minimum_score
    ]
    if not pool:
        return [], {
            "mode": "adaptive_minimum",
            "selection_reason": "empty_eligible_pool",
            "selected_size": 0,
            "candidate_pool_size": pool_size,
        }

    required = query_intent_needs(plan)
    top_score = max(float(pool[0].final_score), 1e-9)
    text = _text_blob(
        plan.objective,
        plan.material_scope,
        plan.target_properties,
        plan.required_stages,
        plan.preferred_usage_roles,
        plan.dataset_role_needs,
    )
    explicit_multi_request = bool(
        re.search(r"\bdatasets\b|\bdata sources\b|multiple|several|哪些数据集|哪几个|多个|数据源", text)
    )
    soft_cap = 1
    if len(base.property_concepts(plan.target_properties)) >= 3:
        soft_cap += 1
    if len(plan.required_stages) >= 2:
        soft_cap += 1
    if len(plan.preferred_usage_roles) >= 2 or len(plan.dataset_role_needs) >= 2:
        soft_cap += 1
    if explicit_multi_request:
        soft_cap += 1
    if len(required) >= 5:
        soft_cap += 1
    soft_cap = max(1, min(max_results, min(5, soft_cap)))
    coverage_by_id = {
        candidate.dataset_id: candidate_intent_coverage(store, candidate)
        for candidate in pool
    }
    selected: list[NodeEdgeDatasetCandidate] = []
    selected_families: set[str] = set()
    covered: set[tuple[str, str]] = set()
    steps: list[dict[str, Any]] = []

    if not required:
        selected = pool[:1]
        return selected, {
            "mode": "adaptive_minimum",
            "selection_reason": "no_explicit_multi_need_keep_top1",
            "required_needs": [],
            "selected_size": len(selected),
            "candidate_pool_size": pool_size,
            "soft_cap": soft_cap,
            "explicit_multi_request": explicit_multi_request,
        }

    while len(selected) < soft_cap:
        best: NodeEdgeDatasetCandidate | None = None
        best_key: tuple[float, float, float, float] | None = None
        best_new: set[tuple[str, str]] = set()
        best_score_ratio = 0.0

        for candidate in pool:
            if candidate in selected:
                continue
            family = base.dataset_family_id(store, candidate.dataset_id)
            if family in selected_families:
                continue
            new_needs = (coverage_by_id[candidate.dataset_id] & required) - covered
            score_ratio = float(candidate.final_score) / top_score
            if selected and not new_needs and score_ratio < 0.90:
                continue
            key = (
                float(len(new_needs)),
                score_ratio,
                candidate.final_score,
                candidate.retrieval_score,
            )
            if best_key is None or key > best_key:
                best = candidate
                best_key = key
                best_new = new_needs
                best_score_ratio = score_ratio

        if best is None:
            break

        if selected:
            if not best_new and best_score_ratio < 0.90:
                steps.append({
                    "dataset_id": best.dataset_id,
                    "decision": "stop",
                    "reason": "no_new_coverage_and_below_near_tie_threshold",
                    "score": best.final_score,
                    "score_ratio_to_top1": round(best_score_ratio, 4),
                })
                break
            if best_new and best_score_ratio < 0.72:
                steps.append({
                    "dataset_id": best.dataset_id,
                    "decision": "stop",
                    "reason": "new_coverage_but_score_too_low",
                    "new_needs": sorted(best_new),
                    "score": best.final_score,
                    "score_ratio_to_top1": round(best_score_ratio, 4),
                })
                break

        selected.append(best)
        selected_families.add(base.dataset_family_id(store, best.dataset_id))
        covered.update(coverage_by_id[best.dataset_id] & required)
        steps.append({
            "dataset_id": best.dataset_id,
            "decision": "select",
            "new_needs": sorted(best_new),
            "covered_after": sorted(covered),
            "score": best.final_score,
            "score_ratio_to_top1": round(best_score_ratio, 4),
        })
        if required <= covered:
            break

    if not selected:
        selected = pool[:1]
        covered.update(coverage_by_id[selected[0].dataset_id] & required)
        steps.append({
            "dataset_id": selected[0].dataset_id,
            "decision": "select",
            "reason": "fallback_keep_top1",
            "new_needs": sorted(coverage_by_id[selected[0].dataset_id] & required),
            "covered_after": sorted(covered),
            "score": selected[0].final_score,
            "score_ratio_to_top1": 1.0,
        })

    return selected, {
        "mode": "adaptive_minimum",
        "selection_reason": (
            "all_explicit_needs_covered"
            if required <= covered else "partial_coverage_stopped_by_marginal_gain"
        ),
        "required_needs": sorted(required),
        "covered_needs": sorted(covered),
        "uncovered_needs": sorted(required - covered),
        "selected_size": len(selected),
        "candidate_pool_size": pool_size,
        "soft_cap": soft_cap,
        "hard_max_results": max_results,
        "explicit_multi_request": explicit_multi_request,
        "steps": steps,
    }


def pair_trace(
    item: TaskDatasetPairDiscovery,
    store: base.WikiStore,
) -> dict[str, Any]:
    return {
        "pair_id": item.pair_id,
        "task_id": item.task_id,
        "dataset_id": item.dataset_id,
        "supporting_use_ids": sorted(item.supporting_use_ids),
        "supporting_use_count": len(item.supporting_use_ids),
        "node_hits": item.node_hits,
        "pair_rrf_score": item.pair_rrf_score,
        "normalized_pair_rrf_score": item.normalized_pair_rrf_score,
        "pair_local_score": item.pair_local_score,
        "pair_seed_score": item.pair_seed_score,
        "rerank_score": item.rerank_score,
        "rerank_position": item.rerank_position,
    }


def dataset_trace(candidate: NodeEdgeDatasetCandidate) -> dict[str, Any]:
    return {
        "dataset_id": candidate.dataset_id,
        "final_score": candidate.final_score,
        "aggregated_pair_score": candidate.aggregated_pair_score,
        "retrieval_pair_score": candidate.retrieval_score,
        "supporting_pair_scores": candidate.supporting_pair_scores,
        "supporting_use_scores": candidate.supporting_use_scores,
        "supporting_use_ids": sorted(candidate.supporting_use_ids),
        "supporting_doc_ids": sorted(candidate.supporting_doc_ids),
        "derivation_notes": candidate.derivation_notes,
        "rerank_reason": candidate.rerank_reason,
    }


def run_node_edge_query(
    *,
    client: OpenAI,
    api_key: str,
    chat_model: str,
    embedding_model: str,
    rerank_model: str,
    rerank_url: str,
    rerank_instruct: str,
    store: base.WikiStore,
    documents: list[base.SearchDocument],
    embeddings: np.ndarray,
    question: str,
    dense_top_k: int,
    bm25_top_k: int,
    rrf_k: int,
    task_seed_top_k: int,
    dataset_seed_top_k: int,
    stage_seed_top_k: int,
    task_node_weight: float,
    dataset_node_weight: float,
    stage_node_weight: float,
    specificity_floor: float,
    pair_top_k: int,
    max_pairs_per_task: int,
    max_pairs_per_dataset: int,
    pair_local_weight: float,
    supporting_pairs_per_dataset: int,
    supporting_uses_per_pair: int,
    retrieval_top_k: int,
    candidate_top_k: int,
    max_results: int,
    minimum_score: float,
    selection_mode: str,
    max_document_chars: int,
    rerank_timeout: float,
    use_rerank: bool,
    use_answer_llm: bool,
    family_dedup: bool,
    map_derived_to_source: bool,
    family_overrides: dict[str, str] | None = None,
) -> tuple[str, dict[str, Any]]:

    # A. Query understanding and deterministic multi-route query construction.
    plan, rewrite_raw = rewrite_hyperedge_query(client, chat_model, question)
    if selection_mode == "scoped":
        add_domain_routes(plan, question)

    # B. Node-only retrieval: Task / Stage / Dataset.
    bm25 = base.BM25Index(documents)
    node_results, raw_rankings = node_only_hybrid_retrieve(
        client,
        embedding_model,
        documents,
        embeddings,
        bm25,
        plan,
        dense_top_k,
        bm25_top_k,
        rrf_k,
    )
    node_seeds, node_seed_diagnostics = select_node_seeds(
        node_results,
        task_seed_top_k,
        dataset_seed_top_k,
        stage_seed_top_k,
    )

    # C. One-hop relation completion. DatasetUse is immediately aggregated into
    # unique (Task, Dataset) candidates and kept as provenance only.
    discovered_pairs, expansion_trace = expand_nodes_to_task_dataset_pairs(
        store,
        documents,
        node_seeds,
        rrf_k,
        task_node_weight,
        dataset_node_weight,
        stage_node_weight,
        specificity_floor,
    )
    pair_local_diagnostics = score_pair_local_semantics(
        client=client,
        embedding_model=embedding_model,
        store=store,
        question=question,
        discovered=discovered_pairs,
        local_weight=pair_local_weight,
    )
    pair_rrf_top, pair_rrf_dropped, pair_diversity_diagnostics = rank_task_dataset_pairs(
        discovered=discovered_pairs,
        pair_top_k=pair_top_k,
        max_per_task=max_pairs_per_task,
        max_per_dataset=max_pairs_per_dataset,
    )

    if selection_mode == "scoped":
        pair_rrf_top, reservation = reserve_need_pairs(
            store, plan, question, discovered_pairs, pair_rrf_top, pair_top_k,
        )
        selected_pair_ids = {p.pair_id for p in pair_rrf_top}
        pair_rrf_dropped = [p for p in discovered_pairs.values() if p.pair_id not in selected_pair_ids]
        pair_diversity_diagnostics["v4_need_reservation"] = reservation

    # D. One expensive semantic rerank over only pair Top-K.
    if use_rerank:
        ranked_pairs, rerank_raw = rerank_task_dataset_pairs(
            store=store,
            question=question,
            plan=plan,
            pool=pair_rrf_top,
            api_key=api_key,
            rerank_url=rerank_url,
            rerank_model=rerank_model,
            rerank_instruct=rerank_instruct,
            max_document_chars=max_document_chars,
            timeout=rerank_timeout,
            supporting_uses_per_pair=supporting_uses_per_pair,
        )
    else:
        ranked_pairs = sorted(
            pair_rrf_top,
            key=lambda item: item.pair_seed_score,
            reverse=True,
        )
        for position, item in enumerate(ranked_pairs, start=1):
            item.rerank_score = item.pair_seed_score
            item.rerank_position = position
        rerank_raw = {"disabled": True}

    # E. Task-Dataset pair -> Dataset aggregation; no second LLM rerank.
    candidates, aggregation_excluded = aggregate_reranked_pairs_to_datasets(
        store=store,
        ranked_pairs=ranked_pairs,
        supporting_pairs_per_dataset=supporting_pairs_per_dataset,
        supporting_uses_per_pair=supporting_uses_per_pair,
        map_derived_to_source=map_derived_to_source,
    )
    candidates, intent_calibration_diagnostics = recalibrate_dataset_candidates(
        store,
        plan,
        candidates,
    )

    # V5 expands only evidence-backed relatives (source_dataset_id or an
    # explicit reviewed override). A relative carries its own DatasetUse facts
    # and never inherits capabilities from the retrieved anchor.
    family_overrides = family_overrides or {}
    v5_selection_candidates, family_expansion_trace = expand_candidates(
        store=store,
        ranked=candidates,
        candidate_class=NodeEdgeDatasetCandidate,
        overrides=family_overrides,
    )

    # Keep the pre-dedup list for evidence_top1.  Family de-duplication is a
    # useful presentation rule for ordinary ranked retrieval, but applying it
    # before checking the DatasetUse evidence can discard the only family
    # member that proves one explicit user need.
    evidence_selection_candidates = list(v5_selection_candidates)
    candidates, family_removed = deduplicate_dataset_families(
        store,
        candidates,
        enabled=family_dedup,
    )

    # Retrieval ranking is frozen here and should be used for Gold Recall@K.
    retrieval_top = candidates[:max(0, retrieval_top_k)]

    # F. Optional downstream minimum/recommendation layer.
    base.candidate_context = node_edge_candidate_context
    selection_candidates = (
        evidence_selection_candidates
        if selection_mode in {"evidence_top1", "scoped"} else candidates
    )
    selected, selection_diagnostics = select_final_datasets(
        store=store,
        plan=plan,
        question=question,
        ranked=selection_candidates,
        selection_mode=selection_mode,
        max_results=max_results,
        minimum_score=minimum_score,
        candidate_top_k=candidate_top_k,
        family_overrides=family_overrides,
    )
    adaptive_selected, adaptive_selection_diagnostics = select_adaptive_minimum_datasets(
        store=store,
        plan=plan,
        ranked=candidates,
        max_results=max_results,
        minimum_score=minimum_score,
        candidate_top_k=candidate_top_k,
    )

    # G. Answer generation still receives DatasetUse provenance through each
    # DatasetCandidate.supporting_use_ids.
    packages = [
        base.build_evidence_package(store, plan, candidate)
        for candidate in selected
    ]
    if selection_mode == "scoped":
        # Render only the actual support matrix; an LLM must not turn unknown
        # metadata or a unioned parent profile into a complete-support claim.
        answer = scoped_answer(store, selected, selection_diagnostics)
        answer_raw = ""
        validation_errors = []
        for package in packages:
            package["v4_scope_warning"] = "Registry fields are discovery metadata, not a joint capability claim."
            package["v4_scoped_support"] = selection_diagnostics["candidate_evidence"][package["dataset_id"]]
    elif use_answer_llm:
        answer, answer_raw = base.generate_answer(
            client,
            chat_model,
            question,
            plan,
            packages,
        )
        validation_errors = base.validate_generated_answer(
            answer,
            question,
            packages,
        )
        if validation_errors:
            answer = base.deterministic_answer(question, packages)
    else:
        answer = base.deterministic_answer(question, packages)
        answer_raw = ""
        validation_errors = []

    unique_discovered_use_ids = sorted({
        use_id
        for pair in discovered_pairs.values()
        for use_id in pair.supporting_use_ids
    })

    trace = {
        "created_at": base.utc_now(),
        "pipeline": "node_only_lane_rrf_task_dataset_pair_v5_family_scoped",
        "question": question,
        "query_plan": asdict(plan),
        "rewrite_raw": rewrite_raw,

        "retrieval_design": {
            "indexed_types": ["Task", "Stage", "Dataset"],
            "dataset_use_direct_retrieval": False,
            "node_rrf": True,
            "intent_lane_rrf": True,
            "one_hop_relation_completion": True,
            "candidate_granularity": "task_dataset_pair",
            "dataset_use_role": "supporting_evidence_only",
            "endpoint_votes_deduplicated_per_pair": True,
            "pair_graph_specificity": True,
            "stage_can_create_pairs": False,
            "pair_local_semantic_auxiliary": pair_local_weight > 0,
            "semantic_rerank_count": 1 if use_rerank else 0,
            "dataset_aggregation": "normalized_decayed_top_task_dataset_pair_scores",
            "retrieval_and_recommendation_separated": True,
        },

        "raw_rankings": raw_rankings,
        "node_rrf_results": node_results[:100],
        "node_seed_diagnostics": node_seed_diagnostics,
        "node_seed_count": len(node_seeds),

        "pair_expansion": expansion_trace,
        "discovered_dataset_use_count": len(unique_discovered_use_ids),
        "discovered_dataset_use_ids": unique_discovered_use_ids,
        "discovered_task_dataset_pair_count": len(discovered_pairs),
        "pair_ranked_count": len(discovered_pairs),
        "pair_top_k": pair_top_k,
        "pair_local_diagnostics": pair_local_diagnostics,
        "pair_diversity_diagnostics": pair_diversity_diagnostics,
        "pair_rrf_top": [pair_trace(item, store) for item in pair_rrf_top],
        "pair_rrf_top_ids": [item.pair_id for item in pair_rrf_top],
        "pair_rrf_dropped_ids": [item.pair_id for item in pair_rrf_dropped],

        "rerank_model": rerank_model if use_rerank else None,
        "rerank_instruct": rerank_instruct if use_rerank else None,
        "rerank_raw": rerank_raw,
        "ranked_task_dataset_pairs": [
            pair_trace(item, store) for item in ranked_pairs
        ],

        "aggregation": {
            "method": "top_m_task_dataset_pair_decayed",
            "weights": list(DEFAULT_DATASET_PAIR_DECAY_WEIGHTS),
            "supporting_pairs_per_dataset": supporting_pairs_per_dataset,
            "supporting_uses_per_pair": supporting_uses_per_pair,
            "map_derived_to_source": map_derived_to_source,
        },
        "aggregation_excluded": aggregation_excluded,
        "family_dedup_enabled": family_dedup,
        "family_dedup_removed": family_removed,
        "family_expansion": family_expansion_trace,
        "intent_calibration_diagnostics": intent_calibration_diagnostics,
        "evidence_selection_candidate_ids": [
            candidate.dataset_id for candidate in evidence_selection_candidates
        ],
        "selection_candidates": [dataset_trace(c) for c in selection_candidates],
        "ranked_candidates": [
            dataset_trace(candidate) for candidate in candidates
        ],

        "retrieval_top_k": retrieval_top_k,
        "retrieval_top_k_dataset_ids": [
            candidate.dataset_id for candidate in retrieval_top
        ],

        "selection_mode": selection_mode,
        "selection_diagnostics": selection_diagnostics,
        "selected_dataset_ids": [
            candidate.dataset_id for candidate in selected
        ],
        "selected_dataset_families": annotate_family_output(
            store=store,
            dataset_ids=[candidate.dataset_id for candidate in selected],
            overrides=family_overrides,
        ),
        "portfolio_dataset_ids": selection_diagnostics.get("portfolio_dataset_ids", [c.dataset_id for c in selected]),
        "adaptive_selection_diagnostics": adaptive_selection_diagnostics,
        "adaptive_selected_dataset_ids": [
            candidate.dataset_id for candidate in adaptive_selected
        ],

        "evidence_packages": packages,
        "answer_raw": answer_raw,
        "answer_validation_errors": validation_errors,
        "final_answer": answer,
    }
    return answer, trace


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description=(
            "V5: family-aware node retrieval -> Task-Dataset pair completion/rerank "
            "-> Dataset aggregation -> optional minimum-set recommendation"
        )
    )
    parser.add_argument("--wiki-root", type=Path, default=script_dir / "newLLMWiki")
    parser.add_argument(
        "--index-dir",
        type=Path,
        default=script_dir / "newWikiNodeOnlyHyperedgeRRFIndex",
    )
    parser.add_argument("--build-index", action="store_true")
    parser.add_argument("--question", help="材料研发数据集问题")

    parser.add_argument(
        "--chat-model",
        default=os.getenv("QWEN_MODEL", base.DEFAULT_CHAT_MODEL),
    )
    parser.add_argument(
        "--embedding-model",
        default=os.getenv("QWEN_EMBEDDING_MODEL", base.DEFAULT_EMBEDDING_MODEL),
    )
    parser.add_argument(
        "--rerank-model",
        default=os.getenv("QWEN_RERANK_MODEL", DEFAULT_RERANK_MODEL),
    )
    parser.add_argument("--rerank-url", default=os.getenv("QWEN_RERANK_URL"))
    parser.add_argument("--rerank-instruct", default=DEFAULT_RERANK_INSTRUCT)
    parser.add_argument("--rerank-timeout", type=float, default=240.0)

    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--dense-top-k", type=int, default=30)
    parser.add_argument("--bm25-top-k", type=int, default=30)
    parser.add_argument("--rrf-k", type=int, default=60)

    parser.add_argument("--task-seed-top-k", type=int, default=DEFAULT_TASK_SEED_TOP_K)
    parser.add_argument("--dataset-seed-top-k", type=int, default=DEFAULT_DATASET_SEED_TOP_K)
    parser.add_argument("--stage-seed-top-k", type=int, default=DEFAULT_STAGE_SEED_TOP_K)

    parser.add_argument("--task-node-weight", type=float, default=DEFAULT_TASK_NODE_WEIGHT)
    parser.add_argument("--dataset-node-weight", type=float, default=DEFAULT_DATASET_NODE_WEIGHT)
    parser.add_argument("--stage-node-weight", type=float, default=DEFAULT_STAGE_NODE_WEIGHT)
    parser.add_argument("--specificity-floor", type=float, default=DEFAULT_SPECIFICITY_FLOOR)

    # New V3 names. Old V2 option names are accepted as aliases where semantics
    # remain close enough, which makes existing batch commands easier to reuse.
    parser.add_argument(
        "--pair-top-k", "--edge-top-k",
        dest="pair_top_k",
        type=int,
        default=DEFAULT_PAIR_TOP_K,
        help="进入昂贵 rerank 的 Task-Dataset pair 数量",
    )
    parser.add_argument(
        "--max-pairs-per-task", "--max-edge-uses-per-task",
        dest="max_pairs_per_task",
        type=int,
        default=DEFAULT_MAX_PAIRS_PER_TASK,
        help="Pair Top-K 前每个 Task 最多保留的不同 Dataset 数；0 表示不限制",
    )
    parser.add_argument(
        "--max-pairs-per-dataset", "--max-edge-uses-per-dataset",
        dest="max_pairs_per_dataset",
        type=int,
        default=DEFAULT_MAX_PAIRS_PER_DATASET,
        help="Pair Top-K 前每个 Dataset 最多保留的不同 Task 数；0 表示不限制",
    )
    parser.add_argument(
        "--pair-local-weight", "--edge-local-weight",
        dest="pair_local_weight",
        type=float,
        default=DEFAULT_PAIR_LOCAL_WEIGHT,
        help="Pair-local embedding 相似度在粗排中的权重，0 可关闭",
    )
    parser.add_argument(
        "--supporting-pairs-per-dataset", "--supporting-uses-per-dataset",
        dest="supporting_pairs_per_dataset",
        type=int,
        default=DEFAULT_SUPPORTING_PAIRS_PER_DATASET,
        help="Dataset 聚合时最多使用的高分 Task-Dataset pair 数",
    )
    parser.add_argument(
        "--supporting-uses-per-pair",
        type=int,
        default=DEFAULT_SUPPORTING_USES_PER_PAIR,
        help="每个 Task-Dataset pair 最多保留/展示的代表性 DatasetUse 证据数",
    )
    # Deprecated V2 argument retained only so old scripts do not fail parsing.
    parser.add_argument(
        "--max-edge-uses-per-task-dataset",
        type=int,
        default=0,
        help=argparse.SUPPRESS,
    )

    parser.add_argument(
        "--retrieval-top-k",
        type=int,
        default=DEFAULT_RETRIEVAL_TOP_K,
        help="独立记录用于 Gold Recall@K/NDCG@K 的 Dataset 排名数量",
    )
    parser.add_argument(
        "--candidate-top-k",
        type=int,
        default=30,
        help="可选 minimum/recommendation 层查看的 Dataset 候选窗口",
    )
    parser.add_argument("--max-results", type=int, default=6)
    parser.add_argument("--minimum-score", type=float, default=0.25)
    parser.add_argument(
        "--selection-mode",
        choices=("scoped", "topk", "evidence_top1", "minimum", "recommend"),
        default="scoped",
        help=(
            "scoped使用单条证据的完整需求匹配并输出待核实候选；topk直接返回检索排名；evidence_top1为V3基线；"
            "minimum只作为检索后的最小数据集组合层；recommend保留原基础模块推荐器"
        ),
    )

    parser.add_argument(
        "--no-family-dedup",
        action="store_true",
        help="关闭 Dataset family 去重，用于检查父集/子集粒度问题",
    )
    parser.add_argument(
        "--family-config",
        type=Path,
        default=script_dir / "dataset_families_v5.json",
        help="可选的、经证据审核的数据集家族覆盖配置",
    )
    parser.add_argument(
        "--map-derived-to-source",
        action="store_true",
        help="将不可推荐派生数据映射到其公共 source_dataset_id；默认关闭以保护检索评测身份",
    )
    parser.add_argument("--max-document-chars", type=int, default=DEFAULT_RERANK_DOCUMENT_CHARS)
    parser.add_argument("--no-rerank", action="store_true")
    parser.add_argument("--no-answer-llm", action="store_true")
    parser.add_argument("--trace-output", type=Path)
    return parser.parse_args()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    load_dotenv(project_root / ".env")

    api_key = os.getenv("QWEN_API_KEY") or os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        raise ValueError("QWEN_API_KEY或DASHSCOPE_API_KEY未配置")

    rerank_api_key = os.getenv("QWEN_RERANK_API_KEY") or api_key
    chat_base_url = os.getenv("QWEN_BASE_URL", base.DEFAULT_BASE_URL)
    rerank_url = derive_rerank_url(chat_base_url, args.rerank_url)

    client = OpenAI(
        api_key=api_key,
        base_url=chat_base_url,
        timeout=240.0,
        max_retries=2,
    )
    store = base.WikiStore(args.wiki_root)
    family_overrides = load_family_overrides(args.family_config)

    index_files = [
        args.index_dir / "documents.json",
        args.index_dir / "embeddings.npy",
        args.index_dir / "index_meta.json",
    ]
    if args.build_index or not all(path.is_file() for path in index_files):
        documents, embeddings, meta = build_node_index(
            store,
            client,
            args.index_dir,
            args.embedding_model,
            args.batch_size,
            args.max_document_chars,
        )
    else:
        documents, embeddings, meta = load_node_index(
            store,
            args.index_dir,
        )
        args.embedding_model = meta["embedding_model"]

    if not args.question:
        print(json.dumps({
            "status": "node_only_task_dataset_pair_v3_index_ready",
            "index_dir": str(args.index_dir.resolve()),
            "documents": len(documents),
            "embedding_model": args.embedding_model,
            "rerank_model": args.rerank_model,
            "wiki_fingerprint": meta["wiki_fingerprint"],
            "note": "V3 node serialization is unchanged from V2; index version remains 4.0.",
        }, ensure_ascii=False, indent=2))
        return 0

    answer, trace = run_node_edge_query(
        client=client,
        api_key=rerank_api_key,
        chat_model=args.chat_model,
        embedding_model=args.embedding_model,
        rerank_model=args.rerank_model,
        rerank_url=rerank_url,
        rerank_instruct=args.rerank_instruct,
        store=store,
        documents=documents,
        embeddings=embeddings,
        question=args.question,
        dense_top_k=args.dense_top_k,
        bm25_top_k=args.bm25_top_k,
        rrf_k=args.rrf_k,
        task_seed_top_k=args.task_seed_top_k,
        dataset_seed_top_k=args.dataset_seed_top_k,
        stage_seed_top_k=args.stage_seed_top_k,
        task_node_weight=args.task_node_weight,
        dataset_node_weight=args.dataset_node_weight,
        stage_node_weight=args.stage_node_weight,
        specificity_floor=args.specificity_floor,
        pair_top_k=args.pair_top_k,
        max_pairs_per_task=args.max_pairs_per_task,
        max_pairs_per_dataset=args.max_pairs_per_dataset,
        pair_local_weight=args.pair_local_weight,
        supporting_pairs_per_dataset=args.supporting_pairs_per_dataset,
        supporting_uses_per_pair=args.supporting_uses_per_pair,
        retrieval_top_k=args.retrieval_top_k,
        candidate_top_k=args.candidate_top_k,
        max_results=args.max_results,
        minimum_score=args.minimum_score,
        selection_mode=args.selection_mode,
        max_document_chars=args.max_document_chars,
        rerank_timeout=args.rerank_timeout,
        use_rerank=not args.no_rerank,
        use_answer_llm=not args.no_answer_llm,
        family_dedup=not args.no_family_dedup,
        map_derived_to_source=args.map_derived_to_source,
        family_overrides=family_overrides,
    )

    trace_path = args.trace_output
    if trace_path is None:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        trace_path = (
            script_dir / "retrieval_runs" /
            f"node_only_task_dataset_pair_v3_{stamp}.json"
        )
    base.write_json(trace_path, trace)
    print(answer)
    print(f"\n[trace] {trace_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
