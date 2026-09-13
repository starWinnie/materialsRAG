# 26_MD_HIT - MatScholar embeddings

## Dataset Use

A literature-derived word embedding for materials, generated from text mining of materials science publications, producing fixed-dimensional (e.g., 200D) feature vectors that encode periodic table structure and structure–property relationships. In this paper, MatScholar features are used to compute composition similarity (via Euclidean distance) for redundancy control in MD-HIT-composition, to define the MatscholarOOD test set (1000 most distant samples), and to analyze sample density–MAE correlations—supporting the task of identifying and mitigating redundancy-induced overfitting in composition-based property prediction.

## Links

- Paper: [26 MD HIT](../papers/26_MD_HIT_paper_364d763e5978.md)
- Task: [task page](../tasks/26_MD_HIT_task_1_task_e55c8a4f2b28.md)
- Dataset: [MatScholar embeddings](../datasets/MatScholar_embeddings_dataset_876dcbb1c40c.md)
- Dataset URL: https://doi.org/10.1038/s41586-019-1312-1

## Task Context

Designing and applying a dataset redundancy control method to enable objective, realistic evaluation of machine learning models for material property prediction—specifically by preventing overestimated interpolation performance and improving out-of-distribution (OOD) generalization capability on formation energy and band gap prediction tasks.

## Metadata

- Dataset use ID: `dataset_use_ece85bbe823c`
- Original dataset title: MatScholar embeddings
- Tags: redundancy reduction, model evaluation, OOD generalization, material property prediction

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Problem Definition
- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
