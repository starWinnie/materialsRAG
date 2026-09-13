# 31_Superconductivity_Ordered_Disordered - Task 1

## Task Description

Predicting the superconducting transition temperature (Tc) of materials given their 3D crystal structures — including both ordered and disordered configurations — to enable high-Tc superconductor screening from known structural databases such as ICSD. The task supports identifying promising candidate superconductors for experimental validation by ranking structures based on predicted Tc values.

## Metadata

- Task ID: `task_e583c77ddbb2`
- Source paper: [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered.md)
- Tags: Tc prediction, superconductor screening, disordered structure modeling

## Supporting Datasets

### [SuperCon3D](../datasets/SuperCon3D.md)

- Usage page: [usage note](../dataset_uses/31_Superconductivity_Ordered_Disordered_SuperCon3D_dataset_use_1ec550fb8fdf.md)
- Original title in paper: SuperCon3D
- Link: https://github.com/pincher-chen/SODNet

SuperCon3D is a newly constructed dataset containing 1,578 experimentally verified superconductors, each with both a 3D crystal structure (ordered or disordered, including substitutional, positional, and combined disorder types) and its experimentally measured superconducting transition temperature (Tc). It was built by matching 11,949 superconductors from the SuperCon database (with chemical formulas and Tc) against 208,425 entries from the ICSD database using chemical composition, space group, and lattice parameters; hydrogen-enriched superconductors were supplemented from literature. This dataset directly supports the Tc prediction task for training and evaluating SODNet and benchmarking other property predictors.

### [Inorganic Crystal Structure Database](../datasets/Inorganic_Crystal_Structure_Database.md)

- Usage page: [usage note](../dataset_uses/31_Superconductivity_Ordered_Disordered_Inorganic_Crystal_Structure_Database_dataset_use_e.md)
- Original title in paper: ICSD (Inorganic Crystal Structure Database)
- Link: https://icsd.products.fiz-karlsruhe.de/

The ICSD contains over 200,000 experimentally determined ordered and disordered inorganic crystal structures. In this paper, it serves two roles: (1) as the source of structural data used to construct SuperCon3D via matching with SuperCon entries; and (2) as the external candidate pool for high-Tc screening — SODNet is applied to predict Tc for ~200k ICSD entries (including disordered ones), yielding 27 prioritized candidates (e.g., Ba1.1432Co0.1429O3.0009Rh0.8574, ErH3) for experimental follow-up. Thus, ICSD supports both dataset construction and real-world superconductor screening.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/31_Superconductivity_Ordered_Disordered_Materials_Project_dataset_use_9c28764cb72e.md)
- Original title in paper: Materials Project
- Link: https://next-gen.materialsproject.org

A computational materials database containing ~1.14 million stable 3D crystal structures (preprocessed and deduplicated), sourced alongside OQMD, Matgen, and ICSD for pre-training DiffCSP-SC. It provides diverse atomic species, lattice geometries, and coordination environments not fully covered in the small SuperCon3D dataset. This large-scale pre-training data enables robust representation learning for crystal generation and improves the model’s ability to generalize to novel high-Tc structures — supporting the inverse design task by expanding the valid search space before fine-tuning on SuperCon3D.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/31_Superconductivity_Ordered_Disordered_Open_Quantum_Materials_Database_dataset_use_8a072c.md)
- Original title in paper: OQMD (Open Quantum Materials Database)
- Link: https://www.oqmd.org

A database of computationally predicted stable and metastable inorganic crystal structures (~300k+ entries at time of publication), used jointly with Materials Project, Matgen, and ICSD to assemble the ~1.14 million-structure pre-training corpus for DiffCSP-SC. Its inclusion ensures broad coverage of elemental combinations and structural motifs beyond experimentally synthesized superconductors, thereby improving the generative model’s capacity to sample chemically plausible and structurally valid crystals during high-Tc-targeted inverse design.

### [Matgen](../datasets/Matgen.md)

- Usage page: [usage note](../dataset_uses/31_Superconductivity_Ordered_Disordered_Matgen_dataset_use_c2144aef171b.md)
- Original title in paper: Matgen
- Link: https://matgen.nscc-gz.cn

A Chinese materials database hosting computationally generated 3D crystal structures, integrated with Materials Project, OQMD, and ICSD to form the 1.14 million-structure pre-training set for DiffCSP-SC. It contributes additional structural diversity — particularly for underrepresented elements and stoichiometries — enabling the diffusion model to learn generalizable periodic lattice and atomic coordinate distributions, which is critical for generating novel, physically realistic superconductor candidates not present in SuperCon3D.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
