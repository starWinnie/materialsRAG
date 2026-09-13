# 31_Superconductivity_Ordered_Disordered - Materials Project

## Dataset Use

A computational materials database containing ~1.14 million stable 3D crystal structures (preprocessed and deduplicated), sourced alongside OQMD, Matgen, and ICSD for pre-training DiffCSP-SC. It provides diverse atomic species, lattice geometries, and coordination environments not fully covered in the small SuperCon3D dataset. This large-scale pre-training data enables robust representation learning for crystal generation and improves the model’s ability to generalize to novel high-Tc structures — supporting the inverse design task by expanding the valid search space before fine-tuning on SuperCon3D.

## Links

- Paper: [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered_paper_3d03cb8978f0.md)
- Task: [task page](../tasks/31_Superconductivity_Ordered_Disordered_task_1_task_e583c77ddbb2.md)
- Dataset: [Materials Project](../datasets/Materials_Project_dataset_d55b16e3041b.md)
- Dataset URL: https://next-gen.materialsproject.org

## Task Context

Predicting the superconducting transition temperature (Tc) of materials given their 3D crystal structures — including both ordered and disordered configurations — to enable high-Tc superconductor screening from known structural databases such as ICSD. The task supports identifying promising candidate superconductors for experimental validation by ranking structures based on predicted Tc values.

## Metadata

- Dataset use ID: `dataset_use_9c28764cb72e`
- Original dataset title: Materials Project
- Tags: Tc prediction, superconductor screening, disordered structure modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
