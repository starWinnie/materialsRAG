# 56_Guided diffusion for the discovery of new superconductors - DS-A dataset (Cerqueira et al.)

## Dataset Use

A labeled dataset of 7,217 dynamically stable metallic compounds with first-principles–derived electron–phonon properties (relaxed structures, density of states at Fermi level, logarithmic average phonon frequency, electron–phonon coupling); the authors fine-tuned their model on 7,183 superconducting samples from this set, using Allen–Dynes–derived Tc values as scalar conditioning targets. This dataset directly supports the task by enabling Tc-conditioned generative modeling—teaching the model to bias structural sampling toward high-Tc superconducting candidates.

## Links

- Paper: [56 Guided diffusion for the discovery of new superconductors](../papers/56_Guided_diffusion_for_the_discovery_of_new_superconductors.md)
- Task: [task page](../tasks/56_Guided_diffusion_for_the_discovery_of_new_superconductors_task_1.md)
- Dataset: [DS-A dataset (Cerqueira et al.)](../datasets/DS-A_dataset_Cerqueira_et_al.md)
- Dataset URL: https://doi.org/10.1002/adma.202307085

## Task Context

Discovering novel crystalline superconductors with critical temperatures (Tc) above 5 K by generating candidate crystal structures conditioned on target Tc values, then computationally screening for thermodynamic stability, dynamic stability, and superconducting performance.

## Metadata

- Dataset use ID: `dataset_use_620ee9436915`
- Original dataset title: DS-A dataset (Cerqueira et al.)
- Tags: superconductor discovery, inverse materials design, Tc-driven structure generation
