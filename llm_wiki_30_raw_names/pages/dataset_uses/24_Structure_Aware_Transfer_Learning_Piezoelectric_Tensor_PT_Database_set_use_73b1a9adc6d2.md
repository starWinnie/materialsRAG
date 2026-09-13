# 24_Structure_Aware_Transfer_Learning - Piezoelectric Tensor (PT) Database

## Dataset Use

A DFT-computed dataset of ~940 non-centrosymmetric crystals with piezoelectric tensors, volumes, and related structural descriptors. Used as a *target dataset* to evaluate transfer learning on highly anisotropic, symmetry-sensitive properties (e.g., Eij piezoelectric coefficients, volume) where data scarcity limits conventional modeling — predictions rely on features transferred from the MP source model.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning_paper_a9ca0fbfd8f7.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1_task_25b6baf65d50.md)
- Dataset: [Piezoelectric Tensor (PT) Database](../datasets/Piezoelectric_Tensor_PT_Database_dataset_15268f4f647c.md)
- Dataset URL: https://github.com/hackingmaterials/automatminer

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_73b1a9adc6d2`
- Original dataset title: Piezoelectric Tensor (PT) Database
- Tags: materials property prediction, transfer learning, structure-aware modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
