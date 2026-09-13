import argparse
import json
import math
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from normalize_query_v2 import (
    fallback_normalization,
    format_subtask_plan,
    normalize_user_query_v2,
    subtask_queries,
)


DEFAULT_INDEX_DIR = Path("wiki_index_all")
DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
DEFAULT_CHAT_MODEL = "qwen-plus"
DEFAULT_EMBEDDING_MODEL = "text-embedding-v4"


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def tokenize(text: str) -> list[str]:
    text = text.lower()
    return re.findall(r"[a-z0-9]+|[\u4e00-\u9fff]", text)


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = 0.0
    norm_a = 0.0
    norm_b = 0.0
    for x, y in zip(a, b):
        dot += x * y
        norm_a += x * x
        norm_b += y * y
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (math.sqrt(norm_a) * math.sqrt(norm_b))


def load_index(index_dir: Path) -> tuple[list[dict], dict, dict]:
    with (index_dir / "documents.json").open("r", encoding="utf-8") as f:
        docs = json.load(f)
    with (index_dir / "embeddings.json").open("r", encoding="utf-8") as f:
        embeddings = json.load(f)
    meta_path = index_dir / "index_meta.json"
    meta = {}
    if meta_path.exists():
        with meta_path.open("r", encoding="utf-8") as f:
            meta = json.load(f)
    return docs, embeddings, meta


def bm25_scores(docs: list[dict], query: str, k1: float = 1.5, b: float = 0.75) -> dict[str, float]:
    query_terms = tokenize(query)
    if not query_terms:
        return {doc["id"]: 0.0 for doc in docs}

    doc_tokens = {doc["id"]: doc.get("tokens") or tokenize(f"{doc.get('title', '')} {doc.get('content', '')}") for doc in docs}
    doc_lengths = {doc_id: len(tokens) for doc_id, tokens in doc_tokens.items()}
    avgdl = sum(doc_lengths.values()) / max(1, len(doc_lengths))

    df = {}
    for term in set(query_terms):
        df[term] = sum(1 for tokens in doc_tokens.values() if term in tokens)

    total_docs = len(docs)
    scores = {}
    for doc in docs:
        doc_id = doc["id"]
        tokens = doc_tokens[doc_id]
        term_counts = {}
        for token in tokens:
            term_counts[token] = term_counts.get(token, 0) + 1

        score = 0.0
        for term in query_terms:
            tf = term_counts.get(term, 0)
            if tf == 0:
                continue
            idf = math.log(1 + (total_docs - df.get(term, 0) + 0.5) / (df.get(term, 0) + 0.5))
            denom = tf + k1 * (1 - b + b * doc_lengths[doc_id] / max(avgdl, 1))
            score += idf * (tf * (k1 + 1)) / denom
        scores[doc_id] = score
    return scores


def normalize_scores(scores: dict[str, float]) -> dict[str, float]:
    if not scores:
        return {}
    values = list(scores.values())
    min_value = min(values)
    max_value = max(values)
    if max_value == min_value:
        return {key: 0.0 for key in scores}
    return {key: (value - min_value) / (max_value - min_value) for key, value in scores.items()}


def retrieve(
    client: OpenAI,
    docs: list[dict],
    embeddings: dict,
    query: str,
    embedding_model: str,
    top_k: int,
    bm25_weight: float,
) -> list[dict]:
    response = client.embeddings.create(model=embedding_model, input=[query])
    query_embedding = response.data[0].embedding

    semantic_scores = {}
    for doc in docs:
        vector = embeddings.get(doc["id"])
        semantic_scores[doc["id"]] = cosine_similarity(query_embedding, vector) if vector else 0.0

    keyword_scores = bm25_scores(docs, query)
    semantic_norm = normalize_scores(semantic_scores)
    keyword_norm = normalize_scores(keyword_scores)

    ranked = []
    doc_by_id = {doc["id"]: doc for doc in docs}
    for doc_id in doc_by_id:
        score = bm25_weight * keyword_norm.get(doc_id, 0.0) + (1 - bm25_weight) * semantic_norm.get(doc_id, 0.0)
        doc = dict(doc_by_id[doc_id])
        doc["score"] = score
        doc["bm25_score"] = keyword_scores.get(doc_id, 0.0)
        doc["semantic_score"] = semantic_scores.get(doc_id, 0.0)
        ranked.append(doc)

    ranked.sort(key=lambda item: item["score"], reverse=True)
    return ranked[:top_k]


def format_context(results: list[dict]) -> str:
    blocks = []
    for index, doc in enumerate(results, start=1):
        source = doc.get("source", {})
        blocks.append(
            f"[{index}]\n"
            f"Document type: {doc.get('type')}\n"
            f"Title: {doc.get('title')}\n"
            f"Paper file: {source.get('paper_file', '')}\n"
            f"Task: {source.get('task_description', '')}\n"
            f"Dataset: {source.get('dataset_title', '')}\n"
            f"Dataset link: {source.get('dataset_link', '')}\n"
            f"Content:\n{doc.get('content', '')}"
        )
    return "\n\n".join(blocks)


def merge_results(result_groups: list[tuple[str, list[dict]]], limit: int) -> list[dict]:
    merged = {}
    for stage_label, results in result_groups:
        for doc in results:
            doc_id = doc["id"]
            if doc_id not in merged or doc.get("score", 0) > merged[doc_id].get("score", 0):
                merged[doc_id] = dict(doc)
                merged[doc_id]["matched_stages"] = []
            if stage_label not in merged[doc_id]["matched_stages"]:
                merged[doc_id]["matched_stages"].append(stage_label)

    ranked = list(merged.values())
    ranked.sort(key=lambda item: item.get("score", 0), reverse=True)
    return ranked[:limit]


