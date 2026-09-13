# 24_Structure_Aware_Transfer_Learning - Kingsbury Experimental Bandgap (KEB)

## Dataset Use

An experimental dataset of 2,432 inorganic semiconductors and insulators with measured optical bandgaps. Serves as a *target dataset* for experimental electronic property prediction — the MP-pretrained ALIGNN model is transferred to predict experimental bandgaps, assessing robustness against measurement noise and methodology differences.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning_paper_a9ca0fbfd8f7.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1_task_25b6baf65d50.md)
- Dataset: [Kingsbury Experimental Bandgap (KEB)](../datasets/Kingsbury_Experimental_Bandgap_KEB_dataset_de06b5abdabd.md)
- Dataset URL: https://github.com/hackingmaterials/automatminer

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_91e22e8a1796`
- Original dataset title: Kingsbury Experimental Bandgap (KEB)
- Tags: materials property prediction, transfer learning, structure-aware modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
