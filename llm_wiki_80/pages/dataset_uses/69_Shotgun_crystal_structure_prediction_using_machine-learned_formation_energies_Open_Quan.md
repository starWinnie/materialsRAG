# 69_Shotgun crystal structure prediction using machine-learned formation energies - Open Quantum Materials Database

## Dataset Use

A computational materials database containing formation energies and structures for ~1,021,917 compounds, including both relaxed and unrelaxed configurations. It was used experimentally to test the generalization capability of the global CGCNN model — specifically, to demonstrate that models trained on relaxed structures from OQMD (like Materials Project) fail to predict pre-relaxed conformational energies accurately, justifying the need for transfer learning on system-specific unrelaxed data.

## Links

- Paper: [69 Shotgun crystal structure prediction using machine-learned formation energies](../papers/69_Shotgun_crystal_structure_prediction_using_machine-learned_formation_energies.md)
- Task: [task page](../tasks/69_Shotgun_crystal_structure_prediction_using_machine-learned_formation_energies_task_1.md)
- Dataset: [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)
- Dataset URL: https://oqmd.org

## Task Context

Predicting stable or metastable crystal structures from a given chemical composition by identifying global or local minima of the energy surface across a broad space of atomic configurations, using machine-learned formation energies to avoid iterative first-principles relaxation.

## Metadata

- Dataset use ID: `dataset_use_771c1239e43c`
- Original dataset title: OQMD (Open Quantum Materials Database)
- Tags: crystal structure prediction, energy minimization, formation energy prediction
