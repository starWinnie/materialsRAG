# 57_Scalable Diffusion for Materials Generation - Perov5

## Dataset Use

A small-scale benchmark dataset containing 5 perovskite crystal structures (e.g., CaTiO₃, SrTiO₃), used for initial validation of structural validity and composition fidelity in unconditional generation. It supports proxy evaluation (e.g., structure/composition validity, CrystalNN fingerprint coverage) but is not used for DFT-based stability assessment due to its limited size and simplicity.

## Links

- Paper: [57 Scalable Diffusion for Materials Generation](../papers/57_Scalable_Diffusion_for_Materials_Generation.md)
- Task: [task page](../tasks/57_Scalable_Diffusion_for_Materials_Generation_task_1.md)
- Dataset: [Perov5](../datasets/Perov5.md)
- Dataset URL: None

## Task Context

Generating novel, physically stable crystal structures for materials discovery, where stability is rigorously assessed via Density Functional Theory (DFT)-computed formation energy and decomposition energy relative to convex hulls. The task requires scaling generative modeling to large, complex chemical systems (e.g., multi-element crystals with >20 atoms) while ensuring generated structures are synthetically plausible and thermodynamically stable.

## Metadata

- Dataset use ID: `dataset_use_6c5cc219695a`
- Original dataset title: Perov5
- Tags: crystal structure generation, materials discovery, thermodynamic stability prediction
