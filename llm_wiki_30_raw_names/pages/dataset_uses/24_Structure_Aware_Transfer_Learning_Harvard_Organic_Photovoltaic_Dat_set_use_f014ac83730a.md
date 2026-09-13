# 24_Structure_Aware_Transfer_Learning - Harvard Organic Photovoltaic Dataset (HOPV)

## Dataset Use

A quantum-chemical dataset of 1,000+ organic molecules with SMILES strings and DFT-computed properties (24 total), including HOMO/LUMO energies, bandgaps, and photovoltaic metrics (e.g., scharber PCE, Jsc, Voc) under multiple functionals (B3LYP, PBE0, etc.). It functions as a *target dataset* for cross-material-class transfer learning — testing whether structure-aware features learned from inorganic crystals (MP) generalize to molecular systems for predicting organic electronic properties.

## Links

- Paper: [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning_paper_a9ca0fbfd8f7.md)
- Task: [task page](../tasks/24_Structure_Aware_Transfer_Learning_task_1_task_25b6baf65d50.md)
- Dataset: [Harvard Organic Photovoltaic Dataset (HOPV)](../datasets/Harvard_Organic_Photovoltaic_Dataset_HOPV_dataset_7bc0d43a09a6.md)
- Dataset URL: https://ndownloader.figshare.com/files/28814184

## Task Context

Predicting diverse materials properties (e.g., formation energy, bandgap, dielectric constant, piezoelectric tensor, exfoliation energy) from crystal or molecular structure inputs, especially when target datasets are small (<10,000 samples), by leveraging knowledge transferred from a large source dataset via structure-aware graph neural networks.

## Metadata

- Dataset use ID: `dataset_use_f014ac83730a`
- Original dataset title: Harvard Organic Photovoltaic Dataset (HOPV)
- Tags: materials property prediction, transfer learning, structure-aware modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
