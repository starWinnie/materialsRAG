# 43_Formation_Energy_Stability_Critical - Task 1

## Task Description

Predicting the thermodynamic stability of inorganic crystalline solids by estimating their decomposition enthalpy (ΔHd), i.e., determining whether a given compound lies on the convex hull of formation enthalpies in its chemical space — a necessary condition for synthesizability — using machine-learned formation energies as input to convex hull construction.

## Metadata

- Task ID: `task_cfac0b638fce`
- Source paper: [43 Formation Energy Stability Critical](../papers/43_Formation_Energy_Stability_Critical.md)
- Tags: stability prediction, decomposition enthalpy, convex hull analysis, materials screening

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/43_Formation_Energy_Stability_Critical_Materials_Project_dataset_use_7d07ad670381.md)
- Original title in paper: Materials Project (MP) database
- Link: https://materialsproject.org

A publicly available database of DFT-calculated thermodynamic properties for 85,014 unique inorganic crystalline solids, including formation enthalpy per atom (ΔHf) and ground-state crystal structures. In this paper, it is used to compute reference decomposition enthalpies (ΔHd) via convex hull construction in composition space, serving as the ground truth for evaluating ML models’ ability to predict stability; all analyses — including cross-validation, sparse-space testing (e.g., Li–Mn–TM–O), and error cancellation quantification — rely exclusively on MP’s ΔHf and structural data.

### [Inorganic Crystal Structure Database](../datasets/Inorganic_Crystal_Structure_Database.md)

- Usage page: [usage note](../dataset_uses/43_Formation_Energy_Stability_Critical_Inorganic_Crystal_Structure_Database_dataset_use_02.md)
- Original title in paper: Inorganic Crystal Structure Database (ICSD)
- Link: https://icsd.fiz-karlsruhe.de

A curated repository of experimentally determined crystal structures for ~10^5 known solid-state materials. In this paper, it is cited as the primary source of experimental structural data underlying many entries in the Materials Project; MP entries are stated to be 'the majority of which are in the ICSD', and ICSD-derived stability bias is explicitly analyzed when interpreting false positive rates in materials discovery contexts.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->
