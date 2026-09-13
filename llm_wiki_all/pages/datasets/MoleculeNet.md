# MoleculeNet

## Metadata

- Dataset ID: `dataset_c9e7ecfca1a5`
- Aliases: MoleculeNet
- Links: https://moleculenet.org
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- MoleculeNet is a collection of molecular datasets for machine learning, used here for four graph-to-property regression tasks: ESOL (1,128 small molecules with aqueous solubility), FreeSolv (643 molecules with experimental and calculated hydration free energies), Lipophilicity (4,200 molecules with octanol/water distribution coefficients), and BACE (1,513 molecules with binding affinities to human β-secretase 1). These datasets provide SMILES strings and experimentally or computationally derived property values, and are used to train and evaluate the transductive OOD predictor for molecular property extrapolation — specifically to screen for molecules with extreme (top 30%) property values beyond the training support.

## Uses

- [17_Known_Unknowns_OOD](../dataset_uses/17_Known_Unknowns_OOD_MoleculeNet_dataset_use_648bb8665f99.md): [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD.md), [task](../tasks/17_Known_Unknowns_OOD_task_1.md)
