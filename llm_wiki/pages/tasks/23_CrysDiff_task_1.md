# 23_CrysDiff - Task 1

## Task Description

Predicting crystal properties (e.g., formation energy, bandgap, bulk modulus) from 3D crystal structures represented as atom types, fractional atomic coordinates, and lattice vectors — specifically by leveraging self-supervised pre-training on unlabeled crystal structures to improve data efficiency and accuracy in downstream regression tasks with sparse labeled data.

## Metadata

- Task ID: `task_1f1a85917ec8`
- Source paper: [23 CrysDiff](../papers/23_CrysDiff.md)
- Tags: crystal property prediction, 3D structure-based regression, self-supervised pre-training

## Supporting Datasets

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/23_CrysDiff_JARVIS-DFT_dataset_use_8fe9915f1b57.md)
- Original title in paper: JARVIS-DFT
- Link: https://jarvis.nist.gov/

A publicly available materials database containing 55,722 DFT-calculated crystalline materials, each with 19 computed properties including formation energy, bandgap (OPT and MBJ), total energy, Ehull, bulk modulus (Kv), shear modulus (Gv), SLME (%), and spillage. It provides full 3D structural information: atom types (A), fractional coordinates (F), and lattice vectors (L). In this paper, JARVIS-DFT is used exclusively for the downstream fine-tuning and evaluation phase — i.e., to train and test the crystal property prediction models on nine target properties under standard train/val/test splits (80%/10%/10%).

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/23_CrysDiff_Materials_Project_dataset_use_d28fd2df6bc1.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org/

A large-scale computational materials database containing over 100,000+ DFT-optimized crystal structures, each annotated with structural metadata (space group, lattice parameters, atomic positions) and computed properties. In this paper, MP contributes ~800K untagged crystal graph data (i.e., structures without property labels) used solely for self-supervised pre-training of CrysDiff via crystal structure reconstruction — enabling learning of latent marginal distributions p(F, L | A) without supervision.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/23_CrysDiff_Open_Quantum_Materials_Database_dataset_use_eb7b12844189.md)
- Original title in paper: OQMD (Open Quantum Materials Database)
- Link: https://oqmd.org/

A high-throughput DFT database containing ~400,000+ predicted crystal structures and their computed thermodynamic properties (e.g., formation energy). Like MP, it provides full 3D structural representations (A, F, L) but no experimental property labels. In this paper, OQMD contributes the remaining portion (~800K total) of unlabelled crystal structures used for pre-training CrysDiff, alongside MP. It serves the same role as MP: enabling unsupervised learning of crystal geometry distributions via diffusion-based reconstruction.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/23_CrysDiff_Open_Quantum_Materials_Database_dataset_use_12bede9081fa.md)
- Original title in paper: OQMD-EXP
- Link: https://oqmd.org/

A small experimental subset of OQMD containing 1,500 experimentally measured formation energies for crystalline materials — curated from literature and validated against synthesis outcomes. This dataset is used only in the experimental validation phase to assess how well CrysDiff mitigates DFT calculation bias: models are fine-tuned on combinations of DFT data (from JARVIS-DFT or OQMD) plus varying percentages (20% or 80%) of OQMD-EXP, then evaluated on held-out experimental formation energy values.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Representation / Feature Construction
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
