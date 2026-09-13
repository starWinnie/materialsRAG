# 29_Structure_OOD_Benchmark - Task 1

## Task Description

Predicting materials properties for out-of-distribution (OOD) crystal structures that deviate significantly from the training distribution — specifically, predicting refractive index, shear modulus, and formation energy for sparse, outlier, or structurally/property-remote materials not well-represented in standard datasets. The task focuses on evaluating and benchmarking graph neural networks' ability to generalize beyond i.i.d. assumptions to realistic discovery scenarios where target materials are novel, underrepresented, or lie in low-density regions of structural or property space.

## Metadata

- Task ID: `task_76299946d005`
- Source paper: [29 Structure OOD Benchmark](../papers/29_Structure_OOD_Benchmark.md)
- Tags: OOD prediction, materials property prediction, generalization benchmark

## Supporting Datasets

### [matbench_dielectric](../datasets/matbench_dielectric.md)

- Usage page: [usage note](../dataset_uses/29_Structure_OOD_Benchmark_matbench_dielectric_dataset_use_c265973208d1.md)
- Original title in paper: matbench_dielectric
- Link: https://matbench.materialsproject.org/

A dataset of 4,764 inorganic crystals from the Materials Project, each with computed refractive index as the target property. It is used in this paper to construct five OOD test sets (LOCO, SparseXsingle, SparseXcluster, SparseYsingle, SparseYcluster) via structure- and property-based clustering in orbital-field matrix (OFM) feature space; these test sets support evaluating GNNs' ability to predict refractive index for outlier materials located in sparsely populated regions of structural or property space.

### [matbench_log_gvrh](../datasets/matbench_log_gvrh.md)

- Usage page: [usage note](../dataset_uses/29_Structure_OOD_Benchmark_matbench_log_gvrh_dataset_use_e3365bf03dac.md)
- Original title in paper: matbench_log_gvrh
- Link: https://matbench.materialsproject.org/

A dataset of 10,987 inorganic crystals from the Materials Project, with log10-transformed shear modulus (log10(GPa)) as the target property. In this paper, it is split into five OOD test configurations using OFM-based t-SNE density estimation and k-means clustering to isolate samples with lowest structural or property density; these splits enable benchmarking of GNNs’ extrapolative capability for elastic property prediction on materials dissimilar to the training set.

### [matbench_perovskites](../datasets/matbench_perovskites.md)

- Usage page: [usage note](../dataset_uses/29_Structure_OOD_Benchmark_matbench_perovskites_dataset_use_2558e92c934a.md)
- Original title in paper: matbench_perovskites
- Link: https://matbench.materialsproject.org/

A dataset of 18,928 perovskite crystal structures from Castelli et al., with formation energy (eV/unit cell) as the target property. The paper uses it to generate five OOD test sets—based on OFM features and property density—to rigorously assess GNNs’ ability to predict formation energies for structurally rare or energetically extreme perovskites outside the training distribution, simulating real-world discovery of novel perovskite materials.
