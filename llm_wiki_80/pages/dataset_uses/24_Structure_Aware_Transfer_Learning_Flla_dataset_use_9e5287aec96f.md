# 24_Structure_Aware_Transfer_Learning - Flla

## Dataset Use

A DFT-computed dataset of ~3,900 inorganic compounds with formation energy, hull energy, and atomic relaxation data. Used as a *target dataset* to assess transfer learning robustness across independently computed DFT databases with different computational settings; its properties (e.g., DeltaE, Ehull) are predicted using the MP-pretrained ALIGNN model.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1.md)
- Dataset: [Flla](../datasets/Flla.md)
- Dataset URL: https://github.com/hackingmaterials/automatminer

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_9e5287aec96f`
- Original dataset title: Flla
- Tags: materials property prediction, transfer learning, structure-aware modeling
