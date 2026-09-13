# 27_Virtual_Node_Phonon_Preprint - Task 1

## Task Description

Predicting full phonon band structures—including Γ-point phonon spectra and momentum-dependent dispersion relations—directly from atomic coordinates of crystalline materials, enabling rapid, high-accuracy phonon property estimation without ab initio dynamical matrix calculations.

## Metadata

- Task ID: `task_081fca9963b9`
- Source paper: [27 Virtual Node Phonon Preprint](../papers/27_Virtual_Node_Phonon_Preprint_paper_1e2428d6caf8.md)
- Tags: phonon prediction, band structure prediction, lattice dynamics, structure-to-property mapping

## Supporting Datasets

### [Materials Project Phonon Database (DFPT-based)](../datasets/Materials_Project_Phonon_Database_DFPT-based_dataset_bbb9b2c9c374.md)

- Usage page: [usage note](../dataset_uses/27_Virtual_Node_Phonon_Preprint_Materials_Project_Phonon_Database_DFP_set_use_4ee42d9fb861.md)
- Original title in paper: Materials Project Phonon Database (DFPT-based)
- Link: None

A high-quality computational dataset containing phonon dispersion along high-symmetry paths for 1,521 semiconducting inorganic crystalline materials, generated using density-functional perturbation theory (DFPT). It includes atomic structures (primitive unit cells), second-order energy derivatives, and phonon frequencies (in cm⁻¹) at Γ and other high-symmetry k-points. This dataset was used as the primary training and validation source for all three VGNN models (VVN, MVN, k-MVN) to train phonon predictors—specifically for learning Γ-phonon spectra (VVN/MVN) and full band structures (k-MVN).

### [PhononDB (Kyoto University)](../datasets/PhononDB_Kyoto_University_dataset_ec1f8697696a.md)

- Usage page: [usage note](../dataset_uses/27_Virtual_Node_Phonon_Preprint_PhononDB_Kyoto_University_dataset_use_set_use_2f265c920a57.md)
- Original title in paper: PhononDB (Kyoto University)
- Link: http://phonondb.mtl.kyoto-u.ac.jp/

A publicly available phonon database curated by Atsushi Togo, containing frozen-phonon–calculated phonon dispersions for complex inorganic materials, many with large unit cells (>40 atoms). The authors selected 156 high-quality entries where the lowest Γ-phonon frequency exceeds −0.07 cm⁻¹ and unit cell size is ≥40 atoms. This dataset served exclusively as an out-of-distribution test set to evaluate generalization to structurally complex materials beyond the DFPT training domain, supporting robustness validation for all three VGNN models.

### [Materials Project (MP) Γ-Phonon Database (VGNN-predicted)](../datasets/Materials_Project_MP_Γ-Phonon_Database_VGNN-predicted_dataset_cf6d81744e01.md)

- Usage page: [usage note](../dataset_uses/27_Virtual_Node_Phonon_Preprint_Materials_Project_MP_Γ-Phonon_Databas_set_use_881abd0f8652.md)
- Original title in paper: Materials Project (MP) Γ-Phonon Database (VGNN-predicted)
- Link: https://osf.io/k5utb/

A large-scale, author-curated phonon database containing predicted Γ-point phonon spectra for 146,323 materials from the Materials Project (as of 2022), generated using the MVN model. Each entry includes MP ID, chemical formula, space group, CIF-formatted structure, number of atoms per unit cell, and a list of 3m predicted Γ-phonon frequencies (in cm⁻¹). This database was constructed post-training to enable high-throughput screening and materials design with engineered phonon properties, and is explicitly used to demonstrate scalability and real-world applicability of the method.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
<!-- RD_STAGES_END -->
