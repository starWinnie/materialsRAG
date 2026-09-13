# 29_Structure_OOD_Benchmark.pdf

## Ontology Type
Task

## Task Description
Predicting materials properties for out-of-distribution (OOD) crystal structures that deviate significantly from the training distribution — specifically, predicting refractive index, shear modulus, and formation energy for sparse, outlier, or structurally/property-remote materials not well-represented in standard datasets. The task focuses on evaluating and benchmarking graph neural networks' ability to generalize beyond i.i.d. assumptions to realistic discovery scenarios where target materials are novel, underrepresented, or lie in low-density regions of structural or property space.

## Material Systems
- [inorganic crystal](../material_systems/inorganic_crystal.md)

## Target Properties
- [formation energy](../target_properties/formation_energy.md)
- [shear modulus](../target_properties/shear_modulus.md)
- [dielectric property](../target_properties/dielectric_property.md)

## Representations
- [crystal structure](../representations/crystal_structure.md)
- [crystal graph](../representations/crystal_graph.md)

## Methods
- [graph neural network](../methods/graph_neural_network.md)
- [benchmarking](../methods/benchmarking.md)

## Supporting Dataset Uses
- [matbench_dielectric](../dataset_uses/matbench_dielectric_2.md)
- [matbench_log_gvrh](../dataset_uses/matbench_log_gvrh.md)
- [matbench_perovskites](../dataset_uses/matbench_perovskites.md)

## Datasets
- [matbench_dielectric](../datasets/matbench_dielectric.md)
- [matbench_log_gvrh](../datasets/matbench_log_gvrh.md)
- [matbench_perovskites](../datasets/matbench_perovskites.md)

## Source Papers
- [29 Structure OOD Benchmark](../papers/29_structure_ood_benchmark.md)

## Metadata
task_id: `task_76299946d005`
tags: OOD prediction; materials property prediction; generalization benchmark
