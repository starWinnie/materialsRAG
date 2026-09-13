# 27_Virtual_Node_Phonon_Preprint - PhononDB (Kyoto University)

## Dataset Use

A publicly available phonon database curated by Atsushi Togo, containing frozen-phonon–calculated phonon dispersions for complex inorganic materials, many with large unit cells (>40 atoms). The authors selected 156 high-quality entries where the lowest Γ-phonon frequency exceeds −0.07 cm⁻¹ and unit cell size is ≥40 atoms. This dataset served exclusively as an out-of-distribution test set to evaluate generalization to structurally complex materials beyond the DFPT training domain, supporting robustness validation for all three VGNN models.

## Links

- Paper: [27 Virtual Node Phonon Preprint](../papers/27_Virtual_Node_Phonon_Preprint.md)
- Task: [task page](../tasks/27_Virtual_Node_Phonon_Preprint_task_1.md)
- Dataset: [PhononDB (Kyoto University)](../datasets/PhononDB_Kyoto_University.md)
- Dataset URL: http://phonondb.mtl.kyoto-u.ac.jp/

## Task Context

Predicting full phonon band structures—including Γ-point phonon spectra and momentum-dependent dispersion relations—directly from atomic coordinates of crystalline materials, enabling rapid, high-accuracy phonon property estimation without ab initio dynamical matrix calculations.

## Metadata

- Dataset use ID: `dataset_use_2f265c920a57`
- Original dataset title: PhononDB (Kyoto University)
- Tags: phonon prediction, band structure prediction, lattice dynamics, structure-to-property mapping

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
