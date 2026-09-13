# 21_ComFormer - Matbench

## Dataset Use

MatBench is a standardized benchmark for materials property prediction, featuring tasks across vastly different scales and complexities. In this work, two MatBench tasks are used: 'e_form' (132,752 crystals) for large-scale evaluation and 'jdft2d' (636 2D crystals) for small-scale, challenging evaluation. These datasets test the scalability and generalizability of ComFormer, particularly its ability to handle extremely large datasets and sparse, low-data regimes, with performance reported using MAE and RMSE metrics.

## Links

- Paper: [21 ComFormer](../papers/21_ComFormer.md)
- Task: [task page](../tasks/21_ComFormer_task_1.md)
- Dataset: [Matbench](../datasets/Matbench.md)
- Dataset URL: https://matbench.materialsproject.org/

## Task Context

Predicting physical and chemical properties of crystalline materials from their atomic structure, specifically by learning geometrically complete graph representations that distinguish any minor structural differences between crystals while remaining invariant or equivariant under crystal passive symmetries (unit cell SE(3) invariance, unit cell SO(3) equivariance, and periodic invariance).

## Metadata

- Dataset use ID: `dataset_use_339a4297cb4d`
- Original dataset title: MatBench
- Tags: crystal property prediction, geometric completeness, graph representation learning

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
