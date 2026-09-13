# 57_Scalable Diffusion for Materials Generation - GNoME (Graph Networks for Materials Exploration)

## Dataset Use

A large-scale dataset of ~2.2 million stable and semi-stable crystal structures generated via high-throughput ab initio random structure search and substitution, including both known and novel materials. In this paper, GNoME is used for training the conditional UniMat model (Section 3.3) and for constructing a more challenging convex hull baseline to evaluate decomposition energy. It enables zero-shot generalization to unseen compositions and supports comparison against AIRSS in conditional generation efficiency.

## Links

- Paper: [57 Scalable Diffusion for Materials Generation](../papers/57_Scalable_Diffusion_for_Materials_Generation.md)
- Task: [task page](../tasks/57_Scalable_Diffusion_for_Materials_Generation_task_1.md)
- Dataset: [GNoME (Graph Networks for Materials Exploration)](../datasets/GNoME_Graph_Networks_for_Materials_Exploration.md)
- Dataset URL: https://github.com/google-research/google-research/tree/master/gnome

## Task Context

Generating novel, physically stable crystal structures for materials discovery, where stability is rigorously assessed via Density Functional Theory (DFT)-computed formation energy and decomposition energy relative to convex hulls. The task requires scaling generative modeling to large, complex chemical systems (e.g., multi-element crystals with >20 atoms) while ensuring generated structures are synthetically plausible and thermodynamically stable.

## Metadata

- Dataset use ID: `dataset_use_962cde31daf3`
- Original dataset title: GNoME (Graph Networks for Materials Exploration)
- Tags: crystal structure generation, materials discovery, thermodynamic stability prediction
