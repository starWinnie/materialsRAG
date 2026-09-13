# Materials Project

## Metadata

- Dataset ID: `dataset_d55b16e3041b`
- Aliases: Materials Project
- Links: https://huggingface.co/datasets/caobin/CPPbenchmark, https://materialsproject.org, https://materialsproject.org/, https://next-gen.materialsproject.org
- Used by papers: 7
- Dataset usage records: 7

## Description Examples

- A large-scale DFT-computed database of inorganic crystalline materials containing 122,959 stable structures, each annotated with formation energy, band gap, metal/non-metal classification, and—on a subset of 9,473 entries—mechanical properties including bulk modulus, shear modulus, and Young’s modulus. The dataset is used in this paper to train and evaluate PRDNet for multi-task crystal property prediction, serving as the primary benchmark for regression and classification tasks.
- A large-scale computational database of crystalline materials containing over 150,000 entries with calculated properties including total energy (eV/atom), band gap (eV), bulk modulus (log GPa), and shear modulus (log GPa). Each entry includes atomic numbers, fractional atomic coordinates within the unit cell, 3×3 lattice vectors, and space group identifier (1–230). The dataset is used in this paper to train and evaluate the Crystal Fourier Transformer for material property prediction and zero-shot generalization across space groups.
- A publicly accessible database of computed materials properties, containing DFT-calculated piezoelectric tensors for bulk inorganic crystals. In this paper, it provides bulk piezoelectric tensor data (in Voigt notation) used to train and evaluate the EATGNN model; after outlier removal and symmetry validation, 3444 entries were curated for training/test splits (9:1). The dataset supports the core task of learning symmetry-constrained, frame-independent tensor mappings from crystal structures.
- A publicly available computational materials database providing DFT-calculated structural and energetic properties for over 145,000 inorganic crystalline compounds. The authors collected crystal structures (CIF files), IDs, and six target properties (band gap, formation energy per atom, energy above hull, unit cell volume, energy per atom, and direct/indirect band gap label) from Materials Project via its free API as of November 1, 2022. This raw data served as the source for generating TextEdge and was used to ensure ground-truth labels for all prediction tasks.
- A large-scale computational database containing DFT-calculated structural and property data for over 100,000 inorganic crystalline materials. It includes atomic positions, lattice parameters, space groups, and computed properties such as formation energy, band gap, bulk modulus, and shear modulus. In this paper, it is used to train and evaluate WPDDFormer and UPDDFormer for multi-task crystal property prediction, with reported results on formation energy, band gap, bulk modulus, and shear modulus using log-scaled and linear metrics.

## Uses

- [01_PRDNet](../dataset_uses/01_PRDNet_Materials_Project_dataset_use_eb53342235c5_set_use_eb53342235c5.md): [01 PRDNet](../papers/01_PRDNet_paper_5138be33ab55.md), [task](../tasks/01_PRDNet_task_1_task_b7092f83ac79.md)
- [02_CFT_Space_Group_Invariance](../dataset_uses/02_CFT_Space_Group_Invariance_Materials_Project_dataset_use_2f4d93fd1_set_use_2f4d93fd1a7c.md): [02 CFT Space Group Invariance](../papers/02_CFT_Space_Group_Invariance_paper_de33568ea5f1.md), [task](../tasks/02_CFT_Space_Group_Invariance_task_1_task_c227f1543640.md)
- [07_EATGNN_Piezoelectric_Tensor](../dataset_uses/07_EATGNN_Piezoelectric_Tensor_Materials_Project_dataset_use_899d362d_set_use_899d362dd3c6.md): [07 EATGNN Piezoelectric Tensor](../papers/07_EATGNN_Piezoelectric_Tensor_paper_527363b91d18.md), [task](../tasks/07_EATGNN_Piezoelectric_Tensor_task_1_task_413133a497b4.md)
- [09_LLM_Prop](../dataset_uses/09_LLM_Prop_Materials_Project_dataset_use_48b1eb2b5f32_set_use_48b1eb2b5f32.md): [09 LLM Prop](../papers/09_LLM_Prop_paper_ff6e0dbcf294.md), [task](../tasks/09_LLM_Prop_task_1_task_dbae0fb23b52.md)
- [12_PDDFormer](../dataset_uses/12_PDDFormer_Materials_Project_dataset_use_248531b22245_set_use_248531b22245.md): [12 PDDFormer](../papers/12_PDDFormer_paper_9e212a4383a8.md), [task](../tasks/12_PDDFormer_task_1_task_502a51c697a5.md)
- [28_JARVIS_Leaderboard](../dataset_uses/28_JARVIS_Leaderboard_Materials_Project_dataset_use_2739e157a7e2_set_use_2739e157a7e2.md): [28 JARVIS Leaderboard](../papers/28_JARVIS_Leaderboard_paper_30ac315b16dd.md), [task](../tasks/28_JARVIS_Leaderboard_task_1_task_933637998dc2.md)
- [31_Superconductivity_Ordered_Disordered](../dataset_uses/31_Superconductivity_Ordered_Disordered_Materials_Project_dataset_use_set_use_9c28764cb72e.md): [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered_paper_3d03cb8978f0.md), [task](../tasks/31_Superconductivity_Ordered_Disordered_task_1_task_e583c77ddbb2.md)
