# 01_PRDNet - Task 1

## Task Description

Predicting multiple physical properties of crystalline materials—including formation energy, band gap, bulk modulus, shear modulus, Young's modulus, exfoliation energy, dielectric constant (refractive index), and metal/non-metal classification—from their atomic structure (i.e., crystal graph defined by atomic types, fractional coordinates, and lattice vectors).

## Metadata

- Task ID: `task_b7092f83ac79`
- Source paper: [01 PRDNet](../papers/01_PRDNet.md)
- Tags: crystal property prediction, materials property regression, materials property classification

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/01_PRDNet_Materials_Project_dataset_use_eb53342235c5.md)
- Original title in paper: Materials Project
- Link: https://huggingface.co/datasets/caobin/CPPbenchmark

A large-scale DFT-computed database of inorganic crystalline materials containing 122,959 stable structures, each annotated with formation energy, band gap, metal/non-metal classification, and—on a subset of 9,473 entries—mechanical properties including bulk modulus, shear modulus, and Young’s modulus. The dataset is used in this paper to train and evaluate PRDNet for multi-task crystal property prediction, serving as the primary benchmark for regression and classification tasks.

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/01_PRDNet_JARVIS-DFT_dataset_use_77880778a960.md)
- Original title in paper: JARVIS-DFT
- Link: None

A DFT-based dataset comprising 75,993 3D crystal structures (dft_3d), each annotated with formation energy, band gap (computed using both OPT and MBJ functionals), bulk modulus, shear modulus, total energy, and energy above hull (Ehull). It also includes the JARVIS-DFT-3D-2021 subset (55,723 entries). This dataset supports comprehensive evaluation of PRDNet across diverse electronic and mechanical property prediction tasks, with emphasis on robustness across computational functionals and stability metrics.

### [Matbench](../datasets/Matbench.md)

- Usage page: [usage note](../dataset_uses/01_PRDNet_Matbench_dataset_use_1f147f5f103e.md)
- Original title in paper: MatBench
- Link: None

A standardized benchmark suite for materials property prediction containing several task-specific datasets: matbench_jdft2d (636 layered materials, exfoliation energy), matbench_mp_e_form (132,752 structures, formation energy), matbench_log_gvrh (10,987 structures, shear modulus), and matbench_dielectric (4,764 structures, refractive index). These are used to assess PRDNet’s generalization across heterogeneous property types, low-data regimes, and distinct material families (e.g., 2D vs. 3D), enabling fair comparison against state-of-the-art baselines.
