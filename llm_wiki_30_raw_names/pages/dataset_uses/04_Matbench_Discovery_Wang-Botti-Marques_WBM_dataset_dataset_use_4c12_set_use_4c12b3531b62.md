# 04_Matbench_Discovery - Wang-Botti-Marques (WBM) dataset

## Dataset Use

A prospectively generated test set of 215,488 unique protostructures derived via chemical similarity-based elemental substitution on MP source structures, followed by DFT relaxation and hull distance calculation against the MP convex hull. Contains unrelaxed input structures and their corresponding DFT-relaxed hull distances (target labels). Used exclusively for evaluating model performance on the stability prediction task under realistic discovery conditions — i.e., predicting stability from unrelaxed inputs without access to relaxation information.

## Links

- Paper: [04 Matbench Discovery](../papers/04_Matbench_Discovery_paper_a008eb6410ec.md)
- Task: [task page](../tasks/04_Matbench_Discovery_task_1_task_b112dbffd75c.md)
- Dataset: [Wang-Botti-Marques (WBM) dataset](../datasets/Wang-Botti-Marques_WBM_dataset_dataset_c103a7259773.md)
- Dataset URL: https://figshare.com/articles/dataset/22715158

## Task Context

Predicting the thermodynamic stability of hypothetical inorganic crystal structures by estimating their distance above the convex hull (hull distance) from only unrelaxed input structures, to enable efficient pre-screening before costly DFT relaxation and stability validation.

## Metadata

- Dataset use ID: `dataset_use_4c12b3531b62`
- Original dataset title: Wang-Botti-Marques (WBM) dataset
- Tags: crystal stability prediction, convex hull distance estimation, pre-screening for DFT validation

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Problem Definition
- Candidate Space Construction
- Dataset Selection
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
