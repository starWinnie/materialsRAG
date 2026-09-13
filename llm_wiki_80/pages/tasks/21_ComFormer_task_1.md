# 21_ComFormer - Task 1

## Task Description

Predicting physical and chemical properties of crystalline materials from their atomic structure, specifically by learning geometrically complete graph representations that distinguish any minor structural differences between crystals while remaining invariant or equivariant under crystal passive symmetries (unit cell SE(3) invariance, unit cell SO(3) equivariance, and periodic invariance).

## Metadata

- Task ID: `task_b2fdc1e458d6`
- Source paper: [21 ComFormer](../papers/21_ComFormer.md)
- Tags: crystal property prediction, geometric completeness, graph representation learning

## Supporting Datasets

### [JARVIS Database](../datasets/JARVIS_Database.md)

- Usage page: [usage note](../dataset_uses/21_ComFormer_JARVIS_Database_dataset_use_82bf6a79848a.md)
- Original title in paper: JARVIS
- Link: https://jarvis.nist.gov/

JARVIS is a curated dataset of crystalline materials containing over 69,000 structures with computed properties such as formation energy, total energy, bandgap (OPT and MBJ), and energy above hull. It includes both experimentally observed and computationally predicted structures. In this paper, JARVIS is used to train and evaluate the ComFormer models on five regression tasks, with specific train/validation/test splits (e.g., 44,578/5,572/5,572 for formation energy), and serves to validate the model's ability to predict diverse material properties using geometrically complete crystal graphs.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/21_ComFormer_Materials_Project_dataset_use_968aa5ac5584.md)
- Original title in paper: The Materials Project
- Link: https://materialsproject.org/

The Materials Project is a large-scale database of computationally derived materials properties, containing over 100,000 crystalline structures with DFT-calculated properties including formation energy, band gap, bulk modulus, and shear modulus. The paper uses a specific version (MP-2018.6.1) with standardized data splits (e.g., 60,000/5,000/4,239 for formation energy) to benchmark ComFormer against prior methods, demonstrating its effectiveness on medium-scale tasks and robustness with limited training samples (e.g., only 4,664 samples for bulk/shear moduli).

### [Matbench](../datasets/Matbench.md)

- Usage page: [usage note](../dataset_uses/21_ComFormer_Matbench_dataset_use_339a4297cb4d.md)
- Original title in paper: MatBench
- Link: https://matbench.materialsproject.org/

MatBench is a standardized benchmark for materials property prediction, featuring tasks across vastly different scales and complexities. In this work, two MatBench tasks are used: 'e_form' (132,752 crystals) for large-scale evaluation and 'jdft2d' (636 2D crystals) for small-scale, challenging evaluation. These datasets test the scalability and generalizability of ComFormer, particularly its ability to handle extremely large datasets and sparse, low-data regimes, with performance reported using MAE and RMSE metrics.
