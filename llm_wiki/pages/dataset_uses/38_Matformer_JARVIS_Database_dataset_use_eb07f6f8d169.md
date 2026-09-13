# 38_Matformer - JARVIS Database

## Dataset Use

A curated, DFT-computed materials database containing structural and property data for ~100,000 materials, designed for data-driven materials discovery. In this paper, the JARVIS dataset is used to evaluate Matformer on five tasks: formation energy, optical band gap (OPT), total energy, energy above hull (Ehull), and modified Becke–Johnson (MBJ) band gap. It provides standardized crystal structures (including lattice matrices and atomic coordinates) and associated property labels, supporting validation of periodic invariance and pattern encoding in crystal representation learning.

## Links

- Paper: [38 Matformer](../papers/38_Matformer.md)
- Task: [task page](../tasks/38_Matformer_task_1.md)
- Dataset: [JARVIS Database](../datasets/JARVIS_Database.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Predicting multiple physical and electronic properties of crystalline materials from their atomic structure, including formation energy, band gap, bulk modulus, and shear modulus, using periodic graph representations that respect crystal symmetry and repeating lattice patterns.

## Metadata

- Dataset use ID: `dataset_use_eb07f6f8d169`
- Original dataset title: JARVIS (Joint Automated Repository for Various Integrated Simulations)
- Tags: crystal property prediction, materials property prediction, periodic graph learning

<!-- RD_STAGES_START -->
## R&D Stages

This dataset-use record supports the following R&D stages:

- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
<!-- RD_STAGES_END -->
