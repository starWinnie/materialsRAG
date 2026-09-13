# 87_Crystal structure prediction with host-guided inpainting generation and foundation potentials - Task 1

## Task Description

Predicting symmetric and thermodynamically stable crystal structures for target chemical compositions—particularly in systems with polyanions (e.g., Zn–P–S) or intercalation chemistry (e.g., Li–Si)—by generating atomic coordinates conditioned on symmetrized host frameworks, thereby overcoming the locality bias of unconditional diffusion models and improving success rates for long-range crystalline order.

## Metadata

- Task ID: `task_773fb9153c6d`
- Source paper: [87 Crystal structure prediction with host-guided inpainting generation and foundation potentials](../papers/87_Crystal_structure_prediction_with_host-guided_inpainting_generation_and_foundation_pote.md)
- Tags: crystal structure prediction, symmetric structure generation, host-guided inpainting

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/87_Crystal_structure_prediction_with_host-guided_inpainting_generation_and_foundation_pote.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org

A publicly available database containing over 100,000 DFT-calculated crystal structures with associated energies, space groups, and structural metadata. In this paper, it is used to (1) train the SE(3)-equivariant GNN score model via denoising score matching on structures with energy above hull ≤ 0.1 eV; (2) provide reference phase diagrams for computing decomposition energies (Ed); and (3) serve as the ground-truth source for evaluating symmetry success rates, RDFs, and local coordination environments during model validation and benchmarking.

### [Alexandria](../datasets/Alexandria.md)

- Usage page: [usage note](../dataset_uses/87_Crystal_structure_prediction_with_host-guided_inpainting_generation_and_foundation_pote.md)
- Original title in paper: Alexandria
- Link: None

A large-scale materials database built from high-throughput DFT calculations, covering diverse inorganic compounds and extended structures. The paper mentions it as a training resource used by MatterGen (a related baseline model), and while CHGGen itself is trained on Materials Project, Alexandria is cited contextually as part of the broader ecosystem of foundational datasets supporting GNN-based diffusion models for CSP — however, the text does not state that CHGGen directly uses Alexandria for training or evaluation. Therefore, per extraction rules, it is excluded.
