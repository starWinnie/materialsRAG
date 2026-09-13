# 24_Structure_Aware_Transfer_Learning - JARVIS-2D

## Dataset Use

A DFT-computed database of ~1,000–2,000 2D layered materials (e.g., graphene, TMDs) with atomic structures and 32 properties including exfoliation energy, dielectric response, and electronic band structure metrics. It serves as a *target dataset* to test cross-dimensionality transfer learning: the MP-pretrained ALIGNN model is applied to predict properties of 2D materials, enabling evaluation of structural generalization beyond the 3D training domain.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1.md)
- Dataset: [JARVIS-2D](../datasets/JARVIS-2D.md)
- Dataset URL: https://jarvis.nist.gov

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_a1488a358518`
- Original dataset title: JARVIS-2D
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
