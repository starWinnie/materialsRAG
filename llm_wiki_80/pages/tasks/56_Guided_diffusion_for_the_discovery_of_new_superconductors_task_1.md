# 56_Guided diffusion for the discovery of new superconductors - Task 1

## Task Description

Discovering novel crystalline superconductors with critical temperatures (Tc) above 5 K by generating candidate crystal structures conditioned on target Tc values, then computationally screening for thermodynamic stability, dynamic stability, and superconducting performance.

## Metadata

- Task ID: `task_3c36cf82ab3c`
- Source paper: [56 Guided diffusion for the discovery of new superconductors](../papers/56_Guided_diffusion_for_the_discovery_of_new_superconductors.md)
- Tags: superconductor discovery, inverse materials design, Tc-driven structure generation

## Supporting Datasets

### [Alexandria Materials Database](../datasets/Alexandria_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/56_Guided_diffusion_for_the_discovery_of_new_superconductors_Alexandria_Materials_Database.md)
- Original title in paper: Alexandria Materials Database
- Link: https://doi.org/10.1038/s41524-023-01078-9

A large-scale computational materials database containing over 5 million crystal structures; the authors used 1,857,222 structures (≤20 atoms/unit cell) for pretraining a DiffCSP foundation model to learn general structural priors—enabling generation of chemically and geometrically plausible crystals independent of superconductivity. This dataset supports the task by providing broad structural knowledge essential for guiding diffusion-based generation toward physically realistic candidates before property conditioning.

### [DS-A dataset (Cerqueira et al.)](../datasets/DS-A_dataset_Cerqueira_et_al.md)

- Usage page: [usage note](../dataset_uses/56_Guided_diffusion_for_the_discovery_of_new_superconductors_DS-A_dataset_Cerqueira_et_al..md)
- Original title in paper: DS-A dataset (Cerqueira et al.)
- Link: https://doi.org/10.1002/adma.202307085

A labeled dataset of 7,217 dynamically stable metallic compounds with first-principles–derived electron–phonon properties (relaxed structures, density of states at Fermi level, logarithmic average phonon frequency, electron–phonon coupling); the authors fine-tuned their model on 7,183 superconducting samples from this set, using Allen–Dynes–derived Tc values as scalar conditioning targets. This dataset directly supports the task by enabling Tc-conditioned generative modeling—teaching the model to bias structural sampling toward high-Tc superconducting candidates.
