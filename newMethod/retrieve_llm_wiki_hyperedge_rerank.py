#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DatasetUse 单超边检索 + 专用 Rerank 模型版本。

本文件不会修改 retrieve_llm_wiki.py。它复用原版本的 Query Rewrite、
Embedding、BM25、RRF、结果集合选择和答案生成，仅替换以下核心逻辑：

1. Task、Stage、Dataset 作为可检索超节点；
2. DatasetUse 作为连接 Task、Stage、Dataset、Paper 的单一超边；
3. 命中超节点后，只获取其直接所属 DatasetUse，不进行递归图扩展；
4. DatasetUse 去重后，将 QueryPlan 与完整 DatasetUse 事实文本提交给专用
   rerank 模型，不再手工组合 task/material/property/stage/role 权重；
5. 同一 Dataset 先聚合本轮最相关的少量 DatasetUse，再把完整Dataset证据包
   放入同一次rerank请求，避免单条用途最大值和大型数据库字段数量主导排序；
6. 通过证据包分数的自然落差确定相关前沿，不设置固定Top-3或相关性阈值；
7. 最终只删除同一数据家族或Task/角色/阶段/需求证据完全重复的候选，并在
   工作流需求尚未满足时继续补充，最多返回6个。

默认调用阿里云百炼 qwen3-rerank。rerank 候选放在同一次请求中，避免把
不同请求返回的相对分数直接进行跨批比较。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit, urlunsplit

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

import retrieve_llm_wiki as base


# ---------------------------------------------------------------------------
# 0. 独立版本配置
# ---------------------------------------------------------------------------

HYPEREDGE_INDEX_VERSION = "dataset-use-hyperedge-rerank-2.0-group-aware"
DEFAULT_RERANK_MODEL = "qwen3-rerank"
DEFAULT_MAX_RERANK_USES = 100
DEFAULT_MAX_RERANK_USES_PER_TASK = 12
DEFAULT_MAX_RERANK_USES_PER_DATASET = 2
DEFAULT_SUPPORTING_USES_PER_DATASET = 3
DEFAULT_RERANK_DOCUMENT_CHARS = 8_000

# qwen3-rerank 的 instruct 使用英文，以符合服务文档建议。这里明确说明
# “跨性质源数据集可以相关”，避免形成能预训练源因不等于目标性质而被误杀。
DEFAULT_RERANK_INSTRUCT = (
    "Rank each DatasetUse factual record by how useful it is as evidence for "
    "selecting datasets needed to complete the materials R&D query. Treat each "
    "record as one possible role in a multi-dataset workflow, not as a dataset "
    "that must satisfy every need alone. Match material scope and task mechanism "
    "first, then dataset role, research stage, properties, and explicit "
    "constraints. For cross-property transfer learning, a pretraining source "
    "may have labels different from the target properties; do not reject it "
    "only for that reason. Small single-property datasets may be valid "
    "fine-tuning or evaluation targets. Prefer explicit evidence and penalize "
    "explicit conflicts."
)

DATASET_PACKAGE_RERANK_INSTRUCT = (
    "Score every Dataset evidence package independently against the materials "
    "R&D query. Judge the task mechanism, material domain, input representation, "
    "DatasetUse role, evaluation protocol and provenance before broad property "
    "availability. A large database is not relevant merely because it contains "
    "many fields. Prefer a benchmark suite for an explicit standardized benchmark "
    "request, an experimental dataset for an experimental-label role, and the "
    "correct source/target side for transfer learning. Treat different databases "
    "used for cross-database validation as complementary evidence, not aliases."
)


# ---------------------------------------------------------------------------
# 1. 本轮 DatasetUse 超边候选与 Dataset 聚合候选
# ---------------------------------------------------------------------------

@dataclass
class HyperedgeDiscovery:
    """一条 DatasetUse 在本轮召回中被发现的全部来源。"""

    dataset_use_id: str
    direct_hits: list[dict[str, Any]] = field(default_factory=list)
    anchor_hits: list[dict[str, Any]] = field(default_factory=list)
    best_discovery_score: float = 0.0
    rerank_score: float = 0.0
    rerank_position: int | None = None


@dataclass
class HyperedgeDatasetCandidate(base.DatasetCandidate):
    """由已评分 DatasetUse 超边聚合而成的数据集候选。"""

    use_rerank_score: float = 0.0
    dataset_package_score: float | None = None
    supporting_use_scores: dict[str, float] = field(default_factory=dict)


@dataclass
class HyperedgeQueryPlan(base.QueryPlan):
    """QueryPlan extended with online-only workflow semantics."""

    task_mechanisms: list[str] = field(default_factory=list)
    input_representations: list[str] = field(default_factory=list)
    dataset_role_needs: list[dict[str, str]] = field(default_factory=list)


# 当前查询中每条 DatasetUse 的 rerank 分数。基础模块的集合选择与证据包
# 构造会调用 candidate_context()；通过该映射让返回用途按本轮相关性排序。
_CURRENT_USE_SCORES: dict[str, float] = {}


# ---------------------------------------------------------------------------
# 2. 干净的超节点与超边文本：复用 raw JSONL，不索引 Markdown 历史列表
# ---------------------------------------------------------------------------

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


def serialize_dataset_use_retrieval(
    store: base.WikiStore,
    use: dict[str, Any],
    max_chars: int = DEFAULT_RERANK_DOCUMENT_CHARS,
) -> str:
    """Build an edge-local document for Dense/BM25 retrieval.

    The complete Task block is intentionally excluded here. Otherwise every
    DatasetUse of one Task becomes a near-duplicate document and the Task gets
    one retrieval vote per incident edge. The full hyperedge serializer above
    is still used after pool construction by the dedicated rerank model.
    """

    task = store.task_by_id[use["task_id"]]
    stage = store.stage_by_id[use["stage_id"]]
    dataset = store.dataset_by_id[use["dataset_id"]]
    mechanism_hints = [
        value for value in task.get("constraints", [])
        if any(token in str(value).casefold() for token in (
            "transfer", "pretrain", "fine-tun", "out-of-distribution",
            "extrapolat", "screen", "generation",
        ))
    ]
    text = "\n".join([
        "[RETRIEVAL RECORD] DatasetUse edge-local facts",
        f"[DATASET USE ID] {use['dataset_use_id']}",
        f"[DATASET ID] {dataset['dataset_id']}",
        f"[DATASET] {dataset.get('canonical_name') or 'unknown'}",
        f"[DATASET ALIASES] {_values(dataset.get('raw_names', []), 12)}",
        f"[USAGE ROLE] {use.get('usage_role') or 'unknown'}",
        f"[PURPOSE] {use.get('purpose') or 'unknown'}",
        f"[USED FIELDS] {_values(use.get('used_fields', []), 24)}",
        f"[FILTER CONDITIONS] {_values(use.get('filter_conditions', []), 12)}",
        f"[CONSTRUCTION METHOD] {use.get('construction_method') or 'unknown'}",
        f"[SAMPLE COUNT] {use.get('sample_count') or 'unknown'}",
        f"[STAGE TYPE] {stage.get('stage_type') or 'unknown'}",
        f"[STAGE NAME] {stage.get('stage_name_raw') or 'unknown'}",
        f"[TASK ID] {task['task_id']}",
        f"[TASK LABEL] {task.get('task_name_raw') or task.get('task_name_canonical')}",
        f"[TASK MECHANISM HINTS] {_values(mechanism_hints, 8)}",
        f"[DATASET MATERIAL SCOPE] {_values(dataset.get('material_scope', []), 20)}",
        f"[DATASET PROPERTIES] {_values(dataset.get('available_properties', []), 32)}",
        f"[DATASET FIELDS] {_values(dataset.get('available_fields', []), 32)}",
        f"[AVAILABILITY] {dataset.get('availability') or 'unknown'}",
    ])
    return text[:max_chars]


# ---------------------------------------------------------------------------
# 2.1 Role- and mechanism-aware Query Rewrite for the hyperedge retriever
# ---------------------------------------------------------------------------

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
- Use concise professional canonical English values.
- support_text must be copied exactly from the question.
- Do not invent a material, property, dataset name, role, scale, constraint,
  numerical range, chemistry, or experimental requirement.
- Extract only what is explicit enough to affect dataset retrieval. Keep a
  field empty when the question does not state it.
- A material_scope item must denote a material class or system. Composition,
  elemental fractions, chemical formula, stoichiometry, crystal/atomic/
  molecular structure and other feature representations belong only in
  input_representations.
- Site definitions and allowed species such as "A = ...; B = ...; X = ..."
  are constraints on one material system, not separate material scopes.
- target_properties must contain only properties explicitly named by the user.
  Never specialize "physical properties" into a list of unstated properties.
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


def _exact_support_present(support: str, question: str) -> bool:
    normalized_support = re.sub(r"\s+", "", support).casefold()
    normalized_question = re.sub(r"\s+", "", question).casefold()
    return bool(normalized_support) and normalized_support in normalized_question


def _first_support(pattern: str, question: str) -> str:
    match = re.search(pattern, question, flags=re.IGNORECASE)
    return match.group(0) if match else ""


def _light_tokens(value: str) -> set[str]:
    """Small lexical normalizer used to reject unsupported specializations."""

    result: set[str] = set()
    for token in re.findall(r"[a-z0-9]+", value.casefold()):
        if token.endswith("ies") and len(token) > 4:
            token = token[:-3] + "y"
        elif token.endswith("s") and len(token) > 3:
            token = token[:-1]
        if token not in {"the", "a", "an", "of", "and", "or", "for"}:
            result.add(token)
    return result


def normalize_conservative_materials(items: Any, question: str) -> list[str]:
    """Keep explicit material systems; reject features and site definitions."""

    result: list[str] = []
    material_pattern = re.compile(
        r"perovsk|molecules?|cataly|polymer|alloy|oxide|semiconductor|"
        r"compounds?|materials?|solid[- ]state|inorganic|organic|"
        r"crystalline|crystals?|ceramic|metal|cathode|钙钛矿|分子|"
        r"催化|聚合物|合金|氧化物|半导体|材料|固体|无机|有机|晶体"
    )
    input_pattern = re.compile(
        r"compositions?|elemental fractions?|chemical formulas?|"
        r"stoichiometr|crystal structures?|atomic structures?|"
        r"molecular structures?|coordinates?|features?|inputs?|"
        r"组成|元素分数|元素比例|化学式|化学计量|晶体结构|"
        r"原子结构|分子结构|坐标|特征|输入"
    )
    for value, support in base.supported_item_pairs(items, question):
        text = f"{value} {support}".casefold()
        if re.search(r"(?:^|[;(,])\s*[abx]\s*=", support, re.IGNORECASE):
            continue
        stripped = input_pattern.sub(" ", text)
        # If removing feature/input phrases leaves no explicit material noun,
        # this is an input representation rather than a material scope.
        if input_pattern.search(text) and not material_pattern.search(stripped):
            continue
        if not material_pattern.search(text):
            continue
        normalized = base.normalize_materials(
            [{"value": value, "support_text": support}], question
        )
        result.extend(normalized)
    return base.unique_strings(result)


def normalize_conservative_properties(items: Any, question: str) -> list[str]:
    """Accept explicit properties without expanding broad wording."""

    result: list[str] = []
    synonym_pattern = re.compile(
        r"band\s*gap|bandgap|stabil|formation energ|decomposition energ|"
        r"energy above (?:the )?hull|e\s*hull|bulk modul|shear modul|"
        r"dielectric|permittivity|thermoelectric|seebeck|piezoelectric|"
        r"exfoliation|homo|lumo|dipole|forces?|stresses?|magnetic moments?|"
        r"charge density|synthesiz|带隙|稳定|形成能|分解能|凸包|体积模量|"
        r"剪切模量|介电|热电|压电|剥离能|偶极|力|应力|磁矩|电荷密度|可合成"
    )
    for value, support in base.supported_item_pairs(items, question):
        grounded = _light_tokens(value) <= _light_tokens(support)
        if not grounded and not synonym_pattern.search(support.casefold()):
            continue
        result.extend(base.normalize_properties(
            [{"value": value, "support_text": support}], question
        ))
    return base.unique_strings(result)


def normalize_conservative_constraints(items: Any, question: str) -> list[str]:
    """Keep only explicit limitations and recover site-species definitions."""

    marker = re.compile(
        r"\bonly\b|without|must|required?|under|varying|range|between|"
        r"at least|at most|exclude|limited|public|open access|"
        r"仅|只|无需|不需要|必须|要求|条件|范围|变化|公开"
    )
    result: list[str] = []
    for _, support in base.supported_item_pairs(items, question):
        if marker.search(support.casefold()) or re.search(
            r"(?:^|[;(,])\s*[abx]\s*=", support, re.IGNORECASE
        ):
            result.append(support)
    # A/B/X definitions form one filter constraint, never three material needs.
    site_clause = re.search(
        r"\([^)]*\bA\s*=.*?\bB\s*=.*?\bX\s*=[^)]]*\)",
        question,
        flags=re.IGNORECASE,
    )
    if site_clause:
        result.append(site_clause.group(0))
    return base.unique_strings(result)


def normalize_conservative_inputs(items: Any, question: str) -> list[str]:
    """Derive input representations from the quoted phrase, not LLM invention."""

    result: list[str] = []
    for _, support in base.supported_item_pairs(items, question):
        text = support.casefold()
        if re.search(r"elemental fractions?|element fractions?|元素分数|元素比例", text):
            result.append("elemental_fractions")
        elif re.search(r"chemical formulas?|化学式", text):
            result.append("chemical_formula")
        elif re.search(r"stoichiometr|化学计量", text):
            result.append("stoichiometry")
        elif re.search(r"\bcompositions?\b|化学组成|组成", text):
            result.append("composition")
        if re.search(r"crystal structures?|\bcif\b|\bposcar\b|晶体结构", text):
            result.append("crystal_structure")
        elif re.search(r"molecular structures?|\bsmiles\b|分子结构", text):
            result.append("molecular_structure")
        elif re.search(r"atomic structures?|atomic coordinates?|原子结构|原子坐标", text):
            result.append("atomic_structure")
    return base.unique_strings(result)


def normalize_conservative_mechanisms(items: Any, question: str) -> list[str]:
    """Use a small explicit workflow vocabulary; omit ordinary model names."""

    result: list[str] = []
    for _, support in base.supported_item_pairs(items, question):
        text = support.casefold()
        if re.search(r"transfer learning|knowledge transferred|迁移学习|知识迁移", text):
            result.append("transfer_learning")
        if re.search(r"pre[- ]?train|预训练", text):
            result.append("pretraining")
        if re.search(r"fine[- ]?tun|微调", text):
            result.append("fine_tuning")
        if re.search(r"out[- ]of[- ]distribution|\bood\b|extrapolat|分布外|外推", text):
            result.append("out_of_distribution")
        if re.search(r"high[- ]throughput|screening|高通量|筛选", text):
            result.append("high_throughput_screening")
        if re.search(r"molecular dynamics|分子动力学", text):
            result.append("molecular_dynamics")
    return base.unique_strings(result)


