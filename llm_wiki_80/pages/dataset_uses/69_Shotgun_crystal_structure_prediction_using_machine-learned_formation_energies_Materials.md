# 69_Shotgun crystal structure prediction using machine-learned formation energies - Materials Project

## Dataset Use

A publicly available database containing DFT-calculated formation energies, crystal structures, and properties for 126,210 stable and metastable inorganic compounds. It was used to pretrain the global CGCNN energy predictor and to extract template structures (33,040 stable crystals) for element substitution (ShotgunCSP-GT), space-group prediction (33,040 instances with 213 distinct space groups), and Wyckoff-letter assignment modeling (same 33,040 instances, excluding 120 benchmark crystals). The dataset supported training surrogate energy models, generating candidate structures, and predicting space groups and Wyckoff patterns.

## Links

- Paper: [69 Shotgun crystal structure prediction using machine-learned formation energies](../papers/69_Shotgun_crystal_structure_prediction_using_machine-learned_formation_energies.md)
- Task: [task page](../tasks/69_Shotgun_crystal_structure_prediction_using_machine-learned_formation_energies_task_1.md)
- Dataset: [Materials Project](../datasets/Materials_Project.md)
- Dataset URL: https://next-gen.materialsproject.org/

## Task Context

Predicting stable or metastable crystal structures from a given chemical composition by identifying global or local minima of the energy surface across a broad space of atomic configurations, using machine-learned formation energies to avoid iterative first-principles relaxation.

## Metadata

- Dataset use ID: `dataset_use_3422e371bf01`
- Original dataset title: Materials Project database
- Tags: crystal structure prediction, energy minimization, formation energy prediction
