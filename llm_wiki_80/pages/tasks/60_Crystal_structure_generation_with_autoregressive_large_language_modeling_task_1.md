# 60_Crystal structure generation with autoregressive large language modeling - Task 1

## Task Description

Generating plausible, physically valid crystal structures for inorganic compounds given only their chemical composition (and optionally space group), with the goal of producing candidates suitable for downstream crystal structure prediction (CSP) and materials discovery workflows.

## Metadata

- Task ID: `task_ed846788cc4a`
- Source paper: [60 Crystal structure generation with autoregressive large language modeling](../papers/60_Crystal_structure_generation_with_autoregressive_large_language_modeling.md)
- Tags: crystal structure generation, inorganic materials design, CSP candidate generation

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_Materials_Proj.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org/

A DFT-optimized database of inorganic crystal structures, containing ~3.6 million total structures obtained from the Materials Project (downloaded April 2022), covering compounds with 1–10 elements, up to atomic number 94 (excluding Po, At, Rn, Fr, Ra). It includes ~800,000 unique formulas and 1.2 million unique cell compositions. This dataset was converted to CIF format using pymatgen and formed the core training corpus (~2.3 million CIF files after deduplication) for CrystaLLM, directly supporting the autoregressive language modeling task of generating syntactically and physically valid CIF files from compositional prompts.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_Open_Quantum_M.md)
- Original title in paper: Open Quantum Materials Database (OQMD)
- Link: https://oqmd.org/

A high-throughput DFT database of predicted inorganic materials, contributing to the combined ~3.6 million structure dataset. Specifically, version 1.5 (released October 2021) was used. The OQMD structures—particularly many pyrochlores used in validation—provided diverse, computationally generated crystal structures that expanded coverage beyond experimentally reported entries, enabling CrystaLLM to learn broader structural patterns and support generalization to unseen compositions and space groups during training and benchmarking.

### [NOMAD Repository](../datasets/NOMAD_Repository.md)

- Usage page: [usage note](../dataset_uses/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_NOMAD_Reposito.md)
- Original title in paper: NOMAD Repository
- Link: https://nomad-lab.eu/

A large-scale repository of computational materials science data, including DFT-optimized crystal structures. Structures were downloaded from NOMAD in April 2023 and integrated into the unified ~3.6 million structure dataset. NOMAD contributed additional structural diversity—especially for less common stoichiometries and element combinations—which helped improve CrystaLLM’s ability to generate valid structures for underrepresented classes (e.g., intermetallics, mixed-anion compounds) during both training and challenge-set evaluation.

### [Perov-5](../datasets/Perov-5.md)

- Usage page: [usage note](../dataset_uses/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_Perov-5_datase.md)
- Original title in paper: Perov-5
- Link: https://archive.materialscloud.org/record/2020.0026/v1

A benchmark dataset of 18,928 perovskite structures used to evaluate CrystaLLM’s conditional generation performance (i.e., predicting structures given composition). It was split into train/validation/test sets (60-20-20) and used to train and benchmark CrystaLLM variants specifically for perovskite CSP tasks. The dataset supports the task of assessing how well CrystaLLM recovers known ground-state perovskite structures from cell composition alone, measured via match rate and RMSE against ground truth.

### [Carbon-24](../datasets/Carbon-24.md)

- Usage page: [usage note](../dataset_uses/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_Carbon-24_data.md)
- Original title in paper: Carbon-24
- Link: https://archive.materialscloud.org/record/2020.0026/v1

A benchmark dataset of 10,153 carbon allotropes used to evaluate CrystaLLM’s conditional and unconditional generation capabilities. It was split using the same 60-20-20 protocol as Perov-5 and employed to assess model performance on complex, low-symmetry carbon frameworks. This dataset supports the task of quantifying CrystaLLM’s validity, coverage (COV-P/COV-R), and structural fidelity for elemental systems far outside typical ionic compound paradigms.

### [MP-20](../datasets/MP-20.md)

- Usage page: [usage note](../dataset_uses/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_MP-20_dataset_.md)
- Original title in paper: MP-20
- Link: https://materialsproject.org/

A benchmark subset of 45,231 stable inorganic materials drawn from the Materials Project, representing diverse structural classes. Used for both conditional (CSP) and unconditional generation evaluation, it supports the task of measuring CrystaLLM’s generalizability across broad chemical space—including validity, compositional validity, and coverage metrics—under standardized train/validation/test splits aligned with prior generative models like CDVAE.

### [MPTS-52](../datasets/MPTS-52.md)

- Usage page: [usage note](../dataset_uses/60_Crystal_structure_generation_with_autoregressive_large_language_modeling_MPTS-52_datase.md)
- Original title in paper: MPTS-52
- Link: https://github.com/sparks-baird/mp-time-split

A challenging benchmark dataset of 40,476 inorganic materials, notable for containing structures with up to 52 atoms per unit cell—making it the most complex benchmark used. It was split into 27,380/5,000/8,096 train/validation/test sets (matching DiffCSP’s protocol) and used to rigorously test CrystaLLM’s ability to generate large, complex structures under composition-only conditioning. This dataset directly supports the task of evaluating scalability and robustness in high-atom-count CSP scenarios.
