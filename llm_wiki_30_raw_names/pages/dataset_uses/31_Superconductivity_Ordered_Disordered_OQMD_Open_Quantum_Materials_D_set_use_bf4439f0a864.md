# 31_Superconductivity_Ordered_Disordered - OQMD (Open Quantum Materials Database)

## Dataset Use

A database of computationally predicted stable and metastable inorganic crystal structures (~300k+ entries at time of publication), used jointly with Materials Project, Matgen, and ICSD to assemble the ~1.14 million-structure pre-training corpus for DiffCSP-SC. Its inclusion ensures broad coverage of elemental combinations and structural motifs beyond experimentally synthesized superconductors, thereby improving the generative model’s capacity to sample chemically plausible and structurally valid crystals during high-Tc-targeted inverse design.

## Links

- Paper: [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered_paper_3d03cb8978f0.md)
- Task: [task page](../tasks/31_Superconductivity_Ordered_Disordered_task_1_task_e583c77ddbb2.md)
- Dataset: [OQMD (Open Quantum Materials Database)](../datasets/OQMD_Open_Quantum_Materials_Database_dataset_9dcd35cc7ac5.md)
- Dataset URL: https://www.oqmd.org

## Task Context

Predicting the superconducting transition temperature (Tc) of materials given their 3D crystal structures — including both ordered and disordered configurations — to enable high-Tc superconductor screening from known structural databases such as ICSD. The task supports identifying promising candidate superconductors for experimental validation by ranking structures based on predicted Tc values.

## Metadata

- Dataset use ID: `dataset_use_bf4439f0a864`
- Original dataset title: OQMD (Open Quantum Materials Database)
- Tags: Tc prediction, superconductor screening, disordered structure modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
