# 43_Formation_Energy_Stability_Critical - Materials Project

## Dataset Use

A publicly available database of DFT-calculated thermodynamic properties for 85,014 unique inorganic crystalline solids, including formation enthalpy per atom (ΔHf) and ground-state crystal structures. In this paper, it is used to compute reference decomposition enthalpies (ΔHd) via convex hull construction in composition space, serving as the ground truth for evaluating ML models’ ability to predict stability; all analyses — including cross-validation, sparse-space testing (e.g., Li–Mn–TM–O), and error cancellation quantification — rely exclusively on MP’s ΔHf and structural data.

## Links

- Paper: [43 Formation Energy Stability Critical](../papers/43_Formation_Energy_Stability_Critical.md)
- Task: [task page](../tasks/43_Formation_Energy_Stability_Critical_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting the thermodynamic stability of inorganic crystalline solids by estimating their decomposition enthalpy (ΔHd), i.e., determining whether a given compound lies on the convex hull of formation enthalpies in its chemical space — a necessary condition for synthesizability — using machine-learned formation energies as input to convex hull construction.

## Metadata

- Dataset use ID: `dataset_use_7d07ad670381`
- Original dataset title: Materials Project (MP) database
- Tags: stability prediction, decomposition enthalpy, convex hull analysis, materials screening

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
