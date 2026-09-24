"""Evidence-local demand matching and bounded portfolio search (no model calls).

Unknown metadata discounts utility instead of rejecting candidates. Complete
joint support still requires one use; profile hints never become verified facts.
The bounded search balances support gains against a small redundancy cost.
"""
from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import asdict, dataclass

from v5_family_evidence import family_id
from typing import Any


ALIASES = {
    "formation_energy": r"formation (?:energ\w*|enthalp\w*)|形成[能焓]|\be_form\b",
    "decomposition_energy": r"decomposition (?:energ\w*|enthalp\w*)|分解[能焓]|Δhd",
    "energy_above_hull": r"e[_ ]?hull|energy above (?:the )?(?:convex )?hull|凸包能",
    "energy": r"^(?:total |potential )?(?:energy|energies)(?:\s*\(.*\))?$|总能量|势能|energy per atom",
    "band_gap": r"band\s*gap\w*|带隙|gap_pbe",
    "bulk_modulus": r"bulk modul\w*|体积模量",
    "shear_modulus": r"shear modul\w*|剪切模量",
    "forces": r"\bforces?\b|原子力",
    "stresses": r"\bstress(?:es)?\b|应力",
    "magnetic_moments": r"magnetic moments?|magmoms?|磁矩",
    "structure": r"(?:crystal|atomic|atomistic) structur\w*|^structures?$|原子构型|晶体结构|cif|atomic positions|fractional coordinates",
    "composition": r"compositions?|chemical formula|elemental fractions?|化学组成|化学成分",
    "dielectric": r"dielectric|介电",
    "slme": r"\bslme\b|spectroscopic limited maximum efficiency",
    "spillage": r"\bspillage\b",
    "stability": r"thermodynamic stability|热力学稳定性",
    "phonon_frequency": r"phonon frequenc\w*|声子频率",
    "exfoliation_energy": r"exfoliation energ\w*|剥离能",
    "dipole_moment": r"dipole moments?|偶极矩",
    "homo": r"\bhomo\b",
    "lumo": r"\blumo\b",
    "piezoelectric": r"piezoelectric (?:coefficient|tensor)\w*|压电",
    "thermoelectric": r"seebeck|thermoelectric (?:coefficient|propert)\w*|热电",
    "synthesizability": r"synthesizab\w*|synthesi[sz]ability|可合成性",
}
MATERIALS = {
    "perovskite": r"perovskit\w*|钙钛矿",
    "molecule": r"\bmolecules?\b|\bmolecular\b(?!\s+(?:dynamics|simulation))|分子(?!动力学|模拟)",
    "crystal": r"crystal\w*|crystalline|solid.state|inorganic bulk|晶体",
    "catalyst": r"cataly\w*|催化",
}


def calibrate_bounded_score(original, bonus, penalty):
    """Normalize the theoretical score range instead of clipping useful ties.

    V4 intent bonus has an upper bound of .10 + .08 + .08 + .06 = .32.
    This is a ranking score, not an estimated probability.
    """
    return max(0.0, min(1.0, (original + bonus - penalty) / 1.32))


def add_domain_routes(plan, question):
    """Independent domain routes prevent crystal-heavy queries drowning molecules.

    Query text is generic by domain; it contains no dataset names or gold labels.
    """
    routes = {"molecule": "molecular property datasets", "crystal": "crystalline materials property datasets",
              "catalyst": "catalysis catalyst datasets", "perovskite": "perovskite property datasets"}
    for domain, query in routes.items():
        if not positive_phrase(question, MATERIALS[domain]):
            continue
        for queries, lanes in ((plan.dense_queries, plan.dense_query_lanes), (plan.bm25_queries, plan.bm25_query_lanes)):
            if query not in queries:
                queries.append(query)
            lanes[query] = "domain_rescue:" + domain


def concepts(values):
    result = set()
    for value in values:
        text = re.sub(r"[_-]", " ", str(value).lower()).strip()
        hits = {name for name, pattern in ALIASES.items() if re.search(pattern, text, re.I)}
        result.update(hits or {re.sub(r"\W+", "_", text).strip("_")})
    return result - {""}


