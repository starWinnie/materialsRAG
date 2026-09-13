# 71_A generative model for inorganic materials design - Task 1

## Task Description

Generating stable, diverse, and novel inorganic crystalline materials that satisfy user-specified property constraints—including target chemical composition, crystal symmetry, magnetic density, electronic bandgap, mechanical bulk modulus, and multi-objective criteria such as high magnetic density combined with low supply-chain risk (quantified by Herfindahl–Hirschman Index)—via fine-tuned diffusion-based generative modeling.

## Metadata

- Task ID: `task_e575ca1db58a`
- Source paper: [71 A generative model for inorganic materials design](../papers/71_A_generative_model_for_inorganic_materials_design.md)
- Tags: inverse materials design, crystal structure generation, property-constrained generation

## Supporting Datasets

### [Alex-MP-20](../datasets/Alex-MP-20.md)

- Usage page: [usage note](../dataset_uses/71_A_generative_model_for_inorganic_materials_design_Alex-MP-20_dataset_use_d1c5f86b09fd.md)
- Original title in paper: Alex-MP-20
- Link: https://github.com/microsoft/mattergen

A curated dataset of 607,683 stable inorganic crystal structures with up to 20 atoms per unit cell, recomputed from the Materials Project (MP) and Alexandria databases. It serves as the primary unlabelled training set for pretraining the base MatterGen diffusion model to generate stable and diverse crystals across the periodic table.

### [Alex-MP-ICSD](../datasets/Alex-MP-ICSD.md)

- Usage page: [usage note](../dataset_uses/71_A_generative_model_for_inorganic_materials_design_Alex-MP-ICSD_dataset_use_af9e59a425ae.md)
- Original title in paper: Alex-MP-ICSD
- Link: https://materialsproject.org, https://doi.org/10.24435/materialscloud:m7-50, https://icsd.products.fiz-karlsruhe.de

An extended reference dataset comprising 850,384 unique ordered structures from Materials Project, Alexandria, and the Inorganic Crystal Structure Database (ICSD), used to compute the convex hull for stability evaluation (energy above hull ≤ 0.1 eV/atom). It also forms the basis for novelty assessment—structures not matching any entry in Alex-MP-ICSD (augmented with 117,652 disordered ICSD entries) are deemed 'new'.

### [Magnetic density labelled dataset](../datasets/Magnetic_density_labelled_dataset.md)

- Usage page: [usage note](../dataset_uses/71_A_generative_model_for_inorganic_materials_design_Magnetic_density_labelled_dataset_dat.md)
- Original title in paper: Magnetic density labelled dataset
- Link: https://github.com/microsoft/mattergen

A dataset of 605,000 crystal structures with DFT-calculated magnetic density labels (assuming ferromagnetic ordering), used to fine-tune MatterGen for generating materials with target magnetic density (e.g., >0.2 Å⁻³). This dataset supports the property-guided inverse design task for permanent magnet candidates.

### [Bandgap labelled dataset](../datasets/Bandgap_labelled_dataset.md)

- Usage page: [usage note](../dataset_uses/71_A_generative_model_for_inorganic_materials_design_Bandgap_labelled_dataset_dataset_use_.md)
- Original title in paper: Bandgap labelled dataset
- Link: https://github.com/microsoft/mattergen

A dataset of 42,000 crystal structures with DFT-computed electronic bandgap labels, used to fine-tune MatterGen for generating materials with target bandgap values (e.g., 3.0 eV). It enables electronic-property-constrained generation for applications such as optoelectronics or photocatalysis.

### [Bulk modulus labelled dataset](../datasets/Bulk_modulus_labelled_dataset.md)

- Usage page: [usage note](../dataset_uses/71_A_generative_model_for_inorganic_materials_design_Bulk_modulus_labelled_dataset_dataset.md)
- Original title in paper: Bulk modulus labelled dataset
- Link: https://github.com/microsoft/mattergen

A dataset of 5,000 crystal structures with DFT-calculated bulk modulus labels, used to fine-tune MatterGen for generating superhard materials with target mechanical stiffness (e.g., >400 GPa). Despite its small size, it supports effective conditional generation under data-scarce property constraints.

### [HHI-score + magnetic density joint labelled dataset](../datasets/HHI-score_magnetic_density_joint_labelled_dataset.md)

- Usage page: [usage note](../dataset_uses/71_A_generative_model_for_inorganic_materials_design_HHI-score_magnetic_density_joint_labe.md)
- Original title in paper: HHI-score + magnetic density joint labelled dataset
- Link: https://github.com/microsoft/mattergen

A multi-label dataset combining magnetic density and Herfindahl–Hirschman Index (HHI) scores—quantifying elemental supply-chain concentration—for fine-tuning MatterGen to jointly optimize for high magnetic density and low supply-chain risk. Used to generate rare-earth-free permanent magnet candidates with HHI < 1,500 and magnetic density ≥ 0.2 Å⁻³.
