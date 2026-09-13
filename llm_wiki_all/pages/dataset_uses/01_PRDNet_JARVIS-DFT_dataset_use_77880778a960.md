# 01_PRDNet - JARVIS-DFT

## Dataset Use

A DFT-based dataset comprising 75,993 3D crystal structures (dft_3d), each annotated with formation energy, band gap (computed using both OPT and MBJ functionals), bulk modulus, shear modulus, total energy, and energy above hull (Ehull). It also includes the JARVIS-DFT-3D-2021 subset (55,723 entries). This dataset supports comprehensive evaluation of PRDNet across diverse electronic and mechanical property prediction tasks, with emphasis on robustness across computational functionals and stability metrics.

## Links

- Paper: [01 PRDNet](../papers/01_PRDNet.md)
- Task: [task page](../tasks/01_PRDNet_task_1.md)
- Dataset: [JARVIS-DFT](../datasets/JARVIS-DFT.md)
- Dataset URL: None

## Task Context

Predicting multiple physical properties of crystalline materials—including formation energy, band gap, bulk modulus, shear modulus, Young's modulus, exfoliation energy, dielectric constant (refractive index), and metal/non-metal classification—from their atomic structure (i.e., crystal graph defined by atomic types, fractional coordinates, and lattice vectors).

## Metadata

- Dataset use ID: `dataset_use_77880778a960`
- Original dataset title: JARVIS-DFT
- Tags: crystal property prediction, materials property regression, materials property classification

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
