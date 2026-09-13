# 32_Perovskite_Bandgap_Database - DFT-calculated bandgap dataset (PBE functional)

## Dataset Use

A custom computational dataset comprising 108 DFT-calculated bandgaps for mixed halide perovskites (e.g., FAPb(I1-xBrx)3, MAPb(I1-xBrx)3, CsPb(I1-xBrx)3, and multi-cation variants), generated using VASP with the PBE functional and structural models built via Pymatgen. This dataset was combined with experimental data to train transfer-learned models (e.g., Fine-Tuned MEGNet, Atomsets-MLP) to bridge accuracy gaps between DFT and experiment.

## Links

- Paper: [32 Perovskite Bandgap Database](../papers/32_Perovskite_Bandgap_Database.md)
- Task: [task page](../tasks/32_Perovskite_Bandgap_Database_task_1.md)
- Dataset: [DFT-calculated bandgap dataset (PBE functional)](../datasets/DFT-calculated_bandgap_dataset_PBE_functional.md)
- Dataset URL: None

## Task Context

Predicting the bandgaps of mixed ABX3 perovskites (where A = Cs, FA, or MA; B = Pb or Sn; X = Br, Cl, or I) with continuously varying compositions to enable thermodynamic modeling and prediction of light-induced halide segregation behavior under illumination.

## Metadata

- Dataset use ID: `dataset_use_8cfbc7b914aa`
- Original dataset title: DFT-calculated bandgap dataset (PBE functional)
- Tags: bandgap prediction, halide segregation prediction, perovskite property modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
