# 10_CrystalFramer - Task 1

## Task Description

Predicting multiple physical properties of crystalline materials from their 3D crystal structures, including formation energy, total energy, bandgap (under two DFT functionals), energy above hull, bulk modulus, and shear modulus — all requiring SE(3)-invariant representations that respect periodicity, rotational/translation symmetry, and unit-cell ambiguity.

## Metadata

- Task ID: `task_f4a8c4f8f856`
- Source paper: [10 CrystalFramer](../papers/10_CrystalFramer.md)
- Tags: crystal property prediction, SE(3)-invariant modeling, materials property regression

## Supporting Datasets

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/10_CrystalFramer_JARVIS-DFT_dataset_use_90b21b3174ab.md)
- Original title in paper: JARVIS-DFT 3D 2021
- Link: https://jarvis.nist.gov/

A publicly available dataset of 55,723 crystalline materials, each represented by its 3D unit cell (atomic species, Cartesian coordinates, lattice vectors) and annotated with DFT-simulated properties: formation energy per atom, total energy (OptB88vdW), bandgap (OptB88vdW and TBmBJ), and energy above hull. Used in this paper to train and evaluate CrystalFramer on five regression tasks with fixed train/validation/test splits (44,578 / 5,572 / 5,572 for most targets; 14,537 / 1,817 / 1,817 for MBJ bandgap), serving as a benchmark for SE(3)-invariant crystal encoders.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/10_CrystalFramer_Materials_Project_dataset_use_8374071ffb4a.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org/

A large-scale database of ~69,239 synthetically feasible crystalline materials, providing DFT-calculated properties including formation energy, PBE bandgap, bulk modulus, and shear modulus. In this paper, it is used for crystal property prediction across four regression tasks using standardized data splits (60,000 / 5,000 / 4,239 for formation energy and bandgap; ~4,664 / ~393 / ~393 for moduli), enabling comparison against state-of-the-art models and validation of generalization beyond JARVIS.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/10_CrystalFramer_Open_Quantum_Materials_Database_dataset_use_e1f9ed19f6e1.md)
- Original title in paper: Open Quantum Materials Database (OQMD)
- Link: https://oqmd.org/

A high-throughput computational database containing 817,636 materials with DFT-derived properties: formation energy (_oqmd_delta_e), bandgap (_oqmd_band_gap), and energy above hull (_oqmd_stability). Used in this work to assess scalability and robustness of CrystalFramer on a much larger scale than prior benchmarks — specifically for three regression tasks with splits of ~654k / ~81.8k / ~81.8k — confirming performance gains hold under massive data regime and validating practical applicability.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Representation / Feature Construction
- Screening / Prediction
<!-- RD_STAGES_END -->
