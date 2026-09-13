# 57_Scalable Diffusion for Materials Generation - Task 1

## Task Description

Generating novel, physically stable crystal structures for materials discovery, where stability is rigorously assessed via Density Functional Theory (DFT)-computed formation energy and decomposition energy relative to convex hulls. The task requires scaling generative modeling to large, complex chemical systems (e.g., multi-element crystals with >20 atoms) while ensuring generated structures are synthetically plausible and thermodynamically stable.

## Metadata

- Task ID: `task_24b6899c3ddd`
- Source paper: [57 Scalable Diffusion for Materials Generation](../papers/57_Scalable_Diffusion_for_Materials_Generation.md)
- Tags: crystal structure generation, materials discovery, thermodynamic stability prediction

## Supporting Datasets

### [Materials Project (MP-20)](../datasets/Materials_Project_MP-20.md)

- Usage page: [usage note](../dataset_uses/57_Scalable_Diffusion_for_Materials_Generation_Materials_Project_MP-20_dataset_use_214b288.md)
- Original title in paper: Materials Project (MP-20)
- Link: https://materialsproject.org

A curated dataset of ~20,000 experimentally verified and computationally relaxed inorganic crystal structures from the Materials Project database, covering diverse chemical compositions and structural complexities. In this paper, MP-20 serves as the primary training and evaluation set for unconditional UniMat generation; it is used to train diffusion models, compute proxy metrics (validity, coverage, property statistics), and—after DFT relaxation—evaluate per-composition formation energy and stability against convex hull baselines.

### [Perov5](../datasets/Perov5.md)

- Usage page: [usage note](../dataset_uses/57_Scalable_Diffusion_for_Materials_Generation_Perov5_dataset_use_6c5cc219695a.md)
- Original title in paper: Perov5
- Link: None

A small-scale benchmark dataset containing 5 perovskite crystal structures (e.g., CaTiO₃, SrTiO₃), used for initial validation of structural validity and composition fidelity in unconditional generation. It supports proxy evaluation (e.g., structure/composition validity, CrystalNN fingerprint coverage) but is not used for DFT-based stability assessment due to its limited size and simplicity.

### [Carbon24](../datasets/Carbon24.md)

- Usage page: [usage note](../dataset_uses/57_Scalable_Diffusion_for_Materials_Generation_Carbon24_dataset_use_4cce8f2352a0.md)
- Original title in paper: Carbon24
- Link: None

A dataset of 24 carbon allotrope structures (e.g., diamond, graphite, various predicted carbon phases), used to evaluate generative performance on elemental systems with high symmetry and strong covalent bonding. It supports proxy metrics including structural validity, composition recall, and property distribution fidelity (e.g., density, number of atoms), but is not subjected to DFT verification in this work.

### [Materials Project 2021 (MP 2021)](../datasets/Materials_Project_2021_MP_2021.md)

- Usage page: [usage note](../dataset_uses/57_Scalable_Diffusion_for_Materials_Generation_Materials_Project_2021_MP_2021_dataset_use_.md)
- Original title in paper: Materials Project 2021 (MP 2021)
- Link: https://materialsproject.org

The full July 2021 release of the Materials Project database, containing over 140,000 experimentally verified and DFT-relaxed inorganic compounds. This dataset is used exclusively to construct the convex hull phase diagram against which decomposition energies (Ed) of generated structures are computed—enabling rigorous stability assessment across differing compositions. It is not used for model training or unconditional generation.

### [GNoME (Graph Networks for Materials Exploration)](../datasets/GNoME_Graph_Networks_for_Materials_Exploration.md)

- Usage page: [usage note](../dataset_uses/57_Scalable_Diffusion_for_Materials_Generation_GNoME_Graph_Networks_for_Materials_Explorat.md)
- Original title in paper: GNoME (Graph Networks for Materials Exploration)
- Link: https://github.com/google-research/google-research/tree/master/gnome

A large-scale dataset of ~2.2 million stable and semi-stable crystal structures generated via high-throughput ab initio random structure search and substitution, including both known and novel materials. In this paper, GNoME is used for training the conditional UniMat model (Section 3.3) and for constructing a more challenging convex hull baseline to evaluate decomposition energy. It enables zero-shot generalization to unseen compositions and supports comparison against AIRSS in conditional generation efficiency.
