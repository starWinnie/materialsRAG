# Inorganic Crystal Structure Database

## Metadata

- Dataset ID: `dataset_0d530002ad88`
- Aliases: ICSD (Inorganic Crystal Structure Database), Inorganic Crystal Structure Database (ICSD)
- Links: https://doi.org/10.18434/M32147, https://icsd.fiz-karlsruhe.de, https://icsd.products.fiz-karlsruhe.de/
- Used by papers: 4
- Dataset usage records: 4

## Description Examples

- The ICSD contains over 200,000 experimentally determined ordered and disordered inorganic crystal structures. In this paper, it serves two roles: (1) as the source of structural data used to construct SuperCon3D via matching with SuperCon entries; and (2) as the external candidate pool for high-Tc screening — SODNet is applied to predict Tc for ~200k ICSD entries (including disordered ones), yielding 27 prioritized candidates (e.g., Ba1.1432Co0.1429O3.0009Rh0.8574, ErH3) for experimental follow-up. Thus, ICSD supports both dataset construction and real-world superconductor screening.
- An experimental database of >200,000 published inorganic crystal structures, with ~20,000 computationally stable entries. Used exclusively for *validation*: 736 experimentally realized ICSD structures were matched to GNoME predictions to confirm real-world synthesizability and validate model accuracy, serving as ground-truth experimental evidence for discovered stability.
- A curated repository of experimentally determined crystal structures for ~10^5 known solid-state materials. In this paper, it is cited as the primary source of experimental structural data underlying many entries in the Materials Project; MP entries are stated to be 'the majority of which are in the ICSD', and ICSD-derived stability bias is explicitly analyzed when interpreting false positive rates in materials discovery contexts.
- A curated repository of experimentally synthesized and structurally characterized inorganic crystalline materials. The paper uses 53,594 unique binary, ternary, and quaternary compositions (8,194 binaries, 26,218 ternaries, 19,182 quaternaries) with integer stoichiometric coefficients, extracted from ICSD in October 2020. These serve as positive labeled examples (‘synthesized’) for training and evaluating the SynthNN model’s ability to predict synthesizability.

## Uses

- [31_Superconductivity_Ordered_Disordered](../dataset_uses/31_Superconductivity_Ordered_Disordered_Inorganic_Crystal_Structure_Database_dataset_use_e.md): [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered.md), [task](../tasks/31_Superconductivity_Ordered_Disordered_task_1.md)
- [34_GNoME](../dataset_uses/34_GNoME_Inorganic_Crystal_Structure_Database_dataset_use_8d4d6ddfa002.md): [34 GNoME](../papers/34_GNoME.md), [task](../tasks/34_GNoME_task_1.md)
- [43_Formation_Energy_Stability_Critical](../dataset_uses/43_Formation_Energy_Stability_Critical_Inorganic_Crystal_Structure_Database_dataset_use_02.md): [43 Formation Energy Stability Critical](../papers/43_Formation_Energy_Stability_Critical.md), [task](../tasks/43_Formation_Energy_Stability_Critical_task_1.md)
- [44_Synthesizability_Crystalline_Inorganic](../dataset_uses/44_Synthesizability_Crystalline_Inorganic_Inorganic_Crystal_Structure_Database_dataset_use.md): [44 Synthesizability Crystalline Inorganic](../papers/44_Synthesizability_Crystalline_Inorganic.md), [task](../tasks/44_Synthesizability_Crystalline_Inorganic_task_1.md)
