# 66_3D Structure Prediction of Atomic Systems with Flow-based Direct Preference Optimization - MPTS-52

## Dataset Use

An extended version of MP-20 containing 40,476 crystal structures with up to 52 atoms per unit cell, representing more complex and challenging materials. It is chronologically split into 27,380 training, 5,000 validation, and 8,096 test structures. This dataset provides high-complexity ground truth for evaluating model generalization and robustness; preference pairs are constructed using the same StructureMatcher-based matching and RMSD criteria as MP-20, supporting DPO refinement for large-unit-cell prediction.

## Links

- Paper: [66 3D Structure Prediction of Atomic Systems with Flow-based Direct Preference Optimization](../papers/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md)
- Task: [task page](../tasks/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md)
- Dataset: [MPTS-52](../datasets/MPTS-52.md)
- Dataset URL: https://github.com/tianxiao-xie/MPTS

## Task Context

Predicting stable 3D crystal structures (unit cells) solely from chemical composition, including lattice matrix and fractional atomic coordinates, with the objective of generating experimentally realistic structures that match known materials while reducing low-quality or mismatched predictions through preference-based alignment.

## Metadata

- Dataset use ID: `dataset_use_900edb3540a9`
- Original dataset title: MPTS-52
- Tags: crystal structure prediction, unit cell generation, materials discovery
