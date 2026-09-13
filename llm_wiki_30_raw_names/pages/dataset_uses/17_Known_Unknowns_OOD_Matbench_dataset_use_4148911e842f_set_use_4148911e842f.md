# 17_Known_Unknowns_OOD - Matbench

## Dataset Use

Matbench is an automated benchmark suite for materials property prediction, containing three composition-based experimental and computational regression tasks: experimentally measured band gap (2,154 samples), experimentally measured yield strength of steels (312 samples), calculated formation energy (37,217 samples), and calculated refractive index (4,764 samples). In this paper, Matbench is used to evaluate OOD extrapolation capability across diverse property types and data sources (experimental vs. computational), supporting the task of identifying top-performing candidates whose property values exceed the training distribution.

## Links

- Paper: [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD_paper_0accd46e95fd.md)
- Task: [task page](../tasks/17_Known_Unknowns_OOD_task_1_task_e097cf9a59e5.md)
- Dataset: [MatBench](../datasets/MatBench_dataset_3ee88ee61ae1.md)
- Dataset URL: https://matbench.materialsproject.org

## Task Context

Predicting out-of-distribution (OOD) property values for solid-state materials and molecules — specifically, extrapolating zero-shot to higher property value ranges not present in the training data — using only chemical composition (for solids) or molecular graph-derived descriptors (for molecules), to enable high-precision virtual screening of extreme-value candidates.

## Metadata

- Dataset use ID: `dataset_use_4148911e842f`
- Original dataset title: Matbench
- Tags: property prediction, out-of-distribution extrapolation, virtual screening

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Problem Definition
- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
