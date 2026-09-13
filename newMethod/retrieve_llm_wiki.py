from __future__ import annotations

"""材料研发数据集的混合检索、关系扩展、重排和答案生成。

该文件完整实现《材料研发数据集在线检索流程设计.md》中的四个主要阶段：

1. Query Rewrite：解析材料范围、目标性质、约束、阶段并生成多路查询；
2. Dense + BM25：分别召回页面，再通过 RRF 按排名融合；
3. Graph + Rerank：沿知识图谱有限扩展，聚合 Dataset 并重排；
4. Answer Generation：只根据通过 DatasetUse 证据校验的候选生成答案。

索引和查询都在本文件中实现。向量由配置的 Qwen 兼容接口生成，BM25、
RRF、图扩展与结构化重排均在本地运行，不依赖外部向量数据库。
"""

import argparse
import hashlib
import json
import math
import os
import re
import sys
import time
from collections import Counter, defaultdict, deque
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI


# ---------------------------------------------------------------------------
# 0. 全局配置：节点范围、默认模型和图关系权重
# ---------------------------------------------------------------------------

DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
DEFAULT_CHAT_MODEL = "qwen-plus"
DEFAULT_EMBEDDING_MODEL = "text-embedding-v4"
INDEX_VERSION = "1.0"
SEARCHABLE_NODE_TYPES = {"Task", "Stage", "DatasetUse", "Dataset"}

# 关系边不作为初始召回的硬过滤，但不同关系对候选的支持强度不同。
RELATION_WEIGHTS = {
    "REPORTS_TASK": 0.35,
    "HAS_STAGE": 0.85,
    "NEXT_STAGE": 0.30,
    "HAS_DATASET_USE": 1.00,
    "AT_STAGE": 1.00,
    "USES_DATASET": 1.00,
    "EVIDENCED_BY": 0.25,
    "DERIVED_FROM": 0.90,
}

ALLOWED_STAGES = {
    "data_acquisition", "data_preparation", "label_generation", "model_training",
    "model_evaluation", "candidate_generation", "candidate_screening",
    "computational_validation", "experimental_validation", "other",
}

ALLOWED_ROLES = {
    "source", "training", "validation", "test", "pretraining", "label_source",
    "candidate_pool", "screening", "benchmark", "computational_validation",
    "experimental_validation",
}


# ---------------------------------------------------------------------------
# 1. 数据结构：QueryPlan、检索文档和数据集候选
# ---------------------------------------------------------------------------

@dataclass
class QueryPlan:
    """Query Rewrite 后的结构化检索计划。"""

    objective: str = ""
    material_scope: list[str] = field(default_factory=list)
    target_properties: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    required_stages: list[str] = field(default_factory=list)
    preferred_usage_roles: list[str] = field(default_factory=list)
    subtasks: list[str] = field(default_factory=list)
    dense_queries: list[str] = field(default_factory=list)
    bm25_queries: list[str] = field(default_factory=list)


@dataclass
class SearchDocument:
    """一个可检索的 Wiki 页面及其结构化元数据。"""

    doc_id: str
    entity_id: str
    node_type: str
    text: str
    paper_id: str | None = None
    task_id: str | None = None
    stage_id: str | None = None
    dataset_id: str | None = None
    dataset_use_id: str | None = None
    stage_type: str | None = None
    usage_role: str | None = None
    availability: str | None = None
    recommendable: bool | None = None
    source_path: str = ""


@dataclass
class DatasetCandidate:
    """页面和关系边聚合后的 Dataset 级候选。"""

    dataset_id: str
    retrieval_score: float = 0.0
    graph_score: float = 0.0
    feature_score: float = 0.0
    deterministic_score: float = 0.0
    llm_score: float | None = None
    final_score: float = 0.0
    supporting_doc_ids: set[str] = field(default_factory=set)
    supporting_use_ids: set[str] = field(default_factory=set)
    derivation_notes: list[dict[str, Any]] = field(default_factory=list)
    rerank_reason: str = ""


# ---------------------------------------------------------------------------
# 2. 通用 I/O：读取 JSONL、保存索引和解析模型 JSON
# ---------------------------------------------------------------------------

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_json_object(raw: str) -> dict[str, Any]:
    """兼容纯 JSON、Markdown code fence 和 JSON 前后的少量说明。"""

    text = (raw or "").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)
    try:
        value = json.loads(text, strict=False)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            raise
        value = json.loads(text[start : end + 1], strict=False)
    if not isinstance(value, dict):
        raise ValueError("模型输出不是 JSON object")
    return value


def unique_strings(values: Iterable[Any]) -> list[str]:
    result, seen = [], set()
    for value in values:
        text = str(value or "").strip()
        key = text.casefold()
        if text and key not in seen:
            seen.add(key)
            result.append(text)
    return result


# ---------------------------------------------------------------------------
# 3. Wiki 数据层：一次加载节点、页面、DatasetUse 和关系边
# ---------------------------------------------------------------------------