def explicit_stages_and_roles(
    question: str,
    stages: Iterable[str],
    roles: Iterable[str],
) -> tuple[list[str], list[str]]:
    """Reject stages/roles inferred only from the existence of an ML model."""

    text = question.casefold()
    stage_patterns = {
        "data_acquisition": r"collect|acquir|download|retrieve|采集|获取|下载",
        "data_preparation": r"preprocess|filter|clean|split|预处理|过滤|清洗|划分",
        "label_generation": r"label generation|generate labels?|标签生成|生成标签",
        "model_training": r"\btrain(?:ing|ed)?\b|fine[- ]?tun|pre[- ]?train|训练|微调|预训练",
        "model_evaluation": r"evaluat|benchmark|compar|\btest(?:ing)?\b|评估|基准|比较|测试",
        "candidate_generation": r"candidate generation|generate candidates?|候选生成|生成候选",
        "candidate_screening": r"screen|筛选",
        "computational_validation": r"computational validation|dft validation|first[- ]principles validation|计算验证|第一性原理验证",
        "experimental_validation": r"experiment|synthesi[sz]|measurement|实验|合成|测量",
        "other": r"$^",
    }
    role_patterns = {
        "source": r"source datasets?|源数据集",
        "training": r"training datasets?|train(?:ing)? data|训练集|训练数据",
        "validation": r"validation datasets?|validation data|验证集|验证数据",
        "test": r"test datasets?|test data|测试集|测试数据",
        "pretraining": r"pre[- ]?train|预训练",
        "label_source": r"label source|labels?|标签源|标签",
        "candidate_pool": r"candidate pool|candidate datasets?|候选池|候选数据",
        "screening": r"screen|筛选",
        "benchmark": r"benchmark|基准",
        "computational_validation": stage_patterns["computational_validation"],
        "experimental_validation": stage_patterns["experimental_validation"],
    }
    kept_stages = [
        stage for stage in stages
        if stage in stage_patterns and re.search(stage_patterns[stage], text)
    ]
    kept_roles = [
        role for role in roles
        if role in role_patterns and re.search(role_patterns[role], text)
    ]
    return base.unique_strings(kept_stages), base.unique_strings(kept_roles)


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


_BASE_PROPERTY_CONCEPTS = base.property_concepts


def hyperedge_property_concepts(values: Iterable[str]) -> set[str]:
    """Normalize Wiki abbreviations only for minimum-set coverage checks."""

    items = [str(value) for value in values]
    concepts = _BASE_PROPERTY_CONCEPTS(items)
    for value in items:
        text = re.sub(r"[_-]+", " ", value.casefold())
        text = re.sub(r"\s+", " ", text).strip()
        mapped = bool(
            _BASE_PROPERTY_CONCEPTS([value])
            & {"formation_energy", "decomposition_energy", "stability", "band_gap"}
        )
        if re.search(r"\bbg\b", text) or "band gap" in text or "bandgap" in text:
            concepts.add("band_gap")
            mapped = True
        # P024把形成能字段写成Deltae/Deltae pa；这是Wiki中的真实字段名，
        # 若不做受控别名，Experimental Formation Energy永远无法满足形成能需求。
        if re.search(r"\bdeltae(?: pa)?\b", text):
            concepts.add("formation_energy")
            mapped = True
        if "exfoli" in text:
            concepts.add("exfoliation_energy")
            mapped = True
        if any(token in text for token in (
            "dielectric", "permittivity", "polytotal", "poly elec",
        )):
            concepts.add("dielectric_property")
            mapped = True
        if "thermoelectric" in text or text == "etc":
            concepts.add("thermoelectric_property")
            mapped = True
        if "seebeck" in text:
            concepts.add("thermoelectric_property")
            mapped = True
        if "bulk modulus" in text or "bulk moduli" in text:
            concepts.add("bulk_modulus")
            mapped = True
        if "shear modulus" in text or "shear moduli" in text:
            concepts.add("shear_modulus")
            mapped = True
        if "total energy" in text:
            concepts.add("total_energy")
            mapped = True
        if "piezoelectric" in text:
            concepts.add("piezoelectric_property")
            mapped = True
        if "homo" in text:
            concepts.add("homo")
            mapped = True
        if "lumo" in text:
            concepts.add("lumo")
            mapped = True
        if mapped:
            fallback = re.sub(r"[^\w]+", "_", text).strip("_")
            canonical_names = {
                "formation_energy", "decomposition_energy", "stability",
                "band_gap", "exfoliation_energy", "dielectric_property",
                "thermoelectric_property", "bulk_modulus", "shear_modulus",
                "total_energy", "piezoelectric_property", "homo", "lumo",
            }
            if fallback not in canonical_names:
                concepts.discard(fallback)
    # 为宽性质类别补充受控的父概念，使“optical properties”可由band gap、
    # dielectric等具体字段证明；不进行任意词向量式扩张。
    snapshot = set(concepts)
    if snapshot & {
        "band_gap", "dielectric_property", "refractive_index", "slme",
        "homo", "lumo",
    } or any("optical" in value for value in snapshot):
        concepts.add("optical_properties")
    if snapshot & {
        "band_gap", "homo", "lumo", "formation_energy",
    } or any("electronic" in value for value in snapshot):
        concepts.add("electronic_properties")
    if snapshot & {
        "formation_energy", "decomposition_energy", "stability", "total_energy",
    } or any("thermodynamic" in value for value in snapshot):
        concepts.add("thermodynamic_properties")
    if snapshot & {
        "bulk_modulus", "shear_modulus", "piezoelectric_property",
    } or any("elastic" in value for value in snapshot):
        concepts.update({"elastic_properties", "tensile_properties"})
    if "thermoelectric_property" in snapshot or any(
        token in value for value in snapshot
        for token in ("thermal", "debye", "heat_capacity")
    ):
        concepts.add("thermal_properties")
    return concepts


def build_stratified_queries(plan: HyperedgeQueryPlan) -> tuple[list[str], list[str], list[str]]:
    """Give mechanisms, source/target roles and input constraints fixed slots."""

    material = " ".join(plan.material_scope) or "materials"
    properties = " ".join(plan.target_properties)
    mechanisms = " ".join(value.replace("_", " ") for value in plan.task_mechanisms)
    stages = " ".join(plan.required_stages)
    roles = " ".join(plan.preferred_usage_roles)

    source_queries: list[str] = []
    target_queries: list[str] = []
    for need in plan.dataset_role_needs:
        if need["role"] == "pretraining_source":
            relation = need["property_relation"].replace("_", " ")
            source_queries.append(
                f"{material} {need['scale']} source dataset pretraining {relation} materials properties"
            )
        elif need["role"] in {"fine_tuning_target", "evaluation_target"}:
            source_role = need["role"].replace("_", " ")
            target_queries.append(
                f"{material} {need['scale']} {source_role} dataset {properties}"
            )

    input_queries = []
    if "elemental_fractions" in plan.input_representations:
        input_queries.append(
            f"{material} elemental fractions composition chemical formula stoichiometric composition dataset"
        )

    mechanism_query = f"{material} {mechanisms} materials dataset" if mechanisms else ""
    property_query = f"{material} {properties} materials dataset" if properties else ""
    stage_query = f"{material} {stages} dataset" if stages else ""
    role_query = f"{material} {roles} dataset" if roles else ""

    # One query per intent group prevents four property queries from consuming
    # all Dense slots and repeatedly rewarding the same broad task page.
    dense = base.unique_strings([
        plan.objective,
        mechanism_query,
        *source_queries[:1],
        *target_queries[:1],
        *input_queries[:1],
        property_query,
        stage_query,
        role_query,
    ])[:8]

    property_bm25 = [
        f"{material} {' '.join(controlled_property_aliases(prop))} dataset"
        for prop in plan.target_properties
    ]
    bm25 = base.unique_strings([
        *input_queries[:1],
        mechanism_query,
        *source_queries[:1],
        *target_queries[:1],
        *property_bm25,
        stage_query,
    ])[:10]

    subtasks = base.unique_strings([
        mechanism_query,
        *source_queries,
        *target_queries,
        *input_queries,
        *[f"dataset for {material} {prop}" for prop in plan.target_properties],
        stage_query,
    ])[:12]
    return dense, bm25, subtasks


def rewrite_hyperedge_query(
    client: OpenAI,
    model: str,
    question: str,
) -> tuple[HyperedgeQueryPlan, str]:
    """Extract and validate workflow semantics, then build stratified queries."""

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

    plan = HyperedgeQueryPlan(
        **asdict(core),
        task_mechanisms=mechanisms,
        input_representations=inputs,
        dataset_role_needs=role_needs,
    )
    dense, bm25, subtasks = build_stratified_queries(plan)
    plan.dense_queries = dense
    plan.bm25_queries = bm25
    plan.subtasks = subtasks
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
# 3. 新索引：页面实体不变，但改用干净结构化文本
# ---------------------------------------------------------------------------

def build_hyperedge_documents(
    store: base.WikiStore,
    max_chars: int = DEFAULT_RERANK_DOCUMENT_CHARS,
) -> list[base.SearchDocument]:
    """构造 Task、Stage、Dataset 超节点以及 DatasetUse 超边检索文档。"""

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
    for use in store.uses:
        stage = store.stage_by_id[use["stage_id"]]
        documents.append(base.SearchDocument(
            doc_id=use["dataset_use_id"],
            entity_id=use["dataset_use_id"],
            node_type="DatasetUse",
            # Retrieval uses edge-local facts. Full Task/Stage/Dataset/Paper
            # evidence is serialized only when this edge reaches reranking.
            text=serialize_dataset_use_retrieval(store, use, max_chars),
            paper_id=use["paper_id"],
            task_id=use["task_id"],
            stage_id=use["stage_id"],
            dataset_id=use["dataset_id"],
            dataset_use_id=use["dataset_use_id"],
            stage_type=stage["stage_type"],
            usage_role=use["usage_role"],
            source_path=str(
                store.root / "pages/dataset_uses" / f"{use['dataset_use_id']}.md"
            ),
        ))
    for dataset in store.datasets:
        # 与原版本保持一致：不可直接推荐的论文派生集不作为 Dataset 初始节点，
        # 但对应 DatasetUse 超边仍可召回，并在聚合时映射到公共源。
        if not dataset.get("recommendable", False):
            continue
        documents.append(base.SearchDocument(
            doc_id=dataset["dataset_id"],
            entity_id=dataset["dataset_id"],
            node_type="Dataset",
            text=serialize_dataset_node(dataset)[:max_chars],
            dataset_id=dataset["dataset_id"],
            availability=dataset["availability"],
            recommendable=dataset["recommendable"],
            source_path=str(
                store.root / "pages/datasets" / f"{dataset['dataset_id']}.md"
            ),
        ))
    return documents


def build_hyperedge_index(
    store: base.WikiStore,
    client: OpenAI,
    index_dir: Path,
    embedding_model: str,
    batch_size: int,
    max_chars: int,
) -> tuple[list[base.SearchDocument], np.ndarray, dict[str, Any]]:
    """为干净超节点和 DatasetUse 超边建立独立 Dense 索引。"""

    documents = build_hyperedge_documents(store, max_chars)
    print(
        f"Building hyperedge embeddings for {len(documents)} records...",
        flush=True,
    )
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
        "index_version": HYPEREDGE_INDEX_VERSION,
        "created_at": base.utc_now(),
        "wiki_fingerprint": store.fingerprint(),
        "embedding_model": embedding_model,
        "document_count": len(documents),
        "embedding_dimension": int(embeddings.shape[1]),
        "node_types": ["Dataset", "DatasetUse", "Stage", "Task"],
        "dataset_use_representation": "edge_local_retrieval_full_hyperedge_rerank",
        "max_document_chars": max_chars,
    }
    base.write_json(index_dir / "index_meta.json", meta)
    return documents, embeddings, meta


def load_hyperedge_index(
    store: base.WikiStore,
    index_dir: Path,
) -> tuple[list[base.SearchDocument], np.ndarray, dict[str, Any]]:
    """加载本版本独立索引，并阻止误用原图检索索引。"""

    meta = json.loads((index_dir / "index_meta.json").read_text(encoding="utf-8"))
    if meta.get("index_version") != HYPEREDGE_INDEX_VERSION:
        raise RuntimeError("索引不是 DatasetUse 超边版本，请使用 --build-index 重建")
    if meta.get("wiki_fingerprint") != store.fingerprint():
        raise RuntimeError("索引与当前 newLLMWiki 不一致，请使用 --build-index 重建")
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
# 3.1 Group-aware retrieval: one RRF vote per Task in each query channel
# ---------------------------------------------------------------------------

def retrieval_group_id(document: base.SearchDocument) -> str:
    """Map Task-bearing documents to one group; keep Dataset nodes separate."""

    if document.task_id:
        return f"task:{document.task_id}"
    return f"dataset:{document.dataset_id or document.doc_id}"


def grouped_rrf_results(
    documents: list[base.SearchDocument],
    channel_rankings: list[tuple[str, list[int], np.ndarray]],
    rrf_k: int,
) -> list[dict[str, Any]]:
    """Collapse each channel by Task before adding its RRF contributions.

    Every original member hit is retained under ``members`` for auditable
    DatasetUse discovery. Only the first occurrence of a Task in one channel
    contributes a reciprocal-rank vote, so a Task with 28 edges cannot receive
    28 votes from that channel.
    """

    fused: dict[str, float] = defaultdict(float)
    group_channels: dict[str, list[dict[str, Any]]] = defaultdict(list)
    group_members: dict[str, dict[int, dict[str, Any]]] = defaultdict(dict)

    for channel, ranking, scores in channel_rankings:
        seen_groups: set[str] = set()
        group_rank = 0
        for original_rank, document_index in enumerate(ranking, start=1):
            document = documents[document_index]
            group_id = retrieval_group_id(document)
            member = group_members[group_id].setdefault(document_index, {
                "doc_index": document_index,
                "doc_id": document.doc_id,
                "node_type": document.node_type,
                "task_id": document.task_id,
                "dataset_id": document.dataset_id,
                "best_original_rank": original_rank,
                "channels": [],
            })
            member["best_original_rank"] = min(
                member["best_original_rank"], original_rank
            )
            member["channels"].append({
                "channel": channel,
                "original_rank": original_rank,
                "score": float(scores[document_index]),
            })

            if group_id in seen_groups:
                continue
            seen_groups.add(group_id)
            group_rank += 1
            contribution = 1.0 / (rrf_k + group_rank)
            fused[group_id] += contribution
            group_channels[group_id].append({
                "channel": channel,
                "rank": group_rank,
                "best_document_rank": original_rank,
                "rrf": contribution,
            })

    ordered_groups = sorted(
        fused,
        key=lambda group_id: (fused[group_id], group_id),
        reverse=True,
    )
    maximum = max(fused.values(), default=1.0)
    results: list[dict[str, Any]] = []
    for group_id in ordered_groups:
        members = sorted(
            group_members[group_id].values(),
            key=lambda row: (row["best_original_rank"], row["doc_id"]),
        )
        representative = members[0]
        results.append({
            "group_id": group_id,
            "doc_index": representative["doc_index"],
            "doc_id": representative["doc_id"],
            "node_type": (
                "TaskGroup" if group_id.startswith("task:")
                else representative["node_type"]
            ),
            "task_id": representative.get("task_id"),
            "rrf_score": fused[group_id],
            "normalized_retrieval_score": fused[group_id] / maximum,
            "channels": group_channels[group_id],
            "members": members,
            "member_count": len(members),
            "origin": "grouped_retrieval",
        })
    return results


