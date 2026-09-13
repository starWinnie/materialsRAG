# 05_Thermodynamic_Stability_Ensemble - Materials Project

## Dataset Use

A large-scale DFT-computed database containing thermodynamic properties (e.g., formation energy, decomposition energy) for 85,014 inorganic crystalline compounds, including experimentally observed and hypothetical materials. Used as the primary training and benchmarking dataset to train and evaluate the ECSG ensemble model for binary classification of compound stability; also used to construct convex hulls for ΔHd labeling and to extract composition-only samples for sample efficiency analysis.

## Links

- Paper: [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble.md)
- Task: [task page](../tasks/05_Thermodynamic_Stability_Ensemble_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting the thermodynamic stability of inorganic compounds by classifying them as stable or unstable based on decomposition energy (ΔHd), where compounds with ΔHd ≤ 0 meV/atom (or relaxed thresholds of 25/40 meV/atom) are labeled stable — enabling high-throughput screening of viable candidates in unexplored compositional spaces.

## Metadata

- Dataset use ID: `dataset_use_75e15c27a639`
- Original dataset title: Materials Project (MP)
- Tags: thermodynamic stability prediction, compound stability classification, decomposition energy estimation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
