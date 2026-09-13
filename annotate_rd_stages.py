import argparse
import csv
import re
from pathlib import Path


DEFAULT_WIKI_DIR = Path("llm_wiki")

STAGE_DEFINITIONS = [
    {
        "name": "Problem Definition",
        "description": "Define the material system, target property, application, or scientific objective.",
        "keywords": [
            "task", "goal", "objective", "problem", "target property", "application",
            "predicting", "identifying", "discovering", "designing",
        ],
    },
    {
        "name": "Candidate Space Construction",
        "description": "Construct or select the material/composition/structure search space.",
        "keywords": [
            "candidate", "candidate space", "search space", "chemical space", "compositional space",
            "hypothetical", "screening space", "high-throughput", "virtual screening",
            "enumerated", "generated", "substitution", "unexplored",
        ],
    },
    {
        "name": "Dataset Selection",
        "description": "Select, curate, merge, clean, or define datasets supporting the task.",
        "keywords": [
            "dataset", "database", "benchmark", "entries", "samples", "curated", "collected",
            "source", "split", "train", "validation", "test", "labels", "ground truth",
        ],
    },
    {
        "name": "Representation / Feature Construction",
        "description": "Build descriptors, embeddings, graphs, text, tensor, symmetry-aware, or physics-aware representations.",
        "keywords": [
            "feature", "features", "descriptor", "descriptors", "representation", "embedding",
            "graph", "crystal graph", "coordinates", "lattice", "atomic structure", "structure representation",
            "symmetry", "invariant", "equivariant", "tensor", "text description", "fingerprint",
        ],
    },
    {
        "name": "Model Training",
        "description": "Train, pretrain, fine-tune, transfer, or calibrate predictive models.",
        "keywords": [
            "train", "training", "trained", "pretrain", "pre-training", "fine-tune", "fine tuning",
            "transfer learning", "model", "surrogate", "regressor", "classifier", "supervised",
            "self-supervised", "learning", "distillation",
        ],
    },
    {
        "name": "Screening / Prediction",
        "description": "Predict properties, classify candidates, estimate scores, rank materials, or perform screening.",
        "keywords": [
            "predict", "prediction", "classify", "classification", "estimate", "estimation",
            "screen", "screening", "rank", "ranking", "identify", "discovery", "select",
            "candidate", "property prediction",
        ],
    },
    {
        "name": "Validation",
        "description": "Validate predictions through experiments, DFT calculations, held-out tests, OOD tests, or reference databases.",
        "keywords": [
            "validate", "validation", "validated", "experimental", "experiment", "dft validation",
            "held-out", "out-of-distribution", "ood", "test set", "generalization", "ground-truth",
            "reference", "confirmed", "synthesized",
        ],
    },
    {
        "name": "Optimization / Iteration",
        "description": "Iteratively optimize candidates, update models, or close active learning/design loops.",
        "keywords": [
            "optimize", "optimization", "iterative", "iteration", "active learning", "bayesian",
            "feedback", "closed-loop", "update", "refine", "loop",
        ],
    },
    {
        "name": "Benchmarking / Evaluation",
        "description": "Evaluate or compare models, methods, baselines, metrics, or leaderboards.",
        "keywords": [
            "benchmark", "benchmarking", "evaluate", "evaluation", "compare", "comparison",
            "baseline", "leaderboard", "performance", "metric", "mae", "accuracy", "auc",
            "cross-validation", "ablation",
        ],
    },
]


def clean_text(value) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value).replace("\x00", " ")).strip()


