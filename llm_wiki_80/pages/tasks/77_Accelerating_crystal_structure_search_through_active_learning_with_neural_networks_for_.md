# 77_Accelerating crystal structure search through active learning with neural networks for rapid relaxations - Task 1

## Task Description

Accelerating global optimization of crystal structures by predicting low-energy local minima on the potential energy surface (PES) for a given chemical composition, using active learning to minimize the number of expensive density functional theory (DFT) calculations required for structure relaxation and validation.

## Metadata

- Task ID: `task_b7e91922ce39`
- Source paper: [77 Accelerating crystal structure search through active learning with neural networks for rapid relaxations](../papers/77_Accelerating_crystal_structure_search_through_active_learning_with_neural_networks_for_.md)
- Tags: crystal structure prediction, global optimization, structure relaxation acceleration

## Supporting Datasets

### [DepositeOnce dataset for 'Accelerating crystal structure search through active learning'](../datasets/DepositeOnce_dataset_for_Accelerating_crystal_structure_search_through_active_learning.md)

- Usage page: [usage note](../dataset_uses/77_Accelerating_crystal_structure_search_through_active_learning_with_neural_networks_for_.md)
- Original title in paper: DepositeOnce dataset for 'Accelerating crystal structure search through active learning'
- Link: https://doi.org/10.14279/depositonce-2100896

This dataset contains the initial and final candidate pools, validated structures, generated training data (energies, forces, and stress computed via DFT), and trained neural network ensembles from the last iteration of the active learning cycles. It supports the core task by providing the experimentally and computationally generated labeled data needed to train and validate the neural network force fields used for rapid, uncertainty-guided structure relaxation and low-energy candidate selection.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/77_Accelerating_crystal_structure_search_through_active_learning_with_neural_networks_for_.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org

A public database of computed materials properties containing pre-relaxed, stable crystal structures and their DFT-computed energies (e.g., MP-149 for Si16, MP-2534 for Ga8As8, MP-22862 for Na8Cl8, MP-1143 for Al4O6, MP-971662 for Si46, MP-2254 for Al16O24). In this paper, it serves two roles: (1) as a source of ground-truth target structures (global and low-energy local minima) to evaluate whether the method successfully discovers known stable configurations; and (2) as a reference for comparing predicted low-energy structures against established benchmarks during post-validation analysis.
