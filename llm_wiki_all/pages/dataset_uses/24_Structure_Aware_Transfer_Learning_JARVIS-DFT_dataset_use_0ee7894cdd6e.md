# 24_Structure_Aware_Transfer_Learning - JARVIS-DFT

## Dataset Use

A DFT-computed database of ~55,000 3D crystalline materials with atomic structures and 46 distinct properties (e.g., bulk modulus, dielectric tensor, piezoelectric coefficients, bandgap). It is used as a *target dataset* for evaluating transfer learning performance — specifically, its formation energy, bandgap, and other solid-state properties are predicted using models fine-tuned or feature-extracted from the MP-pretrained ALIGNN model.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1.md)
- Dataset: [JARVIS-DFT](../datasets/JARVIS-DFT.md)
- Dataset URL: https://jarvis.nist.gov

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_0ee7894cdd6e`
- Original dataset title: JARVIS-3D
- Tags: materials property prediction, transfer learning, structure-aware modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
