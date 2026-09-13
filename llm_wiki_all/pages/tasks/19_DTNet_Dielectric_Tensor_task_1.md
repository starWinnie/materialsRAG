# 19_DTNet_Dielectric_Tensor - Task 1

## Task Description

Predicting the full 3×3 dielectric tensor—including electronic (ε∞), ionic (ε⁰), and total (ε) components—for inorganic crystalline materials, while preserving O(3) rotational equivariance to ensure physically consistent predictions under arbitrary 3D rotations of the input crystal structure.

## Metadata

- Task ID: `task_241faca80cb0`
- Source paper: [19 DTNet Dielectric Tensor](../papers/19_DTNet_Dielectric_Tensor.md)
- Tags: dielectric tensor prediction, equivariant modeling, materials property prediction

## Supporting Datasets

### [Materials Project (v2023.11.1) Dielectric Dataset](../datasets/Materials_Project_v2023.11.1_Dielectric_Dataset.md)

- Usage page: [usage note](../dataset_uses/19_DTNet_Dielectric_Tensor_Materials_Project_v2023.11.1_Dielectric_Dataset_dataset_use_6ab.md)
- Original title in paper: Materials Project (v2023.11.1) Dielectric Dataset
- Link: https://next-gen.materialsproject.org/api

A DFT-calculated dataset of 7,277 inorganic crystal structures with computed dielectric tensors, sourced from the Materials Project database. It contains three components per material: electronic dielectric tensor (ε∞), ionic dielectric tensor (ε⁰), and their sum (total ε), each as symmetric 3×3 tensors. After cleaning—removing entries with any tensor element outside [−10, 100] and structures containing elements unsupported by PFP—6,648 structures remained. This dataset is used to train and evaluate the DTNet model for equivariant dielectric tensor prediction across 72 elements and all crystal systems.

### [matbench_dielectric](../datasets/matbench_dielectric.md)

- Usage page: [usage note](../dataset_uses/19_DTNet_Dielectric_Tensor_matbench_dielectric_dataset_use_a9c60cb9113f.md)
- Original title in paper: Matbench Dielectric Task
- Link: https://matbench.materialsvirtuallab.org/

A benchmark subset of Materials Project structures curated for dielectric property prediction, where the target property is the refractive index η (related to the electronic dielectric constant via η = √ε∞). The dataset includes ~1,000–2,000 structures (exact size not specified but drawn from MP) and is used exclusively for out-of-distribution benchmarking—evaluating DTNet’s generalization by predicting ε∞ and computing η from predicted tensors. It supports model validation and leaderboard comparison against state-of-the-art methods like MODNet.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
<!-- RD_STAGES_END -->
