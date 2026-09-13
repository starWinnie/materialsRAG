# 51_Unified Model for Crystalline Material Generation - Task 1

## Task Description

Generating thermodynamically stable crystalline materials by simultaneously optimizing both atomic positions and crystal lattice geometry to minimize total energy, enabling de novo design of novel crystals with desired properties such as suitable band gaps for solar-driven hydrogen production or hydrogen storage capacity.

## Metadata

- Task ID: `task_e3db808171fa`
- Source paper: [51 Unified Model for Crystalline Material Generation](../papers/51_Unified_Model_for_Crystalline_Material_Generation.md)
- Tags: crystal generation, geometry optimization, energy minimization, materials discovery

## Supporting Datasets

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/51_Unified_Model_for_Crystalline_Material_Generation_Perov-5_dataset_use_0534bad3ab93.md)
- Original title in paper: Perov-5
- Link: https://doi.org/10.1039/C2EE22748C

A dataset of 5 stable perovskite (cubic) crystal structures with highly uniform geometries but varying chemical compositions; used in this paper for lattice reconstruction and denoising tasks to evaluate how well the proposed models (EGNN and GemsNet) can recover original lattice parameters (a,b,c,α,β,γ) and atomic positions from noisy or unstructured inputs, supporting the core task of generating stable crystal geometries.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/51_Unified_Model_for_Crystalline_Material_Generation_Carbon-24_dataset_use_62013801db90.md)
- Original title in paper: Carbon-24
- Link: https://www.materialscloud.org/work/2020.0036/v1

A dataset of 24 stable carbon-only crystal structures under pressure, exhibiting high geometric diversity (e.g., diamond, graphite, BC8); used to benchmark model performance on reconstructing complex lattice shapes and atomic arrangements, specifically testing the ability of EGNN and GemsNet to generalize across varied topologies while maintaining periodicity and thermodynamic stability during generation.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/51_Unified_Model_for_Crystalline_Material_Generation_Mp-20_dataset_use_39ff5a1e8310.md)
- Original title in paper: Mp-20
- Link: https://materialsproject.org

A curated subset of 20 diverse, experimentally plausible crystalline materials from the Materials Project database, spanning multiple chemical species (including binaries, ternaries, and quaternaries like uranium-containing compounds), lattice symmetries, and structural complexities; used as the primary benchmark for denoising and reconstruction tasks to assess robustness, generalizability, and accuracy of simultaneous atomic position and lattice geometry optimization in realistic, heterogeneous crystal generation scenarios.
