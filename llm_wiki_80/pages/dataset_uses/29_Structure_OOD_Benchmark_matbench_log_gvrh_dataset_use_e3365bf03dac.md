# 29_Structure_OOD_Benchmark - matbench_log_gvrh

## Dataset Use

A dataset of 10,987 inorganic crystals from the Materials Project, with log10-transformed shear modulus (log10(GPa)) as the target property. In this paper, it is split into five OOD test configurations using OFM-based t-SNE density estimation and k-means clustering to isolate samples with lowest structural or property density; these splits enable benchmarking of GNNs’ extrapolative capability for elastic property prediction on materials dissimilar to the training set.

## Links

- Paper: [29 Structure OOD Benchmark](../papers/29_Structure_OOD_Benchmark.md)
- Task: [task page](../tasks/29_Structure_OOD_Benchmark_task_1.md)
- Dataset: [matbench_log_gvrh](../datasets/matbench_log_gvrh.md)
- Dataset URL: https://matbench.materialsproject.org/

## Task Context

Predicting materials properties for out-of-distribution (OOD) crystal structures that deviate significantly from the training distribution — specifically, predicting refractive index, shear modulus, and formation energy for sparse, outlier, or structurally/property-remote materials not well-represented in standard datasets. The task focuses on evaluating and benchmarking graph neural networks' ability to generalize beyond i.i.d. assumptions to realistic discovery scenarios where target materials are novel, underrepresented, or lie in low-density regions of structural or property space.

## Metadata

- Dataset use ID: `dataset_use_e3365bf03dac`
- Original dataset title: matbench_log_gvrh
- Tags: OOD prediction, materials property prediction, generalization benchmark
