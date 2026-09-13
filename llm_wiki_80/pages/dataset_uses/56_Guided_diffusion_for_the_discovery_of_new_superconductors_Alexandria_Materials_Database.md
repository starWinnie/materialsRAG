# 56_Guided diffusion for the discovery of new superconductors - Alexandria Materials Database

## Dataset Use

A large-scale computational materials database containing over 5 million crystal structures; the authors used 1,857,222 structures (≤20 atoms/unit cell) for pretraining a DiffCSP foundation model to learn general structural priors—enabling generation of chemically and geometrically plausible crystals independent of superconductivity. This dataset supports the task by providing broad structural knowledge essential for guiding diffusion-based generation toward physically realistic candidates before property conditioning.

## Links

- Paper: [56 Guided diffusion for the discovery of new superconductors](../papers/56_Guided_diffusion_for_the_discovery_of_new_superconductors.md)
- Task: [task page](../tasks/56_Guided_diffusion_for_the_discovery_of_new_superconductors_task_1.md)
- Dataset: [Alexandria Materials Database](../datasets/Alexandria_Materials_Database.md)
- Dataset URL: https://doi.org/10.1038/s41524-023-01078-9

## Task Context

Discovering novel crystalline superconductors with critical temperatures (Tc) above 5 K by generating candidate crystal structures conditioned on target Tc values, then computationally screening for thermodynamic stability, dynamic stability, and superconducting performance.

## Metadata

- Dataset use ID: `dataset_use_8803e8a610c4`
- Original dataset title: Alexandria Materials Database
- Tags: superconductor discovery, inverse materials design, Tc-driven structure generation
