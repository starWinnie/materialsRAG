# 68_Diffusion models for conditional generation of hypothetical new families of superconductors - Task 1

## Task Description

Generating hypothetical new families of superconductors—defined as chemically distinct clusters not present in existing databases—by conditionally interpolating between reference superconductor compounds and learned chemical composition distributions, enabling controlled discovery beyond known superconductor families.

## Metadata

- Task ID: `task_11e7339f61bf`
- Source paper: [68 Diffusion models for conditional generation of hypothetical new families of superconductors](../papers/68_Diffusion_models_for_conditional_generation_of_hypothetical_new_families_of_superconduc.md)
- Tags: generative modeling, superconductor discovery, conditional generation

## Supporting Datasets

### [SuperCon](../datasets/SuperCon.md)

- Usage page: [usage note](../dataset_uses/68_Diffusion_models_for_conditional_generation_of_hypothetical_new_families_of_superconduc.md)
- Original title in paper: SuperCon
- Link: https://doi.org/10.48505/nims.3739

The SuperCon database is the largest publicly available collection of experimentally verified superconducting materials, containing over 26,000 entries with chemical compositions, critical temperatures (Tc), crystal structures, and synthesis conditions. In this paper, it serves as the primary training dataset for the diffusion model: only chemical composition data (encoded as 96-dimensional element-count vectors) is used to train four class-specific unconditional DDPMs (cuprates, pnictides, 'others', and 'everything'); the dataset is also used for clustering-based evaluation (via Roter et al.'s method) to identify whether generated compounds form new families (i.e., novel clusters absent from SuperCon).
