"""Behavioral regression cases for false capability claims and portfolio loss."""
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace as NS

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "newMethod"))
from v4_scoped_selection import Need, concepts, make_needs, match_use, select_scoped, scoped_answer, reserve_need_pairs, calibrate_bounded_score, add_domain_routes


def use(uid, fields, text="DFT crystal structures with labelled data", role="training"):
    return dict(dataset_use_id=uid, used_fields=fields, usage_role=role, purpose="",
                paper_id="P1", evidence=[dict(text=text, inferred=False)])


def choose(uses, targets, question="predict band gap", scores=None):
    candidates, by_id, ds = [], {}, {}
    for i, records in enumerate(uses):
        did = f"D{i}"
        ds[did] = dict(dataset_id=did, canonical_name=did, recommendable=True, availability="public",
                       available_properties=["band gap", "forces", "energy", "stresses"])
        by_id.update({r["dataset_use_id"]: r for r in records})
        candidates.append(NS(dataset_id=did, supporting_use_ids=set(r["dataset_use_id"] for r in records),
                             final_score=scores[i] if scores else 1 - i / 10))
    store = NS(dataset_by_id=ds, use_by_id=by_id)
    plan = NS(target_properties=targets, constraints=[])
    result, diag = select_scoped(store=store, plan=plan, question=question, ranked=candidates,
                                 max_results=6, candidate_top_k=30)
    return result, diag, store


