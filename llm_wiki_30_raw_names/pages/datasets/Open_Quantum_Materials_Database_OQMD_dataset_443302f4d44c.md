# Open Quantum Materials Database (OQMD)

## Metadata

- Dataset ID: `dataset_443302f4d44c`
- Aliases: Open Quantum Materials Database (OQMD)
- Links: https://oqmd.org/
- Used by papers: 2
- Dataset usage records: 2

## Description Examples

- A DFT-generated database of predicted inorganic materials, providing formation energies and structural data for over 400,000 compounds. Used alongside MP and JARVIS for cross-database performance validation of ECSG, particularly to assess robustness under class imbalance (11.3% stable samples) and to serve as a reference convex hull for DFT validation of predicted perovskite oxides.
- A high-throughput computational database containing 817,636 materials with DFT-derived properties: formation energy (_oqmd_delta_e), bandgap (_oqmd_band_gap), and energy above hull (_oqmd_stability). Used in this work to assess scalability and robustness of CrystalFramer on a much larger scale than prior benchmarks — specifically for three regression tasks with splits of ~654k / ~81.8k / ~81.8k — confirming performance gains hold under massive data regime and validating practical applicability.

## Uses

- [05_Thermodynamic_Stability_Ensemble](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Open_Quantum_Materials_Database_O_set_use_4cbf254eebe5.md): [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble_paper_dfa00819e2d0.md), [task](../tasks/05_Thermodynamic_Stability_Ensemble_task_1_task_134b6e57d77b.md)
- [10_CrystalFramer](../dataset_uses/10_CrystalFramer_Open_Quantum_Materials_Database_OQMD_dataset_use_7ed_set_use_7ed9f470379f.md): [10 CrystalFramer](../papers/10_CrystalFramer_paper_376c54bdb055.md), [task](../tasks/10_CrystalFramer_task_1_task_f4a8c4f8f856.md)
