import argparse
import csv
import hashlib
import json
import re
import shutil
from pathlib import Path


DEFAULT_INPUT = Path("outputs/80results.json")
DEFAULT_OUTPUT_DIR = Path("llm_wiki_80")

# DEFAULT_INPUT = Path("outputs/all_results.json")
# DEFAULT_OUTPUT_DIR = Path("llm_wiki_all")


SCHEMA_TEXT = """# LLM Wiki Schema

version: 1
source: outputs/80results.json

layers:
  raw:
    description: Original and extracted source material used by the wiki.
    files:
      - raw/source_records.json
      - raw/manifest.json
      - raw/papers.csv
      - raw/tasks.csv
      - raw/datasets.csv
      - raw/dataset_uses.csv
  pages:
    description: Human-readable Markdown wiki pages generated from the extracted records.
    directories:
      - pages/papers
      - pages/tasks
      - pages/datasets
      - pages/dataset_uses
  schema:
    description: Knowledge organization rules for entities, relations, and page templates.

entities:
  Paper:
    id: paper_id
    properties:
      - paper_file
      - title
    page: pages/papers/{paper_slug}.md
  Task:
    id: task_id
    properties:
      - task_description
      - task_tags
      - paper_id
    page: pages/tasks/{task_slug}.md
  Dataset:
    id: dataset_id
    properties:
      - db_title
      - aliases
      - links
      - descriptions
    page: pages/datasets/{dataset_slug}.md
  DatasetUse:
    id: dataset_use_id
    properties:
      - paper_id
      - task_id
      - dataset_id
      - db_description
      - db_link
    page: pages/dataset_uses/{dataset_use_slug}.md

relations:
  HAS_TASK:
    from: Paper
    to: Task
  USES_DATASET:
    from: Task
    to: Dataset
  HAS_DATASET_USE:
    from: Task
    to: DatasetUse
  DESCRIBES_DATASET:
    from: DatasetUse
    to: Dataset
  MENTIONS_TAG:
    from: Task
    to: tag string

page_rules:
  Paper:
    purpose: Summarize one source paper, its extracted tasks, and used datasets.
  Task:
    purpose: Describe one research task or intent and list supporting datasets.
  Dataset:
    purpose: Aggregate all mentions/usages of the same real dataset across papers.
  DatasetUse:
    purpose: Preserve paper-specific dataset role and evidence context.
"""


def clean_text(value) -> str:
    if value is None:
        return ""
    text = str(value).replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def stable_id(prefix: str, *parts: str) -> str:
    raw = "||".join((part or "").strip().lower() for part in parts)
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]
    return f"{prefix}_{digest}"


def slugify(value: str, fallback: str) -> str:
    value = clean_text(value)
    value = re.sub(r"[\u2010-\u2015]", "-", value)
    value = re.sub(r"[^\w\u4e00-\u9fff.-]+", "_", value, flags=re.UNICODE)
    value = re.sub(r"_+", "_", value).strip("._ ")
    return value[:90] or fallback


def markdown_escape(value: str) -> str:
    return clean_text(value).replace("|", "\\|")


def markdown_link(label: str, target: str) -> str:
    return f"[{label}]({target.replace(' ', '%20')})"


def paper_title_from_file(paper_file: str) -> str:
    return re.sub(r"\s+", " ", Path(paper_file).stem.replace("_", " ")).strip()


