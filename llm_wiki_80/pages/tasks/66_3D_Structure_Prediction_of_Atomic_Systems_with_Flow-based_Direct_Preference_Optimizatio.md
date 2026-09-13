# 66_3D Structure Prediction of Atomic Systems with Flow-based Direct Preference Optimization - Task 2

## Task Description

Predicting stable 3D crystal structures (unit cells) solely from chemical composition, including lattice matrix and fractional atomic coordinates, with the objective of generating experimentally realistic structures that match known materials while reducing low-quality or mismatched predictions through preference-based alignment.

## Metadata

- Task ID: `task_41c680985839`
- Source paper: [66 3D Structure Prediction of Atomic Systems with Flow-based Direct Preference Optimization](../papers/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md)
- Tags: crystal structure prediction, unit cell generation, materials discovery

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md)
- Original title in paper: Perov-5
- Link: https://doi.org/10.1039/C2EE22676E

A dataset of 18,928 perovskite crystals, each with exactly 5 atoms per unit cell and similar structural motifs but varying compositions. Used for crystal structure prediction experiments, it provides ground-truth lattice matrices and fractional coordinates. The dataset is split 60-20-20 for training/validation/testing and supports preference pair construction via StructureMatcher-based matching and RMSD computation, enabling DPO fine-tuning of flow models for lattice and coordinate generation.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org/

A subset of the Materials Project database containing 45,231 experimentally synthesized inorganic materials, each with up to 20 atoms per unit cell. It includes ground-truth crystal structures (lattice + fractional coordinates) derived from experimental characterization. Used for training and evaluation, it supports preference dataset construction via pymatgen's StructureMatcher (stol=0.5, angle_tol=10, ltol=0.3) and RMSD calculation on matched structures, enabling DPO optimization to improve match rate and reduce RMSD.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/66_3D_Structure_Prediction_of_Atomic_Systems_with_Flow-based_Direct_Preference_Optimizatio.md)
- Original title in paper: MPTS-52
- Link: https://github.com/tianxiao-xie/MPTS

An extended version of MP-20 containing 40,476 crystal structures with up to 52 atoms per unit cell, representing more complex and challenging materials. It is chronologically split into 27,380 training, 5,000 validation, and 8,096 test structures. This dataset provides high-complexity ground truth for evaluating model generalization and robustness; preference pairs are constructed using the same StructureMatcher-based matching and RMSD criteria as MP-20, supporting DPO refinement for large-unit-cell prediction.
