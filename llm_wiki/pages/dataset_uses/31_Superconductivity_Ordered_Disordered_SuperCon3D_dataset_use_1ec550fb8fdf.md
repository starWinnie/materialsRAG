# 31_Superconductivity_Ordered_Disordered - SuperCon3D

## Dataset Use

SuperCon3D is a newly constructed dataset containing 1,578 experimentally verified superconductors, each with both a 3D crystal structure (ordered or disordered, including substitutional, positional, and combined disorder types) and its experimentally measured superconducting transition temperature (Tc). It was built by matching 11,949 superconductors from the SuperCon database (with chemical formulas and Tc) against 208,425 entries from the ICSD database using chemical composition, space group, and lattice parameters; hydrogen-enriched superconductors were supplemented from literature. This dataset directly supports the Tc prediction task for training and evaluating SODNet and benchmarking other property predictors.

## Links

- Paper: [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered.md)
- Task: [task page](../tasks/31_Superconductivity_Ordered_Disordered_task_1.md)
- Dataset: [SuperCon3D](../datasets/SuperCon3D.md)
- Dataset URL: https://github.com/pincher-chen/SODNet

## Task Context

Predicting the superconducting transition temperature (Tc) of materials given their 3D crystal structures — including both ordered and disordered configurations — to enable high-Tc superconductor screening from known structural databases such as ICSD. The task supports identifying promising candidate superconductors for experimental validation by ranking structures based on predicted Tc values.

## Metadata

- Dataset use ID: `dataset_use_1ec550fb8fdf`
- Original dataset title: SuperCon3D
- Tags: Tc prediction, superconductor screening, disordered structure modeling

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
