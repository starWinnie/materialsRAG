# 24_Structure_Aware_Transfer_Learning - Materials Project

## Dataset Use

A large-scale DFT-computed database containing ~140,000 inorganic crystalline materials with relaxed crystal structures (POSCAR files) and computed properties including formation energy, bandgap, elastic tensors, and more. In this paper, it serves as the *source dataset*: its formation energy labels and 3D crystal structures are used to pre-train the ALIGNN source model for transfer learning across diverse target properties and material classes.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_adb846e44575`
- Original dataset title: Materials Project (MP)
- Tags: materials property prediction, transfer learning, structure-aware modeling
