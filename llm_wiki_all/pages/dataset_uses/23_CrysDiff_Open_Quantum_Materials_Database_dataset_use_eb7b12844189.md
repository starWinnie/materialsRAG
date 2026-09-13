# 23_CrysDiff - Open Quantum Materials Database

## Dataset Use

A high-throughput DFT database containing ~400,000+ predicted crystal structures and their computed thermodynamic properties (e.g., formation energy). Like MP, it provides full 3D structural representations (A, F, L) but no experimental property labels. In this paper, OQMD contributes the remaining portion (~800K total) of unlabelled crystal structures used for pre-training CrysDiff, alongside MP. It serves the same role as MP: enabling unsupervised learning of crystal geometry distributions via diffusion-based reconstruction.

## Links

- Paper: [23 CrysDiff](../papers/23_CrysDiff.md)
- Task: [task page](../tasks/23_CrysDiff_task_1.md)
- Dataset: [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)
- Dataset URL: https://oqmd.org/

## Task Context

Predicting crystal properties (e.g., formation energy, bandgap, bulk modulus) from 3D crystal structures represented as atom types, fractional atomic coordinates, and lattice vectors — specifically by leveraging self-supervised pre-training on unlabeled crystal structures to improve data efficiency and accuracy in downstream regression tasks with sparse labeled data.

## Metadata

- Dataset use ID: `dataset_use_eb7b12844189`
- Original dataset title: OQMD (Open Quantum Materials Database)
- Tags: crystal property prediction, 3D structure-based regression, self-supervised pre-training

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
