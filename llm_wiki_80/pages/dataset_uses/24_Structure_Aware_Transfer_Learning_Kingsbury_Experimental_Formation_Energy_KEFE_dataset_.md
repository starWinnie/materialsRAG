# 24_Structure_Aware_Transfer_Learning - Kingsbury Experimental Formation Energy (KEFE)

## Dataset Use

An experimental dataset of 1,557 inorganic compounds with measured formation enthalpies, curated from literature sources. Used as a *target dataset* to further test transfer learning on experimental thermodynamics data — its DeltaE values are predicted using fine-tuning or feature extraction from the MP source model, demonstrating generalization beyond DFT artifacts.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1.md)
- Dataset: [Kingsbury Experimental Formation Energy (KEFE)](../datasets/Kingsbury_Experimental_Formation_Energy_KEFE.md)
- Dataset URL: https://github.com/hackingmaterials/automatminer

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_11fc222081ba`
- Original dataset title: Kingsbury Experimental Formation Energy (KEFE)
- Tags: materials property prediction, transfer learning, structure-aware modeling
