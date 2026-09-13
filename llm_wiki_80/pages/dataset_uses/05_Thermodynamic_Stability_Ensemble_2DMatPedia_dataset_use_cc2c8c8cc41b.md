# 05_Thermodynamic_Stability_Ensemble - 2DMatPedia

## Dataset Use

A computational database of 4,743 2D materials with precomputed bandgaps and stability labels derived from DFT. Used as an independent test set to evaluate ECSG’s stability predictions for 2D materials and to validate the joint screening pipeline (ECSG + DARWIN-7B LLM) for wide-bandgap semiconductors, yielding 313 experimentally stable candidates out of 393 predicted.

## Links

- Paper: [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble.md)
- Task: [task page](../tasks/05_Thermodynamic_Stability_Ensemble_task_1.md)
- Dataset: [2DMatPedia](../datasets/2DMatPedia.md)
- Dataset URL: None

## Task Context

Predicting the thermodynamic stability of inorganic compounds by classifying them as stable or unstable based on decomposition energy (ΔHd), where compounds with ΔHd ≤ 0 meV/atom (or relaxed thresholds of 25/40 meV/atom) are labeled stable — enabling high-throughput screening of viable candidates in unexplored compositional spaces.

## Metadata

- Dataset use ID: `dataset_use_cc2c8c8cc41b`
- Original dataset title: 2DMatPedia
- Tags: thermodynamic stability prediction, compound stability classification, decomposition energy estimation
