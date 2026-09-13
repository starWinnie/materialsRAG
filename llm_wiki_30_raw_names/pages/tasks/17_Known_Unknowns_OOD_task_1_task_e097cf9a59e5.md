# 17_Known_Unknowns_OOD - Task 1

## Task Description

Predicting out-of-distribution (OOD) property values for solid-state materials and molecules — specifically, extrapolating zero-shot to higher property value ranges not present in the training data — using only chemical composition (for solids) or molecular graph-derived descriptors (for molecules), to enable high-precision virtual screening of extreme-value candidates.

## Metadata

- Task ID: `task_e097cf9a59e5`
- Source paper: [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD_paper_0accd46e95fd.md)
- Tags: property prediction, out-of-distribution extrapolation, virtual screening

## Supporting Datasets

### [AFLOW](../datasets/AFLOW_dataset_bad7a184ddcb.md)

- Usage page: [usage note](../dataset_uses/17_Known_Unknowns_OOD_AFLOW_dataset_use_7f67e60ee559_set_use_7f67e60ee559.md)
- Original title in paper: AFLOW
- Link: https://aflowlib.org

AFLOW is a high-throughput computational database containing ~14,000 solid materials with stoichiometric compositions and associated property values derived from density functional theory calculations. It includes six curated properties: band gap, bulk modulus, Debye temperature, shear modulus, thermal conductivity, and thermal expansion (the latter four log-scaled). In this paper, AFLOW is used to train and evaluate OOD property predictors on composition-based regression tasks, specifically to assess zero-shot extrapolation performance beyond the upper range of training property values during virtual screening of high-performing solids.

### [MatBench](../datasets/MatBench_dataset_3ee88ee61ae1.md)

- Usage page: [usage note](../dataset_uses/17_Known_Unknowns_OOD_Matbench_dataset_use_4148911e842f_set_use_4148911e842f.md)
- Original title in paper: Matbench
- Link: https://matbench.materialsproject.org

Matbench is an automated benchmark suite for materials property prediction, containing three composition-based experimental and computational regression tasks: experimentally measured band gap (2,154 samples), experimentally measured yield strength of steels (312 samples), calculated formation energy (37,217 samples), and calculated refractive index (4,764 samples). In this paper, Matbench is used to evaluate OOD extrapolation capability across diverse property types and data sources (experimental vs. computational), supporting the task of identifying top-performing candidates whose property values exceed the training distribution.

### [Materials Project (MP)](../datasets/Materials_Project_MP_dataset_9b0af3c4a714.md)

- Usage page: [usage note](../dataset_uses/17_Known_Unknowns_OOD_Materials_Project_MP_dataset_use_c7404036124f_set_use_c7404036124f.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org

The Materials Project is a high-throughput computational database providing thermodynamic and mechanical properties for over 100,000 inorganic compounds, derived from DFT calculations. The paper uses a subset of 6,184–6,331 entries focused on bulk modulus, shear modulus, and elastic anisotropy — retaining the lowest-formation-enthalpy entry for duplicate compositions. This dataset supports the OOD property prediction task by enabling evaluation on large-scale, composition-driven mechanical property extrapolation under realistic database screening conditions.

### [MoleculeNet](../datasets/MoleculeNet_dataset_c9e7ecfca1a5.md)

- Usage page: [usage note](../dataset_uses/17_Known_Unknowns_OOD_MoleculeNet_dataset_use_648bb8665f99_set_use_648bb8665f99.md)
- Original title in paper: MoleculeNet
- Link: https://moleculenet.org

MoleculeNet is a collection of molecular datasets for machine learning, used here for four graph-to-property regression tasks: ESOL (1,128 small molecules with aqueous solubility), FreeSolv (643 molecules with experimental and calculated hydration free energies), Lipophilicity (4,200 molecules with octanol/water distribution coefficients), and BACE (1,513 molecules with binding affinities to human β-secretase 1). These datasets provide SMILES strings and experimentally or computationally derived property values, and are used to train and evaluate the transductive OOD predictor for molecular property extrapolation — specifically to screen for molecules with extreme (top 30%) property values beyond the training support.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Candidate Space Construction
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
