# 70_Scalable crystal structure relaxation using an iteration-free deep generative model with uncertainty quantification - Task 1

## Task Description

Predicting equilibrium crystal structures directly from unrelaxed initial configurations in milliseconds per structure, without iterative optimization, to enable scalable and trustworthy pre-relaxation for downstream property calculations and large-scale virtual screening.

## Metadata

- Task ID: `task_bcf8db5ad546`
- Source paper: [70 Scalable crystal structure relaxation using an iteration-free deep generative model with uncertainty quantification](../papers/70_Scalable_crystal_structure_relaxation_using_an_iteration-free_deep_generative_model_wit.md)
- Tags: crystal structure relaxation, geometric prediction, pre-relaxation

## Supporting Datasets

### [X-Mn-O dataset](../datasets/X-Mn-O_dataset.md)

- Usage page: [usage note](../dataset_uses/70_Scalable_crystal_structure_relaxation_using_an_iteration-free_deep_generative_model_wit.md)
- Original title in paper: X-Mn-O dataset
- Link: https://zenodo.org/records/8081655

A hypothetical elemental substitution database derived from the Materials Project, containing 28,579 pairs of unrelaxed and DFT-relaxed crystal structures of ternary oxides (e.g., Sr4Mn2O6, Ba1Mn4O8) formed by substituting X elements (Mg, Ca, Ba, Sr) into Mn-O prototypes. Each pair includes full atomic coordinates, lattice parameters, and cell volumes for both states. It is used to train and benchmark DeepRelax’s ability to predict relaxed geometries with high accuracy, especially for structures exhibiting large deviations from equilibrium.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/70_Scalable_crystal_structure_relaxation_using_an_iteration-free_deep_generative_model_wit.md)
- Original title in paper: Materials Project (MP) dataset
- Link: https://figshare.com/articles/dataset/MPF_2021_2_8/19470599

A large-scale computational materials database containing 62,724 DFT-validated structure pairs (initial and fully relaxed), spanning 89 elements and 62,783 compounds, with structural snapshots captured during relaxation. The dataset provides comprehensive ground-truth atomic coordinates, lattice matrices, and cell volumes. It is used to train DeepRelax for universal applicability across diverse chemistries and crystal symmetries, and to evaluate robustness on structures where initial configurations are often close to relaxed states.

### [C2DB](../datasets/C2DB.md)

- Usage page: [usage note](../dataset_uses/70_Scalable_crystal_structure_relaxation_using_an_iteration-free_deep_generative_model_wit.md)
- Original title in paper: Computational 2D Materials Database (C2DB)
- Link: https://cmr.fysik.dtu.dk/c2db/c2db.html

A database of 11,581 pairs of initial and DFT-relaxed 2D crystal structures covering 62 elements, including monolayers and bilayers. Each entry contains full Cartesian coordinates, lattice vectors, and cell metrics for both unrelaxed and relaxed states. It is used to evaluate DeepRelax’s transfer learning capability—where a model pre-trained on 3D MP data is fine-tuned—to assess generalization to low-dimensional materials without requiring energy/force labels.

### [MoS2 defect dataset](../datasets/MoS2_defect_dataset.md)

- Usage page: [usage note](../dataset_uses/70_Scalable_crystal_structure_relaxation_using_an_iteration-free_deep_generative_model_wit.md)
- Original title in paper: MoS2 defect dataset
- Link: https://research.constructor.tech/p/2d-defects-prediction

A collection of 5,933 MoS2 supercell configurations (8×8) with neutral point defects, curated by Huang et al., providing unrelaxed and DFT-relaxed structures. It includes atomic positions and lattice parameters for each defect configuration. This dataset is used to test DeepRelax’s robustness to structural imperfections and validate its performance on defective crystals—critical for realistic materials modeling—via MAE analysis and DFT residual-step reduction.

### [Layered van der Waals (vdW) crystals dataset](../datasets/Layered_van_der_Waals_vdW_crystals_dataset.md)

- Usage page: [usage note](../dataset_uses/70_Scalable_crystal_structure_relaxation_using_an_iteration-free_deep_generative_model_wit.md)
- Original title in paper: Layered van der Waals (vdW) crystals dataset
- Link: None

An in-house dataset of 58 layered vdW crystals (e.g., graphite, h-BN analogs) covering 29 elements, each with unrelaxed, DFT-D3-relaxed, and DeepRelax-predicted structures. It includes interlayer distances, intra-layer bond lengths, and lattice parameters. Used to demonstrate DeepRelax’s transferability to weakly bonded systems where interlayer relaxation dominates, validating predictions via interlayer distance MAE and bond-length error analysis.
