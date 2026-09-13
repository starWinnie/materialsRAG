# 24_Structure_Aware_Transfer_Learning - Materials Project (MP)

## Dataset Use

A large-scale DFT-computed database containing ~140,000 inorganic crystalline materials with relaxed crystal structures (POSCAR files) and computed properties including formation energy, bandgap, elastic tensors, and more. In this paper, it serves as the *source dataset*: its formation energy labels and 3D crystal structures are used to pre-train the ALIGNN source model for transfer learning across diverse target properties and material classes.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning_paper_a9ca0fbfd8f7.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1_task_25b6baf65d50.md)
- Dataset: [Materials Project (MP)](../datasets/Materials_Project_MP_dataset_9b0af3c4a714.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_d0e53778f61f`
- Original dataset title: Materials Project (MP)
- Tags: materials property prediction, transfer learning, structure-aware modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