def positive_phrase(text, pattern):
    """Conservative local negation check; not a general natural-language parser."""
    for match in re.finditer(pattern, text, re.I):
        prefix = text[max(0, match.start() - 55):match.start()]
        if not re.search(r"(?:\bno\b|\bnot\b|without|不需要|无需|不要|不进行)[^,.;，。；]*$", prefix, re.I):
            return True
    return False


@dataclass
class Need:
    need_id: str
    properties: list[str]
    fields: list[str]
    materials: list[str]
    provenance: str = ""
    role: str = ""
    constraints: list[str] = None


def make_needs(plan, question):
    props = sorted(concepts(plan.target_properties) - {"composition", "structure", "potential_energy_surface"})
    materials = [name for name, pattern in MATERIALS.items() if positive_phrase(question, pattern)]
    # Perovskite already denotes the specific material family; do not also make
    # generic crystal an independent alternative.
    if "perovskite" in materials and "crystal" in materials and not any(m in materials for m in ("molecule", "catalyst")):
        materials.remove("crystal")
    fields = []
    if positive_phrase(question, r"(?:from|using|based on) (?:atomic |crystal |atomic-scale crystal )?structures?|structure inputs?|从.*结构|基于.*结构"):
        fields.append("structure")
    if positive_phrase(question, r"composition.only|only (?:elemental fractions|.*composition)|solely from.*composition|仅.*成分|只.*组成"):
        fields.append("composition")
    provenance = ""
    if positive_phrase(question, r"experimental (?:band\s*gap|data|labels|measurements)|实验(?:带隙|数据|测量)"):
        provenance = "experimental"
    elif positive_phrase(question, r"DFT.calculated|DFT data|计算带隙|计算数据"):
        provenance = "computed"
    # Explicit fine-tuning attaches to target properties, not a free role atom.
    target_role = "fine_tuning" if positive_phrase(question, r"fine[- ]?tun\w*|微调") else ""
    # A PES fit requires co-labelled configurations, not labels stitched from
    # unrelated datasets. Other multi-property benchmarks may use separate tasks.
    joint = len(set(props) & {"energy", "forces", "stresses", "magnetic_moments"}) >= 2 and positive_phrase(question, r"potential energy surface|interatomic potential|势能面|原子间势|同时含|jointly")
    groups = [props] if joint or not props else [[p] for p in props]
    # Do not make model goals (e.g. lower training cost) hard dataset filters.
    # Unparsed constraints remain visible in diagnostics for human review.
    constraints = [str(c) for c in getattr(plan, "constraints", [])
                   if re.search(r"\b[ABX]\s*=|\bABX3\b|\b(?:temperature|pressure|sample count)\b.*\d|温度.*\d|压力.*\d", str(c), re.I)]
    needs = []
    # A list of domains and a list of labels do NOT imply their Cartesian
    # product. Require target labels plus domain coverage as separate needs.
    for group in groups:
        needs.append(Need(f"N{len(needs)+1}", group, fields,
                          materials if len(materials) == 1 else [], provenance, target_role, constraints))
    if len(materials) > 1:
        for material in materials:
            needs.append(Need(f"N{len(needs)+1}", [], [], [material], provenance, "", []))
    # Keep source needs independent of target labels in cross-property transfer.
    if positive_phrase(question, r"pre[- ]?train\w*|预训练"):
        needs.append(Need(f"N{len(needs)+1}", [], [], [], "", "pretraining", []))
    if positive_phrase(question, r"standardized.*evaluation|fair.*comparison|标准化评估|benchmark suite|基准套件"):
        needs.append(Need(f"N{len(needs)+1}", [], [], [], "", "benchmark_suite", []))
    elif positive_phrase(question, r"benchmark|baseline comparison|compare.*models|基准比较|基准对比"):
        needs.append(Need(f"N{len(needs)+1}", [], [], [], "", "benchmark", []))
    if positive_phrase(question, r"external validation|independent validation|外部验证|独立验证"):
        needs.append(Need(f"N{len(needs)+1}", [], [], materials, "", "validation", []))
    return needs


