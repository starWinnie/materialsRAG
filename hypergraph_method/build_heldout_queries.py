import argparse
from pathlib import Path

from hypergraph_common import PROJECT_ROOT, canonical_dataset_title, read_records, write_json


DEFAULT_TRAIN = PROJECT_ROOT / "outputs" / "30results.json"
DEFAULT_ALL = PROJECT_ROOT / "outputs" / "all_results.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "hypergraph_method" / "outputs" / "heldout_queries.json"


def build_queries(train_path: Path, all_path: Path) -> list[dict]:
    train_papers = {record["paper_file"] for record in read_records(train_path)}
    records = read_records(all_path)
    queries = []
    for record in records:
        paper_file = record.get("paper_file", "")
        if paper_file in train_papers:
            continue
        paper_stem = Path(paper_file).stem
        for task_index, task in enumerate(record.get("result") or [], start=1):
            task_description = task.get("task_description", "")
            task_tags = task.get("task_tags") or []
            for dataset_index, dataset in enumerate(task.get("datasets") or [], start=1):
                dataset_name = canonical_dataset_title(dataset.get("db_title", ""))
                query_text = (
                    f"Find datasets for this materials research task: {task_description} "
                    f"Task tags: {', '.join(task_tags)}. "
                    f"Needed dataset role: {dataset.get('db_description', '')}"
                )
                queries.append(
                    {
                        "query_id": f"{paper_stem}__task{task_index}__dataset{dataset_index}",
                        "paper_file": paper_file,
                        "task_description": task_description,
                        "task_tags": task_tags,
                        "heldout_dataset": dataset_name,
                        "heldout_original_dataset": dataset.get("db_title", ""),
                        "heldout_dataset_description": dataset.get("db_description", ""),
                        "query": query_text,
                    }
                )
    return queries


def parse_args():
    parser = argparse.ArgumentParser(description="Build held-out dataset-use queries from papers outside the 30-paper training split.")
    parser.add_argument("--train", type=Path, default=DEFAULT_TRAIN)
    parser.add_argument("--all", type=Path, default=DEFAULT_ALL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main():
    args = parse_args()
    queries = build_queries(args.train, args.all)
    write_json(args.output, queries)
    print(f"Wrote {len(queries)} held-out queries: {args.output}")


if __name__ == "__main__":
    main()
