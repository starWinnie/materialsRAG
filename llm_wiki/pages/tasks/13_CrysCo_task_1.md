# 13_CrysCo - Task 1

## Task Description

Predicting multiple inorganic materials properties—including energy-related properties (formation energy, energy above convex hull, band gap) and data-scarce mechanical properties (bulk modulus, shear modulus)—using a hybrid graph-transformer model that explicitly incorporates four-body atomic interactions to improve accuracy, generalization, and interpretability, especially under limited data conditions.

## Metadata

- Task ID: `task_f54c6e9beff9`
- Source paper: [13 CrysCo](../papers/13_CrysCo.md)
- Tags: property prediction, mechanical property prediction, thermodynamic stability prediction

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/13_CrysCo_Materials_Project_dataset_use_de1c07d75869.md)
- Original title in paper: Materials Project 2021 (MP21)
- Link: https://materialsproject.org

A publicly available DFT-computed database of inorganic materials containing 133,785 entries with crystal structures, compositions, and computed physical properties. It provides primary properties (e.g., formation energy per atom, band gap, energy above convex hull, Fermi energy) and secondary properties (e.g., bulk/shear moduli via Voigt-Reuss-Hill approximation, dielectric refractive index, phonon frequencies). In this paper, MP21 is used to train and benchmark the CrysCo model across eight regression tasks—serving as the source for both abundant primary-property data (e.g., ~126k formation energy samples) and scarce secondary-property data (e.g., only ~12k elasticity entries)—and enabling transfer learning from formation energy to mechanical properties.

### [In-house DFT-relaxed novel structures dataset](../datasets/In-house_DFT-relaxed_novel_structures_dataset.md)

- Usage page: [usage note](../dataset_uses/13_CrysCo_In-house_DFT-relaxed_novel_structures_dataset_dataset_use_2a8c8d9c10db.md)
- Original title in paper: In-house DFT-relaxed novel structures dataset
- Link: None

A custom dataset of 751 novel crystalline structures generated and DFT-relaxed internally by the authors. It contains ground-truth formation energies and energies above the convex hull computed via first-principles methods. This dataset is used exclusively for out-of-distribution evaluation—testing the model’s generalization capability on materials not present in the Materials Project—by predicting Ef and EHull and reporting parity plots, Pearson correlations (0.894 and 0.931), and MAEs (0.0318 and 0.0294 eV/atom), thereby validating real-world applicability for new material discovery.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
<!-- RD_STAGES_END -->
