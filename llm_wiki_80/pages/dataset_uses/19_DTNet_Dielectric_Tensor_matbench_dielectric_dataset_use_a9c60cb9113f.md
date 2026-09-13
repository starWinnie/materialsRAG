# 19_DTNet_Dielectric_Tensor - matbench_dielectric

## Dataset Use

A benchmark subset of Materials Project structures curated for dielectric property prediction, where the target property is the refractive index η (related to the electronic dielectric constant via η = √ε∞). The dataset includes ~1,000–2,000 structures (exact size not specified but drawn from MP) and is used exclusively for out-of-distribution benchmarking—evaluating DTNet’s generalization by predicting ε∞ and computing η from predicted tensors. It supports model validation and leaderboard comparison against state-of-the-art methods like MODNet.

## Links

- Paper: [19 DTNet Dielectric Tensor](../papers/19_DTNet_Dielectric_Tensor.md)
- Task: [task page](../tasks/19_DTNet_Dielectric_Tensor_task_1.md)
- Dataset: [matbench_dielectric](../datasets/matbench_dielectric.md)
- Dataset URL: https://matbench.materialsvirtuallab.org/

## Task Context

Predicting the full 3×3 dielectric tensor—including electronic (ε∞), ionic (ε⁰), and total (ε) components—for inorganic crystalline materials, while preserving O(3) rotational equivariance to ensure physically consistent predictions under arbitrary 3D rotations of the input crystal structure.

## Metadata

- Dataset use ID: `dataset_use_a9c60cb9113f`
- Original dataset title: Matbench Dielectric Task
- Tags: dielectric tensor prediction, equivariant modeling, materials property prediction