class ScopedSelectionTests(unittest.TestCase):
    def test_input_only_is_not_a_property_match(self):
        n = Need("N1", ["synthesizability"], ["composition"], [])
        cell = match_use(n, use("a", ["composition", "formation energy"]))
        self.assertEqual(cell["utility"], 0)

    def test_finetuning_pretrained_model_is_not_pretraining_source(self):
        n = Need("N1", [], [], [], role="pretraining")
        u = use("a", ["band gap"], "We fine-tune the pre-trained model on this dataset.")
        u["purpose"] = "Fine-tune the pre-trained model on labeled prediction tasks"
        self.assertEqual(match_use(n, u)["utility"], 0)

    def test_other_dataset_in_same_quote_cannot_supply_domain(self):
        n = Need("N1", [], [], ["molecule"])
        u = use("a", ["structure"], "We use molecules from database B and inorganic crystals from database A.")
        u["purpose"] = "train on inorganic crystals"
        self.assertEqual(match_use(n, u, {"material_scope": ["inorganic crystals"]})["utility"], 0)

    def test_single_task_benchmark_is_not_suite(self):
        n = Need("N1", [], [], [], role="benchmark_suite")
        u = use("a", ["formation energy"], "Table 1: datasets derived from a suite", "benchmark")
        u["is_derived"] = True
        u["purpose"] = "benchmark formation energy prediction"
        self.assertEqual(match_use(n, u)["utility"], 0)

    def test_independent_equivalent_source_is_marked_as_alternative(self):
        selected, diag, _ = choose([[use("a", ["band gap"])], [use("b", ["band gap"])]],
                                   ["band gap"], scores=[1.0, .98])
        self.assertEqual(len(selected), 2)
        self.assertEqual(len(diag["portfolio_dataset_ids"]), 1)
        self.assertEqual(len(diag["alternatives"]), 1)

    def test_domain_routes_are_generic_and_idempotent(self):
        plan = NS(dense_queries=[], bm25_queries=[], dense_query_lanes={}, bm25_query_lanes={})
        add_domain_routes(plan, "predict properties of crystals and molecules")
        add_domain_routes(plan, "predict properties of crystals and molecules")
        self.assertEqual(len(plan.dense_queries), 2)
        self.assertIn("domain_rescue:molecule", plan.dense_query_lanes.values())
    def test_high_rerank_scores_do_not_collapse_to_one(self):
        self.assertGreater(calibrate_bounded_score(.98, .24, 0), calibrate_bounded_score(.91, .24, 0))
        self.assertLessEqual(calibrate_bounded_score(1, .32, 0), 1)

    def test_need_reservation_recovers_complementary_pair_within_budget(self):
        store = NS(dataset_by_id={"D0": {}, "D1": {}},
                   use_by_id={"u0": use("u0", ["band gap"]), "u1": use("u1", ["bulk modulus"])})
        a = NS(pair_id="a", dataset_id="D0", supporting_use_ids={"u0"}, pair_seed_score=.95)
        b = NS(pair_id="b", dataset_id="D1", supporting_use_ids={"u1"}, pair_seed_score=.4)
        selected, _ = reserve_need_pairs(store, NS(target_properties=["band gap", "bulk modulus"], constraints=[]),
                                         "predict band gap and bulk modulus", {"a": a, "b": b}, [a], 2)
        self.assertEqual({p.pair_id for p in selected}, {"a", "b"})
        self.assertEqual(len(selected), 2)
    def test_energy_aliases_do_not_merge_formation_with_total(self):
        self.assertEqual(concepts(["energy", "energies", "total energy", "energy per atom"]), {"energy"})
        self.assertEqual(concepts(["formation energy"]), {"formation_energy"})
        self.assertNotEqual(concepts(["decomposition energy"]), concepts(["energy above hull"]))

    def test_joint_labels_cannot_be_stitched_across_uses(self):
        selected, diag, _ = choose([[use("a", ["energy"]), use("b", ["forces"])]],
                                   ["energy", "forces"], "predict potential energy surface with energy and forces")
        self.assertEqual([c.dataset_id for c in selected], ["D0"])
        self.assertEqual(diag["covered_needs"], [])
        self.assertEqual(diag["conditional_selected_dataset_ids"], ["D0"])
        self.assertLess(diag["need_support_scores"]["N1"], 1)

    def test_complete_record_beats_high_score_incomplete_record(self):
        selected, _, _ = choose([[use("a", ["energy"])], [use("b", ["energies", "forces"])]],
                                ["energy", "forces"], "predict potential energy surface with energy and forces")
        self.assertEqual([c.dataset_id for c in selected], ["D1"])

    def test_complementary_datasets_are_kept(self):
        selected, diag, _ = choose([[use("a", ["band gap"])], [use("b", ["bulk modulus"])]],
                                   ["band gap", "bulk modulus"], "predict band gap and bulk modulus")
        self.assertEqual(len(selected), 2)
        self.assertEqual(diag["uncovered_needs"], [])

    def test_redundant_alternative_not_added(self):
        selected, _, _ = choose([[use("a", ["band gap"])], [use("b", ["band gap"])]], ["band gap"])
        self.assertEqual([c.dataset_id for c in selected], ["D0"])

    def test_output_order_prefers_larger_marginal_contribution(self):
        selected, _, _ = choose([[use("a", ["band gap"])],
                                 [use("b", ["bulk modulus", "shear modulus"])]],
                                ["band gap", "bulk modulus", "shear modulus"],
                                "predict band gap and elastic properties")
        self.assertEqual([c.dataset_id for c in selected], ["D1", "D0"])

    def test_computed_is_not_experimental(self):
        n = Need("N1", ["band_gap"], [], [], "experimental")
        self.assertEqual(match_use(n, use("a", ["band gap"], "DFT calculated band gap"))["status"], "conflict")

    def test_unknown_scope_is_not_verified(self):
        n = Need("N1", ["band_gap"], [], ["perovskite"])
        self.assertEqual(match_use(n, use("a", ["band gap"]))["status"], "unknown")

    def test_downstream_purpose_does_not_create_a_label(self):
        record = use("a", ["formation energy"], "DFT structures used for downstream band gap prediction")
        record["purpose"] = "predict band gap"
        n = Need("N1", ["band_gap"], [], [])
        cell = match_use(n, record, {"available_properties": ["band gap"]})
        self.assertEqual(cell["utility"], 0)
        self.assertNotEqual(cell["status"], "supported")

    def test_explicit_label_quote_is_conditional_hint(self):
        n = Need("N1", ["band_gap"], [], [])
        cell = match_use(n, use("a", [], "Dataset contains measured band gap labels"))
        self.assertGreater(cell["utility"], 0)
        self.assertLess(cell["utility"], 1)
        self.assertEqual(cell["status"], "unknown")

    def test_multidomain_query_does_not_make_cartesian_demands(self):
        needs = make_needs(NS(target_properties=["band gap", "bulk modulus"], constraints=[]),
                           "predict band gap and bulk modulus for crystals and molecules")
        self.assertEqual(len(needs), 4)
        self.assertFalse(any(n.properties and n.materials for n in needs))

    def test_only_computed_data_still_returns_empty_for_experimental_request(self):
        selected, _, _ = choose([[use("a", ["band gap"], "DFT calculated band gap")]],
                                ["band gap"], "Find experimental band gap data")
        self.assertEqual(selected, [])

    def test_missing_scope_can_be_conditionally_recommended(self):
        selected, diag, _ = choose([[use("a", ["band gap"])]], ["band gap"],
                                   "predict perovskite band gap")
        self.assertEqual(len(selected), 1)
        self.assertEqual(diag["covered_needs"], [])

    def test_negated_pretraining_not_added(self):
        plan = NS(target_properties=["band gap"], constraints=[])
        needs = make_needs(plan, "Predict band gap without pretraining")
        self.assertFalse(any(n.role == "pretraining" for n in needs))

    def test_molecular_dynamics_is_not_molecular_dataset_scope(self):
        plan = NS(target_properties=["energy", "forces"], constraints=["low training cost"])
        needs = make_needs(plan, "crystalline materials potential energy surface for molecular dynamics")
        self.assertEqual(len(needs), 1)
        self.assertEqual(needs[0].materials, ["crystal"])
        self.assertEqual(needs[0].constraints, [])

    def test_source_does_not_need_target_labels(self):
        plan = NS(target_properties=["band gap"], constraints=[])
        needs = make_needs(plan, "Predict band gap with pretraining on other properties")
        source = next(n for n in needs if n.role == "pretraining")
        self.assertEqual(match_use(source, use("a", ["formation energy"], "pretraining source data"))["status"], "supported")

    def test_no_profile_union_and_no_complete_answer_on_gap(self):
        selected, diag, store = choose([[use("a", ["formation energy"])]], ["band gap"])
        self.assertEqual(selected, [])
        self.assertIn("没有证据足够完整", scoped_answer(store, selected, diag))


if __name__ == "__main__":
    unittest.main()
