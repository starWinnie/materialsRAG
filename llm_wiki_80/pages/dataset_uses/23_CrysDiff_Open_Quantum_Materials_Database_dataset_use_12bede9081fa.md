# 23_CrysDiff - Open Quantum Materials Database

## Dataset Use

A small experimental subset of OQMD containing 1,500 experimentally measured formation energies for crystalline materials — curated from literature and validated against synthesis outcomes. This dataset is used only in the experimental validation phase to assess how well CrysDiff mitigates DFT calculation bias: models are fine-tuned on combinations of DFT data (from JARVIS-DFT or OQMD) plus varying percentages (20% or 80%) of OQMD-EXP, then evaluated on held-out experimental formation energy values.

## Links

- Paper: [23 CrysDiff](../papers/23_CrysDiff.md)
- Task: [task page](../tasks/23_CrysDiff_task_1.md)
- Dataset: [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)
- Dataset URL: https://oqmd.org/

## Task Context

Predicting crystal properties (e.g., formation energy, bandgap, bulk modulus) from 3D crystal structures represented as atom types, fractional atomic coordinates, and lattice vectors — specifically by leveraging self-supervised pre-training on unlabeled crystal structures to improve data efficiency and accuracy in downstream regression tasks with sparse labeled data.

## Metadata

- Dataset use ID: `dataset_use_12bede9081fa`
- Original dataset title: OQMD-EXP
- Tags: crystal property prediction, 3D structure-based regression, self-supervised pre-training
