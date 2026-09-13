# matbench_dielectric

## Metadata

- Dataset ID: `dataset_f5fc3794aeae`
- Aliases: Matbench Dielectric Task, matbench_dielectric
- Links: https://matbench.materialsproject.org/, https://matbench.materialsvirtuallab.org/
- Used by papers: 2
- Dataset usage records: 2

## Description Examples

- A benchmark subset of Materials Project structures curated for dielectric property prediction, where the target property is the refractive index η (related to the electronic dielectric constant via η = √ε∞). The dataset includes ~1,000–2,000 structures (exact size not specified but drawn from MP) and is used exclusively for out-of-distribution benchmarking—evaluating DTNet’s generalization by predicting ε∞ and computing η from predicted tensors. It supports model validation and leaderboard comparison against state-of-the-art methods like MODNet.
- A dataset of 4,764 inorganic crystals from the Materials Project, each with computed refractive index as the target property. It is used in this paper to construct five OOD test sets (LOCO, SparseXsingle, SparseXcluster, SparseYsingle, SparseYcluster) via structure- and property-based clustering in orbital-field matrix (OFM) feature space; these test sets support evaluating GNNs' ability to predict refractive index for outlier materials located in sparsely populated regions of structural or property space.

## Uses

- [19_DTNet_Dielectric_Tensor](../dataset_uses/19_DTNet_Dielectric_Tensor_matbench_dielectric_dataset_use_a9c60cb9113f.md): [19 DTNet Dielectric Tensor](../papers/19_DTNet_Dielectric_Tensor.md), [task](../tasks/19_DTNet_Dielectric_Tensor_task_1.md)
- [29_Structure_OOD_Benchmark](../dataset_uses/29_Structure_OOD_Benchmark_matbench_dielectric_dataset_use_c265973208d1.md): [29 Structure OOD Benchmark](../papers/29_Structure_OOD_Benchmark.md), [task](../tasks/29_Structure_OOD_Benchmark_task_1.md)
