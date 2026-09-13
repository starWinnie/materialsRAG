# SAbDab

## Metadata

- Dataset ID: `dataset_1bf08acf65bd`
- Aliases: SAbDab
- Links: https://opig.stats.ox.ac.uk/webapps/sabdab/
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A structural antibody database containing experimentally determined antibody-antigen complex structures from the PDB. The authors extracted 12,428 antibodies deposited before April 11th, 2024, filtered by resolution ≤4.0Å and protein-only targets, then clustered by 50% CDR sequence identity to construct a training set disjoint from the test set. This dataset provides the ground-truth 3D backbone coordinates (N, Cα, C, O) and sequences for CDRs and framework regions, used to train and validate flow matching models and construct preference pairs via RMSD-based ranking.

## Uses

- [66_3D Structure Prediction of Atomic Systems with Flow-based Direct Preference Optimization](../dataset_uses/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md): [66 3D Structure Prediction of Atomic Systems with Flow-based Direct Preference Optimization](../papers/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md), [task](../tasks/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md)
