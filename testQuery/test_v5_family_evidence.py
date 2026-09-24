"""V5 regressions: family recall must not become capability inheritance."""

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace as NS

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "newMethod"))

from retrieve_llm_wiki_node_edge_rerank_v5 import NodeEdgeDatasetCandidate
from v5_family_evidence import expand_candidates, family_id
from v5_scoped_selection import select_scoped


def usage(uid, did, fields):
    return {
        "dataset_use_id": uid, "dataset_id": did, "paper_id": "P1",
        "usage_role": "training", "used_fields": fields, "purpose": "",
        "evidence": [{"text": "Dataset contains labelled data", "inferred": False}],
    }


class V5FamilyTests(unittest.TestCase):
    def store(self):
        parent_use = usage("up", "parent", ["structure"])
        child_use = usage("uc", "child", ["band gap"])
        datasets = {
            "parent": {"dataset_id": "parent", "canonical_name": "Parent", "source_dataset_id": None,
                       "recommendable": True, "availability": "public", "available_properties": []},
            "child": {"dataset_id": "child", "canonical_name": "Child", "source_dataset_id": "parent",
                      "recommendable": True, "availability": "public", "available_properties": ["band gap"]},
        }
        return NS(dataset_by_id=datasets, use_by_id={"up": parent_use, "uc": child_use},
                  uses_by_dataset={"parent": [parent_use], "child": [child_use]})

    def test_source_relation_defines_family(self):
        store = self.store()
        self.assertEqual(family_id(store, "child", {}), "parent")

    def test_expansion_uses_member_own_evidence(self):
        store = self.store()
        anchor = NodeEdgeDatasetCandidate(dataset_id="parent", final_score=.9, supporting_use_ids={"up"})
        expanded, trace = expand_candidates(store=store, ranked=[anchor],
                                            candidate_class=NodeEdgeDatasetCandidate, overrides={})
        child = next(candidate for candidate in expanded if candidate.dataset_id == "child")
        self.assertEqual(child.supporting_use_ids, {"uc"})
        self.assertFalse(child.derivation_notes[0]["capability_inherited"])
        self.assertEqual(len(trace), 1)

    def test_family_top1_prefers_capable_member(self):
        store = self.store()
        ranked = [
            NS(dataset_id="parent", supporting_use_ids={"up"}, final_score=.95),
            NS(dataset_id="child", supporting_use_ids={"uc"}, final_score=.65),
        ]
        selected, diagnostics = select_scoped(
            store=store, plan=NS(target_properties=["band gap"], constraints=[]),
            question="predict band gap", ranked=ranked, max_results=3, candidate_top_k=10,
        )
        self.assertEqual([candidate.dataset_id for candidate in selected], ["child"])
        self.assertEqual(diagnostics["family_representative_removed"][0]["dataset_id"], "parent")

    def test_empty_selection_returns_unverified_fallback(self):
        store = self.store()
        ranked = [NS(dataset_id="parent", supporting_use_ids={"up"}, final_score=.9)]
        selected, diagnostics = select_scoped(
            store=store, plan=NS(target_properties=["synthesizability"], constraints=[]),
            question="predict crystal synthesizability from structure", ranked=ranked,
            max_results=3, candidate_top_k=10,
        )
        self.assertEqual([candidate.dataset_id for candidate in selected], ["parent"])
        self.assertTrue(diagnostics["fallback_used"])
        self.assertEqual(diagnostics["selection_reason"], "empty_result_unverified_fallback")
        self.assertEqual(diagnostics["fallback_candidates"][0]["status"], "unverified_fallback")

    def test_conflict_is_never_used_as_fallback(self):
        store = self.store()
        store.use_by_id["up"]["evidence"] = [{"text": "DFT computed band gap", "inferred": False}]
        ranked = [NS(dataset_id="parent", supporting_use_ids={"up"}, final_score=.9)]
        selected, diagnostics = select_scoped(
            store=store, plan=NS(target_properties=["band gap"], constraints=[]),
            question="find experimental crystal band gap", ranked=ranked,
            max_results=3, candidate_top_k=10,
        )
        self.assertEqual(selected, [])
        self.assertFalse(diagnostics["fallback_used"])


if __name__ == "__main__":
    unittest.main()
