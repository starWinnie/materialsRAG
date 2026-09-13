import argparse
import csv
import os
import sys
from collections import defaultdict
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from ask_wiki import (
    DEFAULT_BASE_URL,
    DEFAULT_CHAT_MODEL,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_INDEX_DIR,
    expanded_question_with_plan,
    generate_answer,
    load_index,
    print_references,
    retrieve,
    retrieve_by_subtasks,
)
from normalize_query_v2 import (
    fallback_normalization,
    format_subtask_plan,
    normalize_user_query_v2,
)


DEFAULT_WIKI_DIR = Path("llm_wiki_80")
ENTITY_BONUS = {
    "dataset_use": 0.25,
    "task": 0.20,
    "dataset": 0.15,
    "paper": 0.08,
    "stage": 0.10,
}
TYPE_BONUS = {
    "dataset_use": 0.20,
    "task": 0.10,
    "dataset": 0.08,
    "paper": 0.03,
}


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def _clean(value) -> str:
    return str(value or "").strip()


def _split_semicolon(value) -> list[str]:
    return [item.strip() for item in _clean(value).split(";") if item.strip()]


def _entity(kind: str, value: str) -> str | None:
    value = _clean(value)
    if not value or value.lower() == "none":
        return None
    return f"{kind}:{value.lower()}"


def _add_entity(mapping: dict[str, set[str]], key: str | None, value: str):
    if key:
        mapping[key].add(value)


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _connect(relations: dict[str, set[str]], keys: list[str | None]):
    clean_keys = [key for key in keys if key]
    for key in clean_keys:
        relations[key].update(other for other in clean_keys if other != key)


def _doc_entities_from_source(doc: dict) -> set[str]:
    source = doc.get("source", {}) or {}
    entities = set()
    for key in [
        _entity("dataset_use", source.get("dataset_use_id")),
        _entity("dataset", source.get("dataset_id")),
        _entity("task", source.get("task_id")),
        _entity("paper_file", source.get("paper_file")),
    ]:
        if key:
            entities.add(key)
    return entities


def load_relation_index(docs: list[dict], wiki_dir: Path) -> dict:
    """Build a light typed-relationship index from existing Wiki raw CSV files."""
    raw_dir = wiki_dir / "raw"
    dataset_uses = _read_csv(raw_dir / "dataset_use_stages.csv") or _read_csv(raw_dir / "dataset_uses.csv")
    tasks = _read_csv(raw_dir / "task_stages.csv") or _read_csv(raw_dir / "tasks.csv")
    papers = _read_csv(raw_dir / "papers.csv")

    doc_entities: dict[str, set[str]] = {}
    entity_docs: dict[str, set[str]] = defaultdict(set)
    entity_relations: dict[str, set[str]] = defaultdict(set)
    paper_file_to_id = {}

    for row in papers:
        paper_id = _clean(row.get("paper_id"))
        paper_file = _clean(row.get("paper_file"))
        if paper_id and paper_file:
            paper_file_to_id[paper_file.lower()] = paper_id

    task_to_row = {}
    dataset_use_to_row = {}

    for row in tasks:
        paper_id = _clean(row.get("paper_id"))
        task_id = _clean(row.get("task_id"))
        task_to_row[task_id] = row
        keys = [
            _entity("task", task_id),
            _entity("paper", paper_id),
            _entity("paper_file", row.get("paper_file")),
        ]
        for dataset_id in _split_semicolon(row.get("dataset_ids")):
            keys.append(_entity("dataset", dataset_id))
        for stage in _split_semicolon(row.get("rd_stages")):
            keys.append(_entity("stage", stage))
        _connect(entity_relations, keys)

    for row in dataset_uses:
        dataset_use_id = _clean(row.get("dataset_use_id"))
        dataset_use_to_row[dataset_use_id] = row
        keys = [
            _entity("dataset_use", dataset_use_id),
            _entity("paper", row.get("paper_id")),
            _entity("paper_file", row.get("paper_file")),
            _entity("task", row.get("task_id")),
            _entity("dataset", row.get("dataset_id")),
            _entity("dataset_title", row.get("db_title")),
            _entity("dataset_title", row.get("original_db_title")),
        ]
        for stage in _split_semicolon(row.get("rd_stages")):
            keys.append(_entity("stage", stage))
        _connect(entity_relations, keys)

    for doc in docs:
        doc_id = doc["id"]
        entities = _doc_entities_from_source(doc)
        source = doc.get("source", {}) or {}

        paper_file_key = _entity("paper_file", source.get("paper_file"))
        if paper_file_key:
            paper_id = paper_file_to_id.get(_clean(source.get("paper_file")).lower())
            if paper_id:
                entities.add(_entity("paper", paper_id))

        dataset_use_id = _clean(source.get("dataset_use_id"))
        if dataset_use_id in dataset_use_to_row:
            row = dataset_use_to_row[dataset_use_id]
            entities.update(
                key
                for key in [
                    _entity("paper", row.get("paper_id")),
                    _entity("paper_file", row.get("paper_file")),
                    _entity("task", row.get("task_id")),
                    _entity("dataset", row.get("dataset_id")),
                    _entity("dataset_title", row.get("db_title")),
                    _entity("dataset_title", row.get("original_db_title")),
                ]
                if key
            )
            for stage in _split_semicolon(row.get("rd_stages")):
                entities.add(_entity("stage", stage))

        task_id = _clean(source.get("task_id"))
        if task_id in task_to_row:
            row = task_to_row[task_id]
            entities.update(
                key
                for key in [
                    _entity("paper", row.get("paper_id")),
                    _entity("paper_file", row.get("paper_file")),
                    _entity("task", task_id),
                ]
                if key
            )
            for dataset_id in _split_semicolon(row.get("dataset_ids")):
                entities.add(_entity("dataset", dataset_id))
            for stage in _split_semicolon(row.get("rd_stages")):
                entities.add(_entity("stage", stage))

        doc_entities[doc_id] = entities
        for entity in entities:
            entity_docs[entity].add(doc_id)

    return {
        "doc_entities": doc_entities,
        "entity_docs": entity_docs,
        "entity_relations": entity_relations,
        "doc_by_id": {doc["id"]: doc for doc in docs},
    }


