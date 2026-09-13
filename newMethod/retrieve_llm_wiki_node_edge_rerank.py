#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Node-only Retrieval -> DatasetUse Hyperedge RRF -> One-stage Rerank -> Dataset Aggregation.

Compared with the previous implementation, this version cleanly separates four layers:

1. Node retrieval:
   only Task / Stage / Dataset pages participate in Dense + BM25 retrieval.
2. Hyperedge completion:
   retrieved nodes are expanded only once to their incident DatasetUse facts.
3. Hyperedge ranking:
   each deduplicated DatasetUse receives an edge-level RRF score propagated from
   its retrieved Task / Dataset / Stage endpoints, with node-type weights and
   degree-specificity attenuation; only Top-K DatasetUse facts are sent to the
   expensive reranker.
4. Dataset ranking and recommendation:
   reranked DatasetUse facts are aggregated to Dataset scores using a decayed
   Top-M evidence score. The retrieval ranking is kept separately from the
   optional minimum-dataset recommendation layer.

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


NODE_EDGE_INDEX_VERSION = "node-only-hyperedge-rrf-3.0"
DEFAULT_RERANK_MODEL = "qwen3-rerank"
DEFAULT_RERANK_DOCUMENT_CHARS = 8_000

DEFAULT_TASK_SEED_TOP_K = 20
DEFAULT_DATASET_SEED_TOP_K = 15
DEFAULT_STAGE_SEED_TOP_K = 5
DEFAULT_EDGE_TOP_K = 30
DEFAULT_RETRIEVAL_TOP_K = 6
DEFAULT_SUPPORTING_USES_PER_DATASET = 3

DEFAULT_TASK_NODE_WEIGHT = 0.50
DEFAULT_DATASET_NODE_WEIGHT = 0.35
DEFAULT_STAGE_NODE_WEIGHT = 0.15
DEFAULT_SPECIFICITY_FLOOR = 0.10

# A Dataset score is based on its strongest few query-relevant DatasetUse facts.
# We renormalize the prefix when fewer than three facts exist.
DEFAULT_DATASET_USE_DECAY_WEIGHTS = (0.70, 0.20, 0.10)


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



@dataclass
class HyperedgeQueryPlan(base.QueryPlan):
    task_mechanisms: list[str] = field(default_factory=list)
    input_representations: list[str] = field(default_factory=list)
    dataset_role_needs: list[dict[str, str]] = field(default_factory=list)


@dataclass
class EdgeDiscovery:
    """One DatasetUse hyperedge reconstructed from retrieved endpoint nodes."""

    dataset_use_id: str
    node_hits: list[dict[str, Any]] = field(default_factory=list)
    edge_rrf_score: float = 0.0
    normalized_edge_rrf_score: float = 0.0
    rerank_score: float = 0.0
    rerank_position: int | None = None


@dataclass
class NodeEdgeDatasetCandidate(base.DatasetCandidate):
    """Dataset candidate aggregated from a few top reranked DatasetUse facts."""

    aggregated_use_score: float = 0.0
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
    channel_rankings: list[tuple[str, list[int], np.ndarray]],
    rrf_k: int,
) -> list[dict[str, Any]]:
    """Fuse ranks for individual nodes. No Task-group collapsing is needed."""

    fused: dict[int, float] = defaultdict(float)
    channels_by_index: dict[int, list[dict[str, Any]]] = defaultdict(list)

    for channel, ranking, scores in channel_rankings:
        for rank, document_index in enumerate(ranking, start=1):
            contribution = 1.0 / (rrf_k + rank)
            fused[document_index] += contribution
            channels_by_index[document_index].append({
                "channel": channel,
                "rank": rank,
                "raw_score": float(scores[document_index]),
                "rrf": contribution,
            })

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
            "normalized_rrf_score": fused[index] / maximum,
            "channels": channels_by_index[index],
        })
    return results


