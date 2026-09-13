# 21_ComFormer - JARVIS Database

## Dataset Use

JARVIS is a curated dataset of crystalline materials containing over 69,000 structures with computed properties such as formation energy, total energy, bandgap (OPT and MBJ), and energy above hull. It includes both experimentally observed and computationally predicted structures. In this paper, JARVIS is used to train and evaluate the ComFormer models on five regression tasks, with specific train/validation/test splits (e.g., 44,578/5,572/5,572 for formation energy), and serves to validate the model's ability to predict diverse material properties using geometrically complete crystal graphs.

## Links

- Paper: [21 ComFormer](../papers/21_ComFormer.md)
- Task: [task page](../tasks/21_ComFormer_task_1.md)
- Dataset: [JARVIS Database](../datasets/JARVIS_Database.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Predicting physical and chemical properties of crystalline materials from their atomic structure, specifically by learning geometrically complete graph representations that distinguish any minor structural differences between crystals while remaining invariant or equivariant under crystal passive symmetries (unit cell SE(3) invariance, unit cell SO(3) equivariance, and periodic invariance).

## Metadata

- Dataset use ID: `dataset_use_82bf6a79848a`
- Original dataset title: JARVIS
- Tags: crystal property prediction, geometric completeness, graph representation learning
