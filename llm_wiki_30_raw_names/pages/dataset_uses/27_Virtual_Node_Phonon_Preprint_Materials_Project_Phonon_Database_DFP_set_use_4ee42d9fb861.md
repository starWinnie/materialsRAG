# 27_Virtual_Node_Phonon_Preprint - Materials Project Phonon Database (DFPT-based)

## Dataset Use

A high-quality computational dataset containing phonon dispersion along high-symmetry paths for 1,521 semiconducting inorganic crystalline materials, generated using density-functional perturbation theory (DFPT). It includes atomic structures (primitive unit cells), second-order energy derivatives, and phonon frequencies (in cm⁻¹) at Γ and other high-symmetry k-points. This dataset was used as the primary training and validation source for all three VGNN models (VVN, MVN, k-MVN) to train phonon predictors—specifically for learning Γ-phonon spectra (VVN/MVN) and full band structures (k-MVN).

## Links

- Paper: [27 Virtual Node Phonon Preprint](../papers/27_Virtual_Node_Phonon_Preprint_paper_1e2428d6caf8.md)
- Task: [task page](../tasks/27_Virtual_Node_Phonon_Preprint_task_1_task_081fca9963b9.md)
- Dataset: [Materials Project Phonon Database (DFPT-based)](../datasets/Materials_Project_Phonon_Database_DFPT-based_dataset_bbb9b2c9c374.md)
- Dataset URL: None

## Task Context

Predicting full phonon band structures—including Γ-point phonon spectra and momentum-dependent dispersion relations—directly from atomic coordinates of crystalline materials, enabling rapid, high-accuracy phonon property estimation without ab initio dynamical matrix calculations.

## Metadata

- Dataset use ID: `dataset_use_4ee42d9fb861`
- Original dataset title: Materials Project Phonon Database (DFPT-based)
- Tags: phonon prediction, band structure prediction, lattice dynamics, structure-to-property mapping

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
