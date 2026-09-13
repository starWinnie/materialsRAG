# 17_Known_Unknowns_OOD - AFLOW

## Dataset Use

AFLOW is a high-throughput computational database containing ~14,000 solid materials with stoichiometric compositions and associated property values derived from density functional theory calculations. It includes six curated properties: band gap, bulk modulus, Debye temperature, shear modulus, thermal conductivity, and thermal expansion (the latter four log-scaled). In this paper, AFLOW is used to train and evaluate OOD property predictors on composition-based regression tasks, specifically to assess zero-shot extrapolation performance beyond the upper range of training property values during virtual screening of high-performing solids.

## Links

- Paper: [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD.md)
- Task: [task page](../tasks/17_Known_Unknowns_OOD_task_1.md)
- Dataset: [AFLOW](../datasets/AFLOW.md)
- Dataset URL: https://aflowlib.org

## Task Context

Predicting out-of-distribution (OOD) property values for solid-state materials and molecules — specifically, extrapolating zero-shot to higher property value ranges not present in the training data — using only chemical composition (for solids) or molecular graph-derived descriptors (for molecules), to enable high-precision virtual screening of extreme-value candidates.

## Metadata

- Dataset use ID: `dataset_use_7f67e60ee559`
- Original dataset title: AFLOW
- Tags: property prediction, out-of-distribution extrapolation, virtual screening

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Candidate Space Construction
- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
