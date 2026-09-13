# 17_Known_Unknowns_OOD - Materials Project (MP)

## Dataset Use

The Materials Project is a high-throughput computational database providing thermodynamic and mechanical properties for over 100,000 inorganic compounds, derived from DFT calculations. The paper uses a subset of 6,184–6,331 entries focused on bulk modulus, shear modulus, and elastic anisotropy — retaining the lowest-formation-enthalpy entry for duplicate compositions. This dataset supports the OOD property prediction task by enabling evaluation on large-scale, composition-driven mechanical property extrapolation under realistic database screening conditions.

## Links

- Paper: [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD_paper_0accd46e95fd.md)
- Task: [task page](../tasks/17_Known_Unknowns_OOD_task_1_task_e097cf9a59e5.md)
- Dataset: [Materials Project (MP)](../datasets/Materials_Project_MP_dataset_9b0af3c4a714.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting out-of-distribution (OOD) property values for solid-state materials and molecules — specifically, extrapolating zero-shot to higher property value ranges not present in the training data — using only chemical composition (for solids) or molecular graph-derived descriptors (for molecules), to enable high-precision virtual screening of extreme-value candidates.

## Metadata

- Dataset use ID: `dataset_use_c7404036124f`
- Original dataset title: Materials Project (MP)
- Tags: property prediction, out-of-distribution extrapolation, virtual screening

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
