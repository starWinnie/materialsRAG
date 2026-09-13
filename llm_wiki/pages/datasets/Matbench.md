# Matbench

## Metadata

- Dataset ID: `dataset_3ee88ee61ae1`
- Aliases: MatBench, Matbench, Matbench v0.1
- Links: https://hackingmaterials.lbl.gov/automatminer/datasets.html, https://matbench.materialsproject.org, https://matbench.materialsproject.org/
- Used by papers: 5
- Dataset usage records: 5

## Description Examples

- A standardized benchmark suite for materials property prediction containing several task-specific datasets: matbench_jdft2d (636 layered materials, exfoliation energy), matbench_mp_e_form (132,752 structures, formation energy), matbench_log_gvrh (10,987 structures, shear modulus), and matbench_dielectric (4,764 structures, refractive index). These are used to assess PRDNet’s generalization across heterogeneous property types, low-data regimes, and distinct material families (e.g., 2D vs. 3D), enabling fair comparison against state-of-the-art baselines.
- Matbench is an automated benchmark suite for materials property prediction, containing three composition-based experimental and computational regression tasks: experimentally measured band gap (2,154 samples), experimentally measured yield strength of steels (312 samples), calculated formation energy (37,217 samples), and calculated refractive index (4,764 samples). In this paper, Matbench is used to evaluate OOD extrapolation capability across diverse property types and data sources (experimental vs. computational), supporting the task of identifying top-performing candidates whose property values exceed the training distribution.
- MatBench is a standardized benchmark for materials property prediction, featuring tasks across vastly different scales and complexities. In this work, two MatBench tasks are used: 'e_form' (132,752 crystals) for large-scale evaluation and 'jdft2d' (636 2D crystals) for small-scale, challenging evaluation. These datasets test the scalability and generalizability of ComFormer, particularly its ability to handle extremely large datasets and sparse, low-data regimes, with performance reported using MAE and RMSE metrics.
- An automated benchmark platform with 13 rigorously curated, domain-diverse solid-state materials property prediction tasks (e.g., phonons, dielectric, perovskites, jdft2d), covering sample sizes from 312 to 132,000 and spanning DFT and experimental sources; used as the primary benchmark to evaluate DenseGNN’s universality, scalability, and performance across materials science domains, including ablation and cross-model fusion studies.
- Matbench v0.1 is a curated benchmark suite comprising 13 distinct supervised machine learning tasks, sourced from 10 independent datasets totaling 312 to 132,752 samples. Each task contains input materials primitives (composition-only or composition + crystal structure) and a single target property (e.g., band gap, formation energy, bulk modulus, metallicity, exfoliation energy), derived from both experimental measurements and density functional theory (DFT) computations. The datasets are precleaned to remove unphysical or task-irrelevant entries (e.g., negative elastic moduli, noble-gas compounds, misconverged DFT structures) and standardized for consistent ML pipeline ingestion. Matbench is used to train, validate, and rigorously evaluate property prediction models—including Automatminer, CGCNN, MEGNet, and Random Forest—via nested cross-validation, enabling unbiased algorithm comparison across property types, data scales, and input modalities.

## Uses

- [01_PRDNet](../dataset_uses/01_PRDNet_Matbench_dataset_use_1f147f5f103e.md): [01 PRDNet](../papers/01_PRDNet.md), [task](../tasks/01_PRDNet_task_1.md)
- [17_Known_Unknowns_OOD](../dataset_uses/17_Known_Unknowns_OOD_Matbench_dataset_use_4148911e842f.md): [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD.md), [task](../tasks/17_Known_Unknowns_OOD_task_1.md)
- [21_ComFormer](../dataset_uses/21_ComFormer_Matbench_dataset_use_339a4297cb4d.md): [21 ComFormer](../papers/21_ComFormer.md), [task](../tasks/21_ComFormer_task_1.md)
- [33_DenseGNN](../dataset_uses/33_DenseGNN_Matbench_dataset_use_40ccd45b11bf.md): [33 DenseGNN](../papers/33_DenseGNN.md), [task](../tasks/33_DenseGNN_task_1.md)
- [42_Matbench](../dataset_uses/42_Matbench_Matbench_dataset_use_cd27b9050483.md): [42 Matbench](../papers/42_Matbench.md), [task](../tasks/42_Matbench_task_1.md)