def retrieve_by_subtasks(
    client: OpenAI,
    docs: list[dict],
    embeddings: dict,
    plan: dict,
    embedding_model: str,
    stage_top_k: int,
    final_top_k: int,
    bm25_weight: float,
) -> list[dict]:
    groups = []
    for stage_label, query in subtask_queries(plan):
        groups.append(
            (
                stage_label,
                retrieve(client, docs, embeddings, query, embedding_model, stage_top_k, bm25_weight),
            )
        )
    return merge_results(groups, final_top_k)


def expanded_question_with_plan(question: str, plan: dict | None) -> str:
    if not plan:
        return question
    return (
        f"用户原始问题：{question}\n\n"
        f"请先依据下面的最小必要数据需求子任务组织答案，再结合检索证据推荐对应数据集。\n"
        f"{format_subtask_plan(plan)}"
    )
def generate_answer(client: OpenAI, model: str, query: str, results: list[dict]) -> str:
    context = format_context(results)
    response = client.chat.completions.create(
        model=model,
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": (
                    "你是一个材料科学论文数据集 Wiki 助手。"
                    "只能依据给定检索证据回答问题，不要编造论文、任务、数据集或链接。"
                    "如果用户问题中包含最小必要数据需求子任务，请按子任务组织答案。"
                    "每个子任务需要说明：子任务目标、所需数据、匹配到的数据集/论文证据、这些数据如何支持该子任务。"
                    "回答使用中文，并在关键结论后使用 [1]、[2] 这样的引用编号。"
                    "如果证据不足，请明确说明不足。"
                ),
            },
            {
                "role": "user",
                "content": f"问题：{query}\n\n检索证据：\n{context}",
            },
        ],
    )
    return response.choices[0].message.content.strip()

def print_references(results: list[dict]):
    print("\n参考来源：")
    for index, doc in enumerate(results, start=1):
        source = doc.get("source", {})
        paper_file = source.get("paper_file", "")
        dataset = source.get("dataset_title", "")
        task = source.get("task_description", "")
        print(f"[{index}] {doc.get('type')} | {doc.get('title')}")
        if paper_file:
            print(f"    Paper: {paper_file}")
        if task:
            print(f"    Task: {task[:220]}{'...' if len(task) > 220 else ''}")
        if dataset:
            print(f"    Dataset: {dataset}")
        if source.get("dataset_link"):
            print(f"    Link: {source.get('dataset_link')}")


def parse_args():
    parser = argparse.ArgumentParser(description="Ask the local paper-task-dataset LLM Wiki.")
    parser.add_argument("question", nargs="*", help="Question to ask. If omitted, interactive mode starts.")
    parser.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--bm25-weight", type=float, default=0.35)
    parser.add_argument("--chat-model", default=os.getenv("QWEN_MODEL", DEFAULT_CHAT_MODEL))
    parser.add_argument("--embedding-model", default=os.getenv("QWEN_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL))
    parser.add_argument("--show-context", action="store_true", help="Print retrieved evidence before the answer.")
    parser.add_argument("--no-normalize-query", action="store_true", help="Disable minimal-subtask query normalization.")
    parser.add_argument("--stage-top-k", type=int, default=5, help="Evidence count retrieved for each minimal subtask.")
    parser.add_argument("--show-plan", action="store_true", help="Deprecated: the normalized minimal subtasks are printed by default.")
    parser.add_argument("--hide-plan", action="store_true", help="Do not print the normalized minimal subtasks before answering.")
    return parser.parse_args()


def ask_once(client: OpenAI, args, docs: list[dict], embeddings: dict, question: str):
    normalized_plan = None
    if args.no_normalize_query:
        results = retrieve(client, docs, embeddings, question, args.embedding_model, args.top_k, args.bm25_weight)
    else:
        try:
            normalized_plan = normalize_user_query_v2(client, args.chat_model, question)
        except Exception as exc:
            print(f"Query normalization failed, using fallback plan: {exc}")
            normalized_plan = fallback_normalization(question)

        if not args.hide_plan:
            print(format_subtask_plan(normalized_plan))
            print()

        results = retrieve_by_subtasks(
            client,
            docs,
            embeddings,
            normalized_plan,
            args.embedding_model,
            args.stage_top_k,
            args.top_k,
            args.bm25_weight,
        )

    if args.show_context:
        print("检索证据：")
        for index, doc in enumerate(results, start=1):
            stages = f" stages={','.join(doc.get('matched_stages', []))}" if doc.get("matched_stages") else ""
            print(f"[{index}] score={doc['score']:.3f} type={doc['type']} title={doc['title']}{stages}")
        print()

    answer_query = expanded_question_with_plan(question, normalized_plan)
    answer = generate_answer(client, args.chat_model, answer_query, results)
    print(answer)
    print_references(results)
def main():
    load_dotenv()
    args = parse_args()

    api_key = os.getenv("QWEN_API_KEY")
    if not api_key:
        raise ValueError("Please set QWEN_API_KEY in .env.")

    base_url = os.getenv("QWEN_BASE_URL", DEFAULT_BASE_URL)
    docs, embeddings, meta = load_index(args.index_dir)
    if meta.get("embedding_model"):
        args.embedding_model = meta["embedding_model"]

    client = OpenAI(api_key=api_key, base_url=base_url)
    question = " ".join(args.question).strip()

    if question:
        ask_once(client, args, docs, embeddings, question)
        return

    print("进入 LLM Wiki 问答模式。输入问题后回车，输入 exit 退出。")
    while True:
        question = input("\nQuestion> ").strip()
        if question.lower() in {"exit", "quit", "q"}:
            break
        if not question:
            continue
        ask_once(client, args, docs, embeddings, question)


if __name__ == "__main__":
    main()





