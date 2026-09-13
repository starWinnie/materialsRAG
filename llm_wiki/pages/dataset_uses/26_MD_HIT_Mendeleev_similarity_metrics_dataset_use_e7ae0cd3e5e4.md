# 26_MD_HIT - Mendeleev similarity metrics

## Dataset Use

A chemically derived composition similarity measure based on elemental properties (e.g., atomic radius, electronegativity) aligned with Mendeleev’s periodic table principles; implemented in the ElMD package. The paper uses Mendeleev distance to filter the Materials Project composition dataset into seven non-redundant subsets (Mendeleev-nr) with thresholds from 0.5 to 3.0, enabling systematic analysis of how chemical similarity–based redundancy control affects Roost and CrabNet performance on formation energy and band gap prediction.

## Links

- Paper: [26 MD HIT](../papers/26_MD_HIT.md)
- Task: [task page](../tasks/26_MD_HIT_task_1.md)
- Dataset: [Mendeleev similarity metrics](../datasets/Mendeleev_similarity_metrics.md)
- Dataset URL: https://doi.org/10.1021/acs.chemmater.0c02922

## Task Context

Designing and applying a dataset redundancy control method to enable objective, realistic evaluation of machine learning models for material property prediction—specifically by preventing overestimated interpolation performance and improving out-of-distribution (OOD) generalization capability on formation energy and band gap prediction tasks.

## Metadata

- Dataset use ID: `dataset_use_e7ae0cd3e5e4`
- Original dataset title: Mendeleev similarity metrics
- Tags: redundancy reduction, model evaluation, OOD generalization, material property prediction

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
