"""V5 family expansion and auditable dataset-level decision helpers."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any


def load_family_overrides(path: Path | None) -> dict[str, str]:
    """Load explicit family memberships without silently guessing from names."""
    if path is None or not path.is_file():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    result: dict[str, str] = {}
    for family in payload.get("families", []):
        family_id = str(family.get("family_id", "")).strip()
        if not family_id:
            continue
        for dataset_id in family.get("members", []):
            dataset_id = str(dataset_id).strip()
            if dataset_id:
                result[dataset_id] = family_id
    return result


def family_id(store, dataset_id: str, overrides: dict[str, str]) -> str:
    """Resolve an override or the evidence-backed source_dataset_id root."""
    if dataset_id in overrides:
        return overrides[dataset_id]
    current = dataset_id
    visited: set[str] = set()
    while current not in visited:
        visited.add(current)
        parent = store.dataset_by_id.get(current, {}).get("source_dataset_id")
        if not parent or parent not in store.dataset_by_id:
            break
        current = parent
    return overrides.get(current, current)


def family_members(store, overrides: dict[str, str]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    for dataset_id in store.dataset_by_id:
        grouped[family_id(store, dataset_id, overrides)].append(dataset_id)
    return {key: sorted(values) for key, values in grouped.items()}


def expand_candidates(*, store, ranked, candidate_class, overrides, score_discount=0.72):
    """Add recommendable relatives; membership supplies recall, never capability."""
    expanded = list(ranked)
    by_id = {candidate.dataset_id: candidate for candidate in expanded}
    grouped = family_members(store, overrides)
    trace: list[dict[str, Any]] = []
    for anchor in list(ranked):
        fid = family_id(store, anchor.dataset_id, overrides)
        for member_id in grouped.get(fid, []):
            if member_id in by_id:
                continue
            dataset = store.dataset_by_id[member_id]
            if dataset.get("recommendable") is False or dataset.get("availability") in {"private", "unavailable"}:
                continue
            uses = store.uses_by_dataset.get(member_id, [])
            if not uses:
                continue
            score = max(0.0, min(1.0, float(anchor.final_score) * score_discount))
            candidate = candidate_class(
                dataset_id=member_id,
                retrieval_score=score,
                deterministic_score=score,
                final_score=score,
                supporting_use_ids={use["dataset_use_id"] for use in uses},
                derivation_notes=[{
                    "type": "family_expansion",
                    "family_id": fid,
                    "anchor_dataset_id": anchor.dataset_id,
                    "score_discount": score_discount,
                    "capability_inherited": False,
                }],
                rerank_reason="Family-expanded candidate; eligibility is decided from its own DatasetUse evidence.",
            )
            expanded.append(candidate)
            by_id[member_id] = candidate
            trace.append({
                "dataset_id": member_id,
                "family_id": fid,
                "anchor_dataset_id": anchor.dataset_id,
                "supporting_use_count": len(uses),
            })
    expanded.sort(key=lambda candidate: candidate.final_score, reverse=True)
    return expanded, trace


def annotate_family_output(*, store, dataset_ids, overrides):
    return [
        {"dataset_id": dataset_id, "family_id": family_id(store, dataset_id, overrides)}
        for dataset_id in dataset_ids
    ]
