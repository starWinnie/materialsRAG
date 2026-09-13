# Materials Project (MP) database

## Metadata

- Dataset ID: `dataset_21f2e95f846f`
- Aliases: Materials Project (MP) database
- Links: https://materialsproject.org, https://next-gen.materialsproject.org/
- Used by papers: 2
- Dataset usage records: 2

## Description Examples

- The 2018.6.1 version contains 69,239 crystalline materials with computed formation energies (Ef) and PBE bandgaps (Eg); used for training and evaluating back-end models (e.g., CGCNN, ALIGNN, MEGNET) and benchmarking ct-UAE performance on formation energy and bandgap prediction. The dataset is split into 60,000 training, 5,000 validation, and 4,239 test samples. It supports the core task by providing ground-truth labels for supervised pretraining of front-end embeddings and downstream property prediction evaluation.
- A publicly available DFT-based high-throughput computational materials database containing over 154,718 entries with thermodynamic, electronic, and structural properties (e.g., formation energy above hull, band gap, crystal structure, unit cell parameters). In this paper, it serves as the primary source for the initial material pool; the authors query it via API and apply thermodynamic stability (Ehull ≤ 0.05 eV/atom), semiconductor band gap (0.1–2 eV), unit cell size (Natoms < 20, Nelements < 4), and elemental constraints (excluding H, lanthanides, actinides) to construct the 2675-material first-level dataset used for unsupervised clustering and feature engineering.

## Uses

- [06_Transformer_Atomic_Embeddings](../dataset_uses/06_Transformer_Atomic_Embeddings_Materials_Project_MP_database_datase_set_use_80bb860fcd04.md): [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings_paper_dd99eeb08a7c.md), [task](../tasks/06_Transformer_Atomic_Embeddings_task_1_task_337f2d813b5e.md)
- [08_HiBoFL_Thermal_Conductivity](../dataset_uses/08_HiBoFL_Thermal_Conductivity_Materials_Project_MP_database_dataset_set_use_7f5787164691.md): [08 HiBoFL Thermal Conductivity](../papers/08_HiBoFL_Thermal_Conductivity_paper_cdf2df178098.md), [task](../tasks/08_HiBoFL_Thermal_Conductivity_task_1_task_29d66873e68c.md)
