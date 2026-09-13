# 57_Scalable Diffusion for Materials Generation - Materials Project 2021 (MP 2021)

## Dataset Use

The full July 2021 release of the Materials Project database, containing over 140,000 experimentally verified and DFT-relaxed inorganic compounds. This dataset is used exclusively to construct the convex hull phase diagram against which decomposition energies (Ed) of generated structures are computed—enabling rigorous stability assessment across differing compositions. It is not used for model training or unconditional generation.

## Links

- Paper: [57 Scalable Diffusion for Materials Generation](../papers/57_Scalable_Diffusion_for_Materials_Generation.md)
- Task: [task page](../tasks/57_Scalable_Diffusion_for_Materials_Generation_task_1.md)
- Dataset: [Materials Project 2021 (MP 2021)](../datasets/Materials_Project_2021_MP_2021.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating novel, physically stable crystal structures for materials discovery, where stability is rigorously assessed via Density Functional Theory (DFT)-computed formation energy and decomposition energy relative to convex hulls. The task requires scaling generative modeling to large, complex chemical systems (e.g., multi-element crystals with >20 atoms) while ensuring generated structures are synthetically plausible and thermodynamically stable.

## Metadata

- Dataset use ID: `dataset_use_bae1ad8e5662`
- Original dataset title: Materials Project 2021 (MP 2021)
- Tags: crystal structure generation, materials discovery, thermodynamic stability prediction
