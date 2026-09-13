# Materials Project (v2023.11.1) Dielectric Dataset

## Metadata

- Dataset ID: `dataset_fed40cdb3663`
- Aliases: Materials Project (v2023.11.1) Dielectric Dataset
- Links: https://next-gen.materialsproject.org/api
- Used by papers: 1
- Dataset usage records: 1

## Description Examples

- A DFT-calculated dataset of 7,277 inorganic crystal structures with computed dielectric tensors, sourced from the Materials Project database. It contains three components per material: electronic dielectric tensor (ε∞), ionic dielectric tensor (ε⁰), and their sum (total ε), each as symmetric 3×3 tensors. After cleaning—removing entries with any tensor element outside [−10, 100] and structures containing elements unsupported by PFP—6,648 structures remained. This dataset is used to train and evaluate the DTNet model for equivariant dielectric tensor prediction across 72 elements and all crystal systems.

## Uses

- [19_DTNet_Dielectric_Tensor](../dataset_uses/19_DTNet_Dielectric_Tensor_Materials_Project_v2023.11.1_Dielectric_Da_set_use_6abcf98e93f6.md): [19 DTNet Dielectric Tensor](../papers/19_DTNet_Dielectric_Tensor_paper_068c396e3b41.md), [task](../tasks/19_DTNet_Dielectric_Tensor_task_1_task_241faca80cb0.md)
