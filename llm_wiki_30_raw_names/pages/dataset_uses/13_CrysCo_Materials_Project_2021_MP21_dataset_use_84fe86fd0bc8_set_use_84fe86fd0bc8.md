# 13_CrysCo - Materials Project 2021 (MP21)

## Dataset Use

A publicly available DFT-computed database of inorganic materials containing 133,785 entries with crystal structures, compositions, and computed physical properties. It provides primary properties (e.g., formation energy per atom, band gap, energy above convex hull, Fermi energy) and secondary properties (e.g., bulk/shear moduli via Voigt-Reuss-Hill approximation, dielectric refractive index, phonon frequencies). In this paper, MP21 is used to train and benchmark the CrysCo model across eight regression tasks—serving as the source for both abundant primary-property data (e.g., ~126k formation energy samples) and scarce secondary-property data (e.g., only ~12k elasticity entries)—and enabling transfer learning from formation energy to mechanical properties.

## Links

- Paper: [13 CrysCo](../papers/13_CrysCo_paper_f11b018703ad.md)
- Task: [task page](../tasks/13_CrysCo_task_1_task_f54c6e9beff9.md)
- Dataset: [Materials Project 2021 (MP21)](../datasets/Materials_Project_2021_MP21_dataset_6786b1d74e0a.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting multiple inorganic materials properties—including energy-related properties (formation energy, energy above convex hull, band gap) and data-scarce mechanical properties (bulk modulus, shear modulus)—using a hybrid graph-transformer model that explicitly incorporates four-body atomic interactions to improve accuracy, generalization, and interpretability, especially under limited data conditions.

## Metadata

- Dataset use ID: `dataset_use_84fe86fd0bc8`
- Original dataset title: Materials Project 2021 (MP21)
- Tags: property prediction, mechanical property prediction, thermodynamic stability prediction

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