class WikiStore:
    """把 JSONL 节点、Markdown 页面和 edges.jsonl 加载到内存。"""

    def __init__(self, wiki_root: Path):
        self.root = wiki_root.resolve()
        self.papers = load_jsonl(self.root / "raw/papers.jsonl")
        self.tasks = load_jsonl(self.root / "raw/tasks.jsonl")
        self.stages = load_jsonl(self.root / "raw/stages.jsonl")
        self.datasets = load_jsonl(self.root / "raw/datasets.jsonl")
        self.raw_uses = load_jsonl(self.root / "raw/dataset_uses.jsonl")
        self.uses = self._expand_dataset_uses(self.raw_uses)
        self.edges = load_jsonl(self.root / "relations/edges.jsonl")

        self.paper_by_id = {row["paper_id"]: row for row in self.papers}
        self.task_by_id = {row["task_id"]: row for row in self.tasks}
        self.stage_by_id = {row["stage_id"]: row for row in self.stages}
        self.dataset_by_id = {row["dataset_id"]: row for row in self.datasets}
        self.use_by_id = {row["dataset_use_id"]: row for row in self.uses}

        self.uses_by_task: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.uses_by_stage: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.uses_by_dataset: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for use in self.uses:
            self.uses_by_task[use["task_id"]].append(use)
            self.uses_by_stage[use["stage_id"]].append(use)
            self.uses_by_dataset[use["dataset_id"]].append(use)

        # 同时保存正向和反向邻接，支持从任意页面进行 1～2 跳扩展。
        self.adjacency: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for edge in self.edges:
            forward = {**edge, "neighbor_id": edge["target_id"], "direction": "out"}
            reverse = {**edge, "neighbor_id": edge["source_id"], "direction": "in"}
            self.adjacency[edge["source_id"]].append(forward)
            self.adjacency[edge["target_id"]].append(reverse)

    @staticmethod
    def _expand_dataset_uses(raw_uses: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Support both event-centered and dataset-centered DatasetUse schemas."""

        uses: list[dict[str, Any]] = []
        for use in raw_uses:
            if all(key in use for key in ("paper_id", "task_id", "stage_id", "dataset_id")):
                uses.append(use)
                continue

            records = use.get("usage_records")
            if not isinstance(records, list):
                continue
            for index, record in enumerate(records, start=1):
                if not isinstance(record, dict):
                    continue
                if not all(key in record for key in ("paper_id", "task_id", "stage_id", "dataset_id")):
                    continue
                event = {
                    **record,
                    "aggregate_dataset_use_id": use.get("dataset_use_id"),
                    "aggregate_usage_roles": use.get("usage_roles", []),
                    "aggregate_purposes": use.get("purposes", []),
                    "aggregate_evidence": use.get("evidence", []),
                }
                event["dataset_use_id"] = str(
                    record.get("dataset_use_id")
                    or record.get("usage_record_id")
                    or f"{use.get('dataset_use_id', 'DU')}_{index:03d}"
                )
                event.setdefault("usage_record_id", event["dataset_use_id"])
                event.setdefault("usage_role", (use.get("usage_roles") or ["unknown"])[0])
                event.setdefault("purpose", (use.get("purposes") or ["unknown"])[0])
                event.setdefault("used_fields", use.get("used_fields", []))
                event.setdefault("filter_conditions", use.get("filter_conditions", []))
                event.setdefault("construction_method", None)
                event.setdefault("sample_count", None)
                event.setdefault("evidence", use.get("evidence", []))
                event.setdefault("confidence", use.get("confidence", 0.5))
                uses.append(event)
        return uses

    def _page_text(self, directory: str, node_id: str) -> tuple[str, str]:
        path = self.root / "pages" / directory / f"{node_id}.md"
        return path.read_text(encoding="utf-8"), str(path)

    def build_documents(self, max_chars: int = 12_000) -> list[SearchDocument]:
        """将 Task、Stage、DatasetUse、Dataset 页面构造成检索文档。"""

        documents: list[SearchDocument] = []
        for task in self.tasks:
            text, path = self._page_text("tasks", task["task_id"])
            documents.append(SearchDocument(
                doc_id=task["task_id"], entity_id=task["task_id"], node_type="Task",
                text=text[:max_chars], paper_id=task["paper_id"], task_id=task["task_id"],
                source_path=path,
            ))
        for stage in self.stages:
            text, path = self._page_text("stages", stage["stage_id"])
            documents.append(SearchDocument(
                doc_id=stage["stage_id"], entity_id=stage["stage_id"], node_type="Stage",
                text=text[:max_chars], paper_id=stage["paper_id"], task_id=stage["task_id"],
                stage_id=stage["stage_id"], stage_type=stage["stage_type"], source_path=path,
            ))
        for use in self.uses:
            page_id = use.get("aggregate_dataset_use_id") or use["dataset_use_id"]
            text, path = self._page_text("dataset_uses", page_id)
            documents.append(SearchDocument(
                doc_id=use["dataset_use_id"], entity_id=use["dataset_use_id"],
                node_type="DatasetUse", text=text[:max_chars], paper_id=use["paper_id"],
                task_id=use["task_id"], stage_id=use["stage_id"],
                dataset_id=use["dataset_id"], dataset_use_id=use["dataset_use_id"],
                stage_type=self.stage_by_id[use["stage_id"]]["stage_type"],
                usage_role=use["usage_role"], source_path=path,
            ))
        for dataset in self.datasets:
            # 论文专属或不可直接复用的 Dataset 页面不参与 Dense/BM25 初始召回。
            # 它们对应的 DatasetUse 页面仍然保留在索引中，用于提供筛选条件、
            # 构建方法和论文证据，并在候选聚合时映射到公共源数据集。
            if not dataset.get("recommendable", False):
                continue
            
            text, path = self._page_text("datasets", dataset["dataset_id"])
            documents.append(SearchDocument(
                doc_id=dataset["dataset_id"], entity_id=dataset["dataset_id"],
                node_type="Dataset", text=text[:max_chars], dataset_id=dataset["dataset_id"],
                availability=dataset["availability"], recommendable=dataset["recommendable"],
                source_path=path,
            ))
        return documents

    def fingerprint(self) -> str:
        """索引指纹用于检测 Wiki 内容变化，避免误用旧向量。"""

        digest = hashlib.sha256()
        paths = [
            self.root / "raw/tasks.jsonl", self.root / "raw/stages.jsonl",
            self.root / "raw/datasets.jsonl", self.root / "raw/dataset_uses.jsonl",
            self.root / "relations/edges.jsonl",
        ]
        for path in paths:
            digest.update(path.read_bytes())
        return digest.hexdigest()


# ---------------------------------------------------------------------------
# 4. 本地 BM25：无需 rank_bm25 依赖，支持英文词和中文字符/二元词
# ---------------------------------------------------------------------------

def tokenize(text: str) -> list[str]:
    """材料术语以英文 token 为主；中文同时生成单字和二元词。"""

    normalized = text.casefold().replace("_", " ")
    english = re.findall(r"[a-z][a-z0-9.+-]*|\d+(?:\.\d+)?", normalized)
    chinese_runs = re.findall(r"[\u4e00-\u9fff]+", normalized)
    chinese = []
    for run in chinese_runs:
        chinese.extend(run)
        chinese.extend(run[index : index + 2] for index in range(len(run) - 1))
    return english + chinese


class BM25Index:
    """标准 Okapi BM25，本地按需由 documents.json 重建。"""

    def __init__(self, documents: list[SearchDocument], k1: float = 1.5, b: float = 0.75):
        self.k1, self.b = k1, b
        self.tokens = [tokenize(document.text) for document in documents]
        self.lengths = np.asarray([len(tokens) for tokens in self.tokens], dtype=np.float32)
        self.average_length = float(self.lengths.mean()) if len(self.lengths) else 1.0
        self.term_frequencies = [Counter(tokens) for tokens in self.tokens]
        document_frequency = Counter()
        for tokens in self.tokens:
            document_frequency.update(set(tokens))
        count = max(1, len(self.tokens))
        self.idf = {
            term: math.log(1.0 + (count - frequency + 0.5) / (frequency + 0.5))
            for term, frequency in document_frequency.items()
        }

    def scores(self, query: str) -> np.ndarray:
        query_terms = tokenize(query)
        result = np.zeros(len(self.tokens), dtype=np.float32)
        if not query_terms:
            return result
        for index, frequencies in enumerate(self.term_frequencies):
            length_norm = self.k1 * (
                1.0 - self.b + self.b * float(self.lengths[index]) / max(self.average_length, 1.0)
            )
            score = 0.0
            for term in query_terms:
                frequency = frequencies.get(term, 0)
                if frequency:
                    score += self.idf.get(term, 0.0) * frequency * (self.k1 + 1.0) / (frequency + length_norm)
            result[index] = score
        return result


# ---------------------------------------------------------------------------
# 5. Dense 索引：批量生成并持久化归一化向量
# ---------------------------------------------------------------------------

def embed_texts(client: OpenAI, model: str, texts: list[str], batch_size: int = 10) -> np.ndarray:
    # DashScope 当前单次 embedding 请求最多接收 10 条；对更大的 CLI 参数自动收敛。
    batch_size = max(1, min(batch_size, 10))
    vectors = []
    for start in range(0, len(texts), batch_size):
        batch = texts[start : start + batch_size]
        response = client.embeddings.create(model=model, input=batch)
        ordered = sorted(response.data, key=lambda item: item.index)
        vectors.extend(item.embedding for item in ordered)
    matrix = np.asarray(vectors, dtype=np.float32)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    return matrix / np.maximum(norms, 1e-12)


def build_index(store: WikiStore, client: OpenAI, index_dir: Path, embedding_model: str,
                batch_size: int = 10) -> tuple[list[SearchDocument], np.ndarray]:
    """构建检索文档和 Dense 向量；BM25 在加载文档后本地即时建立。"""

    documents = store.build_documents()
    print(f"Building embeddings for {len(documents)} Wiki pages...", flush=True)
    embeddings = embed_texts(client, embedding_model, [document.text for document in documents], batch_size)
    index_dir.mkdir(parents=True, exist_ok=True)
    write_json(index_dir / "documents.json", [asdict(document) for document in documents])
    np.save(index_dir / "embeddings.npy", embeddings)
    write_json(index_dir / "index_meta.json", {
        "index_version": INDEX_VERSION, "created_at": utc_now(),
        "wiki_fingerprint": store.fingerprint(), "embedding_model": embedding_model,
        "document_count": len(documents), "embedding_dimension": int(embeddings.shape[1]),
        "node_types": sorted(SEARCHABLE_NODE_TYPES),
    })
    return documents, embeddings


def load_index(store: WikiStore, index_dir: Path) -> tuple[list[SearchDocument], np.ndarray, dict[str, Any]]:
    meta = json.loads((index_dir / "index_meta.json").read_text(encoding="utf-8"))
    if meta.get("wiki_fingerprint") != store.fingerprint():
        raise RuntimeError("检索索引与当前 newLLMWiki 不一致，请使用 --build-index 重建")
    documents = [SearchDocument(**row) for row in json.loads((index_dir / "documents.json").read_text(encoding="utf-8"))]
    embeddings = np.load(index_dir / "embeddings.npy")
    if len(documents) != len(embeddings):
        raise RuntimeError("documents.json 与 embeddings.npy 数量不一致")
    return documents, embeddings, meta


# ---------------------------------------------------------------------------
# 6. Query Rewrite：意图解析、子任务拆解、Dense/BM25 查询生成
# ---------------------------------------------------------------------------

QUERY_REWRITE_SYSTEM = """
You rewrite a user's materials R&D dataset request into a structured retrieval plan.
Return one JSON object only. Use concise professional English canonical terms in
the value fields. Every material, property, and constraint must quote the exact
substring of the user's question that supports it.

Schema:
{
  "objective": string,
  "material_scope": [{"value": string, "support_text": string}],
  "target_properties": [{"value": string, "support_text": string}],
  "constraints": [{"value": string, "support_text": string}],
  "required_stages": [string],
  "preferred_usage_roles": [string],
  "subtasks": [string],
  "dense_queries": [string],
  "bm25_queries": [string]
}

Allowed required_stages:
data_acquisition, data_preparation, label_generation, model_training,
model_evaluation, candidate_generation, candidate_screening,
computational_validation, experimental_validation, other.

Allowed preferred_usage_roles:
source, training, validation, test, pretraining, label_source, candidate_pool,
screening, benchmark, computational_validation, experimental_validation.

Rules:
- support_text must be copied exactly from the user question.
- value may professionally normalize support_text but must not be more specific.
- Never add a composition/formula, element, numeric range, application domain,
  environmental condition, or stability subtype not explicitly stated.
- "suitable band gap" must remain qualitative when no numeric range is given.
- When stages are not explicitly named, infer only the minimal R&D stages needed
  to fulfill the objective and make the inference visible in required_stages.
- Do not infer experimental_validation unless the user explicitly asks for
  experiments, synthesis, measurements, or experimental validation.
- Decompose complex requests into minimal data needs, not modeling methods.
- dense_queries and bm25_queries may be empty; the program will deterministically
  construct grounded retrieval queries from the validated fields.
""".strip()


def normalize_supported_items(items: Any, question: str, use_original: bool = False) -> list[str]:
    """只接受能逐字回指用户问题的字段，阻断 Rewrite 擅自添加约束。"""

    question_normalized = re.sub(r"\s+", "", question).casefold()
    result = []
    for item in items if isinstance(items, list) else []:
        if not isinstance(item, dict):
            continue
        value = str(item.get("value") or "").strip()
        support = str(item.get("support_text") or "").strip()
        support_normalized = re.sub(r"\s+", "", support).casefold()
        if not value or not support or support_normalized not in question_normalized:
            continue
        # 专业化结果不得引入用户原文不存在的数字范围或具体化学式。
        value_numbers = set(re.findall(r"\d+(?:\.\d+)?", value))
        support_numbers = set(re.findall(r"\d+(?:\.\d+)?", support))
        if not value_numbers <= support_numbers:
            continue
        result.append(support if use_original else value)
    return unique_strings(result)


def supported_item_pairs(items: Any, question: str) -> list[tuple[str, str]]:
    """Return validated (normalized value, exact user evidence) pairs."""

    question_normalized = re.sub(r"\s+", "", question).casefold()
    result: list[tuple[str, str]] = []
    for item in items if isinstance(items, list) else []:
        if not isinstance(item, dict):
            continue
        value = str(item.get("value") or "").strip()
        support = str(item.get("support_text") or "").strip()
        support_normalized = re.sub(r"\s+", "", support).casefold()
        if value and support and support_normalized in question_normalized:
            result.append((value, support))
    return result


def normalize_materials(items: Any, question: str) -> list[str]:
    """Normalize material classes without inventing compositions or elements."""

    materials: list[str] = []
    for value, support in supported_item_pairs(items, question):
        support_lower = support.casefold()
        if "\u65e0\u673a\u9499\u949b\u77ff" in support:
            materials.append("inorganic perovskite")
        elif "\u65e0\u673a\u6676\u4f53" in support:
            materials.append("inorganic crystal")
        elif "\u9499\u949b\u77ff" in support or "perovskite" in support_lower:
            materials.append("perovskite")
        else:
            value_numbers = set(re.findall(r"\d+(?:\.\d+)?", value))
            support_numbers = set(re.findall(r"\d+(?:\.\d+)?", support))
            materials.append(value if value_numbers <= support_numbers else support)
    return unique_strings(materials)


def normalize_properties(items: Any, question: str) -> list[str]:
    """Recover grounded property classes even when the model over-specifies them."""

    properties: list[str] = []
    for value, support in supported_item_pairs(items, question):
        support_lower = support.casefold()
        if re.search(r"\u5e26\u9699|band\s*gap|bandgap", support_lower):
            properties.append("band gap")
        if re.search(r"\u7a33\u5b9a|stabil", support_lower):
            properties.append("stability")
        if not (
            re.search(r"\u5e26\u9699|band\s*gap|bandgap", support_lower)
            or re.search(r"\u7a33\u5b9a|stabil", support_lower)
        ):
            value_numbers = set(re.findall(r"\d+(?:\.\d+)?", value))
            support_numbers = set(re.findall(r"\d+(?:\.\d+)?", support))
            properties.append(value if value_numbers <= support_numbers else support)
    return unique_strings(properties)


def controlled_query_terms(properties: list[str]) -> list[str]:
    """受控专业同义扩展只用于召回，不写回用户的目标性质。"""

    terms = []
    for prop in properties:
        lowered = prop.casefold()
        terms.append(prop)
        if "stabil" in lowered:
            terms.extend(["thermodynamic stability", "formation energy", "energy above hull"])
        if "band" in lowered and "gap" in lowered:
            terms.append("band gap")
    return unique_strings(terms)


def normalize_query_plan(value: dict[str, Any], question: str) -> QueryPlan:
    """校验枚举并补充兜底查询，确保 QueryPlan 始终可执行。"""

    stages = [str(item).strip() for item in value.get("required_stages", [])]
    roles = [str(item).strip() for item in value.get("preferred_usage_roles", [])]
    materials = normalize_materials(value.get("material_scope"), question)
    properties = normalize_properties(value.get("target_properties"), question)
    constraints = normalize_supported_items(value.get("constraints"), question, use_original=True)
    # The LLM may translate support_text instead of copying it. Recover only
    # conservative concepts that are directly detectable in the original query.
    question_lower = question.casefold()
    if "\u65e0\u673a\u9499\u949b\u77ff" in question:
        materials = unique_strings([*materials, "inorganic perovskite"])
    elif "\u65e0\u673a\u6676\u4f53" in question:
        materials = unique_strings([*materials, "inorganic crystal"])
    elif "\u9499\u949b\u77ff" in question or "perovskite" in question_lower:
        materials = unique_strings([*materials, "perovskite"])
    if re.search(r"\u5e26\u9699|band\s*gap|bandgap", question_lower):
        properties = unique_strings([*properties, "band gap"])
    if re.search(r"\u7a33\u5b9a|stabil", question_lower):
        properties = unique_strings([*properties, "stability"])
    # Experimental validation requires explicit wording in the user question.
    experiment_pattern = r"\u5b9e\u9a8c|\u5408\u6210|\u6d4b\u91cf|\u6d4b\u8bd5|\u9a8c\u8bc1|experiment|synthesi[sz]|measurement|validation"
    if not re.search(experiment_pattern, question, flags=re.IGNORECASE):
        stages = [stage for stage in stages if stage != "experimental_validation"]
    professional_terms = controlled_query_terms(properties)
    material_text = " ".join(materials)
    subtasks = []
    for prop in properties:
        subtasks.append(f"dataset for {material_text} {prop}".strip())
    for stage in stages:
        if stage in ALLOWED_STAGES:
            subtasks.append(f"{material_text} {stage} dataset".strip())
    subtasks = unique_strings(subtasks)[:6]
    dense_queries = unique_strings([question, f"{material_text} {' '.join(properties)} materials dataset", *subtasks])[:7]
    bm25_queries = unique_strings([
        f"{material_text} {' '.join(professional_terms)} dataset",
        *[f"{material_text} {term} dataset" for term in professional_terms],
    ])[:6]
    # 原始问题包含 source/target、计算/实验、小样本等限定，不能被简化 objective 覆盖。
    grounded_objective = question
    return QueryPlan(
        objective=grounded_objective,
        material_scope=materials,
        target_properties=properties,
        constraints=constraints,
        required_stages=unique_strings(stage for stage in stages if stage in ALLOWED_STAGES),
        preferred_usage_roles=unique_strings(role for role in roles if role in ALLOWED_ROLES),
        subtasks=subtasks,
        dense_queries=dense_queries,
        bm25_queries=bm25_queries,
    )


def rewrite_query(client: OpenAI, model: str, question: str) -> tuple[QueryPlan, str]:
    """调用 LLM 将自然语言需求转换为可审计的 QueryPlan。"""

    response = client.chat.completions.create(
        model=model, temperature=0, max_tokens=2500,
        messages=[
            {"role": "system", "content": QUERY_REWRITE_SYSTEM},
            {"role": "user", "content": question},
        ],
    )
    raw = response.choices[0].message.content or ""
    return normalize_query_plan(parse_json_object(raw), question), raw


# ---------------------------------------------------------------------------
# 7. 多路召回：每个查询独立 Dense/BM25 排名，再通过 RRF 融合
# ---------------------------------------------------------------------------

def ranked_indices(scores: np.ndarray, top_k: int, require_positive: bool = False) -> list[int]:
    order = np.argsort(-scores)
    result = []
    for index in order:
        if require_positive and float(scores[index]) <= 0:
            continue
        result.append(int(index))
        if len(result) >= top_k:
            break
    return result


def reciprocal_rank_fusion(rankings: list[tuple[str, list[int]]], rrf_k: int = 60) -> tuple[dict[int, float], dict[int, list[dict[str, Any]]]]:
    """RRF 只依赖排名，不受 Dense 与 BM25 分数量纲差异影响。"""

    fused: dict[int, float] = defaultdict(float)
    channels: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for channel, ranking in rankings:
        for rank, document_index in enumerate(ranking, start=1):
            contribution = 1.0 / (rrf_k + rank)
            fused[document_index] += contribution
            channels[document_index].append({"channel": channel, "rank": rank, "rrf": contribution})
    return dict(fused), dict(channels)


def hybrid_retrieve(
    client: OpenAI,
    embedding_model: str,
    documents: list[SearchDocument],
    embeddings: np.ndarray,
    bm25: BM25Index,
    plan: QueryPlan,
    dense_top_k: int,
    bm25_top_k: int,
    rrf_k: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """执行多 Dense 查询和多 BM25 查询，并返回统一页面候选。"""

    query_vectors = embed_texts(client, embedding_model, plan.dense_queries, batch_size=16)
    rankings: list[tuple[str, list[int]]] = []
    raw_rankings: list[dict[str, Any]] = []
    for query, vector in zip(plan.dense_queries, query_vectors):
        scores = embeddings @ vector
        ranking = ranked_indices(scores, dense_top_k)
        channel = f"dense:{query}"
        rankings.append((channel, ranking))
        raw_rankings.append({
            "channel": channel,
            "results": [{"doc_id": documents[index].doc_id, "score": float(scores[index])} for index in ranking],
        })
    for query in plan.bm25_queries:
        scores = bm25.scores(query)
        ranking = ranked_indices(scores, bm25_top_k, require_positive=True)
        channel = f"bm25:{query}"
        rankings.append((channel, ranking))
        raw_rankings.append({
            "channel": channel,
            "results": [{"doc_id": documents[index].doc_id, "score": float(scores[index])} for index in ranking],
        })
    fused, channels = reciprocal_rank_fusion(rankings, rrf_k)
    ordered = sorted(fused, key=fused.get, reverse=True)
    maximum = max(fused.values(), default=1.0)
    results = [{
        "doc_index": index,
        "doc_id": documents[index].doc_id,
        "node_type": documents[index].node_type,
        "rrf_score": fused[index],
        "normalized_retrieval_score": fused[index] / maximum,
        "channels": channels.get(index, []),
        "origin": "retrieval",
    } for index in ordered]
    return results, raw_rankings


# ---------------------------------------------------------------------------
# 8. 关系扩展：从初始页面进行有限跳扩展，并保留来源路径
# ---------------------------------------------------------------------------

def expand_graph(store: WikiStore, seed_results: list[dict[str, Any]], max_hops: int = 2,
                 seed_top_k: int = 40) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    """关系是加分证据；未连接页面不会在本步骤被硬删除。"""

    page_scores: dict[str, dict[str, Any]] = {}
    expansion_trace: list[dict[str, Any]] = []
    for seed in seed_results[:seed_top_k]:
        seed_id = seed["doc_id"]
        base_score = float(seed["normalized_retrieval_score"])
        current = page_scores.setdefault(seed_id, {
            "retrieval_score": 0.0, "graph_score": 0.0, "paths": [], "origin": "retrieval",
        })
        current["retrieval_score"] = max(current["retrieval_score"], base_score)
        queue = deque([(seed_id, 0, base_score, [seed_id])])
        best_seen = {(seed_id, 0): base_score}
        while queue:
            node_id, hop, path_score, path = queue.popleft()
            if hop >= max_hops:
                continue
            for edge in store.adjacency.get(node_id, []):
                neighbor = edge["neighbor_id"]
                relation_weight = RELATION_WEIGHTS.get(edge["relation_type"], 0.25)
                next_score = path_score * relation_weight * 0.65
                if next_score <= best_seen.get((neighbor, hop + 1), -1.0):
                    continue
                best_seen[(neighbor, hop + 1)] = next_score
                next_path = [*path, neighbor]
                candidate = page_scores.setdefault(neighbor, {
                    "retrieval_score": 0.0, "graph_score": 0.0, "paths": [], "origin": "graph",
                })
                candidate["graph_score"] = max(candidate["graph_score"], next_score)
                path_record = {
                    "seed_id": seed_id, "from_id": node_id, "to_id": neighbor,
                    "relation_type": edge["relation_type"], "direction": edge["direction"],
                    "hop": hop + 1, "score": next_score, "path": next_path,
                }
                candidate["paths"].append(path_record)
                expansion_trace.append(path_record)
                queue.append((neighbor, hop + 1, next_score, next_path))
    return page_scores, expansion_trace


def document_dataset_uses(store: WikiStore, document: SearchDocument) -> list[dict[str, Any]]:
    """把任意命中页面映射到其可证实的 DatasetUse 事件。"""

    if document.node_type == "DatasetUse" and document.dataset_use_id:
        return [store.use_by_id[document.dataset_use_id]]
    if document.node_type == "Task" and document.task_id:
        return store.uses_by_task.get(document.task_id, [])
    if document.node_type == "Stage" and document.stage_id:
        return store.uses_by_stage.get(document.stage_id, [])
    if document.node_type == "Dataset" and document.dataset_id:
        return store.uses_by_dataset.get(document.dataset_id, [])
    return []


# ---------------------------------------------------------------------------
# 9. Dataset 聚合：页面结果最终统一落到 DatasetUse → Dataset 事实
# ---------------------------------------------------------------------------

def aggregate_dataset_candidates(
    store: WikiStore,
    documents: list[SearchDocument],
    page_scores: dict[str, dict[str, Any]],
) -> tuple[dict[str, DatasetCandidate], list[dict[str, Any]]]:
    """按 dataset_id 聚合页面；私有派生集转换为“公共源 + 构建说明”。"""

    document_by_id = {document.doc_id: document for document in documents}
    candidates: dict[str, DatasetCandidate] = {}
    excluded: list[dict[str, Any]] = []
    for doc_id, score_info in page_scores.items():
        document = document_by_id.get(doc_id)
        if document is None:
            continue  # Paper 等非检索节点只用于路径，不参与 Dataset 聚合。
        uses = document_dataset_uses(store, document)
        for use in uses:
            dataset = store.dataset_by_id[use["dataset_id"]]
            target_dataset_id = dataset["dataset_id"]
            derivation_note = None
            if not dataset.get("recommendable", False):
                source_id = dataset.get("source_dataset_id")
                if source_id and source_id in store.dataset_by_id:
                    target_dataset_id = source_id
                    derivation_note = {
                        "derived_dataset_id": dataset["dataset_id"],
                        "derived_dataset_name": dataset["canonical_name"],
                        "source_dataset_id": source_id,
                        "construction_method": use.get("construction_method"),
                        "filter_conditions": use.get("filter_conditions", []),
                        "paper_id": use["paper_id"],
                        "dataset_use_id": use["dataset_use_id"],
                    }
                else:
                    excluded.append({
                        "dataset_id": dataset["dataset_id"], "dataset_name": dataset["canonical_name"],
                        "reason": "not_recommendable_and_no_public_source",
                        "supporting_doc_id": doc_id, "dataset_use_id": use["dataset_use_id"],
                    })
                    continue
            candidate = candidates.setdefault(target_dataset_id, DatasetCandidate(dataset_id=target_dataset_id))
            candidate.retrieval_score = max(candidate.retrieval_score, float(score_info["retrieval_score"]))
            candidate.graph_score = max(candidate.graph_score, float(score_info["graph_score"]))
            candidate.supporting_doc_ids.add(doc_id)
            candidate.supporting_use_ids.add(use["dataset_use_id"])
            if derivation_note and derivation_note not in candidate.derivation_notes:
                candidate.derivation_notes.append(derivation_note)
    # 最终推荐必须有 DatasetUse 事实；只有 Dataset 页面但无实际使用关系时不能推荐。
    candidates = {key: value for key, value in candidates.items() if value.supporting_use_ids}
    return candidates, excluded


# ---------------------------------------------------------------------------
# 10. 确定性特征重排：任务、材料、性质、阶段、角色、关系和可用性
# ---------------------------------------------------------------------------

def term_set(values: Iterable[Any]) -> set[str]:
    return set(tokenize(" ".join(str(value or "") for value in values)))


def overlap(query_values: Iterable[Any], candidate_values: Iterable[Any]) -> float:
    query_terms = term_set(query_values)
    if not query_terms:
        return 0.0
    candidate_terms = term_set(candidate_values)
    return len(query_terms & candidate_terms) / len(query_terms)


def candidate_context(store: WikiStore, candidate: DatasetCandidate) -> dict[str, Any]:
    dataset = store.dataset_by_id[candidate.dataset_id]
    # 候选一旦被发现，就补齐 Wiki 中该数据集的全部 DatasetUse。否则图路径可能只碰到
    # OQMD 的测试用法，却漏掉更符合当前问题的预训练用法。
    uses = list(store.uses_by_dataset.get(candidate.dataset_id, []))
    candidate.supporting_use_ids.update(use["dataset_use_id"] for use in uses)
    tasks = [store.task_by_id[use["task_id"]] for use in uses]
    stages = [store.stage_by_id[use["stage_id"]] for use in uses]
    return {"dataset": dataset, "uses": uses, "tasks": tasks, "stages": stages}


def deterministic_rerank(store: WikiStore, plan: QueryPlan,
                         candidates: dict[str, DatasetCandidate]) -> list[DatasetCandidate]:
    """可解释的特征重排，为后续 LLM rerank 提供稳定基线。"""

    for candidate in candidates.values():
        context = candidate_context(store, candidate)
        dataset, uses, tasks, stages = context["dataset"], context["uses"], context["tasks"], context["stages"]
        task_values = [plan.objective, *plan.subtasks]
        task_context = [value for task in tasks for value in [task["task_name_raw"], task["objective"]]]
        material_context = dataset.get("material_scope", []) + [
            value for task in tasks for value in task.get("material_scope", [])
        ]
        property_context = dataset.get("available_properties", []) + dataset.get("available_fields", []) + [
            value for use in uses for value in use.get("used_fields", [])
        ] + [value for task in tasks for value in task.get("target_properties", [])]
        observed_stages = {stage["stage_type"] for stage in stages}
        observed_roles = {use["usage_role"] for use in uses}

        task_match = overlap(task_values, task_context)
        material_match = overlap(plan.material_scope, material_context)
        property_match = overlap(plan.target_properties, property_context)
        stage_match = (
            len(set(plan.required_stages) & observed_stages) / len(plan.required_stages)
            if plan.required_stages else 0.0
        )
        role_match = (
            len(set(plan.preferred_usage_roles) & observed_roles) / len(plan.preferred_usage_roles)
            if plan.preferred_usage_roles else 0.0
        )
        relation_evidence = min(1.0, math.log1p(len(uses)) / math.log(6.0))
        availability_score = {
            "public": 1.0, "restricted": 0.45, "unknown": 0.20,
            "not_directly_available": 0.0,
        }.get(dataset.get("availability"), 0.0)

        candidate.feature_score = (
            0.20 * task_match + 0.15 * material_match + 0.25 * property_match
            + 0.20 * stage_match + 0.10 * role_match + 0.10 * relation_evidence
        )
        candidate.deterministic_score = (
            0.38 * candidate.retrieval_score + 0.10 * candidate.graph_score
            + 0.42 * candidate.feature_score + 0.10 * availability_score
        )
        candidate.final_score = candidate.deterministic_score
    return sorted(candidates.values(), key=lambda item: item.final_score, reverse=True)


# ---------------------------------------------------------------------------
# 11. LLM Rerank：再次判断任务相关性、数据作用和可用性
# ---------------------------------------------------------------------------

RERANK_SYSTEM = """
You rerank candidate materials datasets for a user's R&D data need. Evaluate only
the supplied structured facts. Do not assume a dataset property or use that is not
listed. A formal recommendation must be supported by at least one DatasetUse.

Return one JSON object:
{
  "results": [
    {
      "dataset_id": string,
      "relevance": number,
      "useful": boolean,
      "reason": string,
      "covered_data_needs": [string],
      "conflicts": [string]
    }
  ]
}

relevance must be between 0 and 1. Penalize material-scope conflicts, missing
required properties/stages, unavailable private datasets, and evidence that is
only weakly related to the user's task. Public source datasets reconstructed from
paper-derived subsets may remain useful when construction instructions exist.
Return exactly one result for every dataset_id in required_dataset_ids; do not
omit low-relevance candidates, and do not return IDs that were not supplied.
Evaluate each dataset as one possible role in the complete dataset combination,
not as if every dataset must cover every property and stage alone. For
cross-property transfer learning, a small single-property computational or
experimental dataset can be highly useful as a fine-tuning/evaluation target.
When structure files, atomic species, or chemical formulas are explicitly
listed, elemental fractions can be derived from them; note the preprocessing
need instead of rejecting the dataset for lacking a separate composition field.
""".strip()


def rerank_payload(store: WikiStore, candidate: DatasetCandidate) -> dict[str, Any]:
    context = candidate_context(store, candidate)
    dataset, uses = context["dataset"], context["uses"]
    return {
        "dataset_id": dataset["dataset_id"], "dataset_name": dataset["canonical_name"],
        "dataset_type": dataset["dataset_type"], "material_scope": dataset["material_scope"],
        "available_properties": dataset["available_properties"],
        "available_fields": dataset["available_fields"], "availability": dataset["availability"],
        "recommendable": dataset["recommendable"],
        "deterministic_score": round(candidate.deterministic_score, 6),
        "observed_uses": [{
            "dataset_use_id": use["dataset_use_id"],
            "task": store.task_by_id[use["task_id"]]["objective"],
            "stage": store.stage_by_id[use["stage_id"]]["stage_type"],
            "usage_role": use["usage_role"], "purpose": use["purpose"],
            "used_fields": use["used_fields"], "confidence": use["confidence"],
        } for use in uses[:12]],
        "derivation_notes": candidate.derivation_notes[:5],
    }


def llm_rerank(client: OpenAI, model: str, plan: QueryPlan, store: WikiStore,
               ranked: list[DatasetCandidate], candidate_top_k: int = 30,
               rerank_batch_size: int = 6) -> tuple[list[DatasetCandidate], str]:
    candidates = ranked[:candidate_top_k]
    candidate_ids = {candidate.dataset_id for candidate in candidates}
    judgments: dict[str, dict[str, Any]] = {}
    raw_batches: list[dict[str, Any]] = []

    # 小批量重排，且对漏答候选单独重试一次，避免一次长响应只返回前几个结果。
    for start in range(0, len(candidates), rerank_batch_size):
        batch = candidates[start:start + rerank_batch_size]
        pending = batch
        for attempt in range(1, 3):
            if not pending:
                break
            prompt = {
                "query_plan": asdict(plan),
                "candidates": [rerank_payload(store, candidate) for candidate in pending],
                "required_dataset_ids": [candidate.dataset_id for candidate in pending],
            }
            response = client.chat.completions.create(
                model=model, temperature=0, max_tokens=3500,
                messages=[
                    {"role": "system", "content": RERANK_SYSTEM},
                    {"role": "user", "content": json.dumps(prompt, ensure_ascii=False)},
                ],
            )
            batch_raw = response.choices[0].message.content or ""
            raw_batches.append({
                "attempt": attempt,
                "candidate_ids": [candidate.dataset_id for candidate in pending],
                "raw": batch_raw,
            })
            parsed = parse_json_object(batch_raw)
            for row in parsed.get("results", []):
                dataset_id = row.get("dataset_id") if isinstance(row, dict) else None
                if dataset_id in candidate_ids:
                    judgments[dataset_id] = row
            pending = [candidate for candidate in pending if candidate.dataset_id not in judgments]

    missing_ids = [candidate.dataset_id for candidate in candidates if candidate.dataset_id not in judgments]
    raw = json.dumps({"batches": raw_batches, "missing_dataset_ids": missing_ids}, ensure_ascii=False)
    for candidate in ranked:
        judgment = judgments.get(candidate.dataset_id)
        if judgment:
            try:
                relevance = min(1.0, max(0.0, float(judgment.get("relevance", 0.0))))
            except (TypeError, ValueError):
                relevance = 0.0
            if not bool(judgment.get("useful", True)):
                relevance *= 0.35
            dataset = store.dataset_by_id[candidate.dataset_id]
            experimental_query = "experimental" in plan.objective.casefold() or "实验" in plan.objective
            experimental_candidate = "experimental" in " ".join([
                dataset.get("canonical_name", ""), *dataset.get("material_scope", []),
            ]).casefold()
            if experimental_query and experimental_candidate:
                # 用户明确要求实验目标集时，不能因其是单性质小数据集而被错误归零。
                relevance = max(relevance, 0.55)
            candidate.llm_score = relevance
            candidate.rerank_reason = str(judgment.get("reason") or "").strip()
            candidate.final_score = 0.72 * candidate.deterministic_score + 0.28 * relevance
        else:
            # LLM 漏答或候选位于重排窗口外不等于不相关，保留可解释的确定性分数。
            candidate.llm_score = None
            candidate.final_score = candidate.deterministic_score
            candidate.rerank_reason = "LLM reranker 未返回该候选，使用确定性分数回退。"
    return sorted(ranked, key=lambda item: item.final_score, reverse=True), raw


# ---------------------------------------------------------------------------
# 12. 组合选择：覆盖必要阶段/性质/角色，而不是机械固定 Top-5
# ---------------------------------------------------------------------------

def candidate_coverage(store: WikiStore, candidate: DatasetCandidate) -> dict[str, set[str]]:
    context = candidate_context(store, candidate)
    return {
        "stages": {stage["stage_type"] for stage in context["stages"]},
        "roles": {use["usage_role"] for use in context["uses"]},
        "properties": term_set([
            *context["dataset"].get("available_properties", []),
            *context["dataset"].get("available_fields", []),
            *[value for use in context["uses"] for value in use.get("used_fields", [])],
        ]),
    }


def dataset_family_id(store: WikiStore, dataset_id: str) -> str:
    """沿 source_dataset_id 找到根数据集，避免同一家族重复占满结果槽位。"""

    current_id = dataset_id
    visited: set[str] = set()
    while current_id not in visited:
        visited.add(current_id)
        dataset = store.dataset_by_id.get(current_id, {})
        source_id = dataset.get("source_dataset_id")
        if not source_id or source_id not in store.dataset_by_id:
            break
        current_id = source_id
    return current_id


def property_concepts(values: Iterable[str]) -> set[str]:
    """把性质名称归一化为可比较的概念，避免同义词造成虚假的覆盖缺口。"""

    concepts: set[str] = set()
    for value in values:
        text = re.sub(r"[_\-]+", " ", str(value).casefold())
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        matched_known_concept = False

        # 在热力学语境中 enthalpy 与 energy 常指向同一检索需求，例如
        # formation enthalpy 与 formation energy 不应被判断为两个必需数据集。
        energy_like = any(token in text for token in ("energy", "enthalpy", "能", "焓"))
        if ("formation" in text and energy_like) or any(
            token in text for token in ("形成能", "形成焓")
        ):
            concepts.add("formation_energy")
            matched_known_concept = True
        if (("decomposition" in text and energy_like)
                or "分解能" in text
                or "分解焓" in text
                or "energy above hull" in text
                or "energy above the convex hull" in text
                or "ehull" in text):
            concepts.add("decomposition_energy")
            matched_known_concept = True
        if ("stability" in text or "thermodynamically stable" in text
                or "稳定性" in text):
            concepts.add("stability")
            matched_known_concept = True
        if "band gap" in text or "bandgap" in text or "带隙" in text:
            concepts.add("band_gap")
            matched_known_concept = True

        # 未命中已知概念时保留规范化原词，保证其他性质仍能参与覆盖判断。
        if not matched_known_concept:
            fallback = re.sub(r"[^\w]+", "_", text).strip("_")
            if fallback:
                concepts.add(fallback)
    return concepts


def is_evaluation_metric(value: str) -> bool:
    """识别模型评估指标；该函数只供 minimum 结果选择逻辑使用。"""

    text = re.sub(r"[_\-]+", " ", str(value).casefold())
    text = re.sub(r"\s+", " ", text).strip()
    metric_phrases = (
        "classification accuracy", "false positive rate", "false negative rate",
        "precision", "recall", "f1 score", "roc auc", "area under curve",
        "mean absolute error", "root mean squared error", "mae", "rmse", "r2 score",
        "分类准确率", "准确率", "假阳性率", "假阴性率", "精确率", "召回率",
        "平均绝对误差", "均方根误差",
    )
    return any(phrase in text for phrase in metric_phrases)


def minimum_required_atoms(plan: QueryPlan) -> set[tuple[str, str]]:
    """构造最小集合必须覆盖的硬需求：任务阶段与目标性质。"""

    atoms = {("stage", value) for value in plan.required_stages}
    for target_property in plan.target_properties:
        # 准确率、假阳性率等由数据标签计算得到，属于模型评估指标而非材料性质。
        # minimum 模式由 model_evaluation 阶段约束它们，避免产生无法覆盖的伪字段。
        if is_evaluation_metric(target_property):
            continue
        atoms.update(
            ("property", value) for value in property_concepts([target_property])
        )
    return atoms


def candidate_requirement_atoms(store: WikiStore,
                                candidate: DatasetCandidate) -> set[tuple[str, str]]:
    """把单个数据集能够支持的阶段和性质转换为统一覆盖原子。"""

    context = candidate_context(store, candidate)
    atoms = {
        ("stage", stage["stage_type"])
        for stage in context["stages"]
        if stage.get("stage_type")
    }
    property_values = [
        *context["dataset"].get("available_properties", []),
        *context["dataset"].get("available_fields", []),
        *[value for use in context["uses"] for value in use.get("used_fields", [])],
    ]
    atoms.update(("property", value) for value in property_concepts(property_values))
    return atoms


def select_minimum_dataset_set(
    store: WikiStore,
    plan: QueryPlan,
    ranked: list[DatasetCandidate],
    max_results: int = 6,
    minimum_score: float = 0.25,
    candidate_pool_size: int = 20,
) -> list[DatasetCandidate]:
    """精确寻找满足硬需求的数据集最小集合，并用相关性打破同规模平局。"""

    if not ranked or max_results <= 0:
        return []

    required_atoms = minimum_required_atoms(plan)

    # 只在高置信候选池中求解，避免低分长尾数据集仅凭字段巧合进入答案。
    # 前两个候选始终保留，以便分数整体偏低时仍能给出有意义的结果。
    eligible = [
        candidate for index, candidate in enumerate(ranked[:candidate_pool_size])
        if index < 2
        or candidate.final_score >= minimum_score
        or (candidate.llm_score is not None and candidate.llm_score >= 0.50)
    ]
    if not eligible:
        return []

    coverage_by_id = {
        candidate.dataset_id: candidate_requirement_atoms(store, candidate)
        for candidate in eligible
    }
    roles_by_id = {
        candidate.dataset_id: candidate_coverage(store, candidate)["roles"]
        for candidate in eligible
    }

    # 若 Query Rewrite 未抽出阶段或性质，最小集合自然退化为最高分的一个数据集。
    if not required_atoms:
        return eligible[:1]

    preferred_roles = set(plan.preferred_usage_roles)
    best_combination: tuple[DatasetCandidate, ...] | None = None
    best_key: tuple[float, float, float] | None = None

    # 从集合大小 1 开始枚举；首次找到完整覆盖时即保证基数最小。
    for size in range(1, min(max_results, len(eligible)) + 1):
        for combination in combinations(eligible, size):
            # 同一公共数据集及其论文专属子集不应同时占用最小集合名额。
            families = [dataset_family_id(store, item.dataset_id) for item in combination]
            if len(families) != len(set(families)):
                continue

            covered_atoms: set[tuple[str, str]] = set()
            covered_roles: set[str] = set()
            for item in combination:
                covered_atoms.update(coverage_by_id[item.dataset_id])
                covered_roles.update(roles_by_id[item.dataset_id])
            if not required_atoms <= covered_atoms:
                continue

            # 角色是软目标：同样少的数据集优先覆盖更多角色，其次比较重排总分和证据量。
            role_ratio = (
                len(covered_roles & preferred_roles) / len(preferred_roles)
                if preferred_roles else 1.0
            )
            tie_break_key = (
                role_ratio,
                sum(item.final_score for item in combination),
                float(sum(len(item.supporting_use_ids) for item in combination)),
            )
            if best_key is None or tie_break_key > best_key:
                best_key = tie_break_key
                best_combination = combination

        if best_combination is not None:
            return list(best_combination)

    # 候选池无法完整覆盖所有硬需求时，回退到原有推荐选择器，避免返回空答案。
    return select_dataset_combination(store, plan, ranked, max_results, minimum_score)


def select_dataset_combination(store: WikiStore, plan: QueryPlan, ranked: list[DatasetCandidate],
                               max_results: int = 8, minimum_score: float = 0.25) -> list[DatasetCandidate]:
    """贪心覆盖数据需求；至少保留高分结果，新增覆盖优先。"""

    required = {
        "stages": set(plan.required_stages),
        "roles": set(plan.preferred_usage_roles),
        "properties": term_set(plan.target_properties),
    }
    covered = {key: set() for key in required}
    selected = []
    selected_families: set[str] = set()
    for candidate in ranked:
        llm_approved = candidate.llm_score is not None and candidate.llm_score >= 0.50
        if candidate.llm_score is not None and candidate.llm_score < 0.30 and len(selected) >= 2:
            continue
        if candidate.final_score < minimum_score and len(selected) >= 2:
            break
        coverage = candidate_coverage(store, candidate)
        adds_coverage = any((coverage[key] & required[key]) - covered[key] for key in required)
        family_id = dataset_family_id(store, candidate.dataset_id)
        if family_id in selected_families:
            continue
        if len(selected) < 2 or adds_coverage or llm_approved or candidate.final_score >= minimum_score + 0.18:
            selected.append(candidate)
            selected_families.add(family_id)
            for key in covered:
                covered[key].update(coverage[key] & required[key])
        if len(selected) >= max_results:
            break
        if selected and all(not required[key] or required[key] <= covered[key] for key in required):
            next_index = len(selected)
            if next_index >= len(ranked) or ranked[next_index].final_score < minimum_score:
                break
    return selected


# ---------------------------------------------------------------------------
# 13. 证据包：答案模型只能看到经过结构关系确认的 DatasetUse 原文
# ---------------------------------------------------------------------------

def use_relevance(store: WikiStore, plan: QueryPlan, use: dict[str, Any]) -> float:
    task = store.task_by_id[use["task_id"]]
    stage = store.stage_by_id[use["stage_id"]]
    textual = overlap(
        [plan.objective, *plan.material_scope, *plan.target_properties, *plan.subtasks],
        [task["objective"], *task["material_scope"], *task["target_properties"],
         use["purpose"], *use["used_fields"]],
    )
    stage_bonus = 1.0 if stage["stage_type"] in plan.required_stages else 0.0
    role_bonus = 1.0 if use["usage_role"] in plan.preferred_usage_roles else 0.0
    return 0.55 * textual + 0.20 * stage_bonus + 0.10 * role_bonus + 0.15 * float(use["confidence"])


def build_evidence_package(store: WikiStore, plan: QueryPlan,
                           candidate: DatasetCandidate, max_uses: int = 4) -> dict[str, Any]:
    dataset = store.dataset_by_id[candidate.dataset_id]
    uses = [store.use_by_id[use_id] for use_id in candidate.supporting_use_ids if use_id in store.use_by_id]
    uses.sort(key=lambda use: use_relevance(store, plan, use), reverse=True)
    evidence_uses = []
    for use in uses[:max_uses]:
        task, stage = store.task_by_id[use["task_id"]], store.stage_by_id[use["stage_id"]]
        evidence_uses.append({
            "paper_id": use["paper_id"], "task_id": use["task_id"],
            "task": task["objective"], "stage_id": use["stage_id"],
            "stage_type": stage["stage_type"], "stage_name": stage["stage_name_raw"],
            "dataset_use_id": use["dataset_use_id"], "usage_role": use["usage_role"],
            "purpose": use["purpose"], "used_fields": use["used_fields"],
            "construction_method": use.get("construction_method"),
            "filter_conditions": use.get("filter_conditions", []),
            "sample_count": use.get("sample_count"), "confidence": use["confidence"],
            "evidence": use["evidence"][:3],
        })
    return {
        "dataset_id": dataset["dataset_id"], "dataset_name": dataset["canonical_name"],
        "dataset_type": dataset["dataset_type"], "material_scope": dataset["material_scope"],
        "available_properties": dataset["available_properties"],
        "available_fields": dataset["available_fields"], "availability": dataset["availability"],
        "recommendable": dataset["recommendable"], "final_score": round(candidate.final_score, 6),
        "rerank_reason": candidate.rerank_reason,
        "dataset_uses": evidence_uses,
        "derived_subset_reconstruction": candidate.derivation_notes,
    }


# ---------------------------------------------------------------------------
# 14. 答案生成：严格引用证据包，不把模型常识写成数据库事实
# ---------------------------------------------------------------------------

ANSWER_SYSTEM = """
You answer a materials R&D dataset recommendation question in Chinese. Use only
the supplied evidence packages. Do not add dataset properties, availability,
sample counts, paper usages, filters, or construction steps not present there.

For each recommended dataset explain:
1. dataset name and whether it is publicly reusable;
2. relevant R&D stages and usage roles;
3. useful fields/properties actually observed;
4. why it supports the user's task;
5. paper evidence with paper_id, PDF physical page, and a short excerpt;
6. when a paper-derived subset is involved, recommend the public source and
   report only the supplied construction_method/filter_conditions.

If evidence does not cover one requested data need, state the gap explicitly.
Never present a paper_specific or derived_subset dataset as directly downloadable
unless the package explicitly says it is public and recommendable.
Do not introduce a numerical screening threshold, chemical composition, example
material, application, experimental method, URL, or next-step recommendation
unless that exact fact appears in the user's question or evidence packages.
Do not use general scientific knowledge. Cover every supplied evidence package;
if one is unsuitable, say so instead of silently replacing it with external data.
""".strip()


def generate_answer(client: OpenAI, model: str, question: str, plan: QueryPlan,
                    evidence_packages: list[dict[str, Any]]) -> tuple[str, str]:
    payload = {"question": question, "query_plan": asdict(plan), "evidence_packages": evidence_packages}
    response = client.chat.completions.create(
        model=model, temperature=0, max_tokens=6000,
        messages=[
            {"role": "system", "content": ANSWER_SYSTEM},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
    )
    raw = response.choices[0].message.content or ""
    return raw.strip(), raw


def validate_generated_answer(answer: str, question: str,
                              evidence_packages: list[dict[str, Any]]) -> list[str]:
    """轻量事实防火墙：拦截证据包之外的 URL 和具体数值。"""

    source = question + " " + json.dumps(evidence_packages, ensure_ascii=False)
    errors = []
    answer_urls = set(re.findall(r"https?://[^\s)]+", answer))
    source_urls = set(re.findall(r"https?://[^\s)]+", source))
    if not answer_urls <= source_urls:
        errors.append("answer contains URL not present in evidence")
    answer_numbers = set(re.findall(r"\d+\.\d+|\d{2,}", answer.replace(",", "")))
    source_numbers = set(re.findall(r"\d+\.\d+|\d{2,}", source.replace(",", "")))
    unsupported_numbers = sorted(answer_numbers - source_numbers)
    if unsupported_numbers:
        errors.append("answer contains unsupported numbers: " + ", ".join(unsupported_numbers))
    return errors


def deterministic_answer(question: str, packages: list[dict[str, Any]]) -> str:
    """无需答案 LLM 时的可复现实验输出。"""

    lines = [f"问题：{question}", "", "推荐结果："]
    if not packages:
        return "\n".join([*lines, "没有找到同时满足 DatasetUse 和证据约束的数据集。"])
    for index, package in enumerate(packages, start=1):
        lines.extend([
            "", f"{index}. {package['dataset_name']} ({package['dataset_id']})",
            f"   - 可用性：{package['availability']}",
            f"   - 数据集类型：{package['dataset_type']}",
            f"   - 观测性质：{', '.join(package['available_properties']) or '论文未明确说明'}",
        ])
        for use in package["dataset_uses"]:
            lines.append(
                f"   - {use['stage_type']} / {use['usage_role']}：{use['purpose']} "
                f"({use['paper_id']}, {use['dataset_use_id']})"
            )
            for evidence in use["evidence"][:1]:
                excerpt = evidence["text"].replace("\n", " ")
                lines.append(f"     证据：PDF page {evidence['page']}，\"{excerpt}\"")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 15. 单次查询编排：把 Rewrite、召回、图扩展、Rerank、生成串起来
# ---------------------------------------------------------------------------

def candidate_trace(candidate: DatasetCandidate) -> dict[str, Any]:
    return {
        "dataset_id": candidate.dataset_id,
        "retrieval_score": candidate.retrieval_score,
        "graph_score": candidate.graph_score,
        "feature_score": candidate.feature_score,
        "deterministic_score": candidate.deterministic_score,
        "llm_score": candidate.llm_score,
        "final_score": candidate.final_score,
        "supporting_doc_ids": sorted(candidate.supporting_doc_ids),
        "supporting_use_ids": sorted(candidate.supporting_use_ids),
        "derivation_notes": candidate.derivation_notes,
        "rerank_reason": candidate.rerank_reason,
    }


def run_query(
    *, client: OpenAI, chat_model: str, embedding_model: str, store: WikiStore,
    documents: list[SearchDocument], embeddings: np.ndarray, question: str,
    dense_top_k: int = 30, bm25_top_k: int = 30, rrf_k: int = 60,
    seed_top_k: int = 40, graph_hops: int = 2, candidate_top_k: int = 30,
    max_results: int = 6, minimum_score: float = 0.25,
    selection_mode: str = "recommend",
    use_llm_rerank: bool = True, use_answer_llm: bool = True,
) -> tuple[str, dict[str, Any]]:
    # A. Query Rewrite 与子任务查询生成。
    plan, rewrite_raw = rewrite_query(client, chat_model, question)

    # B. 多路 Dense/BM25 召回和 RRF 融合。
    bm25 = BM25Index(documents)
    fused_results, raw_rankings = hybrid_retrieve(
        client, embedding_model, documents, embeddings, bm25, plan,
        dense_top_k, bm25_top_k, rrf_k,
    )

    # C. 对融合页面进行有限图扩展，再映射到有证据的 DatasetUse。
    page_scores, graph_trace = expand_graph(store, fused_results, graph_hops, seed_top_k)
    candidates, excluded = aggregate_dataset_candidates(store, documents, page_scores)

    # D. 先做确定性特征重排，可选再做一次 LLM 相关性判断。
    ranked = deterministic_rerank(store, plan, candidates)
    rerank_raw = ""
    if use_llm_rerank and ranked:
        ranked, rerank_raw = llm_rerank(client, chat_model, plan, store, ranked, candidate_top_k)
    # recommend 保留多个高价值备选；minimum 求满足阶段和性质需求的最小数据集集合。
    if selection_mode == "minimum":
        selected = select_minimum_dataset_set(
            store, plan, ranked, max_results, minimum_score,
            candidate_pool_size=candidate_top_k,
        )
    else:
        selected = select_dataset_combination(store, plan, ranked, max_results, minimum_score)

    # E. 只把最终 DatasetUse 证据包交给答案生成模型。
    packages = [build_evidence_package(store, plan, candidate) for candidate in selected]
    if use_answer_llm:
        answer, answer_raw = generate_answer(client, chat_model, question, plan, packages)
        answer_validation_errors = validate_generated_answer(answer, question, packages)
        if answer_validation_errors:
            answer = deterministic_answer(question, packages)
    else:
        answer, answer_raw = deterministic_answer(question, packages), ""
        answer_validation_errors = []

    trace = {
        "created_at": utc_now(), "question": question, "query_plan": asdict(plan),
        "selection_mode": selection_mode,
        "rewrite_raw": rewrite_raw, "raw_rankings": raw_rankings,
        "rrf_results": fused_results[:100], "graph_expansion": graph_trace,
        "excluded_candidates": excluded,
        "ranked_candidates": [candidate_trace(candidate) for candidate in ranked],
        "selected_dataset_ids": [candidate.dataset_id for candidate in selected],
        "evidence_packages": packages, "rerank_raw": rerank_raw, "answer_raw": answer_raw,
        "answer_validation_errors": answer_validation_errors, "final_answer": answer,
    }
    return answer, trace


# ---------------------------------------------------------------------------
# 16. CLI：支持单独建索引、自动校验索引和执行带追踪的查询
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Hybrid retrieval over newLLMWiki")
    parser.add_argument("--wiki-root", type=Path, default=script_dir / "newLLMWiki")
    parser.add_argument("--index-dir", type=Path, default=script_dir / "newWikiIndex")
    parser.add_argument("--build-index", action="store_true", help="重建本地 Dense/BM25 文档索引")
    parser.add_argument("--question", help="材料研发数据集问题")
    parser.add_argument("--chat-model", default=os.getenv("QWEN_MODEL", DEFAULT_CHAT_MODEL))
    parser.add_argument("--embedding-model", default=os.getenv("QWEN_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL))
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--dense-top-k", type=int, default=30)
    parser.add_argument("--bm25-top-k", type=int, default=30)
    parser.add_argument("--rrf-k", type=int, default=60)
    parser.add_argument("--seed-top-k", type=int, default=40)
    parser.add_argument("--graph-hops", type=int, default=2)
    parser.add_argument("--candidate-top-k", type=int, default=30)
    parser.add_argument("--max-results", type=int, default=6)
    parser.add_argument("--minimum-score", type=float, default=0.25)
    parser.add_argument(
        "--selection-mode", choices=("recommend", "minimum"), default="recommend",
        help="结果选择策略：recommend 保留多个候选；minimum 返回满足需求的最小集合",
    )
    parser.add_argument("--no-llm-rerank", action="store_true")
    parser.add_argument("--no-answer-llm", action="store_true")
    parser.add_argument("--trace-output", type=Path, help="保存完整检索轨迹 JSON")
    return parser.parse_args()


def main() -> int:
    # Windows 中文环境常默认为 GBK；化学式下标等 Unicode 字符需要 UTF-8 输出。
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    load_dotenv(project_root / ".env")
    api_key = os.getenv("QWEN_API_KEY")
    if not api_key:
        raise ValueError("QWEN_API_KEY 未配置")
    base_url = os.getenv("QWEN_BASE_URL", DEFAULT_BASE_URL)
    client = OpenAI(api_key=api_key, base_url=base_url, timeout=240.0, max_retries=2)
    store = WikiStore(args.wiki_root)

    index_files = [args.index_dir / "documents.json", args.index_dir / "embeddings.npy", args.index_dir / "index_meta.json"]
    if args.build_index or not all(path.is_file() for path in index_files):
        documents, embeddings = build_index(
            store, client, args.index_dir, args.embedding_model, args.batch_size
        )
        meta = json.loads((args.index_dir / "index_meta.json").read_text(encoding="utf-8"))
    else:
        documents, embeddings, meta = load_index(store, args.index_dir)
        # 查询必须复用建库时的模型，否则查询向量维度或语义空间可能不一致。
        args.embedding_model = meta["embedding_model"]

    if not args.question:
        print(json.dumps({
            "status": "index_ready", "index_dir": str(args.index_dir.resolve()),
            "documents": len(documents), "embedding_model": args.embedding_model,
            "wiki_fingerprint": meta["wiki_fingerprint"],
        }, ensure_ascii=False, indent=2))
        return 0

    answer, trace = run_query(
        client=client, chat_model=args.chat_model, embedding_model=args.embedding_model,
        store=store, documents=documents, embeddings=embeddings, question=args.question,
        dense_top_k=args.dense_top_k, bm25_top_k=args.bm25_top_k, rrf_k=args.rrf_k,
        seed_top_k=args.seed_top_k, graph_hops=args.graph_hops,
        candidate_top_k=args.candidate_top_k, max_results=args.max_results,
        minimum_score=args.minimum_score, selection_mode=args.selection_mode,
        use_llm_rerank=not args.no_llm_rerank,
        use_answer_llm=not args.no_answer_llm,
    )
    trace_path = args.trace_output
    if trace_path is None:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        trace_path = script_dir / "retrieval_runs" / f"run_{stamp}.json"
    write_json(trace_path, trace)
    print(answer)
    print(f"\n[trace] {trace_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
