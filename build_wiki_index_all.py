import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


DEFAULT_INPUT = Path("outputs/all_results.json")
DEFAULT_WIKI_DIR = Path("llm_wiki_all")
DEFAULT_OUTPUT_DIR = Path("wiki_index_all")
DEFAULT_EMBEDDING_MODEL = "text-embedding-v4"
DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def stable_id(prefix: str, *parts: str) -> str:
    raw = "||".join((part or "").strip().lower() for part in parts)
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]
    return f"{prefix}_{digest}"


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean_text(value) -> str:
    if value is None:
        return ""
    text = str(value).replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def canonical_dataset_title(title: str) -> str:
    title = clean_text(title)
    normalized = title.lower()
    normalized = normalized.replace("&", " and ")
    normalized = re.sub(r"[\u2010-\u2015]", "-", normalized)
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    normalized = re.sub(r"\bthe\b", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()

    if re.fullmatch(r"qm9", normalized):
        return "QM9"
    if re.fullmatch(r"matbench(?: v0 1)?", normalized):
        return "Matbench"
    if re.fullmatch(r"matbench dielectric(?: task)?", normalized):
        return "matbench_dielectric"
    if re.fullmatch(r"computational 2d materials database c2db|c2db computational 2d materials database|c2db", normalized):
        return "C2DB"
    if re.fullmatch(r"wang botti marques wbm dataset|wang botti marques dataset|wbm dataset", normalized):
        return "Wang-Botti-Marques (WBM) dataset"
    if re.fullmatch(r"hybrid organic inorganic perovskite hoip dataset|hybrid organic inorganic perovskite dataset|hoip dataset|hoip dataset hybrid organic inorganic perovskite dataset", normalized):
        return "HOIP Dataset"
    if re.fullmatch(r"jarvis dft(?: dataset)?(?: 3d 2021| 2021 8 18)?|jarvis dft 3d 2021", normalized):
        return "JARVIS-DFT"
    if re.fullmatch(r"jarvis 3d", normalized):
        return "JARVIS-DFT"

    known_aliases = [
        (
            "Materials Project",
            [
                "materials project",
                "materials project database",
                "materials project dataset",
                "materials project mp",
                "materials project mp database",
                "materials project mp dataset",
                "materials project mp 2018 6 1",
                "materials project 2018 6 1",
                "materials project 2021",
                "materials project 2021 snapshot",
                "materials project 2021 mp21",
                "materials project mp21",
                "materials project mp 2022 10 28",
                "materials project mp v 2022 10 28",
                "materials project mp 2023 6 23",
                "materials project mp database 2023 6 23",
                "materials project megnet",
            ],
        ),
        (
            "Open Quantum Materials Database",
            [
                "oqmd",
                "oqmd exp",
                "open quantum materials database",
                "open quantum materials database oqmd",
                "oqmd open quantum materials database",
                "open quantum materials database oqmd 2021 snapshot",
            ],
        ),
        (
            "Inorganic Crystal Structure Database",
            [
                "icsd",
                "icsd database",
                "icsd inorganic crystal structure database",
                "inorganic crystal structure database",
                "inorganic crystal structure database icsd",
            ],
        ),
        (
            "JARVIS Database",
            [
                "jarvis",
                "jarvis database",
                "jarvis dataset",
                "jarvis tools datasets",
                "joint automated repository for various integrated simulations",
                "jarvis joint automated repository for various integrated simulations",
                "joint automated repository for various integrated simulations jarvis",
            ],
        ),
    ]

    for canonical, aliases in known_aliases:
        if normalized in aliases:
            return canonical

    title = re.sub(r"^\s*the\s+", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def tokenize(text: str) -> list[str]:
    text = text.lower()
    return re.findall(r"[a-z0-9]+|[\u4e00-\u9fff]", text)


def make_document(doc_id: str, doc_type: str, title: str, content: str, source: dict) -> dict:
    content = clean_text(content)
    return {
        "id": doc_id,
        "type": doc_type,
        "title": clean_text(title),
        "content": content,
        "tokens": tokenize(f"{title} {content}"),
        "source": source,
    }


def directory_hash(path: Path) -> str:
    digest = hashlib.sha256()
    for file_path in sorted(path.rglob("*.md")):
        digest.update(str(file_path.relative_to(path)).replace("\\", "/").encode("utf-8"))
        digest.update(b"\0")
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                digest.update(chunk)
        digest.update(b"\0")
    return digest.hexdigest()


def title_from_markdown(text: str, fallback: str) -> str:
    for line in text.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return clean_text(match.group(1))
    return fallback


def doc_type_from_page(relative_path: Path) -> str:
    parts = relative_path.parts
    if relative_path.name == "index.md":
        return "wiki_index"
    if len(parts) >= 2 and parts[0] in {"papers", "tasks", "datasets", "dataset_uses"}:
        return parts[0].removesuffix("s")
    return "wiki_page"


def extract_source_from_markdown(relative_path: Path, text: str) -> dict:
    source = {
        "wiki_page": relative_path.as_posix(),
    }
    paper_match = re.search(r"- Paper file: `([^`]+)`", text)
    if paper_match:
        source["paper_file"] = paper_match.group(1)

    dataset_url_match = re.search(r"- Dataset URL: ([^\n]+)", text)
    if dataset_url_match:
        source["dataset_link"] = clean_text(dataset_url_match.group(1))

    original_title_match = re.search(r"- Original dataset title: ([^\n]+)", text)
    if original_title_match:
        source["original_dataset_title"] = clean_text(original_title_match.group(1))

    dataset_id_match = re.search(r"- Dataset ID: `([^`]+)`", text)
    if dataset_id_match:
        source["dataset_id"] = dataset_id_match.group(1)

    task_id_match = re.search(r"- Task ID: `([^`]+)`", text)
    if task_id_match:
        source["task_id"] = task_id_match.group(1)

    dataset_use_id_match = re.search(r"- Dataset use ID: `([^`]+)`", text)
    if dataset_use_id_match:
        source["dataset_use_id"] = dataset_use_id_match.group(1)

    return source


def build_documents_from_wiki(wiki_dir: Path) -> list[dict]:
    pages_dir = wiki_dir / "pages"
    if not pages_dir.exists():
        raise FileNotFoundError(f"Wiki pages directory not found: {pages_dir}")

    docs = []
    for page_path in sorted(pages_dir.rglob("*.md")):
        relative_path = page_path.relative_to(pages_dir)
        text = page_path.read_text(encoding="utf-8")
        title = title_from_markdown(text, page_path.stem)
        doc_type = doc_type_from_page(relative_path)
        source = extract_source_from_markdown(relative_path, text)
        doc_id = stable_id("wiki_page", relative_path.as_posix(), text)
        docs.append(make_document(doc_id, doc_type, title, text, source))

    return docs


def build_documents(records: list[dict]) -> list[dict]:
    docs = []
    dataset_docs = {}

    for paper_record in records:
        paper_file = clean_text(paper_record.get("paper_file"))
        if not paper_file:
            continue

        paper_title = Path(paper_file).stem.replace("_", " ")
        tasks = paper_record.get("result", [])
        if not isinstance(tasks, list):
            continue

        paper_task_summaries = []

        for task_index, task in enumerate(tasks, start=1):
            if not isinstance(task, dict):
                continue

            task_description = clean_text(task.get("task_description"))
            if not task_description:
                continue

            task_tags = task.get("task_tags", [])
            if not isinstance(task_tags, list):
                task_tags = []
            task_tags = [clean_text(tag) for tag in task_tags if clean_text(tag)]
            task_id = stable_id("task", paper_file, str(task_index), task_description)

            datasets = task.get("datasets", [])
            if not isinstance(datasets, list):
                datasets = []

            dataset_titles = []
            dataset_blocks = []
            for dataset in datasets:
                if not isinstance(dataset, dict):
                    continue

                raw_title = clean_text(dataset.get("db_title"))
                if not raw_title:
                    continue

                dataset_title = canonical_dataset_title(raw_title)
                dataset_description = clean_text(dataset.get("db_description"))
                dataset_link = clean_text(dataset.get("db_link")) or "None"
                dataset_titles.append(dataset_title)
                dataset_blocks.append(
                    f"Dataset: {dataset_title}\n"
                    f"Original dataset title: {raw_title}\n"
                    f"Dataset link: {dataset_link}\n"
                    f"Dataset description and task role: {dataset_description}"
                )

                dataset_id = stable_id("dataset", dataset_title)
                dataset_source = {
                    "paper_file": paper_file,
                    "task_id": task_id,
                    "task_description": task_description,
                    "task_tags": task_tags,
                    "dataset_title": dataset_title,
                    "original_dataset_title": raw_title,
                    "dataset_link": dataset_link,
                }
                dataset_content = (
                    f"Dataset name: {dataset_title}\n"
                    f"Alias in paper: {raw_title}\n"
                    f"Used by paper: {paper_file}\n"
                    f"Related task: {task_description}\n"
                    f"Task tags: {'; '.join(task_tags)}\n"
                    f"Dataset content and role: {dataset_description}\n"
                    f"Dataset link: {dataset_link}"
                )
                doc_id = stable_id("dataset_use", paper_file, task_id, dataset_title, dataset_description)
                dataset_docs[doc_id] = make_document(
                    doc_id,
                    "dataset_use",
                    f"{dataset_title} used in {paper_title}",
                    dataset_content,
                    dataset_source,
                )

            task_content = (
                f"Paper: {paper_file}\n"
                f"Task: {task_description}\n"
                f"Task tags: {'; '.join(task_tags)}\n"
                f"Datasets used: {'; '.join(dataset_titles) if dataset_titles else 'None'}\n"
                f"{chr(10).join(dataset_blocks)}"
            )
            docs.append(
                make_document(
                    task_id,
                    "task",
                    f"{paper_title} - task {task_index}",
                    task_content,
                    {
                        "paper_file": paper_file,
                        "task_id": task_id,
                        "task_description": task_description,
                        "task_tags": task_tags,
                        "dataset_titles": dataset_titles,
                    },
                )
            )
            paper_task_summaries.append(
                f"Task {task_index}: {task_description}\n"
                f"Tags: {'; '.join(task_tags)}\n"
                f"Datasets: {'; '.join(dataset_titles) if dataset_titles else 'None'}"
            )

        if paper_task_summaries:
            paper_id = stable_id("paper", paper_file)
            docs.append(
                make_document(
                    paper_id,
                    "paper",
                    paper_title,
                    f"Paper: {paper_file}\n" + "\n\n".join(paper_task_summaries),
                    {"paper_file": paper_file},
                )
            )

    docs.extend(dataset_docs.values())
    docs.sort(key=lambda doc: (doc["type"], doc["title"], doc["id"]))
    return docs


def embed_texts(client: OpenAI, model: str, texts: list[str], batch_size: int, sleep_seconds: float) -> list[list[float]]:
    vectors = []
    for start in range(0, len(texts), batch_size):
        batch = texts[start : start + batch_size]
        response = client.embeddings.create(model=model, input=batch)
        vectors.extend(item.embedding for item in response.data)
        if sleep_seconds and start + batch_size < len(texts):
            time.sleep(sleep_seconds)
    return vectors


def parse_args():
    parser = argparse.ArgumentParser(description="Build a local retrieval index from LLM Wiki Markdown pages.")
    parser.add_argument("--wiki-dir", type=Path, default=DEFAULT_WIKI_DIR, help="Path to the generated llm_wiki directory.")
    parser.add_argument("--input", type=Path, default=None, help="Legacy mode: path to extraction JSON.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directory for wiki index files.")
    parser.add_argument("--embedding-model", default=os.getenv("QWEN_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL))
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--sleep", type=float, default=0.0, help="Seconds to sleep between embedding batches.")
    parser.add_argument("--force", action="store_true", help="Rebuild embeddings even if the source hash is unchanged.")
    return parser.parse_args()


def main():
    load_dotenv()
    args = parse_args()

    api_key = os.getenv("QWEN_API_KEY")
    if not api_key:
        raise ValueError("Please set QWEN_API_KEY in .env before building the embedding index.")

    base_url = os.getenv("QWEN_BASE_URL", DEFAULT_BASE_URL)
    if args.input:
        if not args.input.exists():
            raise FileNotFoundError(f"Input JSON not found: {args.input}")
        source = str(args.input)
        source_type = "json"
        source_hash = file_hash(args.input)
    else:
        pages_dir = args.wiki_dir / "pages"
        if not pages_dir.exists():
            raise FileNotFoundError(f"Wiki pages directory not found: {pages_dir}")
        source = str(pages_dir)
        source_type = "llm_wiki_pages"
        source_hash = directory_hash(pages_dir)

    meta_path = args.output_dir / "index_meta.json"

    if meta_path.exists() and not args.force:
        with meta_path.open("r", encoding="utf-8") as f:
            old_meta = json.load(f)
        if (
            old_meta.get("source_hash") == source_hash
            and old_meta.get("embedding_model") == args.embedding_model
            and old_meta.get("source_type") == source_type
        ):
            print("Index source is unchanged. Use --force to rebuild embeddings.")
            print(f"Index directory: {args.output_dir}")
            return

    if args.input:
        with args.input.open("r", encoding="utf-8") as f:
            records = json.load(f)
        if not isinstance(records, list):
            raise ValueError("Input JSON must be a list of paper records.")
        docs = build_documents(records)
    else:
        docs = build_documents_from_wiki(args.wiki_dir)

    if not docs:
        raise ValueError("No wiki documents were generated from the selected source.")

    client = OpenAI(api_key=api_key, base_url=base_url)
    texts = [f"{doc['title']}\n{doc['content']}" for doc in docs]
    vectors = embed_texts(client, args.embedding_model, texts, args.batch_size, args.sleep)

    embeddings = {doc["id"]: vector for doc, vector in zip(docs, vectors)}
    args.output_dir.mkdir(parents=True, exist_ok=True)

    with (args.output_dir / "documents.json").open("w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False, indent=2)
    with (args.output_dir / "embeddings.json").open("w", encoding="utf-8") as f:
        json.dump(embeddings, f)
    with meta_path.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "source": source,
                "source_type": source_type,
                "source_hash": source_hash,
                "document_count": len(docs),
                "embedding_model": args.embedding_model,
                "base_url": base_url,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    type_counts = {}
    for doc in docs:
        type_counts[doc["type"]] = type_counts.get(doc["type"], 0) + 1

    print(f"Wiki index built from: {source}")
    print(f"Source type: {source_type}")
    print(f"Output directory: {args.output_dir}")
    print(f"Documents: {len(docs)} {type_counts}")
    print(f"Embedding model: {args.embedding_model}")


if __name__ == "__main__":
    main()
