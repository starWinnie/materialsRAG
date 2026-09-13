# 57_Scalable Diffusion for Materials Generation - Carbon24

## Dataset Use

A dataset of 24 carbon allotrope structures (e.g., diamond, graphite, various predicted carbon phases), used to evaluate generative performance on elemental systems with high symmetry and strong covalent bonding. It supports proxy metrics including structural validity, composition recall, and property distribution fidelity (e.g., density, number of atoms), but is not subjected to DFT verification in this work.

## Links

- Paper: [57 Scalable Diffusion for Materials Generation](../papers/57_Scalable_Diffusion_for_Materials_Generation.md)
- Task: [task page](../tasks/57_Scalable_Diffusion_for_Materials_Generation_task_1.md)
- Dataset: [Carbon24](../datasets/Carbon24.md)
- Dataset URL: None

## Task Context

Generating novel, physically stable crystal structures for materials discovery, where stability is rigorously assessed via Density Functional Theory (DFT)-computed formation energy and decomposition energy relative to convex hulls. The task requires scaling generative modeling to large, complex chemical systems (e.g., multi-element crystals with >20 atoms) while ensuring generated structures are synthetically plausible and thermodynamically stable.

## Metadata

- Dataset use ID: `dataset_use_4cce8f2352a0`
- Original dataset title: Carbon24
- Tags: crystal structure generation, materials discovery, thermodynamic stability prediction