def match_use(need, use, dataset=None):
    # All facts below belong to this one use. No parent profile/Task union.
    quotes = [e.get("text", "") for e in use.get("evidence", []) if not e.get("inferred", False)]
    text = " ".join([str(use.get("purpose") or ""), str(use.get("construction_method") or ""),
                     " ".join(use.get("filter_conditions", [])), " ".join(quotes)])
    local_text = " ".join([str(use.get("purpose") or ""), str(use.get("construction_method") or ""),
                           " ".join(use.get("filter_conditions", [])), " ".join(use.get("used_fields", []))])
    available = concepts(use.get("used_fields", []))
    # Text/registry hints increase conditional utility, not verified coverage.
    # Purpose text can name the OUTPUT of an analysis, not a dataset column.
    # Only quoted sentences explicitly describing supplied labels form hints.
    label_sentences = [sentence for quote in quotes for sentence in re.split(r"[.;。；]", quote)
                       if re.search(r"contain|provid|compris|annotat|label|include|字段|包含|提供|标签", sentence, re.I)]
    hints = {name for name, pattern in ALIASES.items()
             if any(positive_phrase(sentence, pattern) for sentence in label_sentences)}
    dataset = dataset or {}
    profile = concepts(dataset.get("available_properties", []) + dataset.get("available_fields", []))
    missing = sorted((set(need.properties) | set(need.fields)) - available)
    if not quotes:
        missing.append("non_inferred_evidence")
    for material in need.materials:
        # A quote can list multiple databases. A domain must agree with this
        # dataset's scope or use-local fields/purpose, not another quoted dataset.
        own_scope = " ".join(dataset.get("material_scope", []))
        local_material = positive_phrase(local_text, MATERIALS[material])
        quote_material = positive_phrase(text, MATERIALS[material])
        scoped_material = positive_phrase(own_scope, MATERIALS[material])
        if not (local_material or (quote_material and (scoped_material or not own_scope))):
            missing.append("material:" + material)
    conflict = []
    experimental = positive_phrase(text, r"experiment\w*|实验")
    computed = positive_phrase(text, r"\bDFT\b|density.functional|computed|computational|计算")
    if need.provenance:
        own, opposite = (experimental, computed) if need.provenance == "experimental" else (computed, experimental)
        if not own:
            (conflict if opposite else missing).append("provenance:" + need.provenance)
        elif opposite:
            missing.append("ambiguous_mixed_provenance")
    role = str(use.get("usage_role", "")).lower()
    role_patterns = {
        "pretraining": r"pre[- ]?train\w*|预训练",
        "fine_tuning": r"fine[- ]?tun\w*|微调",
        "benchmark": r"benchmark|baseline|基准|对比",
        "benchmark_suite": r"benchmark suite|suite|multiple (?:prediction )?tasks|基准套件",
        "validation": r"validat\w*|independent test|验证",
    }
    role_exact = {"pretraining": {"pretraining", "pretraining_source"},
                  "fine_tuning": {"fine_tuning", "fine_tuning_target"},
                  "benchmark": {"benchmark"}, "benchmark_suite": {"benchmark_suite"}, "validation": {"validation"}}
    if need.role:
        role_match = role in role_exact[need.role] or positive_phrase(local_text, role_patterns[need.role])
        if need.role == "pretraining":
            # "Fine-tune the pre-trained model" is a target use, not a source.
            target_use = positive_phrase(local_text, r"fine[- ]?tun|微调")
            role_match = role in role_exact[need.role] or (not target_use and
                (positive_phrase(local_text, r"pre[- ]?training|pre[- ]?train\s+(?:on|a |the |model)|预训练") or
                 positive_phrase(" ".join(quotes), r"pre[- ]?training (?:source|data)|used (?:for|to) pre[- ]?train")))
        elif need.role == "benchmark_suite":
            role_match = role_match or (not use.get("is_derived", False) and
                positive_phrase(" ".join(quotes), role_patterns[need.role]))
        if not role_match:
            missing.append("role:" + need.role)
    # Unparsed fine constraints remain explicitly unknown. Do not silently
    # turn ABX3 species/fractions into a verified generic-perovskite match.
    for constraint in need.constraints or []:
        normalized = re.sub(r"\s+", " ", constraint).lower()
        if normalized not in re.sub(r"\s+", " ", text).lower():
            missing.append("constraint:" + constraint)
    evidence_hits = len((set(need.properties) | set(need.fields)) & available)
    requested = set(need.properties) | set(need.fields)
    material_hits = sum("material:" + m not in missing for m in need.materials)
    # Input compatibility cannot substitute for an output label. In particular,
    # composition alone says nothing about synthesizability ground truth.
    label_hits = set(need.properties) & (available | hints)
    relevant = (bool(label_hits) if need.properties else evidence_hits > 0) or (not requested and (
        (bool(need.role) and "role:" + need.role not in missing) or material_hits > 0))
    # A profile alone cannot rescue an unrelated use. Profile support is only
    # available when this use has at least one query-related field or role.
    targets = set(need.properties) or requested
    direct_fraction = len(targets & available) / len(targets) if targets else float(relevant)
    hint_fraction = len(targets & (available | hints)) / len(targets) if targets else float(relevant)
    profile_fraction = len(targets & (available | profile)) / len(targets) if targets else float(relevant)
    utility = max(direct_fraction, 0.65 * hint_fraction, 0.45 * profile_fraction if relevant else 0.0)
    if not quotes:
        utility *= 0.5
    if need.fields and not set(need.fields) <= available:
        utility *= 0.85
    # Missing scope is a confidence discount; it is not a veto. Matching
    # Dataset scope can corroborate missing use metadata but remains conditional.
    for material in need.materials:
        if "material:" + material in missing:
            scope = " ".join(dataset.get("material_scope", []))
            utility *= 0.85 if positive_phrase(scope, MATERIALS[material]) else 0.55
    if need.role and "role:" + need.role in missing:
        utility = 0.0
    if need.provenance and any("provenance" in m for m in missing):
        utility *= 0.65
    if any(m.startswith("constraint:") for m in missing):
        utility *= 0.85
    status = "conflict" if conflict else "supported" if not missing and relevant else "unknown" if relevant else "irrelevant"
    utility = 0.0 if status in {"conflict", "irrelevant"} else 1.0 if status == "supported" else min(0.85, utility)
    return {"status": status, "use_id": use["dataset_use_id"], "missing": missing,
            "utility": utility, "profile_hint_fields": sorted(requested & profile - available),
            "text_hint_fields": sorted(requested & hints - available),
            "conflicts": conflict, "matched_fields": sorted(available & (set(need.properties) | set(need.fields))),
            "paper_id": use.get("paper_id"), "evidence": quotes}


