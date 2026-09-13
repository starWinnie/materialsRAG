# 23_CrysDiff - JARVIS-DFT

## Dataset Use

A publicly available materials database containing 55,722 DFT-calculated crystalline materials, each with 19 computed properties including formation energy, bandgap (OPT and MBJ), total energy, Ehull, bulk modulus (Kv), shear modulus (Gv), SLME (%), and spillage. It provides full 3D structural information: atom types (A), fractional coordinates (F), and lattice vectors (L). In this paper, JARVIS-DFT is used exclusively for the downstream fine-tuning and evaluation phase — i.e., to train and test the crystal property prediction models on nine target properties under standard train/val/test splits (80%/10%/10%).

## Links

- Paper: [23 CrysDiff](../papers/23_CrysDiff.md)
- Task: [task page](../tasks/23_CrysDiff_task_1.md)
- Dataset: [JARVIS-DFT](../datasets/JARVIS-DFT.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Predicting crystal properties (e.g., formation energy, bandgap, bulk modulus) from 3D crystal structures represented as atom types, fractional atomic coordinates, and lattice vectors — specifically by leveraging self-supervised pre-training on unlabeled crystal structures to improve data efficiency and accuracy in downstream regression tasks with sparse labeled data.

## Metadata

- Dataset use ID: `dataset_use_8fe9915f1b57`
- Original dataset title: JARVIS-DFT
- Tags: crystal property prediction, 3D structure-based regression, self-supervised pre-training

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