def plan_stage_entities(plan: dict | None) -> set[str]:
    stages = set()
    if not plan:
        return stages
    for subtask in plan.get("minimal_subtasks", []):
        stage = _entity("stage", subtask.get("related_rd_stage"))
        if stage:
            stages.add(stage)
    return stages


def entity_kind(entity: str) -> str:
    return entity.split(":", 1)[0]


def same_entity_bonus(entity: str) -> float:
    return ENTITY_BONUS.get(entity_kind(entity), 0.05)


def related_entity_bonus(entity: str) -> float:
    return same_entity_bonus(entity) * 0.65


def graph_expand_and_rerank(
    seed_results: list[dict],
    relation_index: dict,
    plan: dict | None,
    final_top_k: int,
) -> list[dict]:
    doc_entities = relation_index["doc_entities"]
    entity_docs = relation_index["entity_docs"]
    entity_relations = relation_index["entity_relations"]
    doc_by_id = relation_index["doc_by_id"]
    expected_stages = plan_stage_entities(plan)

    candidates = {}

    def touch(doc_id: str, inherited_score: float, relation_bonus: float, path: str):
        if doc_id not in doc_by_id:
            return
        state = candidates.setdefault(
            doc_id,
            {
                "base_score": 0.0,
                "relation_bonus": 0.0,
                "matched_paths": set(),
                "seed_hits": 0,
            },
        )
        state["base_score"] = max(state["base_score"], inherited_score)
        state["relation_bonus"] = max(state["relation_bonus"], relation_bonus)
        state["matched_paths"].add(path)

    for seed in seed_results:
        seed_id = seed["id"]
        seed_score = float(seed.get("score", 0.0))
        seed_entities = doc_entities.get(seed_id, set())
        touch(seed_id, seed_score, 0.0, "seed")
        candidates[seed_id]["seed_hits"] += 1

        for entity in seed_entities:
            for doc_id in entity_docs.get(entity, set()):
                touch(doc_id, seed_score * 0.80, same_entity_bonus(entity), f"same {entity_kind(entity)}")

            for related in entity_relations.get(entity, set()):
                for doc_id in entity_docs.get(related, set()):
                    touch(
                        doc_id,
                        seed_score * 0.55,
                        related_entity_bonus(related),
                        f"{entity_kind(entity)}->{entity_kind(related)}",
                    )

    ranked = []
    for doc_id, state in candidates.items():
        doc = dict(doc_by_id[doc_id])
        doc_type = doc.get("type", "")
        doc_stage_entities = {entity for entity in doc_entities.get(doc_id, set()) if entity.startswith("stage:")}
        stage_bonus = 0.10 if expected_stages and (expected_stages & doc_stage_entities) else 0.0
        type_bonus = TYPE_BONUS.get(doc_type, 0.0)
        multi_seed_bonus = min(0.12, 0.03 * max(0, state["seed_hits"] - 1))
        graph_score = state["relation_bonus"] + stage_bonus + type_bonus + multi_seed_bonus
        final_score = state["base_score"] + graph_score

        doc["original_score"] = state["base_score"]
        doc["graph_score"] = graph_score
        doc["relation_bonus"] = state["relation_bonus"]
        doc["stage_bonus"] = stage_bonus
        doc["type_bonus"] = type_bonus
        doc["score"] = final_score
        doc["matched_paths"] = sorted(state["matched_paths"])
        ranked.append(doc)

    ranked.sort(key=lambda item: item.get("score", 0.0), reverse=True)
    return ranked[:final_top_k]