def select_scoped(*, store, plan, question, ranked, max_results, candidate_top_k,
                  beam_width=128, family_overrides=None):
    needs = make_needs(plan, question)
    pool = ranked[:max(0, candidate_top_k)]
    matrix = {}
    vectors = {}
    decision_vectors = {}
    provisional = []
    for candidate in pool:
        dataset = store.dataset_by_id[candidate.dataset_id]
        cells = {}
        for need in needs:
            matches = [match_use(need, store.use_by_id[u], dataset) for u in sorted(candidate.supporting_use_ids) if u in store.use_by_id]
            priority = {"supported": 3, "unknown": 2, "conflict": 1, "irrelevant": 0}
            matches.sort(key=lambda m: (m["utility"], priority[m["status"]], -len(m["missing"]), m["use_id"]), reverse=True)
            cells[need.need_id] = matches[0] if matches else {"status": "irrelevant", "utility": 0.0, "missing": ["no_use_evidence"]}
        # Private/paper-specific identities must not silently become public parents.
        usable = dataset.get("availability") not in {"private", "unavailable"} and dataset.get("recommendable") is not False
        matrix[candidate.dataset_id] = {"usable": usable, "needs": cells}
        vectors[candidate.dataset_id] = tuple(cells[n.need_id]["utility"] if usable else 0.0 for n in needs)
        # Semantic score qualifies evidence gains; adding a dataset has no
        # unconditional score reward. This prevents tiny gains buying many FPs.
        reliability = 0.8 + 0.2 * min(1.0, max(0.0, float(candidate.final_score)))
        decision_vectors[candidate.dataset_id] = tuple(v * reliability for v in vectors[candidate.dataset_id])
        if any(c["status"] == "unknown" for c in cells.values()) or not usable:
            provisional.append(candidate.dataset_id)

    # Choose one concrete representative per source family using this query's
    # own DatasetUse evidence. Family membership expands recall but supplies no
    # capability evidence. Prefer support, then total utility, then retrieval.
    family_overrides = family_overrides or {}
    family_groups = defaultdict(list)
    for candidate in pool:
        family_groups[family_id(store, candidate.dataset_id, family_overrides)].append(candidate)
    family_choices = []
    family_removed = []
    for fid, members in family_groups.items():
        def member_key(candidate):
            cells = matrix[candidate.dataset_id]["needs"]
            return (
                sum(cell["status"] == "supported" for cell in cells.values()),
                sum(vectors[candidate.dataset_id]),
                candidate.final_score,
                candidate.dataset_id,
            )
        winner = max(members, key=member_key)
        family_choices.append(winner)
        for member in members:
            if member.dataset_id != winner.dataset_id:
                family_removed.append({
                    "family_id": fid,
                    "dataset_id": member.dataset_id,
                    "kept_dataset_id": winner.dataset_id,
                    "reason": "lower_query_specific_evidence_within_family",
                })
    original_position = {candidate.dataset_id: i for i, candidate in enumerate(pool)}
    pool = sorted(family_choices, key=lambda candidate: original_position[candidate.dataset_id])
    # Soft evidence coverage, not cardinality-first set cover. A new candidate
    # can improve an uncertain need even if another candidate already touches it.
    # The cost stops redundant additions; there is no forced minimum result count.
    cost = 0.18
    relevance_weight = 0.2
    states = {(tuple(0.0 for _ in needs), ()): 0.0}
    def objective(item):
        (coverage, chosen), quality = item
        return sum(coverage) - cost * len(chosen)
    for index, candidate in enumerate(pool):
        vector = decision_vectors[candidate.dataset_id]
        if not any(vector):
            continue
        expanded = dict(states)
        for (covered, chosen), quality in states.items():
            improved = tuple(max(a, b) for a, b in zip(covered, vector))
            if len(chosen) < max_results and improved != covered:
                key = (improved, chosen + (index,))
                expanded[key] = quality + min(1.0, max(0.0, float(candidate.final_score)))
        ordered = sorted(expanded.items(), key=lambda item: (-objective(item), len(item[0][1]), item[0][1]))
        states = dict(ordered[:max(1, beam_width)])
    (coverage, indices), _ = min(states.items(), key=lambda item: (-objective(item), len(item[0][1]), item[0][1]))
    selected = [pool[i] for i in indices]
    # Rank the chosen set by its marginal contribution, not registry/pool order.
    ordered_selected, remaining = [], list(selected)
    running = tuple(0.0 for _ in needs)
    while remaining:
        best = max(remaining, key=lambda c: (
            sum(max(0.0, b-a) for a,b in zip(running, decision_vectors[c.dataset_id])),
            c.final_score, c.dataset_id))
        ordered_selected.append(best)
        running = tuple(max(a,b) for a,b in zip(running, decision_vectors[best.dataset_id]))
        remaining.remove(best)
    selected = ordered_selected
    fallback = []
    if not selected and needs:
        # Empty-result fallback: return a small, explicitly unverified set.
        # It may use input/domain evidence, but never upgrades a missing target
        # label to supported. Explicit conflicts and unusable datasets remain
        # excluded. This preserves an actionable answer without a false claim.
        fallback_ranked = []
        for candidate in pool:
            row = matrix[candidate.dataset_id]
            if not row["usable"]:
                continue
            cells = row["needs"]
            if any(cell["status"] == "conflict" for cell in cells.values()):
                continue
            matched = 0
            unknown = 0
            missing_count = 0
            for need in needs:
                cell = cells[need.need_id]
                matched += len(cell.get("matched_fields", []))
                matched += sum("material:" + material not in cell.get("missing", [])
                               for material in need.materials)
                matched += int(bool(need.role) and "role:" + need.role not in cell.get("missing", []))
                unknown += int(cell["status"] == "unknown")
                missing_count += len(cell.get("missing", []))
            if matched <= 0:
                continue
            fallback_ranked.append((matched, unknown, -missing_count, candidate.final_score, candidate))
        fallback_ranked.sort(key=lambda item: item[:-1], reverse=True)
        # At most two different families: enough to expose complementary data
        # sources while keeping the fallback conservative.
        seen_families = set()
        for item in fallback_ranked:
            candidate = item[-1]
            fid = family_id(store, candidate.dataset_id, family_overrides)
            if fid in seen_families:
                continue
            selected.append(candidate)
            seen_families.add(fid)
            fallback.append({
                "dataset_id": candidate.dataset_id,
                "family_id": fid,
                "status": "unverified_fallback",
                "matched_requirement_count": item[0],
                "reason": "no_fully_or_conditionally_supported_portfolio",
            })
            if len(selected) >= min(2, max_results):
                break
    portfolio = list(selected)
    # Dataset search and minimum portfolio answer different questions. Retain
    # one independently qualified close alternative per portfolio member, with
    # explicit substitution metadata. Do not silently count it as necessary.
    alternatives = []
    used = {c.dataset_id for c in selected}
    def lineage(dataset_id):
        seen = set()
        while dataset_id not in seen:
            seen.add(dataset_id)
            parent = store.dataset_by_id.get(dataset_id, {}).get("source_dataset_id")
            if not parent or parent not in store.dataset_by_id:
                return dataset_id
            dataset_id = parent
        return min(seen)
    for primary in ([] if fallback else portfolio):
        if len(selected) >= max_results:
            break
        # Substitute the member's contribution to THIS portfolio, not every
        # capability it happens to have (other members may already supply it).
        other_coverage = tuple(max((vectors[c.dataset_id][i] for c in portfolio if c.dataset_id != primary.dataset_id),
                                   default=0.0) for i in range(len(needs)))
        required_indices = [i for i,v in enumerate(vectors[primary.dataset_id]) if v >= 0.65 and v > other_coverage[i]]
        if not required_indices:
            continue
        eligible = [c for c in pool if c.dataset_id not in used
                    and lineage(c.dataset_id) != lineage(primary.dataset_id)
                    and c.final_score >= 0.95 * primary.final_score
                    and all(vectors[c.dataset_id][i] >= vectors[primary.dataset_id][i] for i in required_indices)]
        if eligible:
            alternative = max(eligible, key=lambda c: (c.final_score, sum(vectors[c.dataset_id]), c.dataset_id))
            selected.append(alternative)
            used.add(alternative.dataset_id)
            alternatives.append({"dataset_id": alternative.dataset_id, "alternative_to": primary.dataset_id,
                                 "need_ids": [needs[i].need_id for i in required_indices],
                                 "reason": "independent_source_with_comparable_evidence_and_semantic_score"})
    coverage = tuple(max((vectors[c.dataset_id][i] for c in selected), default=0.0) for i in range(len(needs)))
    diagnostics = {"mode": "scoped", "algorithm": "family_evidence_scoped_recommendation_v5", "beam_width": beam_width,
                   "decision_states": ["supported", "unknown", "conflict", "irrelevant"],
                   "fallback_used": bool(fallback), "fallback_candidates": fallback,
                   "family_representative_policy": "max_supported_then_utility_then_retrieval",
                   "family_representative_removed": family_removed,
                   "portfolio_dataset_ids": [c.dataset_id for c in portfolio], "alternatives": alternatives,
                   "ranking_policy": "marginal_evidence_gain",
                   "selection_cost": cost, "relevance_weight": relevance_weight,
                   "need_support_scores": {n.need_id: coverage[i] for i, n in enumerate(needs)},
                   "conditional_selected_dataset_ids": [c.dataset_id for c in selected if not any(
                       v["status"] == "supported" for v in matrix[c.dataset_id]["needs"].values())],
                   "unparsed_query_constraints": [str(c) for c in getattr(plan, "constraints", [])
                                                   if not any(str(c) in (n.constraints or []) for n in needs)],
                   "needs": [asdict(n) for n in needs], "candidate_evidence": matrix,
                   "covered_needs": [n.need_id for i, n in enumerate(needs) if coverage[i] >= 1.0],
                   "partially_supported_needs": [n.need_id for i, n in enumerate(needs) if 0 < coverage[i] < 1],
                   "uncovered_needs": [n.need_id for i, n in enumerate(needs) if coverage[i] < 1.0],
                   "provisional_dataset_ids": [i for i in provisional if i not in {c.dataset_id for c in selected}],
                   "selected_size": len(selected), "candidate_pool_size": len(pool),
                   "coverage_semantics": "support in a single extracted use; not sample-level data validation",
                   "selection_reason": "empty_result_unverified_fallback" if fallback else
                       "all_parsed_needs_supported" if all(v >= 1 for v in coverage) else "conditional_or_partial_recommendation"}
    return selected, diagnostics


