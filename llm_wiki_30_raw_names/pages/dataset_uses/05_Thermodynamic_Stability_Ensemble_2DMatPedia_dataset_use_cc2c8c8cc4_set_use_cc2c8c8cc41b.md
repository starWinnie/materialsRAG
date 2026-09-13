# 05_Thermodynamic_Stability_Ensemble - 2DMatPedia

## Dataset Use

A computational database of 4,743 2D materials with precomputed bandgaps and stability labels derived from DFT. Used as an independent test set to evaluate ECSG’s stability predictions for 2D materials and to validate the joint screening pipeline (ECSG + DARWIN-7B LLM) for wide-bandgap semiconductors, yielding 313 experimentally stable candidates out of 393 predicted.

## Links

- Paper: [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble_paper_dfa00819e2d0.md)
- Task: [task page](../tasks/05_Thermodynamic_Stability_Ensemble_task_1_task_134b6e57d77b.md)
- Dataset: [2DMatPedia](../datasets/2DMatPedia_dataset_fb64b91da67e.md)
- Dataset URL: None

## Task Context

Predicting the thermodynamic stability of inorganic compounds by classifying them as stable or unstable based on decomposition energy (ΔHd), where compounds with ΔHd ≤ 0 meV/atom (or relaxed thresholds of 25/40 meV/atom) are labeled stable — enabling high-throughput screening of viable candidates in unexplored compositional spaces.

## Metadata

- Dataset use ID: `dataset_use_cc2c8c8cc41b`
- Original dataset title: 2DMatPedia
- Tags: thermodynamic stability prediction, compound stability classification, decomposition energy estimation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