def canonical_dataset_title(title: str) -> str:
    title = clean_text(title)
    normalized = title.lower()
    normalized = normalized.replace("&", " and ")
    normalized = re.sub(r"[\u2010-\u2015]", "-", normalized)
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    normalized = re.sub(r"\bthe\b", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()

    regex_aliases = [
        (r"qm9", "QM9"),
        (r"matbench(?: v0 1)?", "Matbench"),
        (r"matbench dielectric(?: task)?", "matbench_dielectric"),
        (r"computational 2d materials database c2db|c2db computational 2d materials database|c2db", "C2DB"),
        (r"wang botti marques wbm dataset|wang botti marques dataset|wbm dataset", "Wang-Botti-Marques (WBM) dataset"),
        (r"hybrid organic inorganic perovskite hoip dataset|hybrid organic inorganic perovskite dataset|hoip dataset|hoip dataset hybrid organic inorganic perovskite dataset", "HOIP Dataset"),
        (r"jarvis dft(?: dataset)?(?: 3d 2021| 2021 8 18)?|jarvis dft 3d 2021", "JARVIS-DFT"),
        (r"jarvis 3d", "JARVIS-DFT"),
    ]
    for pattern, canonical in regex_aliases:
        if re.fullmatch(pattern, normalized):
            return canonical

    known_aliases = {
        "Materials Project": [
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
        "Open Quantum Materials Database": [
            "oqmd",
            "oqmd exp",
            "open quantum materials database",
            "open quantum materials database oqmd",
            "oqmd open quantum materials database",
            "open quantum materials database oqmd 2021 snapshot",
        ],
        "Inorganic Crystal Structure Database": [
            "icsd",
            "icsd database",
            "icsd inorganic crystal structure database",
            "inorganic crystal structure database",
            "inorganic crystal structure database icsd",
        ],
        "JARVIS Database": [
            "jarvis",
            "jarvis database",
            "jarvis dataset",
            "jarvis tools datasets",
            "joint automated repository for various integrated simulations",
            "jarvis joint automated repository for various integrated simulations",
            "joint automated repository for various integrated simulations jarvis",
        ],
    }
    for canonical, aliases in known_aliases.items():
        if normalized in aliases:
            return canonical

    title = re.sub(r"^\s*the\s+", "", title, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", title).strip()


def read_records(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        records = json.load(f)
    if not isinstance(records, list):
        raise ValueError("Input JSON must be a list of paper records.")
    return records


def build_entities(records: list[dict]) -> dict:
    papers = {}
    tasks = {}
    datasets = {}
    dataset_uses = {}

    for paper_record in records:
        paper_file = clean_text(paper_record.get("paper_file"))
        if not paper_file:
            continue

        paper_id = stable_id("paper", paper_file)
        paper = {
            "paper_id": paper_id,
            "paper_file": paper_file,
            "title": paper_title_from_file(paper_file),
            "task_ids": [],
            "dataset_ids": set(),
            "dataset_use_ids": [],
        }
        papers[paper_id] = paper

        result = paper_record.get("result", [])
        if not isinstance(result, list):
            continue

        for task_index, task_record in enumerate(result, start=1):
            if not isinstance(task_record, dict):
                continue

            task_description = clean_text(task_record.get("task_description"))
            if not task_description:
                continue

            task_id = stable_id("task", paper_file, str(task_index), task_description)
            task_tags = task_record.get("task_tags", [])
            if not isinstance(task_tags, list):
                task_tags = []
            task_tags = [clean_text(tag) for tag in task_tags if clean_text(tag)]

            task = {
                "task_id": task_id,
                "paper_id": paper_id,
                "paper_file": paper_file,
                "task_index": task_index,
                "task_description": task_description,
                "task_tags": task_tags,
                "dataset_ids": [],
                "dataset_use_ids": [],
            }
            tasks[task_id] = task
            paper["task_ids"].append(task_id)

            datasets_raw = task_record.get("datasets", [])
            if not isinstance(datasets_raw, list):
                continue

            for dataset_index, dataset_record in enumerate(datasets_raw, start=1):
                if not isinstance(dataset_record, dict):
                    continue

                raw_title = clean_text(dataset_record.get("db_title"))
                if not raw_title:
                    continue

                canonical_title = canonical_dataset_title(raw_title)
                dataset_id = stable_id("dataset", canonical_title)
                db_description = clean_text(dataset_record.get("db_description"))
                db_link = clean_text(dataset_record.get("db_link")) or "None"
                dataset_use_id = stable_id("dataset_use", paper_id, task_id, dataset_id, str(dataset_index), db_description)

                dataset = datasets.setdefault(
                    dataset_id,
                    {
                        "dataset_id": dataset_id,
                        "db_title": canonical_title,
                        "aliases": set(),
                        "links": set(),
                        "description_examples": [],
                        "paper_ids": set(),
                        "task_ids": set(),
                        "dataset_use_ids": [],
                    },
                )
                dataset["aliases"].add(raw_title)
                if db_link and db_link.lower() != "none":
                    dataset["links"].add(db_link)
                if db_description and len(dataset["description_examples"]) < 5:
                    dataset["description_examples"].append(db_description)
                dataset["paper_ids"].add(paper_id)
                dataset["task_ids"].add(task_id)
                dataset["dataset_use_ids"].append(dataset_use_id)

                dataset_use = {
                    "dataset_use_id": dataset_use_id,
                    "paper_id": paper_id,
                    "task_id": task_id,
                    "dataset_id": dataset_id,
                    "paper_file": paper_file,
                    "task_description": task_description,
                    "task_tags": task_tags,
                    "db_title": canonical_title,
                    "original_db_title": raw_title,
                    "db_description": db_description,
                    "db_link": db_link,
                }
                dataset_uses[dataset_use_id] = dataset_use

                task["dataset_ids"].append(dataset_id)
                task["dataset_use_ids"].append(dataset_use_id)
                paper["dataset_ids"].add(dataset_id)
                paper["dataset_use_ids"].append(dataset_use_id)

    for paper in papers.values():
        paper["dataset_ids"] = sorted(paper["dataset_ids"])
    for dataset in datasets.values():
        dataset["aliases"] = sorted(dataset["aliases"])
        dataset["links"] = sorted(dataset["links"])
        dataset["paper_ids"] = sorted(dataset["paper_ids"])
        dataset["task_ids"] = sorted(dataset["task_ids"])

    return {
        "papers": papers,
        "tasks": tasks,
        "datasets": datasets,
        "dataset_uses": dataset_uses,
    }


def prepare_output_dir(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    for child in ["raw", "pages", "schema"]:
        path = output_dir / child
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)

    for child in ["papers", "tasks", "datasets", "dataset_uses", "tags"]:
        (output_dir / "pages" / child).mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]):
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def write_raw_layer(output_dir: Path, input_path: Path, entities: dict):
    raw_dir = output_dir / "raw"
    shutil.copy2(input_path, raw_dir / "source_records.json")
    manifest = {
        "source_json": str(input_path),
        "copied_source_json": "raw/source_records.json",
        "paper_count": len(entities["papers"]),
        "task_count": len(entities["tasks"]),
        "dataset_count": len(entities["datasets"]),
        "dataset_use_count": len(entities["dataset_uses"]),
        "layers": {
            "raw": "raw/",
            "pages": "pages/",
            "schema": "schema/",
        },
    }
    with (raw_dir / "manifest.json").open("w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    write_csv(
        raw_dir / "papers.csv",
        [
            {
                "paper_id": item["paper_id"],
                "paper_file": item["paper_file"],
                "title": item["title"],
                "task_count": len(item["task_ids"]),
                "dataset_count": len(item["dataset_ids"]),
            }
            for item in entities["papers"].values()
        ],
        ["paper_id", "paper_file", "title", "task_count", "dataset_count"],
    )
    write_csv(
        raw_dir / "tasks.csv",
        [
            {
                "task_id": item["task_id"],
                "paper_id": item["paper_id"],
                "paper_file": item["paper_file"],
                "task_index": item["task_index"],
                "task_description": item["task_description"],
                "task_tags": "; ".join(item["task_tags"]),
                "dataset_ids": "; ".join(item["dataset_ids"]),
            }
            for item in entities["tasks"].values()
        ],
        ["task_id", "paper_id", "paper_file", "task_index", "task_description", "task_tags", "dataset_ids"],
    )
    write_csv(
        raw_dir / "datasets.csv",
        [
            {
                "dataset_id": item["dataset_id"],
                "db_title": item["db_title"],
                "aliases": "; ".join(item["aliases"]),
                "links": "; ".join(item["links"]),
                "paper_count": len(item["paper_ids"]),
                "task_count": len(item["task_ids"]),
                "dataset_use_count": len(item["dataset_use_ids"]),
            }
            for item in entities["datasets"].values()
        ],
        ["dataset_id", "db_title", "aliases", "links", "paper_count", "task_count", "dataset_use_count"],
    )
    write_csv(
        raw_dir / "dataset_uses.csv",
        list(entities["dataset_uses"].values()),
        [
            "dataset_use_id",
            "paper_id",
            "task_id",
            "dataset_id",
            "paper_file",
            "db_title",
            "original_db_title",
            "db_description",
            "db_link",
        ],
    )


def entity_paths(entities: dict) -> dict:
    paths = {"papers": {}, "tasks": {}, "datasets": {}, "dataset_uses": {}}
    for item in entities["papers"].values():
        slug = slugify(item["title"], item["paper_id"])
        paths["papers"][item["paper_id"]] = f"papers/{slug}.md"
    for item in entities["tasks"].values():
        paper_title = paper_title_from_file(item["paper_file"])
        slug = slugify(f"{paper_title}_task_{item['task_index']}", item["task_id"])
        paths["tasks"][item["task_id"]] = f"tasks/{slug}.md"
    for item in entities["datasets"].values():
        slug = slugify(item["db_title"], item["dataset_id"])
        paths["datasets"][item["dataset_id"]] = f"datasets/{slug}.md"
    for item in entities["dataset_uses"].values():
        slug = slugify(f"{Path(item['paper_file']).stem}_{item['db_title']}_{item['dataset_use_id']}", item["dataset_use_id"])
        paths["dataset_uses"][item["dataset_use_id"]] = f"dataset_uses/{slug}.md"
    return paths


def rel_link(from_rel_path: str, to_rel_path: str, label: str) -> str:
    source_dir = Path(from_rel_path).parent
    relative = Path("..") / to_rel_path
    return markdown_link(label, relative.as_posix())


def write_page(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(content.rstrip() + "\n")


def write_pages(output_dir: Path, entities: dict):
    pages_dir = output_dir / "pages"
    paths = entity_paths(entities)

    paper_count = len(entities["papers"])
    task_count = len(entities["tasks"])
    dataset_count = len(entities["datasets"])
    dataset_use_count = len(entities["dataset_uses"])

    index_lines = [
        "# LLM Wiki",
        "",
        "This wiki is generated from extracted paper-task-dataset records.",
        "",
        "## Overview",
        "",
        f"- Papers: {paper_count}",
        f"- Tasks: {task_count}",
        f"- Unique datasets: {dataset_count}",
        f"- Dataset usages: {dataset_use_count}",
        "",
        "## Entry Points",
        "",
        "- [Papers](papers/index.md)",
        "- [Tasks](tasks/index.md)",
        "- [Datasets](datasets/index.md)",
        "- [Dataset Uses](dataset_uses/index.md)",
        "",
        "## Schema",
        "",
        "- [Schema](../schema/wiki_schema.yaml)",
    ]
    write_page(pages_dir / "index.md", "\n".join(index_lines))

    write_collection_indexes(pages_dir, entities, paths)
    write_paper_pages(pages_dir, entities, paths)
    write_task_pages(pages_dir, entities, paths)
    write_dataset_pages(pages_dir, entities, paths)
    write_dataset_use_pages(pages_dir, entities, paths)


def write_collection_indexes(pages_dir: Path, entities: dict, paths: dict):
    paper_lines = ["# Papers", ""]
    for paper in sorted(entities["papers"].values(), key=lambda x: x["paper_file"]):
        link = markdown_link(paper["title"], paths["papers"][paper["paper_id"]])
        paper_lines.append(f"- {link} ({paper['paper_file']})")
    write_page(pages_dir / "papers" / "index.md", "\n".join(paper_lines))

    task_lines = ["# Tasks", ""]
    for task in sorted(entities["tasks"].values(), key=lambda x: (x["paper_file"], x["task_index"])):
        label = f"{Path(task['paper_file']).stem} - task {task['task_index']}"
        link = markdown_link(label, paths["tasks"][task["task_id"]])
        task_lines.append(f"- {link}")
    write_page(pages_dir / "tasks" / "index.md", "\n".join(task_lines))

    dataset_lines = ["# Datasets", ""]
    for dataset in sorted(entities["datasets"].values(), key=lambda x: x["db_title"].lower()):
        link = markdown_link(dataset["db_title"], paths["datasets"][dataset["dataset_id"]])
        dataset_lines.append(f"- {link} ({len(dataset['dataset_use_ids'])} uses)")
    write_page(pages_dir / "datasets" / "index.md", "\n".join(dataset_lines))

    use_lines = ["# Dataset Uses", ""]
    for use in sorted(entities["dataset_uses"].values(), key=lambda x: (x["paper_file"], x["db_title"])):
        label = f"{Path(use['paper_file']).stem} - {use['db_title']}"
        use_lines.append(f"- {markdown_link(label, paths['dataset_uses'][use['dataset_use_id']])}")
    write_page(pages_dir / "dataset_uses" / "index.md", "\n".join(use_lines))


def write_paper_pages(pages_dir: Path, entities: dict, paths: dict):
    for paper in entities["papers"].values():
        rel_path = paths["papers"][paper["paper_id"]]
        lines = [
            f"# {paper['title']}",
            "",
            "## Metadata",
            "",
            f"- Paper file: `{paper['paper_file']}`",
            f"- Paper ID: `{paper['paper_id']}`",
            "",
            "## Tasks",
            "",
        ]
        for task_id in paper["task_ids"]:
            task = entities["tasks"][task_id]
            task_link = rel_link(rel_path, paths["tasks"][task_id], f"Task {task['task_index']}")
            lines.append(f"### {task_link}")
            lines.append("")
            lines.append(task["task_description"])
            lines.append("")
            if task["task_tags"]:
                lines.append(f"- Tags: {', '.join(task['task_tags'])}")
            if task["dataset_ids"]:
                dataset_links = [
                    rel_link(rel_path, paths["datasets"][dataset_id], entities["datasets"][dataset_id]["db_title"])
                    for dataset_id in task["dataset_ids"]
                ]
                lines.append(f"- Datasets: {', '.join(dataset_links)}")
            lines.append("")

        write_page(pages_dir / rel_path, "\n".join(lines))


def write_task_pages(pages_dir: Path, entities: dict, paths: dict):
    for task in entities["tasks"].values():
        rel_path = paths["tasks"][task["task_id"]]
        paper = entities["papers"][task["paper_id"]]
        lines = [
            f"# {Path(task['paper_file']).stem} - Task {task['task_index']}",
            "",
            "## Task Description",
            "",
            task["task_description"],
            "",
            "## Metadata",
            "",
            f"- Task ID: `{task['task_id']}`",
            f"- Source paper: {rel_link(rel_path, paths['papers'][task['paper_id']], paper['title'])}",
            f"- Tags: {', '.join(task['task_tags']) if task['task_tags'] else 'None'}",
            "",
            "## Supporting Datasets",
            "",
        ]
        if task["dataset_use_ids"]:
            for use_id in task["dataset_use_ids"]:
                use = entities["dataset_uses"][use_id]
                dataset = entities["datasets"][use["dataset_id"]]
                dataset_link = rel_link(rel_path, paths["datasets"][use["dataset_id"]], dataset["db_title"])
                use_link = rel_link(rel_path, paths["dataset_uses"][use_id], "usage note")
                lines.extend(
                    [
                        f"### {dataset_link}",
                        "",
                        f"- Usage page: {use_link}",
                        f"- Original title in paper: {use['original_db_title']}",
                        f"- Link: {use['db_link']}",
                        "",
                        use["db_description"] or "No dataset description extracted.",
                        "",
                    ]
                )
        else:
            lines.append("No dataset extracted for this task.")
            lines.append("")

        write_page(pages_dir / rel_path, "\n".join(lines))


def write_dataset_pages(pages_dir: Path, entities: dict, paths: dict):
    for dataset in entities["datasets"].values():
        rel_path = paths["datasets"][dataset["dataset_id"]]
        lines = [
            f"# {dataset['db_title']}",
            "",
            "## Metadata",
            "",
            f"- Dataset ID: `{dataset['dataset_id']}`",
            f"- Aliases: {', '.join(dataset['aliases']) if dataset['aliases'] else 'None'}",
            f"- Links: {', '.join(dataset['links']) if dataset['links'] else 'None'}",
            f"- Used by papers: {len(dataset['paper_ids'])}",
            f"- Dataset usage records: {len(dataset['dataset_use_ids'])}",
            "",
            "## Description Examples",
            "",
        ]
        for description in dataset["description_examples"]:
            lines.append(f"- {description}")
        if not dataset["description_examples"]:
            lines.append("- No description extracted.")

        lines.extend(["", "## Uses", ""])
        for use_id in dataset["dataset_use_ids"]:
            use = entities["dataset_uses"][use_id]
            paper = entities["papers"][use["paper_id"]]
            use_link = rel_link(rel_path, paths["dataset_uses"][use_id], Path(use["paper_file"]).stem)
            paper_link = rel_link(rel_path, paths["papers"][use["paper_id"]], paper["title"])
            task_link = rel_link(rel_path, paths["tasks"][use["task_id"]], "task")
            lines.append(f"- {use_link}: {paper_link}, {task_link}")

        write_page(pages_dir / rel_path, "\n".join(lines))


def write_dataset_use_pages(pages_dir: Path, entities: dict, paths: dict):
    for use in entities["dataset_uses"].values():
        rel_path = paths["dataset_uses"][use["dataset_use_id"]]
        paper = entities["papers"][use["paper_id"]]
        dataset = entities["datasets"][use["dataset_id"]]
        lines = [
            f"# {Path(use['paper_file']).stem} - {use['db_title']}",
            "",
            "## Dataset Use",
            "",
            use["db_description"] or "No dataset description extracted.",
            "",
            "## Links",
            "",
            f"- Paper: {rel_link(rel_path, paths['papers'][use['paper_id']], paper['title'])}",
            f"- Task: {rel_link(rel_path, paths['tasks'][use['task_id']], 'task page')}",
            f"- Dataset: {rel_link(rel_path, paths['datasets'][use['dataset_id']], dataset['db_title'])}",
            f"- Dataset URL: {use['db_link']}",
            "",
            "## Task Context",
            "",
            use["task_description"],
            "",
            "## Metadata",
            "",
            f"- Dataset use ID: `{use['dataset_use_id']}`",
            f"- Original dataset title: {use['original_db_title']}",
            f"- Tags: {', '.join(use['task_tags']) if use['task_tags'] else 'None'}",
        ]
        write_page(pages_dir / rel_path, "\n".join(lines))


def write_schema_layer(output_dir: Path):
    schema_dir = output_dir / "schema"
    write_page(schema_dir / "wiki_schema.yaml", SCHEMA_TEXT)


def parse_args():
    parser = argparse.ArgumentParser(description="Build a standard three-layer LLM Wiki from extracted records.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Path to extracted JSON records.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Output LLM Wiki directory.")
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.input.exists():
        raise FileNotFoundError(f"Input JSON not found: {args.input}")

    records = read_records(args.input)
    entities = build_entities(records)
    prepare_output_dir(args.output_dir)
    write_raw_layer(args.output_dir, args.input, entities)
    write_schema_layer(args.output_dir)
    write_pages(args.output_dir, entities)

    print(f"LLM Wiki built from: {args.input}")
    print(f"Output directory: {args.output_dir}")
    print(f"Papers: {len(entities['papers'])}")
    print(f"Tasks: {len(entities['tasks'])}")
    print(f"Unique datasets: {len(entities['datasets'])}")
    print(f"Dataset uses: {len(entities['dataset_uses'])}")
    print(f"Start page: {args.output_dir / 'pages' / 'index.md'}")
    print(f"Schema: {args.output_dir / 'schema' / 'wiki_schema.yaml'}")


if __name__ == "__main__":
    main()

