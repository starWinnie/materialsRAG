# 23_CrysDiff - OQMD-EXP

## Dataset Use

A small experimental subset of OQMD containing 1,500 experimentally measured formation energies for crystalline materials — curated from literature and validated against synthesis outcomes. This dataset is used only in the experimental validation phase to assess how well CrysDiff mitigates DFT calculation bias: models are fine-tuned on combinations of DFT data (from JARVIS-DFT or OQMD) plus varying percentages (20% or 80%) of OQMD-EXP, then evaluated on held-out experimental formation energy values.

## Links

- Paper: [23 CrysDiff](../papers/23_CrysDiff_paper_0010b7688bb5.md)
- Task: [task page](../tasks/23_CrysDiff_task_1_task_1f1a85917ec8.md)
- Dataset: [OQMD-EXP](../datasets/OQMD-EXP_dataset_11b359c2e5db.md)
- Dataset URL: https://oqmd.org/

## Task Context

Predicting crystal properties (e.g., formation energy, bandgap, bulk modulus) from 3D crystal structures represented as atom types, fractional atomic coordinates, and lattice vectors — specifically by leveraging self-supervised pre-training on unlabeled crystal structures to improve data efficiency and accuracy in downstream regression tasks with sparse labeled data.

## Metadata

- Dataset use ID: `dataset_use_50ba78c0072e`
- Original dataset title: OQMD-EXP
- Tags: crystal property prediction, 3D structure-based regression, self-supervised pre-training

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
