# 23_CrysDiff - Materials Project

## Dataset Use

A large-scale computational materials database containing over 100,000+ DFT-optimized crystal structures, each annotated with structural metadata (space group, lattice parameters, atomic positions) and computed properties. In this paper, MP contributes ~800K untagged crystal graph data (i.e., structures without property labels) used solely for self-supervised pre-training of CrysDiff via crystal structure reconstruction — enabling learning of latent marginal distributions p(F, L | A) without supervision.

## Links

- Paper: [23 CrysDiff](../papers/23_CrysDiff.md)
- Task: [task page](../tasks/23_CrysDiff_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Predicting crystal properties (e.g., formation energy, bandgap, bulk modulus) from 3D crystal structures represented as atom types, fractional atomic coordinates, and lattice vectors — specifically by leveraging self-supervised pre-training on unlabeled crystal structures to improve data efficiency and accuracy in downstream regression tasks with sparse labeled data.

## Metadata

- Dataset use ID: `dataset_use_d28fd2df6bc1`
- Original dataset title: Materials Project (MP)
- Tags: crystal property prediction, 3D structure-based regression, self-supervised pre-training

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
