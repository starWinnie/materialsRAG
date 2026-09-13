# MatBench

## Metadata

- Dataset ID: `dataset_3ee88ee61ae1`
- Aliases: MatBench, Matbench
- Links: https://matbench.materialsproject.org, https://matbench.materialsproject.org/
- Used by papers: 3
- Dataset usage records: 3

## Description Examples

- A standardized benchmark suite for materials property prediction containing several task-specific datasets: matbench_jdft2d (636 layered materials, exfoliation energy), matbench_mp_e_form (132,752 structures, formation energy), matbench_log_gvrh (10,987 structures, shear modulus), and matbench_dielectric (4,764 structures, refractive index). These are used to assess PRDNet’s generalization across heterogeneous property types, low-data regimes, and distinct material families (e.g., 2D vs. 3D), enabling fair comparison against state-of-the-art baselines.
- Matbench is an automated benchmark suite for materials property prediction, containing three composition-based experimental and computational regression tasks: experimentally measured band gap (2,154 samples), experimentally measured yield strength of steels (312 samples), calculated formation energy (37,217 samples), and calculated refractive index (4,764 samples). In this paper, Matbench is used to evaluate OOD extrapolation capability across diverse property types and data sources (experimental vs. computational), supporting the task of identifying top-performing candidates whose property values exceed the training distribution.
- MatBench is a standardized benchmark for materials property prediction, featuring tasks across vastly different scales and complexities. In this work, two MatBench tasks are used: 'e_form' (132,752 crystals) for large-scale evaluation and 'jdft2d' (636 2D crystals) for small-scale, challenging evaluation. These datasets test the scalability and generalizability of ComFormer, particularly its ability to handle extremely large datasets and sparse, low-data regimes, with performance reported using MAE and RMSE metrics.

## Uses

- [01_PRDNet](../dataset_uses/01_PRDNet_MatBench_dataset_use_1f147f5f103e_set_use_1f147f5f103e.md): [01 PRDNet](../papers/01_PRDNet_paper_5138be33ab55.md), [task](../tasks/01_PRDNet_task_1_task_b7092f83ac79.md)
- [17_Known_Unknowns_OOD](../dataset_uses/17_Known_Unknowns_OOD_Matbench_dataset_use_4148911e842f_set_use_4148911e842f.md): [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD_paper_0accd46e95fd.md), [task](../tasks/17_Known_Unknowns_OOD_task_1_task_e097cf9a59e5.md)
- [21_ComFormer](../dataset_uses/21_ComFormer_MatBench_dataset_use_339a4297cb4d_set_use_339a4297cb4d.md): [21 ComFormer](../papers/21_ComFormer_paper_7eb9d3cfd258.md), [task](../tasks/21_ComFormer_task_1_task_b2fdc1e458d6.md)