def scoped_answer(store, selected, diagnostics):
    lines = ["以下推荐结合使用证据与数据集元数据；有条件推荐不代表已满足全部需求，实际字段配对和可下载性仍需核实。", ""]
    matrix = diagnostics["candidate_evidence"]
    for candidate in selected:
        ds = store.dataset_by_id[candidate.dataset_id]
        fallback = next((a for a in diagnostics.get("fallback_candidates", [])
                         if a["dataset_id"] == candidate.dataset_id), None)
        alternative = next((a for a in diagnostics.get("alternatives", []) if a["dataset_id"] == candidate.dataset_id), None)
        suffix = "；兜底候选，相关但尚未验证可完成任务" if fallback else (
            f"；可替代 {alternative['alternative_to']}，不表示必须同时使用" if alternative else "；主组合")
        lines.append(f"- {ds['canonical_name']}（{candidate.dataset_id}{suffix}）")
        for need_id, cell in matrix[candidate.dataset_id]["needs"].items():
            if cell["status"] == "supported":
                lines.append(f"  支持 {need_id}；证据：{cell['use_id']} / {cell.get('paper_id', '')}。")
            elif cell.get("utility", 0) > 0:
                lines.append(f"  有条件支持 {need_id}；依据：{cell['use_id']}；仍需核实：{'；'.join(cell['missing'])}。")
        lines.append("  适用范围限于上述使用记录，不代表该数据库的所有数据或其他版本。")
    if not selected:
        lines.append("当前候选中没有证据足够完整的正式推荐；这不等于知识库中没有可用数据。")
    lines.append("\n需求定义：")
    for n in diagnostics["needs"]:
        lines.append(f"- {n['need_id']}: 性质={n['properties']}；输入={n['fields']}；材料={n['materials']}；来源={n['provenance'] or '未限定'}；用途={n['role'] or '未限定'}；约束={n['constraints'] or []}")
    if diagnostics["uncovered_needs"]:
        lines.append("\n尚无充分证据的需求：" + ", ".join(diagnostics["uncovered_needs"]))
    if diagnostics.get("unparsed_query_constraints"):
        lines.append("\n以下任务描述尚未转为可核验的数据条件，不能据此宣称完整完成任务：" + "; ".join(diagnostics["unparsed_query_constraints"]))
    if diagnostics["provisional_dataset_ids"]:
        lines.append("\n待核实候选（不计入正式推荐）：")
        for dataset_id in diagnostics["provisional_dataset_ids"][:5]:
            missing = sorted({m for c in matrix[dataset_id]["needs"].values() if c["status"] == "unknown" for m in c["missing"]})
            lines.append(f"- {store.dataset_by_id[dataset_id]['canonical_name']}: " + "; ".join(missing or ["公开可用性/身份需要核实"]))
    return "\n".join(lines)


