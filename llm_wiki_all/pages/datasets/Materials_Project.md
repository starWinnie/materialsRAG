# Materials Project

## Metadata

- Dataset ID: `dataset_d55b16e3041b`
- Aliases: Materials Project, Materials Project (2021 snapshot), Materials Project (MEGNet), Materials Project (MP), Materials Project (MP) 2018.6.1, Materials Project (MP) database, Materials Project (MP) v.2022.10.28, Materials Project (MP*) database, Materials Project 2021 (MP21), Materials Project Dataset, Materials Project database, The Materials Project
- Links: https://huggingface.co/datasets/caobin/CPPbenchmark, https://materialsproject.org, https://materialsproject.org/, https://next-gen.materialsproject.org, https://next-gen.materialsproject.org/
- Used by papers: 29
- Dataset usage records: 30

## Description Examples

- A large-scale DFT-computed database of inorganic crystalline materials containing 122,959 stable structures, each annotated with formation energy, band gap, metal/non-metal classification, and—on a subset of 9,473 entries—mechanical properties including bulk modulus, shear modulus, and Young’s modulus. The dataset is used in this paper to train and evaluate PRDNet for multi-task crystal property prediction, serving as the primary benchmark for regression and classification tasks.
- A large-scale computational database of crystalline materials containing over 150,000 entries with calculated properties including total energy (eV/atom), band gap (eV), bulk modulus (log GPa), and shear modulus (log GPa). Each entry includes atomic numbers, fractional atomic coordinates within the unit cell, 3×3 lattice vectors, and space group identifier (1–230). The dataset is used in this paper to train and evaluate the Crystal Fourier Transformer for material property prediction and zero-shot generalization across space groups.
- A high-throughput DFT-computed database of ~154,719 inorganic crystals, providing relaxed and initial structures, full relaxation trajectories (energies, forces, stresses, magnetic moments at each ionic step), and formation energies. Used as the training set for all models in Matbench Discovery to learn mappings from atomic structure to energy-related properties, supporting the core task of predicting hull distance for stability classification.
- A large-scale DFT-computed database containing thermodynamic properties (e.g., formation energy, decomposition energy) for 85,014 inorganic crystalline compounds, including experimentally observed and hypothetical materials. Used as the primary training and benchmarking dataset to train and evaluate the ECSG ensemble model for binary classification of compound stability; also used to construct convex hulls for ΔHd labeling and to extract composition-only samples for sample efficiency analysis.
- The 2018.6.1 version contains 69,239 crystalline materials with computed formation energies (Ef) and PBE bandgaps (Eg); used for training and evaluating back-end models (e.g., CGCNN, ALIGNN, MEGNET) and benchmarking ct-UAE performance on formation energy and bandgap prediction. The dataset is split into 60,000 training, 5,000 validation, and 4,239 test samples. It supports the core task by providing ground-truth labels for supervised pretraining of front-end embeddings and downstream property prediction evaluation.

## Uses

