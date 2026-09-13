# 31_Superconductivity_Ordered_Disordered - Matgen

## Dataset Use

A Chinese materials database hosting computationally generated 3D crystal structures, integrated with Materials Project, OQMD, and ICSD to form the 1.14 million-structure pre-training set for DiffCSP-SC. It contributes additional structural diversity — particularly for underrepresented elements and stoichiometries — enabling the diffusion model to learn generalizable periodic lattice and atomic coordinate distributions, which is critical for generating novel, physically realistic superconductor candidates not present in SuperCon3D.

## Links

- Paper: [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered_paper_3d03cb8978f0.md)
- Task: [task page](../tasks/31_Superconductivity_Ordered_Disordered_task_1_task_e583c77ddbb2.md)
- Dataset: [Matgen](../datasets/Matgen_dataset_aed6baa5fc51.md)
- Dataset URL: https://matgen.nscc-gz.cn

## Task Context

Predicting the superconducting transition temperature (Tc) of materials given their 3D crystal structures — including both ordered and disordered configurations — to enable high-Tc superconductor screening from known structural databases such as ICSD. The task supports identifying promising candidate superconductors for experimental validation by ranking structures based on predicted Tc values.

## Metadata

- Dataset use ID: `dataset_use_c2144aef171b`
- Original dataset title: Matgen
- Tags: Tc prediction, superconductor screening, disordered structure modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Candidate Space Construction
- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
