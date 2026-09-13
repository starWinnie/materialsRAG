# 10_CrystalFramer - Open Quantum Materials Database

## Dataset Use

A high-throughput computational database containing 817,636 materials with DFT-derived properties: formation energy (_oqmd_delta_e), bandgap (_oqmd_band_gap), and energy above hull (_oqmd_stability). Used in this work to assess scalability and robustness of CrystalFramer on a much larger scale than prior benchmarks — specifically for three regression tasks with splits of ~654k / ~81.8k / ~81.8k — confirming performance gains hold under massive data regime and validating practical applicability.

## Links

- Paper: [10 CrystalFramer](../papers/10_CrystalFramer.md)
- Task: [task page](../tasks/10_CrystalFramer_task_1.md)
- Dataset: [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)
- Dataset URL: https://oqmd.org/

## Task Context

Predicting multiple physical properties of crystalline materials from their 3D crystal structures, including formation energy, total energy, bandgap (under two DFT functionals), energy above hull, bulk modulus, and shear modulus — all requiring SE(3)-invariant representations that respect periodicity, rotational/translation symmetry, and unit-cell ambiguity.

## Metadata

- Dataset use ID: `dataset_use_e1f9ed19f6e1`
- Original dataset title: Open Quantum Materials Database (OQMD)
- Tags: crystal property prediction, SE(3)-invariant modeling, materials property regression
