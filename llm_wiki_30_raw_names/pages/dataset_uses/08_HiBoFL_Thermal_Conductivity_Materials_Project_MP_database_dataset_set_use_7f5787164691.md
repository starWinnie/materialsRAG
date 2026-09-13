# 08_HiBoFL_Thermal_Conductivity - Materials Project (MP) database

## Dataset Use

A publicly available DFT-based high-throughput computational materials database containing over 154,718 entries with thermodynamic, electronic, and structural properties (e.g., formation energy above hull, band gap, crystal structure, unit cell parameters). In this paper, it serves as the primary source for the initial material pool; the authors query it via API and apply thermodynamic stability (Ehull ≤ 0.05 eV/atom), semiconductor band gap (0.1–2 eV), unit cell size (Natoms < 20, Nelements < 4), and elemental constraints (excluding H, lanthanides, actinides) to construct the 2675-material first-level dataset used for unsupervised clustering and feature engineering.

## Links

- Paper: [08 HiBoFL Thermal Conductivity](../papers/08_HiBoFL_Thermal_Conductivity_paper_cdf2df178098.md)
- Task: [task page](../tasks/08_HiBoFL_Thermal_Conductivity_task_1_task_29d66873e68c.md)
- Dataset: [Materials Project (MP) database](../datasets/Materials_Project_MP_database_dataset_21f2e95f846f.md)
- Dataset URL: https://next-gen.materialsproject.org/

## Task Context

Identifying semiconductors with ultralow lattice thermal conductivity (κL) — specifically, screening and classifying candidate materials from a vast chemical space to discover those with κL ≤ 2 W/mK at 300 K for thermoelectric applications, while uncovering interpretable structural and compositional descriptors governing ultralow κL.

## Metadata

- Dataset use ID: `dataset_use_7f5787164691`
- Original dataset title: Materials Project (MP) database
- Tags: screening, classifying, discovering, interpreting

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
