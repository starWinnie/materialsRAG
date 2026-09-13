# Open Quantum Materials Database

## Metadata

- Dataset ID: `dataset_f6b0e6dabd69`
- Aliases: OQMD (Open Quantum Materials Database), OQMD-EXP, Open Quantum Materials Database (OQMD), Open Quantum Materials Database (OQMD, 2021 snapshot)
- Links: http://oqmd.org, https://oqmd.org, https://oqmd.org/, https://www.oqmd.org
- Used by papers: 8
- Dataset usage records: 9

## Description Examples

- A DFT-generated database of predicted inorganic materials, providing formation energies and structural data for over 400,000 compounds. Used alongside MP and JARVIS for cross-database performance validation of ECSG, particularly to assess robustness under class imbalance (11.3% stable samples) and to serve as a reference convex hull for DFT validation of predicted perovskite oxides.
- A high-throughput computational database containing 817,636 materials with DFT-derived properties: formation energy (_oqmd_delta_e), bandgap (_oqmd_band_gap), and energy above hull (_oqmd_stability). Used in this work to assess scalability and robustness of CrystalFramer on a much larger scale than prior benchmarks — specifically for three regression tasks with splits of ~654k / ~81.8k / ~81.8k — confirming performance gains hold under massive data regime and validating practical applicability.
- A large-scale ab initio database of ~1M predicted stable and metastable inorganic compounds, with formation energies, crystal structures, and elemental compositions. Its scale (~10× larger than MP) enables rigorous scaling analysis: the paper uses it to validate learning curves (training set size and time effects) on representationally OOD tasks (e.g., leave-H-out), confirm domain misidentification biases, and demonstrate adverse scaling behavior where increased data degrades OOD performance.
- A high-throughput DFT database containing ~400,000+ predicted crystal structures and their computed thermodynamic properties (e.g., formation energy). Like MP, it provides full 3D structural representations (A, F, L) but no experimental property labels. In this paper, OQMD contributes the remaining portion (~800K total) of unlabelled crystal structures used for pre-training CrysDiff, alongside MP. It serves the same role as MP: enabling unsupervised learning of crystal geometry distributions via diffusion-based reconstruction.
- A small experimental subset of OQMD containing 1,500 experimentally measured formation energies for crystalline materials — curated from literature and validated against synthesis outcomes. This dataset is used only in the experimental validation phase to assess how well CrysDiff mitigates DFT calculation bias: models are fine-tuned on combinations of DFT data (from JARVIS-DFT or OQMD) plus varying percentages (20% or 80%) of OQMD-EXP, then evaluated on held-out experimental formation energy values.

## Uses

- [05_Thermodynamic_Stability_Ensemble](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Open_Quantum_Materials_Database_dataset_use_edcc03281e.md): [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble.md), [task](../tasks/05_Thermodynamic_Stability_Ensemble_task_1.md)
- [10_CrystalFramer](../dataset_uses/10_CrystalFramer_Open_Quantum_Materials_Database_dataset_use_e1f9ed19f6e1.md): [10 CrystalFramer](../papers/10_CrystalFramer.md), [task](../tasks/10_CrystalFramer_task_1.md)
- [16_OOD_Generalization_Materials](../dataset_uses/16_OOD_Generalization_Materials_Open_Quantum_Materials_Database_dataset_use_67179fd578bb.md): [16 OOD Generalization Materials](../papers/16_OOD_Generalization_Materials.md), [task](../tasks/16_OOD_Generalization_Materials_task_1.md)
- [23_CrysDiff](../dataset_uses/23_CrysDiff_Open_Quantum_Materials_Database_dataset_use_eb7b12844189.md): [23 CrysDiff](../papers/23_CrysDiff.md), [task](../tasks/23_CrysDiff_task_1.md)
- [23_CrysDiff](../dataset_uses/23_CrysDiff_Open_Quantum_Materials_Database_dataset_use_12bede9081fa.md): [23 CrysDiff](../papers/23_CrysDiff.md), [task](../tasks/23_CrysDiff_task_1.md)
- [31_Superconductivity_Ordered_Disordered](../dataset_uses/31_Superconductivity_Ordered_Disordered_Open_Quantum_Materials_Database_dataset_use_8a072c.md): [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered.md), [task](../tasks/31_Superconductivity_Ordered_Disordered_task_1.md)
- [34_GNoME](../dataset_uses/34_GNoME_Open_Quantum_Materials_Database_dataset_use_a828569e0e3b.md): [34 GNoME](../papers/34_GNoME.md), [task](../tasks/34_GNoME_task_1.md)
- [37_CrysGNN](../dataset_uses/37_CrysGNN_Open_Quantum_Materials_Database_dataset_use_3cec11bf24e2.md): [37 CrysGNN](../papers/37_CrysGNN.md), [task](../tasks/37_CrysGNN_task_1.md)
- [41_Cross_Property_Transfer_Learning](../dataset_uses/41_Cross_Property_Transfer_Learning_Open_Quantum_Materials_Database_dataset_use_9f2ed8de4e.md): [41 Cross Property Transfer Learning](../papers/41_Cross_Property_Transfer_Learning.md), [task](../tasks/41_Cross_Property_Transfer_Learning_task_1.md)