def node_only_hybrid_retrieve(
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
        channel = f"bm25:{query}"
        channels.append((channel, ranking, scores))
        raw_rankings.append({
            "channel": channel,
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

    return seeds, selected_by_type



# ---------------------------------------------------------------------------
# 3. Controlled one-hop expansion + Hyperedge RRF
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


def expand_nodes_to_dataset_uses(
    store: base.WikiStore,
    documents: list[base.SearchDocument],
    node_seeds: list[dict[str, Any]],
    rrf_k: int,
    task_weight: float,
    dataset_weight: float,
    stage_weight: float,
    specificity_floor: float,
) -> tuple[dict[str, EdgeDiscovery], list[dict[str, Any]]]:
    """Expand only seed nodes to incident DatasetUse edges and score each edge.

    Edge RRF is a true rank-fusion score propagated from endpoint node ranks:
      sum(type_weight * node_specificity * 1/(k + node_rank_in_channel))

    The same DatasetUse discovered from multiple endpoints is exact-deduplicated,
    while all endpoint/channel evidence is retained.
    """

    document_by_id = {document.doc_id: document for document in documents}
    type_weights = {
        "Task": max(0.0, task_weight),
        "Dataset": max(0.0, dataset_weight),
        "Stage": max(0.0, stage_weight),
    }
    total_edges = max(1, len(store.uses))
    degree_cache: dict[str, int] = {}
    discovered: dict[str, EdgeDiscovery] = {}
    expansion_trace: list[dict[str, Any]] = []

    for seed in node_seeds:
        document = document_by_id.get(seed["doc_id"])
        if document is None:
            continue
        uses = base.document_dataset_uses(store, document)
        degree = degree_cache.setdefault(document.doc_id, len(uses))
        specificity = node_specificity(
            total_edges, degree, floor=specificity_floor
        )
        type_weight = type_weights.get(document.node_type, 0.0)

        if type_weight <= 0.0 or not uses:
            continue

        # Endpoint contribution is based on channel ranks rather than raw Dense/
        # BM25 scores, preserving RRF's scale invariance.
        endpoint_rrf = sum(
            type_weight * specificity * (1.0 / (rrf_k + int(channel_hit["rank"])))
            for channel_hit in seed.get("channels", [])
        )

        node_hit = {
            "node_id": document.doc_id,
            "node_type": document.node_type,
            "node_rrf_score": float(seed["rrf_score"]),
            "node_normalized_rrf_score": float(seed["normalized_rrf_score"]),
            "node_global_rank": int(seed["rank"]),
            "degree": degree,
            "specificity": specificity,
            "type_weight": type_weight,
            "edge_rrf_contribution": endpoint_rrf,
            "channels": seed.get("channels", []),
        }

        for use in uses:
            use_id = use["dataset_use_id"]
            item = discovered.setdefault(
                use_id,
                EdgeDiscovery(dataset_use_id=use_id),
            )
            item.node_hits.append(node_hit)
            item.edge_rrf_score += endpoint_rrf
            expansion_trace.append({
                "dataset_use_id": use_id,
                "task_id": use["task_id"],
                "stage_id": use["stage_id"],
                "dataset_id": use["dataset_id"],
                **node_hit,
            })

    maximum = max(
        (item.edge_rrf_score for item in discovered.values()),
        default=1.0,
    )
    for item in discovered.values():
        item.normalized_edge_rrf_score = (
            item.edge_rrf_score / maximum if maximum > 0 else 0.0
        )

    return discovered, expansion_trace


def rank_hyperedges_by_rrf(
    discovered: dict[str, EdgeDiscovery],
    edge_top_k: int,
) -> tuple[list[EdgeDiscovery], list[EdgeDiscovery]]:
    ranked = sorted(
        discovered.values(),
        key=lambda item: (
            item.edge_rrf_score,
            len({hit["node_type"] for hit in item.node_hits}),
            item.dataset_use_id,
        ),
        reverse=True,
    )
    limit = max(1, edge_top_k)
    return ranked[:limit], ranked[limit:]



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
    pool: list[EdgeDiscovery],
    api_key: str,
    rerank_url: str,
    rerank_model: str,
    rerank_instruct: str,
    max_document_chars: int,
    timeout: float,
) -> tuple[list[EdgeDiscovery], dict[str, Any]]:
    """One expensive semantic rerank over only Top-K hyperedges."""

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
        key=lambda item: (
            item.rerank_score,
            item.normalized_edge_rrf_score,
            item.dataset_use_id,
        ),
        reverse=True,
    )
    for position, item in enumerate(ranked, start=1):
        item.rerank_position = position
    return ranked, raw



# ---------------------------------------------------------------------------
# 4. Dataset aggregation
# ---------------------------------------------------------------------------

def _normalized_decay_score(
    scores: list[float],
    weights: tuple[float, ...] = DEFAULT_DATASET_USE_DECAY_WEIGHTS,
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


def aggregate_reranked_edges_to_datasets(
    *,
    store: base.WikiStore,
    ranked_uses: list[EdgeDiscovery],
    supporting_uses_per_dataset: int,
    map_derived_to_source: bool,
) -> tuple[list[NodeEdgeDatasetCandidate], list[dict[str, Any]]]:
    """Aggregate top query-relevant DatasetUse facts into Dataset scores.

    No evidence-count sum is used. A normalized 0.7/0.2/0.1 decay over at most
    three best uses provides robustness to one anomalous edge without rewarding
    large databases for having many historical uses.
    """

    grouped: dict[str, list[tuple[EdgeDiscovery, dict[str, Any]]]] = defaultdict(list)
    derivations: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for item in ranked_uses:
        use = store.use_by_id[item.dataset_use_id]
        dataset = store.dataset_by_id[use["dataset_id"]]
        target_dataset_id = dataset["dataset_id"]

        if map_derived_to_source:
            source_id = dataset.get("source_dataset_id")
            if (
                not dataset.get("recommendable", False)
                and source_id
                and source_id in store.dataset_by_id
            ):
                target_dataset_id = source_id
                derivations[target_dataset_id].append(
                    _derivation_note(dataset, target_dataset_id, use)
                )

        grouped[target_dataset_id].append((item, use))

    candidates: list[NodeEdgeDatasetCandidate] = []
    global _CURRENT_USE_SCORES
    _CURRENT_USE_SCORES = {}

    limit = max(1, supporting_uses_per_dataset)
    for dataset_id, rows in grouped.items():
        rows.sort(
            key=lambda pair: (
                pair[0].rerank_score,
                pair[0].normalized_edge_rrf_score,
            ),
            reverse=True,
        )
        kept = rows[:limit]
        kept_scores = [item.rerank_score for item, _ in kept]
        aggregate_score = _normalized_decay_score(kept_scores)

        candidate = NodeEdgeDatasetCandidate(dataset_id=dataset_id)
        candidate.aggregated_use_score = aggregate_score
        candidate.final_score = aggregate_score
        candidate.retrieval_score = max(
            item.normalized_edge_rrf_score for item, _ in rows
        )
        candidate.supporting_use_scores = {
            use["dataset_use_id"]: item.rerank_score
            for item, use in kept
        }
        candidate.supporting_use_ids = set(candidate.supporting_use_scores)
        candidate.supporting_doc_ids = set(candidate.supporting_use_ids)

        for item, _ in kept:
            candidate.supporting_doc_ids.update(
                hit["node_id"] for hit in item.node_hits
            )

        candidate.derivation_notes = derivations.get(dataset_id, [])
        candidate.rerank_reason = (
            "Dataset score uses normalized decayed Top DatasetUse evidence: "
            + ", ".join(
                f"{use['dataset_use_id']}={item.rerank_score:.6f}"
                for item, use in kept
            )
            + f"; aggregate={aggregate_score:.6f}"
        )
        _CURRENT_USE_SCORES.update(candidate.supporting_use_scores)
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

def select_final_datasets(
    *,
    store: base.WikiStore,
    plan: base.QueryPlan,
    ranked: list[NodeEdgeDatasetCandidate],
    selection_mode: str,
    max_results: int,
    minimum_score: float,
    candidate_top_k: int,
) -> tuple[list[NodeEdgeDatasetCandidate], dict[str, Any]]:
    """Keep retrieval Top-K separate from the downstream recommendation policy."""

    if selection_mode == "topk":
        selected = ranked[:max(0, max_results)]
        return selected, {
            "mode": "topk",
            "selection_reason": "top_ranked_datasets_after_family_dedup",
            "selected_size": len(selected),
        }

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


def edge_trace(item: EdgeDiscovery, store: base.WikiStore) -> dict[str, Any]:
    use = store.use_by_id[item.dataset_use_id]
    return {
        "dataset_use_id": item.dataset_use_id,
        "dataset_id": use["dataset_id"],
        "task_id": use["task_id"],
        "stage_id": use["stage_id"],
        "paper_id": use["paper_id"],
        "usage_role": use.get("usage_role"),
        "node_hits": item.node_hits,
        "edge_rrf_score": item.edge_rrf_score,
        "normalized_edge_rrf_score": item.normalized_edge_rrf_score,
        "rerank_score": item.rerank_score,
        "rerank_position": item.rerank_position,
    }


def dataset_trace(candidate: NodeEdgeDatasetCandidate) -> dict[str, Any]:
    return {
        "dataset_id": candidate.dataset_id,
        "final_score": candidate.final_score,
        "aggregated_use_score": candidate.aggregated_use_score,
        "retrieval_edge_score": candidate.retrieval_score,
        "supporting_use_scores": candidate.supporting_use_scores,
        "supporting_use_ids": sorted(candidate.supporting_use_ids),
        "supporting_doc_ids": sorted(candidate.supporting_doc_ids),
        "derivation_notes": candidate.derivation_notes,
        "rerank_reason": candidate.rerank_reason,
    }



# ---------------------------------------------------------------------------
# 6. Query orchestration
# ---------------------------------------------------------------------------

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
    edge_top_k: int,
    supporting_uses_per_dataset: int,
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
) -> tuple[str, dict[str, Any]]:

    # A. Query understanding and deterministic multi-route query construction.
    plan, rewrite_raw = rewrite_hyperedge_query(client, chat_model, question)

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

    # C. One-hop hyperedge completion and edge-level RRF.
    discovered, expansion_trace = expand_nodes_to_dataset_uses(
        store,
        documents,
        node_seeds,
        rrf_k,
        task_node_weight,
        dataset_node_weight,
        stage_node_weight,
        specificity_floor,
    )
    edge_rrf_top, edge_rrf_dropped = rank_hyperedges_by_rrf(
        discovered,
        edge_top_k,
    )

    # D. One semantic rerank over only the edge-RRF Top-K.
    if use_rerank:
        ranked_uses, rerank_raw = rerank_dataset_use_hyperedges(
            store=store,
            question=question,
            plan=plan,
            pool=edge_rrf_top,
            api_key=api_key,
            rerank_url=rerank_url,
            rerank_model=rerank_model,
            rerank_instruct=rerank_instruct,
            max_document_chars=max_document_chars,
            timeout=rerank_timeout,
        )
    else:
        ranked_uses = sorted(
            edge_rrf_top,
            key=lambda item: item.normalized_edge_rrf_score,
            reverse=True,
        )
        for position, item in enumerate(ranked_uses, start=1):
            item.rerank_score = item.normalized_edge_rrf_score
            item.rerank_position = position
        rerank_raw = {"disabled": True}

    # E. DatasetUse -> Dataset aggregation; no second LLM rerank.
    candidates, aggregation_excluded = aggregate_reranked_edges_to_datasets(
        store=store,
        ranked_uses=ranked_uses,
        supporting_uses_per_dataset=supporting_uses_per_dataset,
        map_derived_to_source=map_derived_to_source,
    )
    candidates, family_removed = deduplicate_dataset_families(
        store,
        candidates,
        enabled=family_dedup,
    )

    # Retrieval ranking is frozen here and should be used for Gold Recall@K.
    retrieval_top = candidates[:max(0, retrieval_top_k)]

    # F. Optional downstream minimum/recommendation layer.
    base.candidate_context = node_edge_candidate_context
    selected, selection_diagnostics = select_final_datasets(
        store=store,
        plan=plan,
        ranked=candidates,
        selection_mode=selection_mode,
        max_results=max_results,
        minimum_score=minimum_score,
        candidate_top_k=candidate_top_k,
    )

    # G. Answer generation uses the selected recommendation set, while trace
    # still preserves the independent retrieval ranking.
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
        "pipeline": "node_only_hyperedge_rrf_rerank",
        "question": question,
        "query_plan": asdict(plan),
        "rewrite_raw": rewrite_raw,

        "retrieval_design": {
            "indexed_types": ["Task", "Stage", "Dataset"],
            "dataset_use_direct_retrieval": False,
            "node_rrf": True,
            "one_hop_hyperedge_completion": True,
            "edge_rrf_from_endpoint_node_ranks": True,
            "semantic_rerank_count": 1 if use_rerank else 0,
            "dataset_aggregation": "normalized_decayed_top_dataset_use_scores",
            "retrieval_and_recommendation_separated": True,
        },

        "raw_rankings": raw_rankings,
        "node_rrf_results": node_results[:100],
        "node_seed_diagnostics": node_seed_diagnostics,
        "node_seed_count": len(node_seeds),

        "hyperedge_expansion": expansion_trace,
        "discovered_dataset_use_count": len(discovered),
        "edge_rrf_ranked_count": len(discovered),
        "edge_top_k": edge_top_k,
        "edge_rrf_top_dataset_use_ids": [
            item.dataset_use_id for item in edge_rrf_top
        ],
        "edge_rrf_dropped_dataset_use_ids": [
            item.dataset_use_id for item in edge_rrf_dropped
        ],

        "rerank_model": rerank_model if use_rerank else None,
        "rerank_instruct": rerank_instruct if use_rerank else None,
        "rerank_raw": rerank_raw,
        "ranked_dataset_uses": [
            edge_trace(item, store) for item in ranked_uses
        ],

        "aggregation": {
            "method": "top_m_decayed",
            "weights": list(DEFAULT_DATASET_USE_DECAY_WEIGHTS),
            "supporting_uses_per_dataset": supporting_uses_per_dataset,
            "map_derived_to_source": map_derived_to_source,
        },
        "aggregation_excluded": aggregation_excluded,
        "family_dedup_enabled": family_dedup,
        "family_dedup_removed": family_removed,
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

        "evidence_packages": packages,
        "answer_raw": answer_raw,
        "answer_validation_errors": validation_errors,
        "final_answer": answer,
    }
    return answer, trace