def reserve_need_pairs(store, plan, question, discovered, ranked, limit):
    """Reserve one evidenced route per demand before expensive pair reranking.

    Uses graph-discovered pairs only; never injects held-out labels or new data.
    The reserved routes share the existing budget, then semantic rank fills it.
    """
    needs = make_needs(plan, question)
    best = {}
    for pair in discovered.values():
        dataset = store.dataset_by_id[pair.dataset_id]
        for need in needs:
            cells = [match_use(need, store.use_by_id[u], dataset) for u in pair.supporting_use_ids if u in store.use_by_id]
            utility = max((c["utility"] for c in cells), default=0.0)
            if utility <= 0:
                continue
            key = (utility, pair.pair_seed_score, pair.pair_id)
            if need.need_id not in best or key > best[need.need_id][0]:
                best[need.need_id] = (key, pair)
    selected, seen = [], set()
    for pair in [best[n.need_id][1] for n in needs if n.need_id in best] + list(ranked):
        if pair.pair_id not in seen and len(selected) < max(1, limit):
            selected.append(pair)
            seen.add(pair.pair_id)
    selected.sort(key=lambda p: (p.pair_seed_score, p.pair_id), reverse=True)
    return selected, {"need_routes": {n: p.pair_id for n, (_, p) in best.items()},
                      "selected_pair_ids": [p.pair_id for p in selected],
                      "budget": limit, "uses_heldout_labels": False}