def read_csv_rows(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def score_stage(text: str, keywords: list[str]) -> int:
    lowered = text.lower()
    score = 0
    for keyword in keywords:
        if keyword in lowered:
            score += 1
    return score


def infer_stages(text: str, always_include_problem: bool = False) -> list[str]:
    scores = []
    for stage in STAGE_DEFINITIONS:
        score = score_stage(text, stage["keywords"])
        if always_include_problem and stage["name"] == "Problem Definition":
            score = max(score, 1)
        if score > 0:
            scores.append((stage["name"], score))

    if not scores:
        return ["Dataset Selection"]

    # Keep all strongly signaled stages, but avoid extremely broad noisy lists.
    max_score = max(score for _, score in scores)
    selected = [name for name, score in scores if score >= 2 or score == max_score]

    stage_order = [stage["name"] for stage in STAGE_DEFINITIONS]
    selected = sorted(set(selected), key=stage_order.index)
    return selected


def split_stages(value: str) -> list[str]:
    return [item.strip() for item in clean_text(value).split(";") if item.strip()]


def find_page_by_marker(pages_dir: Path, marker: str) -> dict[str, Path]:
    mapping = {}
    for path in pages_dir.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(re.escape(marker) + r"\s*`([^`]+)`", text):
            mapping[match.group(1)] = path
    return mapping


def replace_marker_section(text: str, marker_name: str, section: str) -> str:
    start = f"<!-- {marker_name}_START -->"
    end = f"<!-- {marker_name}_END -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), flags=re.DOTALL)
    block = f"{start}\n{section.rstrip()}\n{end}"
    if pattern.search(text):
        return pattern.sub(block, text)
    return text.rstrip() + "\n\n" + block + "\n"


def append_task_stage_sections(wiki_dir: Path, task_stage_rows: list[dict]):
    pages_dir = wiki_dir / "pages"
    task_pages = find_page_by_marker(pages_dir / "tasks", "- Task ID:")
    for row in task_stage_rows:
        path = task_pages.get(row["task_id"])
        if not path:
            continue
        stages = split_stages(row["rd_stages"])
        section = "\n".join(
            [
                "## R&D Stages",
                "",
                "This task is mapped to the following R&D stages:",
                "",
                *[f"- {stage}" for stage in stages],
            ]
        )
        path.write_text(replace_marker_section(path.read_text(encoding="utf-8"), "RD_STAGES", section), encoding="utf-8")


def append_dataset_use_stage_sections(wiki_dir: Path, use_stage_rows: list[dict]):
    pages_dir = wiki_dir / "pages"
    use_pages = find_page_by_marker(pages_dir / "dataset_uses", "- Dataset use ID:")
    for row in use_stage_rows:
        path = use_pages.get(row["dataset_use_id"])
        if not path:
            continue
        stages = split_stages(row["rd_stages"])
        section = "\n".join(
            [
                "## R&D Stages",
                "",
                "This dataset-use record supports the following R&D stages:",
                "",
                *[f"- {stage}" for stage in stages],
            ]
        )
        path.write_text(replace_marker_section(path.read_text(encoding="utf-8"), "RD_STAGES", section), encoding="utf-8")


def rel_link(from_path: Path, to_path: Path, label: str) -> str:
    relative = to_path.relative_to(from_path.parent.parent)
    return f"[{label}]({relative.as_posix().replace(' ', '%20')})"


def write_stage_pages(wiki_dir: Path, task_stage_rows: list[dict], use_stage_rows: list[dict]):
    pages_dir = wiki_dir / "pages"
    stage_dir = pages_dir / "stages"
    stage_dir.mkdir(parents=True, exist_ok=True)

    task_pages = find_page_by_marker(pages_dir / "tasks", "- Task ID:")
    use_pages = find_page_by_marker(pages_dir / "dataset_uses", "- Dataset use ID:")

    index_lines = ["# R&D Stages", ""]
    stage_names = [stage["name"] for stage in STAGE_DEFINITIONS]
    for stage in STAGE_DEFINITIONS:
        name = stage["name"]
        slug = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")
        stage_path = stage_dir / f"{slug}.md"
        task_matches = [row for row in task_stage_rows if name in split_stages(row["rd_stages"])]
        use_matches = [row for row in use_stage_rows if name in split_stages(row["rd_stages"])]

        lines = [
            f"# {name}",
            "",
            stage["description"],
            "",
            "## Tasks",
            "",
        ]
        if task_matches:
            for row in task_matches:
                path = task_pages.get(row["task_id"])
                label = f"{row['paper_file']} - task {row.get('task_index', '')}".strip()
                if path:
                    lines.append(f"- {rel_link(stage_path, path, label)}")
                else:
                    lines.append(f"- {label}")
        else:
            lines.append("- None")

        lines.extend(["", "## Dataset Uses", ""])
        if use_matches:
            for row in use_matches:
                path = use_pages.get(row["dataset_use_id"])
                label = f"{row['paper_file']} - {row['db_title']}"
                if path:
                    lines.append(f"- {rel_link(stage_path, path, label)}")
                else:
                    lines.append(f"- {label}")
        else:
            lines.append("- None")

        stage_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        index_lines.append(f"- [{name}]({stage_path.name}) ({len(task_matches)} tasks, {len(use_matches)} dataset uses)")

    (stage_dir / "index.md").write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")

    main_index = pages_dir / "index.md"
    if main_index.exists():
        text = main_index.read_text(encoding="utf-8")
        if "- [R&D Stages](stages/index.md)" not in text:
            text = text.replace("- [Dataset Uses](dataset_uses/index.md)", "- [Dataset Uses](dataset_uses/index.md)\n- [R&D Stages](stages/index.md)")
            main_index.write_text(text, encoding="utf-8")


def write_schema_note(wiki_dir: Path):
    schema_path = wiki_dir / "schema" / "wiki_schema.yaml"
    if not schema_path.exists():
        return
    text = schema_path.read_text(encoding="utf-8")
    if "R&DStage" in text:
        return
    addition = """

  R&DStage:
    id: stage_name
    properties:
      - stage_name
      - description
    page: pages/stages/{stage_slug}.md

stage_annotation:
  Task:
    property: rd_stages
    meaning: R&D stages covered by the paper-level research task.
  DatasetUse:
    property: rd_stages
    meaning: R&D stages supported by this dataset in the context of the paper task.
"""
    schema_path.write_text(text.rstrip() + addition + "\n", encoding="utf-8")


def annotate(wiki_dir: Path):
    raw_dir = wiki_dir / "raw"
    tasks = read_csv_rows(raw_dir / "tasks.csv")
    dataset_uses = read_csv_rows(raw_dir / "dataset_uses.csv")

    task_stage_rows = []
    for row in tasks:
        text = " ".join([row.get("task_description", ""), row.get("task_tags", "")])
        stages = infer_stages(text, always_include_problem=True)
        if "Problem Definition" not in stages:
            stages.insert(0, "Problem Definition")
        if row.get("dataset_ids") and "Dataset Selection" not in stages:
            stages.insert(1, "Dataset Selection")
        out = dict(row)
        out["rd_stages"] = "; ".join(stages)
        task_stage_rows.append(out)

    task_stage_by_id = {row["task_id"]: split_stages(row["rd_stages"]) for row in task_stage_rows}
    use_stage_rows = []
    for row in dataset_uses:
        text = " ".join([row.get("db_title", ""), row.get("db_description", ""), row.get("task_description", "")])
        stages = infer_stages(text)
        if "Dataset Selection" not in stages:
            stages.insert(0, "Dataset Selection")
        inherited = task_stage_by_id.get(row.get("task_id", ""), [])
        # Dataset uses should inherit dataset selection and task-specific prediction/training signals when present.
        merged = sorted(set(stages + [stage for stage in inherited if stage in {"Screening / Prediction", "Model Training", "Validation", "Benchmarking / Evaluation"}]), key=[stage["name"] for stage in STAGE_DEFINITIONS].index)
        out = dict(row)
        out["rd_stages"] = "; ".join(merged)
        use_stage_rows.append(out)

    write_csv(raw_dir / "task_stages.csv", task_stage_rows, list(task_stage_rows[0].keys()) if task_stage_rows else ["task_id", "rd_stages"])
    write_csv(raw_dir / "dataset_use_stages.csv", use_stage_rows, list(use_stage_rows[0].keys()) if use_stage_rows else ["dataset_use_id", "rd_stages"])

    summary_rows = []
    for stage in STAGE_DEFINITIONS:
        name = stage["name"]
        summary_rows.append(
            {
                "stage_name": name,
                "description": stage["description"],
                "task_count": sum(1 for row in task_stage_rows if name in split_stages(row["rd_stages"])),
                "dataset_use_count": sum(1 for row in use_stage_rows if name in split_stages(row["rd_stages"])),
            }
        )
    write_csv(raw_dir / "stage_summary.csv", summary_rows, ["stage_name", "description", "task_count", "dataset_use_count"])

    append_task_stage_sections(wiki_dir, task_stage_rows)
    append_dataset_use_stage_sections(wiki_dir, use_stage_rows)
    write_stage_pages(wiki_dir, task_stage_rows, use_stage_rows)
    write_schema_note(wiki_dir)

    return task_stage_rows, use_stage_rows, summary_rows


def parse_args():
    parser = argparse.ArgumentParser(description="Annotate LLM Wiki tasks and dataset uses with R&D stages.")
    parser.add_argument("--wiki-dir", type=Path, default=DEFAULT_WIKI_DIR)
    return parser.parse_args()


def main():
    args = parse_args()
    task_rows, use_rows, summary_rows = annotate(args.wiki_dir)
    print(f"Annotated R&D stages for: {args.wiki_dir}")
    print(f"Tasks: {len(task_rows)}")
    print(f"Dataset uses: {len(use_rows)}")
    print("Stage summary:")
    for row in summary_rows:
        print(f"- {row['stage_name']}: {row['task_count']} tasks, {row['dataset_use_count']} dataset uses")


if __name__ == "__main__":
    main()

