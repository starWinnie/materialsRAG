# DiffAb test set

## Metadata

- Dataset ID: `dataset_01650f0db0a5`
- Aliases: DiffAb test set
- Links: https://github.com/luosy01/DiffAb
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A manually curated test set of 19 antibody-antigen complexes originally introduced in DiffAb (Luo et al., NeurIPS 2022). It serves as the held-out evaluation benchmark for antibody structure prediction. For each complex, the task is to predict CDR structures conditioned on sequence and context; performance is measured using RMSD on Cα and backbone atoms across 20 generated samples per target. This dataset provides the ground-truth reference structures against which candidate generations are evaluated and ranked to build the preference dataset.

## Uses

- [66_3D Structure Prediction of Atomic Systems with Flow-based Direct Preference Optimization](../dataset_uses/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md): [66 3D Structure Prediction of Atomic Systems with Flow-based Direct Preference Optimization](../papers/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md), [task](../tasks/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md)