# ---------------------------------------------------------------------------
# 7. CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description=(
            "Node-only retrieval -> DatasetUse hyperedge RRF -> one rerank "
            "-> Dataset aggregation -> optional minimum-set recommendation"
        )
    )
    parser.add_argument("--wiki-root", type=Path, default=script_dir / "LLMWiki_new")
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

    parser.add_argument(
        "--edge-top-k",
        type=int,
        default=DEFAULT_EDGE_TOP_K,
        help="Edge RRF 后进入昂贵 rerank 的 DatasetUse 数量",
    )
    parser.add_argument(
        "--supporting-uses-per-dataset",
        type=int,
        default=DEFAULT_SUPPORTING_USES_PER_DATASET,
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
        choices=("topk", "minimum", "recommend"),
        default="minimum",
        help=(
            "topk直接返回检索排名；minimum只作为检索后的最小数据集组合层；"
            "recommend保留原基础模块推荐器"
        ),
    )

    parser.add_argument(
        "--no-family-dedup",
        action="store_true",
        help="关闭 Dataset family 去重，用于检查父集/子集粒度问题",
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
            "status": "node_only_hyperedge_rrf_index_ready",
            "index_dir": str(args.index_dir.resolve()),
            "documents": len(documents),
            "embedding_model": args.embedding_model,
            "rerank_model": args.rerank_model,
            "wiki_fingerprint": meta["wiki_fingerprint"],
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
        edge_top_k=args.edge_top_k,
        supporting_uses_per_dataset=args.supporting_uses_per_dataset,
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
    )

    trace_path = args.trace_output
    if trace_path is None:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        trace_path = (
            script_dir / "retrieval_runs" /
            f"node_only_hyperedge_rrf_{stamp}.json"
        )
    base.write_json(trace_path, trace)
    print(answer)
    print(f"\n[trace] {trace_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

