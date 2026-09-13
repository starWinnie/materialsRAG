# 29_Structure_OOD_Benchmark - matbench_perovskites

## Dataset Use

A dataset of 18,928 perovskite crystal structures from Castelli et al., with formation energy (eV/unit cell) as the target property. The paper uses it to generate five OOD test sets—based on OFM features and property density—to rigorously assess GNNs’ ability to predict formation energies for structurally rare or energetically extreme perovskites outside the training distribution, simulating real-world discovery of novel perovskite materials.

## Links

- Paper: [29 Structure OOD Benchmark](../papers/29_Structure_OOD_Benchmark.md)
- Task: [task page](../tasks/29_Structure_OOD_Benchmark_task_1.md)
- Dataset: [matbench_perovskites](../datasets/matbench_perovskites.md)
- Dataset URL: https://matbench.materialsproject.org/

## Task Context

Predicting materials properties for out-of-distribution (OOD) crystal structures that deviate significantly from the training distribution — specifically, predicting refractive index, shear modulus, and formation energy for sparse, outlier, or structurally/property-remote materials not well-represented in standard datasets. The task focuses on evaluating and benchmarking graph neural networks' ability to generalize beyond i.i.d. assumptions to realistic discovery scenarios where target materials are novel, underrepresented, or lie in low-density regions of structural or property space.

## Metadata

- Dataset use ID: `dataset_use_2558e92c934a`
- Original dataset title: matbench_perovskites
- Tags: OOD prediction, materials property prediction, generalization benchmark