def group_aware_hybrid_retrieve(
    client: OpenAI,
    embedding_model: str,
    documents: list[base.SearchDocument],
    embeddings: np.ndarray,
    bm25: base.BM25Index,
    plan: base.QueryPlan,
    dense_top_k: int,
    bm25_top_k: int,
    rrf_k: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Run Dense/BM25 retrieval and fuse unique Task/Dataset groups."""

    query_vectors = base.embed_texts(
        client, embedding_model, plan.dense_queries, batch_size=16
    )
    channels: list[tuple[str, list[int], np.ndarray]] = []
    raw_rankings: list[dict[str, Any]] = []

    for query, vector in zip(plan.dense_queries, query_vectors):
        scores = embeddings @ vector
        ranking = base.ranked_indices(scores, dense_top_k)
        channel = f"dense:{query}"
        channels.append((channel, ranking, scores))
        raw_rankings.append({
            "channel": channel,
            "results": [
                {"doc_id": documents[index].doc_id, "score": float(scores[index])}
                for index in ranking
            ],
        })

    for query in plan.bm25_queries:
        scores = bm25.scores(query)
        ranking = base.ranked_indices(
            scores, bm25_top_k, require_positive=True
        )
        channel = f"bm25:{query}"
        channels.append((channel, ranking, scores))
        raw_rankings.append({
            "channel": channel,
            "results": [
                {"doc_id": documents[index].doc_id, "score": float(scores[index])}
                for index in ranking
            ],
        })

    return grouped_rrf_results(documents, channels, rrf_k), raw_rankings


# ---------------------------------------------------------------------------
# 4. 超边发现：直接 DatasetUse + 命中节点的一次关联，不递归遍历
# ---------------------------------------------------------------------------

def _hit_summary(result: dict[str, Any]) -> dict[str, Any]:
    """保存RRF及各Dense/BM25通道证据，不把已命中的直接证据清零。"""

    return {
        "doc_id": result["doc_id"],
        "node_type": result["node_type"],
        "rrf_score": float(result["rrf_score"]),
        "normalized_retrieval_score": float(result["normalized_retrieval_score"]),
        "channels": result.get("channels", []),
        "group_id": result.get("group_id"),
        "group_channels": result.get("group_channels", []),
    }


def grouped_member_result(
    group_result: dict[str, Any],
    member: dict[str, Any],
) -> dict[str, Any]:
    """Project one grouped RRF result back to an original member hit."""

    return {
        "doc_id": member["doc_id"],
        "node_type": member["node_type"],
        "rrf_score": group_result["rrf_score"],
        "normalized_retrieval_score": group_result["normalized_retrieval_score"],
        "channels": member.get("channels", []),
        "group_id": group_result.get("group_id"),
        "group_channels": group_result.get("channels", []),
    }


def discover_dataset_use_hyperedges(
    store: base.WikiStore,
    documents: list[base.SearchDocument],
    fused_results: list[dict[str, Any]],
    node_seed_top_k: int,
) -> tuple[dict[str, HyperedgeDiscovery], list[dict[str, Any]]]:
    """
    从直接 DatasetUse 命中和Top超节点获取DatasetUse。

    - 所有进入RRF结果的直接DatasetUse均保留；
    - Task/Stage/Dataset分别通过现有反向索引获取一次关联用途；
    - 不从DatasetUse继续经过Paper、Stage或Dataset传播到其他用途；
    - 同一DatasetUse通过多条路径发现时只保留一份，并记录全部来源。
    """

    document_by_id = {document.doc_id: document for document in documents}
    discovered: dict[str, HyperedgeDiscovery] = {}
    trace: list[dict[str, Any]] = []

    def ensure(use_id: str) -> HyperedgeDiscovery:
        return discovered.setdefault(
            use_id,
            HyperedgeDiscovery(dataset_use_id=use_id),
        )

    # 直接 DatasetUse 召回不受 node_seed_top_k 截断。
    for result in fused_results:
        for member in result.get("members", []):
            if member["node_type"] != "DatasetUse":
                continue
            document = document_by_id.get(member["doc_id"])
            if document is None or not document.dataset_use_id:
                continue
            item = ensure(document.dataset_use_id)
            hit = _hit_summary(grouped_member_result(result, member))
            item.direct_hits.append(hit)
            item.best_discovery_score = max(
                item.best_discovery_score,
                hit["normalized_retrieval_score"],
            )
            trace.append({
                "dataset_use_id": document.dataset_use_id,
                "discovery_type": "direct_dataset_use_group_member",
                **hit,
            })

    # RRF只决定哪些实体节点获得一次超边关联资格；不是递归图扩展。
    node_results = [
        result for result in fused_results
        if any(
            member["node_type"] in {"Task", "Stage", "Dataset"}
            for member in result.get("members", [])
        )
    ][:node_seed_top_k]
    for result in node_results:
        for member in result.get("members", []):
            if member["node_type"] not in {"Task", "Stage", "Dataset"}:
                continue
            document = document_by_id.get(member["doc_id"])
            if document is None:
                continue
            uses = base.document_dataset_uses(store, document)
            hit = _hit_summary(grouped_member_result(result, member))
            for use in uses:
                item = ensure(use["dataset_use_id"])
                anchor = {
                    **hit,
                    "anchor_id": document.doc_id,
                    "anchor_type": document.node_type,
                }
                item.anchor_hits.append(anchor)
                item.best_discovery_score = max(
                    item.best_discovery_score,
                    hit["normalized_retrieval_score"],
                )
                trace.append({
                    "dataset_use_id": use["dataset_use_id"],
                    "discovery_type": "incident_hyperedge_group_member",
                    **anchor,
                })

    return discovered, trace


def discovery_sort_key(item: HyperedgeDiscovery) -> tuple[Any, ...]:
    """Order evidence without adding task/property/material manual weights."""

    best_direct = max(
        (
            hit["normalized_retrieval_score"]
            for hit in item.direct_hits
        ),
        default=0.0,
    )
    return (
        bool(item.direct_hits),
        best_direct,
        item.best_discovery_score,
        item.dataset_use_id,
    )


def select_rerank_pool(
    store: base.WikiStore,
    discovered: dict[str, HyperedgeDiscovery],
    max_uses: int,
    max_uses_per_task: int = DEFAULT_MAX_RERANK_USES_PER_TASK,
    max_uses_per_dataset: int = DEFAULT_MAX_RERANK_USES_PER_DATASET,
) -> tuple[list[HyperedgeDiscovery], list[str], dict[str, Any]]:
    """
    控制一次rerank请求的Token规模。

    直接召回的DatasetUse优先保留，其余按最强超节点入口排序。该步骤只用于
    候选池控制，不手工计算DatasetUse任务相关性。
    """

    # Build one ranked queue per Task. Selection then proceeds round-robin, so
    # one Task cannot consume the pool merely because it has many incident uses.
    queues: dict[str, list[HyperedgeDiscovery]] = defaultdict(list)
    for item in discovered.values():
        use = store.use_by_id[item.dataset_use_id]
        queues[use["task_id"]].append(item)
    for queue in queues.values():
        queue.sort(key=discovery_sort_key, reverse=True)

    task_order = sorted(
        queues,
        key=lambda task_id: (discovery_sort_key(queues[task_id][0]), task_id),
        reverse=True,
    )
    pool_limit = max(1, max_uses)
    task_limit = max(1, max_uses_per_task)
    dataset_limit = max(1, max_uses_per_dataset)
    selected: list[HyperedgeDiscovery] = []
    selected_ids: set[str] = set()
    task_counts: dict[str, int] = defaultdict(int)
    dataset_counts: dict[str, int] = defaultdict(int)
    task_roles: dict[str, set[str]] = defaultdict(set)

    def take_one(task_id: str, require_new_dataset: bool) -> bool:
        if task_counts[task_id] >= task_limit:
            return False
        eligible: list[tuple[tuple[Any, ...], int, HyperedgeDiscovery]] = []
        for index, item in enumerate(queues[task_id]):
            if item.dataset_use_id in selected_ids:
                continue
            use = store.use_by_id[item.dataset_use_id]
            dataset_id = use["dataset_id"]
            if dataset_counts[dataset_id] >= dataset_limit:
                continue
            if require_new_dataset and dataset_counts[dataset_id] > 0:
                continue
            role_is_new = use.get("usage_role") not in task_roles[task_id]
            key = (role_is_new, *discovery_sort_key(item))
            eligible.append((key, index, item))
        if not eligible:
            return False
        _, _, chosen = max(eligible, key=lambda row: row[0])
        use = store.use_by_id[chosen.dataset_use_id]
        selected.append(chosen)
        selected_ids.add(chosen.dataset_use_id)
        task_counts[task_id] += 1
        dataset_counts[use["dataset_id"]] += 1
        if use.get("usage_role"):
            task_roles[task_id].add(use["usage_role"])
        return True

    # Pass 1 maximizes distinct Dataset coverage. Pass 2 allows a second use of
    # an already represented Dataset, still respecting Task/Dataset caps.
    for require_new_dataset in (True, False):
        while len(selected) < pool_limit:
            progress = False
            for task_id in task_order:
                if len(selected) >= pool_limit:
                    break
                progress = take_one(task_id, require_new_dataset) or progress
            if not progress:
                break

    dropped_items = sorted(
        (
            item for item in discovered.values()
            if item.dataset_use_id not in selected_ids
        ),
        key=discovery_sort_key,
        reverse=True,
    )
    diagnostics = {
        "strategy": "task_round_robin_dataset_diversity",
        "max_uses": pool_limit,
        "max_uses_per_task": task_limit,
        "max_uses_per_dataset": dataset_limit,
        "selected_task_counts": dict(sorted(task_counts.items())),
        "selected_dataset_counts": dict(sorted(dataset_counts.items())),
        "unique_tasks": len(task_counts),
        "unique_datasets": len(dataset_counts),
    }
    return selected, [item.dataset_use_id for item in dropped_items], diagnostics


# ---------------------------------------------------------------------------
# 5. 专用 Rerank API：一次请求比较全部候选，避免跨批相对分数混用
# ---------------------------------------------------------------------------

def derive_rerank_url(chat_base_url: str, explicit_url: str | None) -> str:
    """从聊天端点推导rerank端点；显式QWEN_RERANK_URL优先。"""

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


def rerank_dataset_use_hyperedges(
    *,
    store: base.WikiStore,
    question: str,
    plan: base.QueryPlan,
    pool: list[HyperedgeDiscovery],
    api_key: str,
    rerank_url: str,
    rerank_model: str,
    rerank_instruct: str,
    max_document_chars: int,
    timeout: float,
) -> tuple[list[HyperedgeDiscovery], dict[str, Any]]:
    """将QueryPlan与去重后的完整DatasetUse超边提交给专用rerank模型。"""

    query = serialize_query_for_rerank(question, plan)
    documents = [
        serialize_dataset_use_hyperedge(
            store,
            store.use_by_id[item.dataset_use_id],
            max_document_chars,
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
        key=lambda item: (item.rerank_score, item.best_discovery_score),
        reverse=True,
    )
    for position, item in enumerate(ranked, start=1):
        item.rerank_position = position
    return ranked, raw


# ---------------------------------------------------------------------------
# 6. Dataset聚合：只由Top相关DatasetUse决定，避免历史用途数量偏置
# ---------------------------------------------------------------------------

def _derivation_note(
    dataset: dict[str, Any],
    target_dataset_id: str,
    use: dict[str, Any],
) -> dict[str, Any]:
    return {
        "derived_dataset_id": dataset["dataset_id"],
        "derived_dataset_name": dataset["canonical_name"],
        "source_dataset_id": target_dataset_id,
        "construction_method": use.get("construction_method"),
        "filter_conditions": use.get("filter_conditions", []),
        "paper_id": use["paper_id"],
        "dataset_use_id": use["dataset_use_id"],
    }


def aggregate_reranked_hyperedges(
    *,
    store: base.WikiStore,
    ranked_uses: list[HyperedgeDiscovery],
    supporting_uses_per_dataset: int,
) -> tuple[list[HyperedgeDatasetCandidate], list[dict[str, Any]]]:
    """
    按Dataset聚合rerank后的DatasetUse。

    DatasetScore直接取该Dataset最高DatasetUse rerank分数。其他用途只作为
    Top证据保留，不求和、不按用途数量持续加分。
    """

    grouped: dict[str, list[tuple[HyperedgeDiscovery, dict[str, Any]]]] = {}
    excluded: list[dict[str, Any]] = []
    derivations: dict[str, list[dict[str, Any]]] = {}

    for item in ranked_uses:
        use = store.use_by_id[item.dataset_use_id]
        dataset = store.dataset_by_id[use["dataset_id"]]
        target_dataset_id = dataset["dataset_id"]
        note = None
        if not dataset.get("recommendable", False):
            source_id = dataset.get("source_dataset_id")
            if source_id and source_id in store.dataset_by_id:
                target_dataset_id = source_id
                note = _derivation_note(dataset, source_id, use)
            else:
                excluded.append({
                    "dataset_id": dataset["dataset_id"],
                    "dataset_name": dataset["canonical_name"],
                    "dataset_use_id": use["dataset_use_id"],
                    "reason": "not_recommendable_and_no_public_source",
                })
                continue
        grouped.setdefault(target_dataset_id, []).append((item, use))
        if note:
            derivations.setdefault(target_dataset_id, []).append(note)

    candidates: list[HyperedgeDatasetCandidate] = []
    global _CURRENT_USE_SCORES
    _CURRENT_USE_SCORES = {}

    for dataset_id, rows in grouped.items():
        rows.sort(key=lambda pair: pair[0].rerank_score, reverse=True)
        kept = rows[:max(1, supporting_uses_per_dataset)]
        best = rows[0][0]
        candidate = HyperedgeDatasetCandidate(dataset_id=dataset_id)
        candidate.use_rerank_score = best.rerank_score
        candidate.final_score = best.rerank_score
        # discovery分数仅用于轨迹和同分参考，不与rerank分数手工加权。
        candidate.retrieval_score = max(
            item.best_discovery_score for item, _ in rows
        )
        candidate.supporting_use_scores = {
            use["dataset_use_id"]: item.rerank_score
            for item, use in kept
        }
        candidate.supporting_use_ids = set(candidate.supporting_use_scores)
        candidate.supporting_doc_ids = set(candidate.supporting_use_ids)
        for item, _ in kept:
            candidate.supporting_doc_ids.update(
                hit["doc_id"] for hit in item.direct_hits
            )
            candidate.supporting_doc_ids.update(
                hit["anchor_id"] for hit in item.anchor_hits
            )
        candidate.derivation_notes = derivations.get(dataset_id, [])
        candidate.rerank_reason = (
            f"{DEFAULT_RERANK_MODEL}最高相关DatasetUse为"
            f"{best.dataset_use_id}，score={best.rerank_score:.6f}。"
        )
        _CURRENT_USE_SCORES.update(candidate.supporting_use_scores)
        candidates.append(candidate)

    return sorted(candidates, key=lambda item: item.final_score, reverse=True), excluded


def complete_adaptive_candidate_evidence(
    *,
    store: base.WikiStore,
    candidates: list[HyperedgeDatasetCandidate],
    discovered: dict[str, HyperedgeDiscovery],
    supporting_uses_per_dataset: int,
) -> dict[str, Any]:
    "只用本轮已发现用途，补回全局池截断掉的角色/阶段互补证据。"

    rows_by_target: dict[
        str, list[tuple[HyperedgeDiscovery, dict[str, Any]]]
    ] = defaultdict(list)
    for item in discovered.values():
        use = store.use_by_id[item.dataset_use_id]
        dataset = store.dataset_by_id[use["dataset_id"]]
        target_id = dataset["dataset_id"]
        if not dataset.get("recommendable", False):
            source_id = dataset.get("source_dataset_id")
            if not source_id or source_id not in store.dataset_by_id:
                continue
            target_id = source_id
        rows_by_target[target_id].append((item, use))

    limit = max(1, supporting_uses_per_dataset)
    selected_by_dataset: dict[str, list[str]] = {}
    anchor_task_by_dataset: dict[str, str] = {}
    removed_cross_task_by_dataset: dict[str, list[str]] = {}
    for candidate in candidates:
        rows = rows_by_target.get(candidate.dataset_id, [])
        if not rows:
            continue

        # 用专用rerank分数确定该Dataset对当前query最相关的TaskGroup；未进入
        # 全局rerank池的用途才退回到发现分数。不同Task的历史能力不再混合。
        def local_score(
            pair: tuple[HyperedgeDiscovery, dict[str, Any]],
        ) -> tuple[Any, ...]:
            item, _ = pair
            return (
                item.rerank_position is not None,
                item.rerank_score
                if item.rerank_position is not None
                else item.best_discovery_score,
                discovery_sort_key(item),
            )

        _, anchor_use = max(rows, key=local_score)
        anchor_task_id = anchor_use["task_id"]
        anchor_task_by_dataset[candidate.dataset_id] = anchor_task_id
        local_rows = [
            pair for pair in rows if pair[1]["task_id"] == anchor_task_id
        ]
        removed_cross_task_by_dataset[candidate.dataset_id] = sorted(
            pair[1]["dataset_use_id"] for pair in rows
            if pair[1]["task_id"] != anchor_task_id
            and pair[1]["dataset_use_id"] in candidate.supporting_use_ids
        )

        chosen_rows: list[
            tuple[HyperedgeDiscovery, dict[str, Any]]
        ] = []
        roles: set[str] = set()
        stages: set[str] = set()
        remaining = list(local_rows)
        while remaining and len(chosen_rows) < limit:
            # 角色/阶段多样性只决定证据保留，不参与最终相关性分数。
            item, use = max(
                remaining,
                key=lambda pair: (
                    str(pair[1].get("usage_role") or "unknown") not in roles,
                    str(pair[1].get("stage_id") or "unknown") not in stages,
                    local_score(pair),
                ),
            )
            chosen_rows.append((item, use))
            roles.add(str(use.get("usage_role") or "unknown"))
            stages.add(str(use.get("stage_id") or "unknown"))
            remaining = [
                pair for pair in remaining
                if pair[1]["dataset_use_id"] != use["dataset_use_id"]
            ]

        candidate.supporting_use_ids = {
            use["dataset_use_id"] for _, use in chosen_rows
        }
        candidate.supporting_use_scores = {}
        candidate.supporting_doc_ids = set(candidate.supporting_use_ids)
        for item, use in chosen_rows:
            uid = use["dataset_use_id"]
            score = (
                item.rerank_score
                if item.rerank_position is not None
                else item.best_discovery_score
            )
            candidate.supporting_use_scores[uid] = score
            candidate.supporting_doc_ids.update(
                hit["doc_id"] for hit in item.direct_hits
            )
            candidate.supporting_doc_ids.update(
                hit["anchor_id"] for hit in item.anchor_hits
            )
            _CURRENT_USE_SCORES[uid] = score
        selected_by_dataset[candidate.dataset_id] = sorted(
            candidate.supporting_use_ids
        )
    return {
        "scope": "current_query_discovered_dataset_uses_only",
        "selection_rule": "top_query_relevant_task_then_role_stage_diversity",
        "supporting_uses_per_dataset": limit,
        "anchor_task_id_by_dataset": anchor_task_by_dataset,
        "selected_use_ids_by_dataset": selected_by_dataset,
        "removed_cross_task_use_ids_by_dataset": removed_cross_task_by_dataset,
    }


def hyperedge_candidate_context(
    store: base.WikiStore,
    candidate: base.DatasetCandidate,
) -> dict[str, Any]:
    """集合选择与答案生成只读取本轮Top DatasetUse，不补齐全部历史用途。"""

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


# ---------------------------------------------------------------------------
# 6.0 Dataset证据包重排：避免单条用途或“大库字段多”直接决定最终次序
# ---------------------------------------------------------------------------

def serialize_dataset_evidence_package(
    store: base.WikiStore,
    candidate: HyperedgeDatasetCandidate,
    max_chars: int,
) -> str:
    """把Dataset本体与本轮最相关DatasetUse组合成一次可比较的证据包。"""

    context = hyperedge_candidate_context(store, candidate)
    dataset = context["dataset"]
    lines = [
        "[CANDIDATE TYPE] Dataset evidence package",
        f"[DATASET ID] {candidate.dataset_id}",
        f"[DATASET NAME] {dataset.get('canonical_name') or candidate.dataset_id}",
        f"[DATASET TYPE] {dataset.get('dataset_type') or 'unknown'}",
        f"[MATERIAL SCOPE] {_values(dataset.get('material_scope', []), 20)}",
        f"[AVAILABLE PROPERTIES] {_values(dataset.get('available_properties', []), 40)}",
        f"[AVAILABLE FIELDS] {_values(dataset.get('available_fields', []), 40)}",
        f"[AVAILABILITY] {dataset.get('availability') or 'unknown'}",
        "",
        "[CURRENT-QUERY DATASETUSE EVIDENCE]",
    ]
    uses = context["uses"]
    per_use_limit = max(1200, max_chars // max(1, len(uses)))
    for position, use in enumerate(uses, start=1):
        lines.extend([
            f"--- Evidence {position} ---",
            serialize_dataset_use_hyperedge(
                store, use, per_use_limit
            ),
        ])
    return "\n".join(lines)[:max_chars]


def rerank_dataset_evidence_packages(
    *,
    store: base.WikiStore,
    question: str,
    plan: base.QueryPlan,
    candidates: list[HyperedgeDatasetCandidate],
    api_key: str,
    rerank_url: str,
    rerank_model: str,
    max_document_chars: int,
    timeout: float,
    candidate_top_k: int,
) -> tuple[list[HyperedgeDatasetCandidate], dict[str, Any]]:
    """统一重排Dataset证据包，分数不再取某一条DatasetUse的最大值。"""

    window = candidates[:max(1, candidate_top_k)]
    documents = [
        serialize_dataset_evidence_package(
            store, candidate, max_document_chars
        )
        for candidate in window
    ]
    scores, raw = call_text_rerank(
        api_key=api_key,
        url=rerank_url,
        model=rerank_model,
        query=serialize_query_for_rerank(question, plan),
        documents=documents,
        instruct=DATASET_PACKAGE_RERANK_INSTRUCT,
        timeout=timeout,
    )
    for candidate, score in zip(window, scores):
        candidate.dataset_package_score = score
        candidate.final_score = score
        candidate.rerank_reason = (
            f"{rerank_model} Dataset证据包重排score={score:.6f}；"
            f"单条DatasetUse最高分={candidate.use_rerank_score:.6f}。"
        )
    # 窗口外候选不伪造证据包分数；保留在末尾供“前6仍不满足”时审计。
    outside = candidates[len(window):]
    return (
        sorted(window, key=lambda item: item.final_score, reverse=True)
        + outside,
        raw,
    )


# ---------------------------------------------------------------------------
# 6.1 自适应最小充分集合：满足需求即停止，绝不为凑数补齐到六个
# ---------------------------------------------------------------------------

ADAPTIVE_MAX_RESULTS = 6


def _normalized_concept(value: Any) -> str:
    text = re.sub(r"[_\-]+", " ", str(value).casefold())
    text = re.sub(r"[^\w]+", "_", text).strip("_")
    return text


def adaptive_material_concepts(values: Iterable[str]) -> set[str]:
    """把用户与候选材料范围映射到少量稳定概念。"""

    concepts: set[str] = set()
    for value in values:
        text = re.sub(r"[_\-]+", " ", str(value).casefold())
        matched = False
        mappings = (
            ("perovsk", "perovskite"),
            ("inorganic", "inorganic"),
            ("crystal", "crystal"),
            ("crystalline", "crystal"),
            ("solid state", "solid_state"),
            ("3d material", "three_dimensional"),
            ("molecul", "molecule"),
            ("cataly", "catalyst"),
            ("polymer", "polymer"),
            ("two dimensional", "two_dimensional"),
            ("2d", "two_dimensional"),
            ("bulk", "bulk"),
        )
        for token, concept in mappings:
            if token in text:
                concepts.add(concept)
                matched = True
        if "钙钛矿" in text:
            concepts.update({"perovskite", "crystal"})
            matched = True
        if "无机" in text:
            concepts.add("inorganic")
            matched = True
        if "晶体" in text:
            concepts.add("crystal")
            matched = True
        if "分子" in text:
            concepts.add("molecule")
            matched = True
        if "催化" in text:
            concepts.add("catalyst")
            matched = True
        # organic不能用子串判断，否则inorganic会同时产生互相冲突的两个材料域。
        if re.search(r"\borganic\b", text) and "inorganic" not in text:
            concepts.add("organic")
            matched = True
        if not matched:
            fallback = _normalized_concept(value)
            if fallback:
                concepts.add(fallback)
    return concepts


def adaptive_input_concepts(values: Iterable[str]) -> set[str]:
    """规范化任务输入表示；结构的具体类型同时覆盖通用atomic_structure。"""

    concepts: set[str] = set()
    for value in values:
        text = re.sub(r"[_\-]+", " ", str(value).casefold())
        if any(token in text for token in (
            "composition", "chemical formula", "elemental fraction",
            "stoichiometr", "元素比例", "元素分数", "化学式", "组成",
        )):
            concepts.add("composition")
        if any(token in text for token in (
            "crystal structure", "cif", "poscar", "lattice vector",
            "fractional coordinate", "晶体结构", "晶格",
        )):
            concepts.update({"atomic_structure", "crystal_structure"})
        if any(token in text for token in (
            "molecular structure", "smiles", "分子结构",
        )):
            concepts.update({"atomic_structure", "molecular_structure"})
        if any(token in text for token in (
            "atomic structure", "atomic position", "atomic coordinate",
            "cartesian coordinate", "原子结构", "原子坐标",
        )):
            concepts.add("atomic_structure")
    return concepts


def _supported_adaptive_role_needs(plan: base.QueryPlan) -> set[str]:
    """只把用户文本明确支持的source/target角色作为集合硬需求。"""

    role_patterns = {
        "pretraining_source": (
            "pretrain", "pre-trained", "source dataset", "source data",
            "预训练", "源数据集",
        ),
        "fine_tuning_target": (
            "fine tun", "fine-tun", "target dataset", "small data",
            "微调", "目标数据集", "小数据",
        ),
        "evaluation_target": (
            "evaluat", "test dataset", "benchmark", "validation",
            "评估", "测试集", "基准", "验证集",
        ),
        "label_source": (
            "label", "ground truth", "标签", "标注", "真值",
        ),
        "candidate_pool": (
            "candidate", "screen", "discovery", "候选", "筛选", "发现",
        ),
    }
    result: set[str] = set()
    for need in getattr(plan, "dataset_role_needs", []):
        if not isinstance(need, dict):
            continue
        role = str(need.get("role") or "")
        support = str(need.get("support_text") or "").casefold()
        if role in role_patterns and any(token in support for token in role_patterns[role]):
            result.add(role)
    return result


def adaptive_required_atoms(plan: base.QueryPlan) -> set[tuple[str, str]]:
    """构造决定返回数量的显式需求，不使用宽泛的通用研发阶段。"""

    atoms: set[tuple[str, str]] = {
        ("material", value)
        for value in adaptive_material_concepts(plan.material_scope)
    }
    generic_properties = {
        "multiple_properties", "properties", "material_properties",
        "property_prediction", "materials_property_prediction",
    }
    for value in plan.target_properties:
        if base.is_evaluation_metric(value):
            continue
        for concept in hyperedge_property_concepts([value]):
            if concept in generic_properties:
                continue
            if concept.startswith("multiple_") and concept.endswith("_properties"):
                continue
            atoms.add(("property", concept))
    atoms.update(
        ("input", value)
        for value in adaptive_input_concepts(
            getattr(plan, "input_representations", [])
        )
    )
    required_roles = _supported_adaptive_role_needs(plan)
    atoms.update(("role", value) for value in required_roles)
    # 迁移学习的预训练源和微调目标在语义上是两个数据位置。即使某个公共库
    # 历史上承担过两种角色，也不能让同一个Dataset同时占据本次source/target。
    if {"pretraining_source", "fine_tuning_target"} <= required_roles:
        atoms.add((
            "role_relation",
            "distinct_pretraining_source_and_fine_tuning_target",
        ))

    objective = plan.objective.casefold()
    constraints = " ".join(plan.constraints).casefold()
    if "experimental" in objective or "实验" in objective:
        atoms.add(("data_kind", "experimental"))
    if any(token in objective or token in constraints for token in (
        "public", "open access", "公开",
    )):
        atoms.add(("availability", "public"))
    return atoms


def adaptive_candidate_atoms(
    store: base.WikiStore,
    candidate: base.DatasetCandidate,
) -> set[tuple[str, str]]:
    """从Dataset本体和本轮Top DatasetUse证据计算候选覆盖。"""

    context = hyperedge_candidate_context(store, candidate)
    dataset = context["dataset"]
    uses = context["uses"]
    tasks = context["tasks"]
    atoms: set[tuple[str, str]] = set()

    material_values = [
        *dataset.get("material_scope", []),
        *[value for task in tasks for value in task.get("material_scope", [])],
    ]
    atoms.update(
        ("material", value)
        for value in adaptive_material_concepts(material_values)
    )

    property_values = [
        *dataset.get("available_properties", []),
        *dataset.get("available_fields", []),
        *[value for use in uses for value in use.get("used_fields", [])],
        *[value for task in tasks for value in task.get("target_properties", [])],
    ]
    atoms.update(
        ("property", value)
        for value in hyperedge_property_concepts(property_values)
    )

    input_values = [
        *dataset.get("available_fields", []),
        *dataset.get("material_scope", []),
        *[value for use in uses for value in use.get("used_fields", [])],
        *[str(use.get("construction_method") or "") for use in uses],
    ]
    atoms.update(
        ("input", value)
        for value in adaptive_input_concepts(input_values)
    )

    # 角色只能由本轮保留的相关DatasetUse证明，不能由全部历史用途补齐。
    for use in uses:
        role = str(use.get("usage_role") or "").casefold()
        task = store.task_by_id.get(use.get("task_id"), {})
        text = " ".join([
            str(use.get("purpose") or ""),
            str(use.get("construction_method") or ""),
            str(task.get("objective") or ""),
            *[str(value) for value in task.get("constraints", [])],
        ]).casefold()
        if role == "pretraining" or "pretrain" in text or "预训练" in text:
            atoms.add(("role", "pretraining_source"))
        if role == "source" and any(token in text for token in (
            "source dataset", "transfer learning", "pretrain", "源数据集", "迁移学习",
        )):
            atoms.add(("role", "pretraining_source"))
        if role == "training" and any(token in text for token in (
            "fine tun", "fine-tun", "target dataset", "transfer learning",
            "微调", "目标数据集", "迁移学习",
        )):
            atoms.add(("role", "fine_tuning_target"))
        if role in {"test", "validation", "benchmark"}:
            atoms.add(("role", "evaluation_target"))
        if role == "label_source":
            atoms.add(("role", "label_source"))
        if role in {"candidate_pool", "screening"}:
            atoms.add(("role", "candidate_pool"))

    searchable_text = " ".join([
        str(dataset.get("canonical_name") or ""),
        *[str(value) for value in dataset.get("raw_names", [])],
        str(dataset.get("dataset_type") or ""),
        *[str(value) for value in property_values],
        *[str(use.get("purpose") or "") for use in uses],
    ]).casefold()
    if "experimental" in searchable_text or "实验" in searchable_text:
        atoms.add(("data_kind", "experimental"))
    if dataset.get("availability") == "public":
        atoms.add(("availability", "public"))
    return atoms


def _serialized_atoms(atoms: set[tuple[str, str]]) -> list[dict[str, str]]:
    return [
        {"kind": kind, "value": value}
        for kind, value in sorted(atoms)
    ]


def _combination_redundancy(
    combination: tuple[base.DatasetCandidate, ...],
    coverage_by_id: dict[str, set[tuple[str, str]]],
) -> int:
    """同规模同分时，优先需求覆盖重叠更少的组合。"""

    overlap_count = 0
    for left, right in combinations(combination, 2):
        overlap_count += len(
            coverage_by_id[left.dataset_id]
            & coverage_by_id[right.dataset_id]
        )
    return overlap_count


def _combination_covered_atoms(
    combination: Iterable[base.DatasetCandidate],
    coverage_by_id: dict[str, set[tuple[str, str]]],
) -> set[tuple[str, str]]:
    """合并候选覆盖，并处理必须由不同Dataset承担的source/target关系。"""

    items = list(combination)
    covered: set[tuple[str, str]] = set()
    for candidate in items:
        covered.update(coverage_by_id[candidate.dataset_id])

    source_ids = {
        item.dataset_id for item in items
        if ("role", "pretraining_source") in coverage_by_id[item.dataset_id]
    }
    target_ids = {
        item.dataset_id for item in items
        if ("role", "fine_tuning_target") in coverage_by_id[item.dataset_id]
    }
    if any(source_id != target_id for source_id in source_ids for target_id in target_ids):
        covered.add((
            "role_relation",
            "distinct_pretraining_source_and_fine_tuning_target",
        ))
    return covered


def select_flat_adaptive_dataset_set(
    store: base.WikiStore,
    plan: base.QueryPlan,
    ranked: list[HyperedgeDatasetCandidate],
    max_results: int = ADAPTIVE_MAX_RESULTS,
    candidate_pool_size: int = 30,
) -> tuple[list[HyperedgeDatasetCandidate], dict[str, Any]]:
    """旧版平面字段覆盖基线；保留用于消融实验，不再作为默认选择器。"""

    limit = min(ADAPTIVE_MAX_RESULTS, max(0, max_results))
    required = adaptive_required_atoms(plan)
    pool = ranked[:max(1, candidate_pool_size)]
    excluded: list[dict[str, str]] = []
    eligible: list[HyperedgeDatasetCandidate] = []
    for candidate in pool:
        dataset = store.dataset_by_id[candidate.dataset_id]
        if not dataset.get("recommendable", False):
            excluded.append({
                "dataset_id": candidate.dataset_id,
                "reason": "not_recommendable",
            })
            continue
        if ("availability", "public") in required and dataset.get("availability") != "public":
            excluded.append({
                "dataset_id": candidate.dataset_id,
                "reason": "public_dataset_required",
            })
            continue
        eligible.append(candidate)

    coverage_by_id = {
        candidate.dataset_id: adaptive_candidate_atoms(store, candidate) & required
        for candidate in eligible
    }
    base_diagnostics: dict[str, Any] = {
        "mode": "adaptive",
        "max_results": limit,
        "candidate_pool_size": candidate_pool_size,
        "required_atoms": _serialized_atoms(required),
        "eligible_dataset_ids": [item.dataset_id for item in eligible],
        "excluded_candidates": excluded,
        "coverage_by_dataset": {
            dataset_id: _serialized_atoms(atoms)
            for dataset_id, atoms in coverage_by_id.items()
        },
    }
    if limit <= 0 or not eligible:
        return [], {
            **base_diagnostics,
            "selection_complete": False,
            "selection_reason": "no_eligible_candidate",
            "selected_size": 0,
            "covered_atoms": [],
            "uncovered_atoms": _serialized_atoms(required),
            "new_coverage_by_dataset": {},
        }

    # 查询没有抽出可验证的显式需求时，最高分一个数据集就是最小合理答案。
    if not required:
        selected = eligible[:1]
        return selected, {
            **base_diagnostics,
            "selection_complete": True,
            "selection_reason": "no_explicit_requirement_return_top1",
            "selected_size": 1,
            "covered_atoms": [],
            "uncovered_atoms": [],
            "new_coverage_by_dataset": {selected[0].dataset_id: []},
        }

    # 零覆盖候选不可能帮助完成任务，不允许它们为了填满六个进入结果。
    useful = [
        candidate for candidate in eligible
        if coverage_by_id[candidate.dataset_id]
    ]
    if not useful:
        selected = eligible[:1]
        return selected, {
            **base_diagnostics,
            "selection_complete": False,
            "selection_reason": "no_candidate_adds_required_coverage",
            "selected_size": 1,
            "covered_atoms": [],
            "uncovered_atoms": _serialized_atoms(required),
            "new_coverage_by_dataset": {selected[0].dataset_id: []},
        }

    best_partial: tuple[HyperedgeDatasetCandidate, ...] | None = None
    best_partial_key: tuple[int, int, float, int] | None = None
    complete_choice: tuple[HyperedgeDatasetCandidate, ...] | None = None

    # 从1开始枚举，第一次找到完整覆盖即保证集合数量最少。
    for size in range(1, min(limit, len(useful)) + 1):
        best_complete_at_size: tuple[HyperedgeDatasetCandidate, ...] | None = None
        best_complete_key: tuple[float, int, int] | None = None
        for combination in combinations(useful, size):
            families = [
                base.dataset_family_id(store, item.dataset_id)
                for item in combination
            ]
            if len(families) != len(set(families)):
                continue

            covered = _combination_covered_atoms(combination, coverage_by_id)
            score_sum = sum(item.final_score for item in combination)
            redundancy = _combination_redundancy(combination, coverage_by_id)

            # 无完整解时：覆盖最多优先，其次集合更小、平均相关性更高、重复更少。
            partial_key = (
                len(covered),
                -size,
                score_sum / size,
                -redundancy,
            )
            if best_partial_key is None or partial_key > best_partial_key:
                best_partial_key = partial_key
                best_partial = combination

            if required <= covered:
                complete_key = (
                    score_sum / size,
                    -redundancy,
                    sum(len(item.supporting_use_ids) for item in combination),
                )
                if best_complete_key is None or complete_key > best_complete_key:
                    best_complete_key = complete_key
                    best_complete_at_size = combination
        if best_complete_at_size is not None:
            complete_choice = best_complete_at_size
            break

    chosen = complete_choice or best_partial or (useful[0],)
    # 答案仍按相关性从高到低展示；最小性由上面的组合搜索保证。
    selected = sorted(chosen, key=lambda item: item.final_score, reverse=True)
    covered: set[tuple[str, str]] = set()
    new_coverage: dict[str, list[dict[str, str]]] = {}
    selected_so_far: list[HyperedgeDatasetCandidate] = []
    for candidate in selected:
        selected_so_far.append(candidate)
        next_covered = _combination_covered_atoms(
            selected_so_far,
            coverage_by_id,
        )
        added = next_covered - covered
        new_coverage[candidate.dataset_id] = _serialized_atoms(added)
        covered = next_covered
    complete = required <= covered
    reason = (
        f"complete_coverage_with_{len(selected)}_datasets"
        if complete
        else f"best_partial_coverage_with_{len(selected)}_datasets"
    )
    return selected, {
        **base_diagnostics,
        "selection_complete": complete,
        "selection_reason": reason,
        "selected_size": len(selected),
        "covered_atoms": _serialized_atoms(covered),
        "uncovered_atoms": _serialized_atoms(required - covered),
        "new_coverage_by_dataset": new_coverage,
    }


# ---------------------------------------------------------------------------
# 6.2 MaterialDataNeed + 本轮RAG证据覆盖
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class MaterialDataNeed:
    """一个必须被数据集集合满足的、带语境的数据需求槽位。

    性质不能脱离材料域和数据角色单独计数。例如“预训练源的形成能”和
    “小目标集的带隙”属于两个不同槽位，不能被某个数据集的历史能力混合覆盖。
    """

    need_id: str
    role: str
    material_concepts: tuple[str, ...]
    property_concepts: tuple[str, ...]
    input_alternatives: tuple[tuple[str, ...], ...]
    availability: str | None
    data_kind: str | None
    scale: str
    property_relation: str
    support_text: str


def _explicit_property_concepts(plan: base.QueryPlan) -> set[str]:
    """只保留用户目标性质；指标名和“多性质”这类占位词不能决定集合大小。"""

    generic = {
        "multiple_properties", "properties", "material_properties",
        "property_prediction", "materials_property_prediction",
    }
    result: set[str] = set()
    for value in plan.target_properties:
        if base.is_evaluation_metric(value):
            continue
        for concept in hyperedge_property_concepts([value]):
            if concept in generic:
                continue
            if concept.startswith("multiple_") and concept.endswith("_properties"):
                continue
            result.add(concept)
    return result


def _material_data_domains(
    values: Iterable[str],
    *,
    controlled_only: bool = False,
) -> list[tuple[str, ...]]:
    """把材料范围拆成独立域，而不是把“晶体+分子”错误合并成一个AND条件。"""

    concepts = adaptive_material_concepts(values)
    if controlled_only:
        concepts &= {
            "perovskite", "molecule", "catalyst", "polymer",
            "two_dimensional", "crystal", "inorganic", "organic", "bulk",
            "solid_state", "three_dimensional",
        }
    generic = {"material", "materials", "material_systems"}
    concepts -= generic
    domains: list[tuple[str, ...]] = []

    # 高特异性域单独建槽；perovskite已经隐含crystal，不再重复建crystal槽。
    for concept in (
        "perovskite", "molecule", "catalyst", "polymer", "two_dimensional",
        "solid_state", "three_dimensional",
    ):
        if concept in concepts:
            domains.append((concept,))

    if "crystal" in concepts and "perovskite" not in concepts:
        qualifiers = tuple(
            value for value in ("inorganic", "organic", "bulk")
            if value in concepts
        )
        domains.append((*qualifiers, "crystal"))
    else:
        consumed: set[str] = set()
        if "bulk" in concepts and "inorganic" in concepts:
            domains.append(("inorganic", "bulk"))
            consumed.update({"inorganic", "bulk"})
        elif "bulk" in concepts and "organic" in concepts:
            domains.append(("organic", "bulk"))
            consumed.update({"organic", "bulk"})
        for concept in ("inorganic", "organic", "bulk"):
            if concept in consumed:
                continue
            if concept in concepts and not (
                concept == "bulk" and "crystal" in concepts
            ):
                domains.append((concept,))

    known = {
        "perovskite", "molecule", "catalyst", "polymer", "two_dimensional",
        "crystal", "inorganic", "organic", "bulk", "solid_state",
        "three_dimensional",
    }
    domains.extend((value,) for value in sorted(concepts - known))

    unique: list[tuple[str, ...]] = []
    for domain in domains:
        if domain and domain not in unique:
            unique.append(domain)
    return unique


def _input_alternative_groups(
    values: Iterable[str],
    material_domain: tuple[str, ...],
) -> tuple[tuple[str, ...], ...]:
    """每组是OR、组间是AND：CIF可由crystal_structure或atomic_structure证明。"""

    concepts = adaptive_input_concepts(values)
    groups: list[tuple[str, ...]] = []
    if "composition" in concepts:
        groups.append(("composition",))
    structure_requested = bool(concepts & {
        "atomic_structure", "crystal_structure", "molecular_structure",
    })
    if structure_requested and "molecule" in material_domain:
        groups.append(("molecular_structure", "atomic_structure"))
    elif structure_requested and any(x in material_domain for x in (
        "crystal", "perovskite", "inorganic", "two_dimensional", "bulk",
        "solid_state", "three_dimensional",
    )):
        groups.append(("crystal_structure", "atomic_structure"))
    elif "crystal_structure" in concepts:
        groups.append(("crystal_structure", "atomic_structure"))
    elif "molecular_structure" in concepts:
        groups.append(("molecular_structure", "atomic_structure"))
    elif "atomic_structure" in concepts:
        if "molecule" in material_domain:
            groups.append(("molecular_structure", "atomic_structure"))
        elif any(x in material_domain for x in (
            "crystal", "perovskite", "inorganic", "two_dimensional", "bulk",
        )):
            groups.append(("crystal_structure", "atomic_structure"))
        else:
            groups.append(("atomic_structure",))
    return tuple(groups)


def _grounded_role_need_rows(plan: base.QueryPlan) -> list[dict[str, str]]:
    """保留同时通过support_text校验和角色词面校验的数据角色需求。"""

    supported_roles = _supported_adaptive_role_needs(plan)
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for item in getattr(plan, "dataset_role_needs", []):
        if not isinstance(item, dict):
            continue
        role = str(item.get("role") or "")
        if role not in supported_roles:
            continue
        row = {
            "role": role,
            "scale": str(item.get("scale") or "unspecified"),
            "property_relation": str(
                item.get("property_relation") or "unspecified"
            ),
            "support_text": str(item.get("support_text") or ""),
        }
        key = (row["role"], row["scale"], row["property_relation"])
        if key not in seen:
            seen.add(key)
            rows.append(row)
    return rows


def build_material_data_needs(
    plan: base.QueryPlan,
) -> tuple[list[MaterialDataNeed], list[tuple[str, str]], bool]:
    """步骤一：把QueryPlan转为可验证的数据需求，而不是直接猜返回数量。"""

    # objective保留了原问题；当LLM漏抽材料/输入时只做词面可验证的确定性回退。
    domains = _material_data_domains(
        plan.material_scope or [plan.objective],
        controlled_only=not bool(plan.material_scope),
    )
    properties = _explicit_property_concepts(plan)
    role_rows = _grounded_role_need_rows(plan)
    input_values = (
        getattr(plan, "input_representations", []) or [plan.objective]
    )
    objective_text = " ".join([
        plan.objective,
        *plan.target_properties,
        *plan.constraints,
    ]).casefold()
    availability = (
        "public"
        if any(x in objective_text for x in ("public", "open access", "公开"))
        else None
    )
    # “experimental formation energy”可能只是多类目标中的一个名称，不能据此
    # 把OQMD/JARVIS等计算源全部硬过滤；只有明确的实验数据限定才设硬约束。
    data_kind = (
        "experimental"
        if any(token in objective_text for token in (
            "experimental-only", "only experimental", "must be experimental",
            "experimentally measured only", "仅实验", "只使用实验", "必须是实验",
        ))
        else None
    )

    benchmark_request = any(token in objective_text for token in (
        "standardized benchmark", "standardized, bias-mitigated evaluation",
        "fair, reproducible comparison", "benchmark suite", "标准化基准",
        "公平、可复现", "公平可复现",
    ))
    if benchmark_request:
        # Benchmark是独立数据作用，不能被“字段相同”的MP/OQMD普通数据库替代。
        role_rows = [{
            "role": "benchmark_suite",
            "scale": "unspecified",
            "property_relation": "same_as_target",
            "support_text": "explicit standardized benchmark request",
        }]

    # 未显式要求source/target时，一个普通任务数据槽即可；训练/测试可由同一数据集
    # 内部划分，不能擅自强迫用户选择两个库。
    grounded_role_rows = list(role_rows)
    if not role_rows:
        role_rows = [{
            "role": "task_dataset",
            "scale": "unspecified",
            "property_relation": "same_as_target",
            "support_text": "",
        }]
    elif properties and not any(
        row["role"] in {
            "fine_tuning_target", "evaluation_target", "label_source",
            "benchmark_suite",
        }
        for row in role_rows
    ):
        # 只有预训练源/候选池并不能完成有标签的目标预测；补一个普通任务数据槽。
        role_rows.append({
            "role": "task_dataset",
            "scale": "unspecified",
            "property_relation": "same_as_target",
            "support_text": "implicit target labels from target_properties",
        })
    domain_rows = domains or [()]

    needs: list[MaterialDataNeed] = []
    for role_row in role_rows:
        for domain in domain_rows:
            role = role_row["role"]
            relation = role_row["property_relation"]
            need_domain = () if role == "benchmark_suite" else domain
            # 跨性质迁移的源数据只需承担预训练能力，不能被目标标签硬过滤。
            support = role_row["support_text"].casefold()
            needs_properties = not (
                role == "pretraining_source"
                and (
                    relation == "different_or_unrelated"
                    or "unlabeled" in support
                    or "无标签" in support
                )
            )
            # 候选池提供待筛材料，本身不必含目标标签。
            if role == "candidate_pool":
                needs_properties = False
            if role == "benchmark_suite":
                # Benchmark套件负责标准化任务/切分/评价协议，不要求其单个页面把
                # 所有宽性质类别逐字列全。
                needs_properties = False
            number = len(needs) + 1
            domain_label = "_".join(need_domain) if need_domain else "general"
            needs.append(MaterialDataNeed(
                need_id=f"need_{number:02d}_{role}_{domain_label}",
                role=role,
                material_concepts=need_domain,
                property_concepts=(
                    tuple(sorted(properties)) if needs_properties else ()
                ),
                input_alternatives=_input_alternative_groups(
                    input_values, need_domain
                ),
                availability=availability,
                data_kind=data_kind,
                scale=role_row["scale"],
                property_relation=relation,
                support_text=role_row["support_text"],
            ))

    # 只有用户明确提出source/target工作流，才要求不同Dataset承担两个位置。
    distinct_pairs: list[tuple[str, str]] = []
    source_needs = [x for x in needs if x.role == "pretraining_source"]
    target_needs = [x for x in needs if x.role == "fine_tuning_target"]
    for source in source_needs:
        for target in target_needs:
            if (
                not source.material_concepts
                or not target.material_concepts
                or source.material_concepts == target.material_concepts
            ):
                distinct_pairs.append((source.need_id, target.need_id))

    # 无材料、性质、输入、角色、公开性或实验性信号时，不能声称Top-1已充分。
    specific = bool(
        domains or properties or adaptive_input_concepts(input_values)
        or grounded_role_rows or availability or data_kind
    )
    return needs, distinct_pairs, specific


def _role_evidence_for_use(
    store: base.WikiStore,
    use: dict[str, Any],
) -> set[str]:
    """从本轮DatasetUse自身判断它能承担的角色，不读取其他历史用途。"""

    task = store.task_by_id.get(use.get("task_id"), {})
    role = str(use.get("usage_role") or "").casefold()
    text = " ".join([
        str(use.get("purpose") or ""),
        str(use.get("construction_method") or ""),
        *[str(value) for value in use.get("filter_conditions", [])],
        str(task.get("objective") or ""),
    ]).casefold()
    roles = {"task_dataset"}
    if role == "pretraining" or any(
        token in text for token in ("pretrain", "预训练")
    ):
        roles.add("pretraining_source")
    if role == "source" and any(token in text for token in (
        "source dataset", "transfer learning", "pretrain", "源数据集", "迁移学习",
    )):
        roles.add("pretraining_source")
    if (
        role == "training"
        or "fine tun" in text
        or "fine-tun" in text
        or "target dataset" in text
        or "微调" in text
        or "目标数据集" in text
    ):
        roles.add("fine_tuning_target")
    if role in {"test", "validation", "benchmark"} or any(
        token in text for token in (
            "held-out", "external test", "evaluation dataset", "测试集", "验证集",
        )
    ):
        roles.add("evaluation_target")
    if role == "label_source":
        roles.add("label_source")
    if role in {"candidate_pool", "screening"}:
        roles.add("candidate_pool")
    return roles


def candidate_data_need_coverage(
    store: base.WikiStore,
    candidate: base.DatasetCandidate,
    needs: list[MaterialDataNeed],
) -> tuple[set[tuple[str, str]], dict[str, Any]]:
    """步骤二：仅用本轮RAG保留的Top DatasetUse和Dataset事实计算覆盖。"""

    context = hyperedge_candidate_context(store, candidate)
    dataset = context["dataset"]
    uses = context["uses"]
    tasks = context["tasks"]

    material_values = [
        *dataset.get("material_scope", []),
        *[value for task in tasks for value in task.get("material_scope", [])],
    ]
    material_concepts = adaptive_material_concepts(material_values)

    # DatasetUse字段和用途是本轮局部证据；Dataset本体字段可证明数据确实包含
    # 某标签，但不再读取这个数据集的全部历史DatasetUse来补能力。
    local_property_values = [
        *[value for use in uses for value in use.get("used_fields", [])],
        *[str(use.get("purpose") or "") for use in uses],
        *[str(use.get("construction_method") or "") for use in uses],
        *dataset.get("available_properties", []),
    ]
    property_concepts = hyperedge_property_concepts(local_property_values)
    input_values = [
        *dataset.get("available_fields", []),
        *dataset.get("material_scope", []),
        *[value for use in uses for value in use.get("used_fields", [])],
        *[str(use.get("construction_method") or "") for use in uses],
    ]
    input_concepts = adaptive_input_concepts(input_values)
    # 某些Wiki条目只在字段中写POSCAR而材料范围写“3D materials”。POSCAR是
    # 晶体结构的直接证据，因此可补充crystal概念，但不扩展其他材料类别。
    if any("poscar" in str(value).casefold() for value in input_values):
        input_concepts.update({"atomic_structure", "crystal_structure"})
        material_concepts.add("crystal")
    # 元素分数可由任何原子/晶体/分子结构中的元素计数确定，不要求Wiki必须额外
    # 写出composition列；这是确定性的可导出输入，不是历史用途能力扩张。
    if input_concepts & {
        "atomic_structure", "crystal_structure", "molecular_structure",
    }:
        input_concepts.add("composition")
    role_concepts: set[str] = set()
    for use in uses:
        role_concepts.update(_role_evidence_for_use(store, use))

    dataset_identity_text = " ".join([
        str(dataset.get("canonical_name") or ""),
        *[str(value) for value in dataset.get("raw_names", [])],
        str(dataset.get("dataset_type") or ""),
    ]).casefold()
    if "matbench" in dataset_identity_text or "benchmark suite" in dataset_identity_text:
        role_concepts.add("benchmark_suite")

    searchable_text = " ".join([
        str(dataset.get("canonical_name") or ""),
        *[str(value) for value in dataset.get("raw_names", [])],
        str(dataset.get("dataset_type") or ""),
        *[str(value) for value in local_property_values],
    ]).casefold()
    candidate_kind = (
        "experimental"
        if "experimental" in searchable_text or "实验" in searchable_text
        else None
    )
    availability = str(dataset.get("availability") or "")

    atoms: set[tuple[str, str]] = set()
    need_checks: dict[str, Any] = {}
    for need in needs:
        material_ok = (
            not need.material_concepts
            or set(need.material_concepts) <= material_concepts
        )
        input_ok = all(
            bool(set(alternatives) & input_concepts)
            for alternatives in need.input_alternatives
        )
        role_ok = need.role in role_concepts
        availability_ok = (
            need.availability is None or availability == need.availability
        )
        data_kind_ok = (
            need.data_kind is None or candidate_kind == need.data_kind
        )
        gates_ok = all((
            material_ok, input_ok, role_ok, availability_ok, data_kind_ok,
        ))
        matched_properties = (
            set(need.property_concepts) & property_concepts
            if gates_ok else set()
        )
        # 有标签需求时，至少命中一个目标性质才算该候选进入了这个需求槽。
        # 这可避免“材料范围相符但标签完全无关”的高分公共库成为最佳部分解。
        anchor_ok = gates_ok and (
            not need.property_concepts or bool(matched_properties)
        )
        if anchor_ok:
            atoms.add(("need_anchor", need.need_id))
            atoms.update(
                ("need_property", f"{need.need_id}|{value}")
                for value in matched_properties
            )
        need_checks[need.need_id] = {
            "anchor_ok": anchor_ok,
            "gates_ok": gates_ok,
            "material_ok": material_ok,
            "input_ok": input_ok,
            "role_ok": role_ok,
            "availability_ok": availability_ok,
            "data_kind_ok": data_kind_ok,
            "matched_properties": sorted(matched_properties),
            "missing_properties": sorted(
                set(need.property_concepts) - matched_properties
            ),
        }

    return atoms, {
        "supporting_use_ids": [x["dataset_use_id"] for x in uses],
        "material_concepts": sorted(material_concepts),
        "property_concepts": sorted(property_concepts),
        "input_concepts": sorted(input_concepts),
        "role_concepts": sorted(role_concepts),
        "availability": availability or None,
        "data_kind": candidate_kind,
        "need_checks": need_checks,
    }


def material_data_need_required_atoms(
    needs: list[MaterialDataNeed],
    distinct_pairs: list[tuple[str, str]],
) -> set[tuple[str, str]]:
    required: set[tuple[str, str]] = set()
    for need in needs:
        required.add(("need_anchor", need.need_id))
        required.update(
            ("need_property", f"{need.need_id}|{value}")
            for value in need.property_concepts
        )
    required.update(
        ("distinct_need", f"{left}|{right}")
        for left, right in distinct_pairs
    )
    return required


def _covered_material_data_need_atoms(
    combination: Iterable[base.DatasetCandidate],
    coverage_by_id: dict[str, set[tuple[str, str]]],
    distinct_pairs: list[tuple[str, str]],
) -> set[tuple[str, str]]:
    items = list(combination)
    covered: set[tuple[str, str]] = set()
    for candidate in items:
        covered.update(coverage_by_id[candidate.dataset_id])
    for left_need, right_need in distinct_pairs:
        left_ids = {
            item.dataset_id for item in items
            if ("need_anchor", left_need) in coverage_by_id[item.dataset_id]
        }
        right_ids = {
            item.dataset_id for item in items
            if ("need_anchor", right_need) in coverage_by_id[item.dataset_id]
        }
        if any(left != right for left in left_ids for right in right_ids):
            covered.add(("distinct_need", f"{left_need}|{right_need}"))
    return covered


def select_material_field_set_legacy(
    store: base.WikiStore,
    plan: base.QueryPlan,
    ranked: list[HyperedgeDatasetCandidate],
    max_results: int = ADAPTIVE_MAX_RESULTS,
    candidate_pool_size: int = 30,
) -> tuple[list[HyperedgeDatasetCandidate], dict[str, Any]]:
    """旧字段覆盖版选择器；保留用于离线对照，不再作为adaptive默认逻辑。

    排序准则严格分层：
    1. 硬约束与需求覆盖是否完整；
    2. 完整解的数据集数量最少；
    3. 同样少时，RAG/rerank相关性更高；
    4. 再以覆盖冗余更低作为末级决胜。
    """

    # adaptive模式不允许外部参数预设返回数量。唯一固定值是用户要求的安全上限6；
    # 实际数量完全由需求是否已覆盖决定。max_results仅为兼容旧函数签名保留。
    _ = max_results
    limit = ADAPTIVE_MAX_RESULTS
    needs, distinct_pairs, has_specific_need = build_material_data_needs(plan)
    required = material_data_need_required_atoms(needs, distinct_pairs)
    pool = ranked[:max(1, candidate_pool_size)]

    excluded: list[dict[str, str]] = []
    eligible: list[HyperedgeDatasetCandidate] = []
    public_required = any(need.availability == "public" for need in needs)
    for candidate in pool:
        dataset = store.dataset_by_id[candidate.dataset_id]
        if not dataset.get("recommendable", False):
            excluded.append({
                "dataset_id": candidate.dataset_id,
                "reason": "not_recommendable",
            })
            continue
        if public_required and dataset.get("availability") != "public":
            excluded.append({
                "dataset_id": candidate.dataset_id,
                "reason": "public_dataset_required",
            })
            continue
        eligible.append(candidate)

    coverage_by_id: dict[str, set[tuple[str, str]]] = {}
    evidence_by_id: dict[str, Any] = {}
    for candidate in eligible:
        atoms, evidence = candidate_data_need_coverage(
            store, candidate, needs
        )
        coverage_by_id[candidate.dataset_id] = atoms & required
        evidence_by_id[candidate.dataset_id] = evidence

    base_diagnostics: dict[str, Any] = {
        "mode": "adaptive_material_data_need",
        "selection_steps": [
            "material_data_need_extraction",
            "rag_local_evidence_coverage",
            "minimum_dataset_set_matching",
        ],
        "max_results": limit,
        "candidate_pool_size": candidate_pool_size,
        "has_specific_data_need": has_specific_need,
        "material_data_needs": [asdict(need) for need in needs],
        "distinct_need_pairs": [
            {"left_need_id": left, "right_need_id": right}
            for left, right in distinct_pairs
        ],
        "required_atoms": _serialized_atoms(required),
        "eligible_dataset_ids": [item.dataset_id for item in eligible],
        "excluded_candidates": excluded,
        "coverage_by_dataset": {
            dataset_id: _serialized_atoms(atoms)
            for dataset_id, atoms in coverage_by_id.items()
        },
        "rag_evidence_by_dataset": evidence_by_id,
        "query_constraints": list(plan.constraints),
        "constraint_policy": (
            "public and explicit experimental-only constraints are hard gates; "
            "other free-form constraints remain RAG/rerank evidence and are "
            "reported rather than converted into unsupported Boolean fields"
        ),
        "scale_policy": (
            "scale is retained as a preference because sample counts are often "
            "missing; it does not create unsupported hard coverage"
        ),
    }
    if limit <= 0 or not eligible:
        return [], {
            **base_diagnostics,
            "selection_complete": False,
            "selection_reason": "no_eligible_candidate",
            "selected_size": 0,
            "covered_atoms": [],
            "uncovered_atoms": _serialized_atoms(required),
            "new_coverage_by_dataset": {},
        }

    # 无可判定需求时无法证明任何数量“已满足”，因此把最多6个RAG候选作为
    # 未验证备选返回；这里不存在默认3个或分数阈值。
    if not has_specific_need:
        selected = eligible[:limit]
        covered = _covered_material_data_need_atoms(
            selected, coverage_by_id, distinct_pairs
        )
        return selected, {
            **base_diagnostics,
            "selection_complete": False,
            "selection_reason": "need_not_judgeable_return_up_to_6_rag_candidates",
            "selected_size": len(selected),
            "covered_atoms": _serialized_atoms(covered),
            "uncovered_atoms": _serialized_atoms(required - covered),
            "new_coverage_by_dataset": {
                item.dataset_id: _serialized_atoms(
                    coverage_by_id[item.dataset_id]
                )
                for item in selected
            },
        }

    useful = [
        candidate for candidate in eligible
        if coverage_by_id[candidate.dataset_id]
    ]
    if not useful:
        selected = eligible[:limit]
        return selected, {
            **base_diagnostics,
            "selection_complete": False,
            "selection_reason": "no_verified_coverage_return_up_to_6_rag_candidates",
            "selected_size": len(selected),
            "covered_atoms": [],
            "uncovered_atoms": _serialized_atoms(required),
            "new_coverage_by_dataset": {
                item.dataset_id: [] for item in selected
            },
        }

    best_partial: tuple[HyperedgeDatasetCandidate, ...] | None = None
    best_partial_key: tuple[int, int, float, int] | None = None
    complete_choice: tuple[HyperedgeDatasetCandidate, ...] | None = None

    # 由1到6枚举。第一次出现完整解就是基数最小解；不会为了max_results补位。
    for size in range(1, min(limit, len(useful)) + 1):
        best_complete_at_size: tuple[HyperedgeDatasetCandidate, ...] | None = None
        best_complete_key: tuple[float, int, int] | None = None
        for combination in combinations(useful, size):
            families = [
                base.dataset_family_id(store, item.dataset_id)
                for item in combination
            ]
            if len(families) != len(set(families)):
                continue

            covered = _covered_material_data_need_atoms(
                combination, coverage_by_id, distinct_pairs
            )
            score_mean = (
                sum(item.final_score for item in combination) / size
            )
            redundancy = _combination_redundancy(
                combination, coverage_by_id
            )
            partial_key = (
                len(covered),
                -size,
                score_mean,
                -redundancy,
            )
            if best_partial_key is None or partial_key > best_partial_key:
                best_partial_key = partial_key
                best_partial = combination

            if required <= covered:
                complete_key = (
                    score_mean,
                    -redundancy,
                    sum(
                        len(item.supporting_use_ids)
                        for item in combination
                    ),
                )
                if best_complete_key is None or complete_key > best_complete_key:
                    best_complete_key = complete_key
                    best_complete_at_size = combination
        if best_complete_at_size is not None:
            complete_choice = best_complete_at_size
            break

    if complete_choice is not None:
        # 已满足：只返回基数最小的完整解，不增加任何补位数据集。
        chosen = complete_choice
    else:
        # 未满足：不存在可证明的停止点。先保留覆盖最多的部分解，再按RAG顺序
        # 补充不同家族的候选，直至候选耗尽或达到6个安全上限。
        partial_items = list(best_partial or (useful[0],))
        chosen_ids = {item.dataset_id for item in partial_items}
        chosen_families = {
            base.dataset_family_id(store, item.dataset_id)
            for item in partial_items
        }
        for candidate in eligible:
            if len(partial_items) >= limit:
                break
            family = base.dataset_family_id(store, candidate.dataset_id)
            if candidate.dataset_id in chosen_ids or family in chosen_families:
                continue
            partial_items.append(candidate)
            chosen_ids.add(candidate.dataset_id)
            chosen_families.add(family)
        chosen = tuple(partial_items)
    selected = sorted(
        chosen, key=lambda item: item.final_score, reverse=True
    )
    covered: set[tuple[str, str]] = set()
    new_coverage: dict[str, list[dict[str, str]]] = {}
    selected_so_far: list[HyperedgeDatasetCandidate] = []
    for candidate in selected:
        selected_so_far.append(candidate)
        next_covered = _covered_material_data_need_atoms(
            selected_so_far, coverage_by_id, distinct_pairs
        )
        new_coverage[candidate.dataset_id] = _serialized_atoms(
            next_covered - covered
        )
        covered = next_covered

    complete = required <= covered
    return selected, {
        **base_diagnostics,
        "selection_complete": complete,
        "selection_reason": (
            f"minimum_complete_set_with_{len(selected)}_datasets"
            if complete
            else f"incomplete_return_up_to_6_candidates_with_{len(selected)}_datasets"
        ),
        "selected_size": len(selected),
        "covered_atoms": _serialized_atoms(covered),
        "uncovered_atoms": _serialized_atoms(required - covered),
        "new_coverage_by_dataset": new_coverage,
    }


def _workflow_evidence_signature(
    store: base.WikiStore,
    candidate: HyperedgeDatasetCandidate,
    need_atoms: set[tuple[str, str]],
) -> tuple[Any, ...]:
    """定义“作用与证据完全重复”；不同任务来源不会被大公共库互相替代。"""

    context = hyperedge_candidate_context(store, candidate)
    task_ids = tuple(sorted({
        str(use.get("task_id"))
        for use in context["uses"] if use.get("task_id")
    }))
    roles: set[str] = set()
    for use in context["uses"]:
        roles.update(_role_evidence_for_use(store, use))
        raw_role = str(use.get("usage_role") or "")
        if raw_role:
            roles.add(raw_role)
    stages = tuple(sorted({
        str(stage.get("stage_type"))
        for stage in context["stages"] if stage.get("stage_type")
    }))
    dataset = context["dataset"]
    data_kind = (
        "experimental"
        if "experimental" in " ".join([
            str(dataset.get("canonical_name") or ""),
            str(dataset.get("dataset_type") or ""),
            *[str(x) for x in dataset.get("material_scope", [])],
        ]).casefold()
        else "computational_or_unspecified"
    )
    return (
        task_ids,
        tuple(sorted(roles)),
        stages,
        tuple(sorted(need_atoms)),
        data_kind,
        str(dataset.get("dataset_type") or ""),
    )


def _natural_relevance_frontier_size(
    candidates: list[HyperedgeDatasetCandidate],
    limit: int,
) -> tuple[int, list[dict[str, float]]]:
    """用同批Dataset证据包分数的最大相邻落差自动确定相关证据前沿。

    这里没有Top-3、0.43等人为数量或阈值。若分数完全相同，说明不存在可判定
    的自然边界，保留到6个安全上限。
    """

    count = min(limit, len(candidates))
    if count <= 1:
        return count, []
    inspected = candidates[:min(len(candidates), limit + 1)]
    gaps = [
        {
            "after_rank": float(index + 1),
            "left_score": float(inspected[index].final_score),
            "right_score": float(inspected[index + 1].final_score),
            "gap": float(
                inspected[index].final_score
                - inspected[index + 1].final_score
            ),
        }
        for index in range(len(inspected) - 1)
    ]
    if not gaps or all(row["gap"] == 0.0 for row in gaps):
        return count, gaps
    best = max(gaps, key=lambda row: (row["gap"], -row["after_rank"]))
    return min(count, int(best["after_rank"])), gaps


def select_adaptive_dataset_set(
    store: base.WikiStore,
    plan: base.QueryPlan,
    ranked: list[HyperedgeDatasetCandidate],
    max_results: int = ADAPTIVE_MAX_RESULTS,
    candidate_pool_size: int = 30,
) -> tuple[list[HyperedgeDatasetCandidate], dict[str, Any]]:
    """按“RAG相关前沿→作用证据去重→需求复核”选择最多6个数据集。

    与旧版的关键区别是：材料/性质覆盖只负责验证候选是否能承担某个作用，
    不能让一个字段齐全的大库替代来自不同Task、不同角色或不同数据类型的证据。
    """

    _ = max_results  # adaptive数量由证据决定；参数仅兼容旧调用。
    limit = ADAPTIVE_MAX_RESULTS
    needs, distinct_pairs, has_specific_need = build_material_data_needs(plan)
    required = material_data_need_required_atoms(needs, distinct_pairs)
    pool = ranked[:max(1, candidate_pool_size)]

    eligible: list[HyperedgeDatasetCandidate] = []
    excluded: list[dict[str, str]] = []
    public_required = any(need.availability == "public" for need in needs)
    for candidate in pool:
        dataset = store.dataset_by_id[candidate.dataset_id]
        if not dataset.get("recommendable", False):
            excluded.append({
                "dataset_id": candidate.dataset_id,
                "reason": "not_recommendable",
            })
            continue
        if public_required and dataset.get("availability") != "public":
            excluded.append({
                "dataset_id": candidate.dataset_id,
                "reason": "public_dataset_required",
            })
            continue
        eligible.append(candidate)

    coverage_by_id: dict[str, set[tuple[str, str]]] = {}
    evidence_by_id: dict[str, Any] = {}
    signature_by_id: dict[str, tuple[Any, ...]] = {}
    for candidate in eligible:
        atoms, evidence = candidate_data_need_coverage(
            store, candidate, needs
        )
        coverage = atoms & required
        coverage_by_id[candidate.dataset_id] = coverage
        evidence_by_id[candidate.dataset_id] = evidence
        signature_by_id[candidate.dataset_id] = _workflow_evidence_signature(
            store, candidate, coverage
        )

    # 先去掉真正重复项：同一数据家族，或者Task/角色/阶段/需求证据完全相同。
    nonredundant: list[HyperedgeDatasetCandidate] = []
    seen_families: set[str] = set()
    seen_signatures: set[tuple[Any, ...]] = set()
    redundant: list[dict[str, str]] = []
    for candidate in eligible:
        family = base.dataset_family_id(store, candidate.dataset_id)
        signature = signature_by_id[candidate.dataset_id]
        if family in seen_families:
            redundant.append({
                "dataset_id": candidate.dataset_id,
                "reason": "same_dataset_family_as_higher_ranked_candidate",
            })
            continue
        if signature in seen_signatures:
            redundant.append({
                "dataset_id": candidate.dataset_id,
                "reason": "same_task_role_stage_and_need_evidence",
            })
            continue
        seen_families.add(family)
        seen_signatures.add(signature)
        nonredundant.append(candidate)

    frontier_size, score_gaps = _natural_relevance_frontier_size(
        nonredundant, limit
    )
    if has_specific_need:
        # 按证据包次序扫描，但只加入能新增角色/性质/材料需求证据的候选；
        # OQMD等无关高分项不会排在Matbench前面占用结果槽。
        selected: list[HyperedgeDatasetCandidate] = []
        covered: set[tuple[str, str]] = set()
        for candidate in nonredundant:
            trial = [*selected, candidate]
            next_covered = _covered_material_data_need_atoms(
                trial, coverage_by_id, distinct_pairs
            )
            if next_covered == covered:
                continue
            selected.append(candidate)
            covered = next_covered
            if required <= covered or len(selected) >= limit:
                break

        # 6个以内仍不能满足时，补充RAG相关且不重复的备选用于人工判断；
        # 已满足时绝不补位。
        if not required <= covered:
            selected_ids = {item.dataset_id for item in selected}
            for candidate in nonredundant:
                if len(selected) >= limit:
                    break
                if candidate.dataset_id in selected_ids:
                    continue
                selected.append(candidate)
                selected_ids.add(candidate.dataset_id)
            covered = _covered_material_data_need_atoms(
                selected, coverage_by_id, distinct_pairs
            )
    else:
        selected = list(nonredundant[:frontier_size])
        covered = _covered_material_data_need_atoms(
            selected, coverage_by_id, distinct_pairs
        )

    complete = has_specific_need and required <= covered
    new_coverage: dict[str, list[dict[str, str]]] = {}
    accumulated: set[tuple[str, str]] = set()
    prefix: list[HyperedgeDatasetCandidate] = []
    for candidate in selected:
        prefix.append(candidate)
        next_covered = _covered_material_data_need_atoms(
            prefix, coverage_by_id, distinct_pairs
        )
        new_coverage[candidate.dataset_id] = _serialized_atoms(
            next_covered - accumulated
        )
        accumulated = next_covered

    reason = (
        f"workflow_evidence_satisfied_with_{len(selected)}_datasets"
        if complete
        else (
            f"workflow_evidence_incomplete_at_{len(selected)}_of_6"
            if len(selected) >= limit
            else "query_need_not_judgeable_use_natural_relevance_frontier"
        )
    )
    return selected, {
        "mode": "adaptive_workflow_evidence",
        "selection_steps": [
            "material_data_need_extraction",
            "dataset_evidence_package_rerank",
            "natural_relevance_frontier",
            "workflow_evidence_deduplication",
            "need_satisfaction_review",
        ],
        "max_results": limit,
        "external_count_parameter_used": False,
        "has_specific_data_need": has_specific_need,
        "material_data_needs": [asdict(need) for need in needs],
        "required_atoms": _serialized_atoms(required),
        "natural_frontier_size": frontier_size,
        "score_gaps": score_gaps,
        "eligible_dataset_ids": [x.dataset_id for x in eligible],
        "nonredundant_dataset_ids": [x.dataset_id for x in nonredundant],
        "excluded_candidates": excluded,
        "redundant_candidates": redundant,
        "coverage_by_dataset": {
            key: _serialized_atoms(value)
            for key, value in coverage_by_id.items()
        },
        "rag_evidence_by_dataset": evidence_by_id,
        "selection_complete": complete,
        "selection_reason": reason,
        "selected_size": len(selected),
        "covered_atoms": _serialized_atoms(covered),
        "uncovered_atoms": _serialized_atoms(required - covered),
        "new_coverage_by_dataset": new_coverage,
    }


# ---------------------------------------------------------------------------
# 7. 轨迹与单次查询编排
# ---------------------------------------------------------------------------

def hyperedge_trace(
    item: HyperedgeDiscovery,
    store: base.WikiStore,
) -> dict[str, Any]:
    use = store.use_by_id[item.dataset_use_id]
    return {
        "dataset_use_id": item.dataset_use_id,
        "dataset_id": use["dataset_id"],
        "task_id": use["task_id"],
        "stage_id": use["stage_id"],
        "paper_id": use["paper_id"],
        "usage_role": use["usage_role"],
        "direct_hits": item.direct_hits,
        "anchor_hits": item.anchor_hits,
        "best_discovery_score": item.best_discovery_score,
        "rerank_score": item.rerank_score,
        "rerank_position": item.rerank_position,
    }


def dataset_candidate_trace(candidate: HyperedgeDatasetCandidate) -> dict[str, Any]:
    return {
        "dataset_id": candidate.dataset_id,
        "dataset_use_rerank_score": candidate.use_rerank_score,
        "dataset_package_rerank_score": candidate.dataset_package_score,
        "final_score": candidate.final_score,
        "retrieval_discovery_score": candidate.retrieval_score,
        "supporting_use_scores": candidate.supporting_use_scores,
        "supporting_use_ids": sorted(candidate.supporting_use_ids),
        "supporting_doc_ids": sorted(candidate.supporting_doc_ids),
        "derivation_notes": candidate.derivation_notes,
        "rerank_reason": candidate.rerank_reason,
    }


def run_hyperedge_query(
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
    node_seed_top_k: int,
    max_rerank_uses: int,
    max_rerank_uses_per_task: int,
    max_rerank_uses_per_dataset: int,
    supporting_uses_per_dataset: int,
    candidate_top_k: int,
    max_results: int,
    minimum_score: float,
    selection_mode: str,
    max_document_chars: int,
    rerank_timeout: float,
    use_rerank: bool,
    use_answer_llm: bool,
) -> tuple[str, dict[str, Any]]:
    """执行DatasetUse单超边检索、rerank、Dataset聚合和答案生成。"""

    # Use the hyperedge-specific rewrite. It reserves independent retrieval
    # slots for workflow mechanism, input representation and source/target roles.
    plan, rewrite_raw = rewrite_hyperedge_query(client, chat_model, question)

    # B. 复用Dense/BM25/RRF，但检索文本来自干净超节点和超边序列化。
    bm25 = base.BM25Index(documents)
    fused_results, raw_rankings = group_aware_hybrid_retrieve(
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

    # C. 直接DatasetUse与命中实体节点的一次超边关联，替代两跳图扩展。
    discovered, expansion_trace = discover_dataset_use_hyperedges(
        store,
        documents,
        fused_results,
        node_seed_top_k,
    )
    # adaptive不执行每Dataset硬配额。全局池仍按Task轮询抑制重复投票；
    # 池外但本轮已发现的用途会在Dataset聚合后补作证据，旧模式保持不变。
    effective_dataset_use_limit = (
        max_rerank_uses
        if selection_mode == "adaptive"
        else max_rerank_uses_per_dataset
    )
    rerank_pool, dropped_use_ids, pool_diagnostics = select_rerank_pool(
        store,
        discovered,
        max_rerank_uses,
        max_rerank_uses_per_task,
        effective_dataset_use_limit,
    )
    pool_diagnostics["adaptive_dataset_pre_rerank_quota_disabled"] = (
        selection_mode == "adaptive"
    )

    # D. 一次专用rerank请求对全部入池DatasetUse评分，不手工融合匹配权重。
    if use_rerank:
        ranked_uses, rerank_raw = rerank_dataset_use_hyperedges(
            store=store,
            question=question,
            plan=plan,
            pool=rerank_pool,
            api_key=api_key,
            rerank_url=rerank_url,
            rerank_model=rerank_model,
            rerank_instruct=rerank_instruct,
            max_document_chars=max_document_chars,
            timeout=rerank_timeout,
        )
    else:
        # 消融模式：仅使用发现分数，便于评价专用rerank模型的真实增益。
        ranked_uses = sorted(
            rerank_pool,
            key=lambda item: item.best_discovery_score,
            reverse=True,
        )
        for position, item in enumerate(ranked_uses, start=1):
            item.rerank_score = item.best_discovery_score
            item.rerank_position = position
        rerank_raw = {"disabled": True}

    # E. 同一Dataset取最高DatasetUse分数，只保留Top用途作为本轮证据。
    candidates, excluded = aggregate_reranked_hyperedges(
        store=store,
        ranked_uses=ranked_uses,
        supporting_uses_per_dataset=supporting_uses_per_dataset,
    )

    # Top-100全局池负责粗排，不再成为不可逆的证据过滤器。只补本轮召回
    # 路径发现的角色/阶段互补用途，不读取该Dataset的全部历史用途。
    if selection_mode == "adaptive":
        evidence_completion_diagnostics = complete_adaptive_candidate_evidence(
            store=store,
            candidates=candidates,
            discovered=discovered,
            supporting_uses_per_dataset=supporting_uses_per_dataset,
        )
    else:
        evidence_completion_diagnostics = {
            "disabled": True,
            "reason": "legacy_selection_mode_keeps_original_evidence_scope",
        }

    # 运行时局部替换证据上下文；不会修改原Python文件。
    base.candidate_context = hyperedge_candidate_context

    # adaptive模式增加Dataset级证据包重排：同一请求内比较“Dataset + Top用途”，
    # 避免单条用途最高分以及大型数据库字段数量直接决定最终次序。
    dataset_package_rerank_raw: dict[str, Any]
    if selection_mode == "adaptive" and use_rerank:
        candidates, dataset_package_rerank_raw = rerank_dataset_evidence_packages(
            store=store,
            question=question,
            plan=plan,
            candidates=candidates,
            api_key=api_key,
            rerank_url=rerank_url,
            rerank_model=rerank_model,
            max_document_chars=max_document_chars,
            timeout=rerank_timeout,
            candidate_top_k=candidate_top_k,
        )
    else:
        dataset_package_rerank_raw = {
            "disabled": True,
            "reason": (
                "only_enabled_for_adaptive_with_rerank"
            ),
        }

    # F. 严格执行MaterialDataNeed -> Dataset证据包相关前沿 -> 作用证据去重；
    # 旧recommend/minimum保留为实验基线，二者逻辑不受adaptive改动影响。
    selection_diagnostics: dict[str, Any]
    if selection_mode == "adaptive":
        selected, selection_diagnostics = select_adaptive_dataset_set(
            store,
            plan,
            candidates,
            max_results=max_results,
            candidate_pool_size=candidate_top_k,
        )
    elif selection_mode == "minimum":
        # Scope the alias extension to minimum mode. Recommend mode therefore
        # keeps exactly the original selection behavior.
        original_property_concepts = base.property_concepts
        base.property_concepts = hyperedge_property_concepts
        try:
            selected = base.select_minimum_dataset_set(
                store,
                plan,
                candidates,
                max_results,
                minimum_score,
                candidate_pool_size=candidate_top_k,
            )
        finally:
            base.property_concepts = original_property_concepts
        selection_diagnostics = {
            "mode": "minimum",
            "selection_reason": "legacy_minimum_selector",
            "selected_size": len(selected),
        }
    else:
        selected = base.select_dataset_combination(
            store,
            plan,
            candidates,
            max_results,
            minimum_score,
        )
        selection_diagnostics = {
            "mode": "recommend",
            "selection_reason": "legacy_recommend_selector",
            "selected_size": len(selected),
        }

    # G. 复用证据包和答案生成；每个Dataset只携带本轮最相关DatasetUse。
    packages = [
        base.build_evidence_package(store, plan, candidate)
        for candidate in selected
    ]
    if use_answer_llm:
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

    trace = {
        "created_at": base.utc_now(),
        "pipeline": "dataset_use_hyperedge_rerank",
        "question": question,
        "query_plan": asdict(plan),
        "selection_mode": selection_mode,
        "rewrite_raw": rewrite_raw,
        "raw_rankings": raw_rankings,
        "rrf_grouping": "one_vote_per_task_or_dataset_group_per_query",
        "rrf_group_count": len(fused_results),
        "rrf_results": fused_results[:100],
        "hyperedge_expansion": expansion_trace,
        "discovered_dataset_use_count": len(discovered),
        "rerank_pool_count": len(rerank_pool),
        "rerank_pool_diagnostics": pool_diagnostics,
        "rerank_pool_dropped_use_ids": dropped_use_ids,
        "candidate_evidence_completion": evidence_completion_diagnostics,
        "ranked_dataset_uses": [
            hyperedge_trace(item, store) for item in ranked_uses
        ],
        "rerank_model": rerank_model if use_rerank else None,
        "rerank_instruct": rerank_instruct if use_rerank else None,
        "rerank_raw": rerank_raw,
        "aggregation": (
            "dataset_score=dataset_evidence_package_rerank_score"
            if selection_mode == "adaptive" and use_rerank
            else "dataset_score=max(dataset_use_rerank_score)"
        ),
        "dataset_package_rerank_instruct": (
            DATASET_PACKAGE_RERANK_INSTRUCT
            if selection_mode == "adaptive" and use_rerank else None
        ),
        "dataset_package_rerank_raw": dataset_package_rerank_raw,
        "excluded_candidates": excluded,
        "ranked_candidates": [
            dataset_candidate_trace(candidate) for candidate in candidates
        ],
        "selected_dataset_ids": [
            candidate.dataset_id for candidate in selected
        ],
        "selection_diagnostics": selection_diagnostics,
        "online_selection_steps": [
            "material_data_need_extraction",
            "rag_retrieval_and_dataset_use_rerank",
            "dataset_evidence_package_rerank",
            "workflow_evidence_deduplication",
            "need_satisfaction_review",
        ],
        "evidence_packages": packages,
        "answer_raw": answer_raw,
        "answer_validation_errors": validation_errors,
        "final_answer": answer,
        "evidence_scope_mode": (
            "current_query_discovered_dataset_use_evidence"
            if selection_mode == "adaptive"
            else "top_reranked_dataset_use_hyperedges_only"
        ),
        "evidence_scope_description": (
            "Adaptive mode restores role/stage-complementary DatasetUse "
            "evidence only from hyperedges discovered by the current query; "
            "it never loads unrelated full history."
            if selection_mode == "adaptive"
            else "Dataset scoring, selection and answer evidence use only the "
            "highest-ranked DatasetUse hyperedges found in the current query."
        ),
    }
    return answer, trace


# ---------------------------------------------------------------------------
# 8. CLI：与原脚本参数尽量一致，增加专用rerank配置
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="DatasetUse hyperedge retrieval with a dedicated rerank model"
    )
    parser.add_argument(
        "--wiki-root",
        type=Path,
        default=script_dir / "newLLMWiki",
    )
    parser.add_argument(
        "--index-dir",
        type=Path,
        default=script_dir / "newWikiHyperedgeRerankIndex",
    )
    parser.add_argument("--build-index", action="store_true")
    parser.add_argument("--question", help="材料研发数据集问题")
    parser.add_argument(
        "--chat-model",
        default=os.getenv("QWEN_MODEL", base.DEFAULT_CHAT_MODEL),
    )
    parser.add_argument(
        "--embedding-model",
        default=os.getenv(
            "QWEN_EMBEDDING_MODEL",
            base.DEFAULT_EMBEDDING_MODEL,
        ),
    )
    parser.add_argument(
        "--rerank-model",
        default=os.getenv("QWEN_RERANK_MODEL", DEFAULT_RERANK_MODEL),
    )
    parser.add_argument(
        "--rerank-url",
        default=os.getenv("QWEN_RERANK_URL"),
        help="完整rerank API URL；未提供时从QWEN_BASE_URL推导",
    )
    parser.add_argument(
        "--rerank-instruct",
        default=DEFAULT_RERANK_INSTRUCT,
    )
    parser.add_argument("--rerank-timeout", type=float, default=240.0)
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--dense-top-k", type=int, default=30)
    parser.add_argument("--bm25-top-k", type=int, default=30)
    parser.add_argument("--rrf-k", type=int, default=60)
    parser.add_argument(
        "--node-seed-top-k",
        type=int,
        default=40,
        help="允许进行一次DatasetUse超边关联的Task/Stage/Dataset节点数",
    )
    parser.add_argument(
        "--max-rerank-uses",
        type=int,
        default=DEFAULT_MAX_RERANK_USES,
        help="一次rerank请求最多比较的DatasetUse数量",
    )
    parser.add_argument(
        "--max-rerank-uses-per-task",
        type=int,
        default=DEFAULT_MAX_RERANK_USES_PER_TASK,
        help="Task diversity cap applied before DatasetUse reranking",
    )
    parser.add_argument(
        "--max-rerank-uses-per-dataset",
        type=int,
        default=DEFAULT_MAX_RERANK_USES_PER_DATASET,
        help="Dataset diversity cap applied before DatasetUse reranking",
    )
    parser.add_argument(
        "--supporting-uses-per-dataset",
        type=int,
        default=DEFAULT_SUPPORTING_USES_PER_DATASET,
    )
    parser.add_argument(
        "--max-document-chars",
        type=int,
        default=DEFAULT_RERANK_DOCUMENT_CHARS,
    )
    parser.add_argument("--candidate-top-k", type=int, default=30)
    parser.add_argument(
        "--max-results",
        type=int,
        default=6,
        help=(
            "仅供旧recommend/minimum模式使用；adaptive模式由需求满足状态"
            "自行决定数量，固定安全上限为6"
        ),
    )
    parser.add_argument(
        "--minimum-score",
        type=float,
        default=0.25,
        help="旧recommend/minimum模式阈值；adaptive模式不以该分数决定数量",
    )
    parser.add_argument(
        "--selection-mode",
        choices=("adaptive", "recommend", "minimum"),
        default="adaptive",
        help=(
            "adaptive按MaterialDataNeed、Dataset证据包重排和作用证据去重返回（最多6个）；"
            "recommend和minimum保留为旧版实验基线"
        ),
    )
    parser.add_argument(
        "--no-rerank",
        action="store_true",
        help="关闭专用rerank模型，用发现分数做消融实验",
    )
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
    index_files = [
        args.index_dir / "documents.json",
        args.index_dir / "embeddings.npy",
        args.index_dir / "index_meta.json",
    ]
    if args.build_index or not all(path.is_file() for path in index_files):
        documents, embeddings, meta = build_hyperedge_index(
            store,
            client,
            args.index_dir,
            args.embedding_model,
            args.batch_size,
            args.max_document_chars,
        )
    else:
        documents, embeddings, meta = load_hyperedge_index(
            store,
            args.index_dir,
        )
        args.embedding_model = meta["embedding_model"]

    if not args.question:
        print(json.dumps({
            "status": "hyperedge_index_ready",
            "index_dir": str(args.index_dir.resolve()),
            "documents": len(documents),
            "embedding_model": args.embedding_model,
            "rerank_model": args.rerank_model,
            "wiki_fingerprint": meta["wiki_fingerprint"],
        }, ensure_ascii=False, indent=2))
        return 0

    answer, trace = run_hyperedge_query(
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
        node_seed_top_k=args.node_seed_top_k,
        max_rerank_uses=args.max_rerank_uses,
        max_rerank_uses_per_task=args.max_rerank_uses_per_task,
        max_rerank_uses_per_dataset=args.max_rerank_uses_per_dataset,
        supporting_uses_per_dataset=args.supporting_uses_per_dataset,
        candidate_top_k=args.candidate_top_k,
        max_results=args.max_results,
        minimum_score=args.minimum_score,
        selection_mode=args.selection_mode,
        max_document_chars=args.max_document_chars,
        rerank_timeout=args.rerank_timeout,
        use_rerank=not args.no_rerank,
        use_answer_llm=not args.no_answer_llm,
    )
    trace_path = args.trace_output
    if trace_path is None:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        trace_path = (
            script_dir / "retrieval_runs" /
            f"hyperedge_rerank_{stamp}.json"
        )
    base.write_json(trace_path, trace)
    print(answer)
    print(f"\n[trace] {trace_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
