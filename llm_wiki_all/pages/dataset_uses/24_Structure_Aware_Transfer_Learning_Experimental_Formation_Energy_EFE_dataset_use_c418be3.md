# 24_Structure_Aware_Transfer_Learning - Experimental Formation Energy (EFE)

## Dataset Use

An experimental dataset of 605 intermetallic compounds with measured formation enthalpies (DeltaE) derived from calorimetry. Functions as a *target dataset* to validate transfer learning on real-world experimental data — the MP-pretrained ALIGNN model is adapted to predict experimental formation energies, bridging computation-to-experiment gaps.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1.md)
- Dataset: [Experimental Formation Energy (EFE)](../datasets/Experimental_Formation_Energy_EFE.md)
- Dataset URL: https://github.com/hackingmaterials/automatminer

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_c418be32b058`
- Original dataset title: Experimental Formation Energy (EFE)
- Tags: materials property prediction, transfer learning, structure-aware modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