def parse_args():
    parser = argparse.ArgumentParser(description="Ask the local LLM Wiki with light graph-aware reranking.")
    parser.add_argument("question", nargs="*", help="Question to ask. If omitted, interactive mode starts.")
    parser.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    parser.add_argument("--wiki-dir", type=Path, default=DEFAULT_WIKI_DIR)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--seed-top-k", type=int, default=30, help="Text-retrieval candidates before graph reranking.")
    parser.add_argument("--bm25-weight", type=float, default=0.35)
    parser.add_argument("--chat-model", default=os.getenv("QWEN_MODEL", DEFAULT_CHAT_MODEL))
    parser.add_argument("--embedding-model", default=os.getenv("QWEN_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL))
    parser.add_argument("--show-context", action="store_true", help="Print reranked evidence before the answer.")
    parser.add_argument("--no-normalize-query", action="store_true", help="Disable minimal-subtask query normalization.")
    parser.add_argument("--stage-top-k", type=int, default=8, help="Evidence count retrieved for each minimal subtask.")
    parser.add_argument("--hide-plan", action="store_true", help="Do not print the normalized minimal subtasks before answering.")
    parser.add_argument("--no-graph-rerank", action="store_true", help="Disable relation-aware expansion and reranking.")
    return parser.parse_args()


def ask_once(client: OpenAI, args, docs: list[dict], embeddings: dict, relation_index: dict, question: str):
    normalized_plan = None
    seed_top_k = max(args.seed_top_k, args.top_k)

    if args.no_normalize_query:
        seed_results = retrieve(client, docs, embeddings, question, args.embedding_model, seed_top_k, args.bm25_weight)
    else:
        try:
            normalized_plan = normalize_user_query_v2(client, args.chat_model, question)
        except Exception as exc:
            print(f"Query normalization failed, using fallback plan: {exc}")
            normalized_plan = fallback_normalization(question)

        if not args.hide_plan:
            print(format_subtask_plan(normalized_plan))
            print()

        seed_results = retrieve_by_subtasks(
            client,
            docs,
            embeddings,
            normalized_plan,
            args.embedding_model,
            args.stage_top_k,
            seed_top_k,
            args.bm25_weight,
        )

    if args.no_graph_rerank:
        results = seed_results[: args.top_k]
    else:
        results = graph_expand_and_rerank(seed_results, relation_index, normalized_plan, args.top_k)

    if args.show_context:
        print("妫€绱㈣瘉鎹細")
        for index, doc in enumerate(results, start=1):
            paths = ",".join(doc.get("matched_paths", []))
            print(
                f"[{index}] score={doc['score']:.3f} original={doc.get('original_score', doc['score']):.3f} "
                f"graph={doc.get('graph_score', 0):.3f} type={doc['type']} title={doc['title']} paths={paths}"
            )
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

    relation_index = load_relation_index(docs, args.wiki_dir)
    client = OpenAI(api_key=api_key, base_url=base_url)
    question = " ".join(args.question).strip()

    if question:
        ask_once(client, args, docs, embeddings, relation_index, question)
        return

    print("Graph-aware LLM Wiki QA mode. Type exit to quit.")
    while True:
        question = input("\nQuestion> ").strip()
        if question.lower() in {"exit", "quit", "q"}:
            break
        if not question:
            continue
        ask_once(client, args, docs, embeddings, relation_index, question)


if __name__ == "__main__":
    main()

