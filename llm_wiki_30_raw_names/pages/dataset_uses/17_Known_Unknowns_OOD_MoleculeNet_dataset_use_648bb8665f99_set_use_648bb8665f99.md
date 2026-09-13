# 17_Known_Unknowns_OOD - MoleculeNet

## Dataset Use

MoleculeNet is a collection of molecular datasets for machine learning, used here for four graph-to-property regression tasks: ESOL (1,128 small molecules with aqueous solubility), FreeSolv (643 molecules with experimental and calculated hydration free energies), Lipophilicity (4,200 molecules with octanol/water distribution coefficients), and BACE (1,513 molecules with binding affinities to human β-secretase 1). These datasets provide SMILES strings and experimentally or computationally derived property values, and are used to train and evaluate the transductive OOD predictor for molecular property extrapolation — specifically to screen for molecules with extreme (top 30%) property values beyond the training support.

## Links

- Paper: [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD_paper_0accd46e95fd.md)
- Task: [task page](../tasks/17_Known_Unknowns_OOD_task_1_task_e097cf9a59e5.md)
- Dataset: [MoleculeNet](../datasets/MoleculeNet_dataset_c9e7ecfca1a5.md)
- Dataset URL: https://moleculenet.org

## Task Context

Predicting out-of-distribution (OOD) property values for solid-state materials and molecules — specifically, extrapolating zero-shot to higher property value ranges not present in the training data — using only chemical composition (for solids) or molecular graph-derived descriptors (for molecules), to enable high-precision virtual screening of extreme-value candidates.

## Metadata

- Dataset use ID: `dataset_use_648bb8665f99`
- Original dataset title: MoleculeNet
- Tags: property prediction, out-of-distribution extrapolation, virtual screening

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
