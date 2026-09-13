# 17_Known_Unknowns_OOD - Materials Project

## Dataset Use

The Materials Project is a high-throughput computational database providing thermodynamic and mechanical properties for over 100,000 inorganic compounds, derived from DFT calculations. The paper uses a subset of 6,184–6,331 entries focused on bulk modulus, shear modulus, and elastic anisotropy — retaining the lowest-formation-enthalpy entry for duplicate compositions. This dataset supports the OOD property prediction task by enabling evaluation on large-scale, composition-driven mechanical property extrapolation under realistic database screening conditions.

## Links

- Paper: [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD.md)
- Task: [task page](../tasks/17_Known_Unknowns_OOD_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://materialsproject.org

## Task Context

Predicting out-of-distribution (OOD) property values for solid-state materials and molecules — specifically, extrapolating zero-shot to higher property value ranges not present in the training data — using only chemical composition (for solids) or molecular graph-derived descriptors (for molecules), to enable high-precision virtual screening of extreme-value candidates.

## Metadata

- Dataset use ID: `dataset_use_f4a7ca4a65b4`
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
