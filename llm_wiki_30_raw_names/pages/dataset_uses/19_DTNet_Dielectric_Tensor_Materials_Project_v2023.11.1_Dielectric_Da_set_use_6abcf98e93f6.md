# 19_DTNet_Dielectric_Tensor - Materials Project (v2023.11.1) Dielectric Dataset

## Dataset Use

A DFT-calculated dataset of 7,277 inorganic crystal structures with computed dielectric tensors, sourced from the Materials Project database. It contains three components per material: electronic dielectric tensor (ε∞), ionic dielectric tensor (ε⁰), and their sum (total ε), each as symmetric 3×3 tensors. After cleaning—removing entries with any tensor element outside [−10, 100] and structures containing elements unsupported by PFP—6,648 structures remained. This dataset is used to train and evaluate the DTNet model for equivariant dielectric tensor prediction across 72 elements and all crystal systems.

## Links

- Paper: [19 DTNet Dielectric Tensor](../papers/19_DTNet_Dielectric_Tensor_paper_068c396e3b41.md)
- Task: [task page](../tasks/19_DTNet_Dielectric_Tensor_task_1_task_241faca80cb0.md)
- Dataset: [Materials Project (v2023.11.1) Dielectric Dataset](../datasets/Materials_Project_v2023.11.1_Dielectric_Dataset_dataset_fed40cdb3663.md)
- Dataset URL: https://next-gen.materialsproject.org/api

## Task Context

Predicting the full 3×3 dielectric tensor—including electronic (ε∞), ionic (ε⁰), and total (ε) components—for inorganic crystalline materials, while preserving O(3) rotational equivariance to ensure physically consistent predictions under arbitrary 3D rotations of the input crystal structure.

## Metadata

- Dataset use ID: `dataset_use_6abcf98e93f6`
- Original dataset title: Materials Project (v2023.11.1) Dielectric Dataset
- Tags: dielectric tensor prediction, equivariant modeling, materials property prediction

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
- Benchmarking / Evaluation
<!-- RD_STAGES_END -->