- [01_PRDNet](../dataset_uses/01_PRDNet_Materials_Project_dataset_use_eb53342235c5.md): [01 PRDNet](../papers/01_PRDNet.md), [task](../tasks/01_PRDNet_task_1.md)
- [02_CFT_Space_Group_Invariance](../dataset_uses/02_CFT_Space_Group_Invariance_Materials_Project_dataset_use_2f4d93fd1a7c.md): [02 CFT Space Group Invariance](../papers/02_CFT_Space_Group_Invariance.md), [task](../tasks/02_CFT_Space_Group_Invariance_task_1.md)
- [04_Matbench_Discovery](../dataset_uses/04_Matbench_Discovery_Materials_Project_dataset_use_0b201a64b0aa.md): [04 Matbench Discovery](../papers/04_Matbench_Discovery.md), [task](../tasks/04_Matbench_Discovery_task_1.md)
- [05_Thermodynamic_Stability_Ensemble](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Materials_Project_dataset_use_75e15c27a639.md): [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble.md), [task](../tasks/05_Thermodynamic_Stability_Ensemble_task_1.md)
- [06_Transformer_Atomic_Embeddings](../dataset_uses/06_Transformer_Atomic_Embeddings_Materials_Project_dataset_use_b6c12572d788.md): [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings.md), [task](../tasks/06_Transformer_Atomic_Embeddings_task_1.md)
- [06_Transformer_Atomic_Embeddings](../dataset_uses/06_Transformer_Atomic_Embeddings_Materials_Project_dataset_use_5a2f67a5af9b.md): [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings.md), [task](../tasks/06_Transformer_Atomic_Embeddings_task_1.md)
- [07_EATGNN_Piezoelectric_Tensor](../dataset_uses/07_EATGNN_Piezoelectric_Tensor_Materials_Project_dataset_use_899d362dd3c6.md): [07 EATGNN Piezoelectric Tensor](../papers/07_EATGNN_Piezoelectric_Tensor.md), [task](../tasks/07_EATGNN_Piezoelectric_Tensor_task_1.md)
- [08_HiBoFL_Thermal_Conductivity](../dataset_uses/08_HiBoFL_Thermal_Conductivity_Materials_Project_dataset_use_d71c1217c4f4.md): [08 HiBoFL Thermal Conductivity](../papers/08_HiBoFL_Thermal_Conductivity.md), [task](../tasks/08_HiBoFL_Thermal_Conductivity_task_1.md)
- [09_LLM_Prop](../dataset_uses/09_LLM_Prop_Materials_Project_dataset_use_48b1eb2b5f32.md): [09 LLM Prop](../papers/09_LLM_Prop.md), [task](../tasks/09_LLM_Prop_task_1.md)
- [10_CrystalFramer](../dataset_uses/10_CrystalFramer_Materials_Project_dataset_use_8374071ffb4a.md): [10 CrystalFramer](../papers/10_CrystalFramer.md), [task](../tasks/10_CrystalFramer_task_1.md)
- [11_DPF](../dataset_uses/11_DPF_Materials_Project_dataset_use_b203a6387245.md): [11 DPF](../papers/11_DPF.md), [task](../tasks/11_DPF_task_1.md)
- [12_PDDFormer](../dataset_uses/12_PDDFormer_Materials_Project_dataset_use_248531b22245.md): [12 PDDFormer](../papers/12_PDDFormer.md), [task](../tasks/12_PDDFormer_task_1.md)
- [13_CrysCo](../dataset_uses/13_CrysCo_Materials_Project_dataset_use_de1c07d75869.md): [13 CrysCo](../papers/13_CrysCo.md), [task](../tasks/13_CrysCo_task_1.md)
- [16_OOD_Generalization_Materials](../dataset_uses/16_OOD_Generalization_Materials_Materials_Project_dataset_use_0ad533aa0657.md): [16 OOD Generalization Materials](../papers/16_OOD_Generalization_Materials.md), [task](../tasks/16_OOD_Generalization_Materials_task_1.md)
- [17_Known_Unknowns_OOD](../dataset_uses/17_Known_Unknowns_OOD_Materials_Project_dataset_use_f4a7ca4a65b4.md): [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD.md), [task](../tasks/17_Known_Unknowns_OOD_task_1.md)
- [21_ComFormer](../dataset_uses/21_ComFormer_Materials_Project_dataset_use_968aa5ac5584.md): [21 ComFormer](../papers/21_ComFormer.md), [task](../tasks/21_ComFormer_task_1.md)
- [22_Crystalformer](../dataset_uses/22_Crystalformer_Materials_Project_dataset_use_d310d33bda1b.md): [22 Crystalformer](../papers/22_Crystalformer.md), [task](../tasks/22_Crystalformer_task_1.md)
- [23_CrysDiff](../dataset_uses/23_CrysDiff_Materials_Project_dataset_use_d28fd2df6bc1.md): [23 CrysDiff](../papers/23_CrysDiff.md), [task](../tasks/23_CrysDiff_task_1.md)
- [24_Structure_Aware_Transfer_Learning](../dataset_uses/24_Structure_Aware_Transfer_Learning_Materials_Project_dataset_use_adb846e44575.md): [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning.md), [task](../tasks/24_Structure_Aware_Transfer_Learning_task_1.md)
- [26_MD_HIT](../dataset_uses/26_MD_HIT_Materials_Project_dataset_use_12a07aebcb53.md): [26 MD HIT](../papers/26_MD_HIT.md), [task](../tasks/26_MD_HIT_task_1.md)
- [28_JARVIS_Leaderboard](../dataset_uses/28_JARVIS_Leaderboard_Materials_Project_dataset_use_2739e157a7e2.md): [28 JARVIS Leaderboard](../papers/28_JARVIS_Leaderboard.md), [task](../tasks/28_JARVIS_Leaderboard_task_1.md)
- [31_Superconductivity_Ordered_Disordered](../dataset_uses/31_Superconductivity_Ordered_Disordered_Materials_Project_dataset_use_9c28764cb72e.md): [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered.md), [task](../tasks/31_Superconductivity_Ordered_Disordered_task_1.md)
- [32_Perovskite_Bandgap_Database](../dataset_uses/32_Perovskite_Bandgap_Database_Materials_Project_dataset_use_8be26692e10f.md): [32 Perovskite Bandgap Database](../papers/32_Perovskite_Bandgap_Database.md), [task](../tasks/32_Perovskite_Bandgap_Database_task_1.md)
- [33_DenseGNN](../dataset_uses/33_DenseGNN_Materials_Project_dataset_use_c9795fce5b7f.md): [33 DenseGNN](../papers/33_DenseGNN.md), [task](../tasks/33_DenseGNN_task_1.md)
- [34_GNoME](../dataset_uses/34_GNoME_Materials_Project_dataset_use_42c27bb87ebc.md): [34 GNoME](../papers/34_GNoME.md), [task](../tasks/34_GNoME_task_1.md)
- [36_PotNet](../dataset_uses/36_PotNet_Materials_Project_dataset_use_b0e828c3c53b.md): [36 PotNet](../papers/36_PotNet.md), [task](../tasks/36_PotNet_task_1.md)
- [37_CrysGNN](../dataset_uses/37_CrysGNN_Materials_Project_dataset_use_b2263e9f177d.md): [37 CrysGNN](../papers/37_CrysGNN.md), [task](../tasks/37_CrysGNN_task_1.md)
- [38_Matformer](../dataset_uses/38_Matformer_Materials_Project_dataset_use_aa99276321ad.md): [38 Matformer](../papers/38_Matformer.md), [task](../tasks/38_Matformer_task_1.md)
- [40_ALIGNN](../dataset_uses/40_ALIGNN_Materials_Project_dataset_use_f1834d449f10.md): [40 ALIGNN](../papers/40_ALIGNN.md), [task](../tasks/40_ALIGNN_task_1.md)
- [43_Formation_Energy_Stability_Critical](../dataset_uses/43_Formation_Energy_Stability_Critical_Materials_Project_dataset_use_7d07ad670381.md): [43 Formation Energy Stability Critical](../papers/43_Formation_Energy_Stability_Critical.md), [task](../tasks/43_Formation_Energy_Stability_Critical_task_1.md)
