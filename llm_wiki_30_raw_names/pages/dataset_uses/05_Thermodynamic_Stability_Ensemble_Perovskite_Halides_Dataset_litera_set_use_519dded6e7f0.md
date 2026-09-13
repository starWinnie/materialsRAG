# 05_Thermodynamic_Stability_Ensemble - Perovskite Halides Dataset (literature-curated)

## Dataset Use

A manually compiled dataset of thermodynamic stability labels for 496 perovskite halides (ABX₃, X = Cl/Br/I) extracted from prior literature; duplicates present in MP were removed to ensure independence. Used to evaluate ECSG’s generalization to unknown chemical space — specifically, its ability to predict stability for perovskite halides not represented in the MP training set.

## Links

- Paper: [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble_paper_dfa00819e2d0.md)
- Task: [task page](../tasks/05_Thermodynamic_Stability_Ensemble_task_1_task_134b6e57d77b.md)
- Dataset: [Perovskite Halides Dataset (literature-curated)](../datasets/Perovskite_Halides_Dataset_literature-curated_dataset_12a3418563ef.md)
- Dataset URL: None

## Task Context

Predicting the thermodynamic stability of inorganic compounds by classifying them as stable or unstable based on decomposition energy (ΔHd), where compounds with ΔHd ≤ 0 meV/atom (or relaxed thresholds of 25/40 meV/atom) are labeled stable — enabling high-throughput screening of viable candidates in unexplored compositional spaces.

## Metadata

- Dataset use ID: `dataset_use_519dded6e7f0`
- Original dataset title: Perovskite Halides Dataset (literature-curated)
- Tags: thermodynamic stability prediction, compound stability classification, decomposition energy estimation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
