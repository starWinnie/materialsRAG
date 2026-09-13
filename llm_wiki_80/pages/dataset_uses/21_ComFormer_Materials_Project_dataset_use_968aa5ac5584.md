# 21_ComFormer - Materials Project

## Dataset Use

The Materials Project is a large-scale database of computationally derived materials properties, containing over 100,000 crystalline structures with DFT-calculated properties including formation energy, band gap, bulk modulus, and shear modulus. The paper uses a specific version (MP-2018.6.1) with standardized data splits (e.g., 60,000/5,000/4,239 for formation energy) to benchmark ComFormer against prior methods, demonstrating its effectiveness on medium-scale tasks and robustness with limited training samples (e.g., only 4,664 samples for bulk/shear moduli).

## Links

- Paper: [21 ComFormer](../papers/21_ComFormer.md)
- Task: [task page](../tasks/21_ComFormer_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org/

## Task Context

Predicting physical and chemical properties of crystalline materials from their atomic structure, specifically by learning geometrically complete graph representations that distinguish any minor structural differences between crystals while remaining invariant or equivariant under crystal passive symmetries (unit cell SE(3) invariance, unit cell SO(3) equivariance, and periodic invariance).

## Metadata

- Dataset use ID: `dataset_use_968aa5ac5584`
- Original dataset title: The Materials Project
- Tags: crystal property prediction, geometric completeness, graph representation learning
