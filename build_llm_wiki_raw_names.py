import argparse
import re
from pathlib import Path

import build_llm_wiki as base


DEFAULT_INPUT = Path("outputs/30results.json")
DEFAULT_OUTPUT_DIR = Path("llm_wiki_30_raw_names")


def keep_extracted_dataset_title(title: str) -> str:
    """Keep the extracted name while retaining basic whitespace cleanup."""
    return base.clean_text(title)


def unique_slugify(value: str, fallback: str) -> str:
    """Preserve the entity ID suffix so distinct raw names cannot overwrite pages."""
    value = base.clean_text(value)
    value = re.sub(r"[\u2010-\u2015]", "-", value)
    value = re.sub(r"[^\w\u4e00-\u9fff.-]+", "_", value, flags=re.UNICODE)
    value = re.sub(r"_+", "_", value).strip("._ ")
    suffix = fallback[-20:]
    prefix_length = max(1, 90 - len(suffix) - 1)
    prefix = (value[:prefix_length] or "entity").rstrip("._ ")
    return f"{prefix}_{suffix}"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Build an LLM Wiki without canonical dataset-name merging."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.input.exists():
        raise FileNotFoundError(f"Input JSON not found: {args.input}")

    records = base.read_records(args.input)

    original_canonicalizer = base.canonical_dataset_title
    base.canonical_dataset_title = keep_extracted_dataset_title
    try:
        entities = base.build_entities(records)
    finally:
        base.canonical_dataset_title = original_canonicalizer

    base.prepare_output_dir(args.output_dir)
    base.write_raw_layer(args.output_dir, args.input, entities)

    schema_text = re.sub(
        r"^source:\s*.*$",
        f"source: {args.input.as_posix()}",
        base.SCHEMA_TEXT,
        count=1,
        flags=re.MULTILINE,
    )
    base.write_page(args.output_dir / "schema" / "wiki_schema.yaml", schema_text)

    original_slugifier = base.slugify
    base.slugify = unique_slugify
    try:
        base.write_pages(args.output_dir, entities)
    finally:
        base.slugify = original_slugifier

    print(f"Raw-name LLM Wiki built from: {args.input}")
    print(f"Output directory: {args.output_dir}")
    print(f"Papers: {len(entities['papers'])}")
    print(f"Tasks: {len(entities['tasks'])}")
    print(f"Unique extracted dataset names: {len(entities['datasets'])}")
    print(f"Dataset uses: {len(entities['dataset_uses'])}")


if __name__ == "__main__":
    main()
