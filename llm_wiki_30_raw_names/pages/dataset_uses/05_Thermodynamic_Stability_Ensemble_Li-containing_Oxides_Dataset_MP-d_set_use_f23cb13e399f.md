# 05_Thermodynamic_Stability_Ensemble - Li-containing Oxides Dataset (MP-derived)

## Dataset Use

A subset of 6,168 lithium-containing oxides (750 stable) extracted from the MP database, fully excluded from the MP training set to create a zero-shot evaluation scenario. Used to test ECSG’s predictive capability in a completely unfamiliar compositional space (Li–O systems), demonstrating its utility for cathode material discovery in Li-ion batteries.

## Links

- Paper: [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble_paper_dfa00819e2d0.md)
- Task: [task page](../tasks/05_Thermodynamic_Stability_Ensemble_task_1_task_134b6e57d77b.md)
- Dataset: [Li-containing Oxides Dataset (MP-derived)](../datasets/Li-containing_Oxides_Dataset_MP-derived_dataset_b8405d6f3030.md)
- Dataset URL: None

## Task Context

Predicting the thermodynamic stability of inorganic compounds by classifying them as stable or unstable based on decomposition energy (ΔHd), where compounds with ΔHd ≤ 0 meV/atom (or relaxed thresholds of 25/40 meV/atom) are labeled stable — enabling high-throughput screening of viable candidates in unexplored compositional spaces.

## Metadata

- Dataset use ID: `dataset_use_f23cb13e399f`
- Original dataset title: Li-containing Oxides Dataset (MP-derived)
- Tags: thermodynamic stability prediction, compound stability classification, decomposition energy estimation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
