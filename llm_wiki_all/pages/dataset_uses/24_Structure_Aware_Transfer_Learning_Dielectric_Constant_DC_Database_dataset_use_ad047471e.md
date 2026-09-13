# 24_Structure_Aware_Transfer_Learning - Dielectric Constant (DC) Database

## Dataset Use

A DFT-computed dataset of ~1,000 inorganic materials with dielectric properties (static/dynamic dielectric tensors, refractive index, polarizability) and structural information. Serves as a *target dataset* for predicting low-data-count dielectric properties (e.g., volume, bandgap, N, poly-electric susceptibility) using transfer learning from MP, enabling validation on physically distinct property types.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1.md)
- Dataset: [Dielectric Constant (DC) Database](../datasets/Dielectric_Constant_DC_Database.md)
- Dataset URL: https://github.com/hackingmaterials/automatminer

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_ad047471e51a`
- Original dataset title: Dielectric Constant (DC) Database
- Tags: materials property prediction, transfer learning, structure-aware modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
