# 57_Scalable Diffusion for Materials Generation - Materials Project (MP-20)

## Dataset Use

A curated dataset of ~20,000 experimentally verified and computationally relaxed inorganic crystal structures from the Materials Project database, covering diverse chemical compositions and structural complexities. In this paper, MP-20 serves as the primary training and evaluation set for unconditional UniMat generation; it is used to train diffusion models, compute proxy metrics (validity, coverage, property statistics), and—after DFT relaxation—evaluate per-composition formation energy and stability against convex hull baselines.

## Links

- Paper: [57 Scalable Diffusion for Materials Generation](../papers/57_Scalable_Diffusion_for_Materials_Generation.md)
- Task: [task page](../tasks/57_Scalable_Diffusion_for_Materials_Generation_task_1.md)
- Dataset: [Materials Project (MP-20)](../datasets/Materials_Project_MP-20.md)
- Dataset URL: https://materialsproject.org

## Task Context

Generating novel, physically stable crystal structures for materials discovery, where stability is rigorously assessed via Density Functional Theory (DFT)-computed formation energy and decomposition energy relative to convex hulls. The task requires scaling generative modeling to large, complex chemical systems (e.g., multi-element crystals with >20 atoms) while ensuring generated structures are synthetically plausible and thermodynamically stable.

## Metadata

- Dataset use ID: `dataset_use_214b2884bbba`
- Original dataset title: Materials Project (MP-20)
- Tags: crystal structure generation, materials discovery, thermodynamic stability prediction
