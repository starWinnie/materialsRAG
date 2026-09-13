# JARVIS Database

## Metadata

- Dataset ID: `dataset_3d1fc9ebc1ce`
- Aliases: JARVIS, JARVIS (Joint Automated Repository for Various Integrated Simulations), JARVIS Database, JARVIS Dataset, JARVIS dataset, JARVIS-Tools datasets, Joint Automated Repository for Various Integrated Simulations (JARVIS)
- Links: https://jarvis.nist.gov, https://jarvis.nist.gov/, https://pages.nist.gov/jarvis/databases/
- Used by papers: 9
- Dataset usage records: 9

## Description Examples

- A DFT-based materials database offering structural, electronic, and thermodynamic properties for ~100,000+ materials, curated for data-driven design. Used to benchmark ECSG’s classification performance (achieving AUC = 0.988) and as an independent convex hull reference for validating DFT-predicted stability of double perovskite oxides selected by ECSG.
- A curated collection of ~50,000 materials with formation energies and bandgaps, derived from high-throughput DFT calculations; used to evaluate the transferability of ct-UAEs across independent databases. Specifically employed to test ct-UAE-enhanced CGCNN and MEGNET models on formation energy and bandgap prediction, demonstrating consistent accuracy improvements (e.g., 17.5% MAE reduction for Ef), thereby supporting the task of validating cross-database generalizability of universal atomic embeddings.
- The Joint Automated Repository for Various Integrated Simulations (JARVIS) is a DFT-based materials database that includes piezoelectric tensor data derived from high-throughput calculations. The paper explicitly states bulk material data was sourced from both the Materials Project and JARVIS; JARVIS contributes additional piezoelectric tensor entries—particularly from the referenced high-throughput study (Choudhary et al., npj Comput. Mater. 6, 64, 2020)—to expand coverage and improve model generalization for bulk crystal tensor prediction.
- A publicly available benchmark dataset containing 55,722 experimentally and computationally derived crystal structures, each annotated with multiple material properties including formation energy, band gap (OPT and MBJ), total energy, energy above hull (Ehull), bulk modulus, and shear modulus. Used as a primary downstream evaluation benchmark to fine-tune and validate the pre-trained models’ performance on crystal property prediction tasks, with MAE as the evaluation metric.
- A database of ~76k DFT-computed materials properties, including formation energies and crystal structures, curated from multiple sources and standardized for materials informatics. It is used alongside MP and OQMD to ensure robust conclusions across data distributions; specifically, it supports chemistry- and structure-based OOD evaluations (e.g., leave-Mg-out, leave-O-out) and UMAP-based representational domain analysis for formation energy prediction.

## Uses

- [05_Thermodynamic_Stability_Ensemble](../dataset_uses/05_Thermodynamic_Stability_Ensemble_JARVIS_Database_dataset_use_992fc756b44d.md): [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble.md), [task](../tasks/05_Thermodynamic_Stability_Ensemble_task_1.md)
- [06_Transformer_Atomic_Embeddings](../dataset_uses/06_Transformer_Atomic_Embeddings_JARVIS_Database_dataset_use_d9081ae49cf6.md): [06 Transformer Atomic Embeddings](../papers/06_Transformer_Atomic_Embeddings.md), [task](../tasks/06_Transformer_Atomic_Embeddings_task_1.md)
- [07_EATGNN_Piezoelectric_Tensor](../dataset_uses/07_EATGNN_Piezoelectric_Tensor_JARVIS_Database_dataset_use_98325f79e378.md): [07 EATGNN Piezoelectric Tensor](../papers/07_EATGNN_Piezoelectric_Tensor.md), [task](../tasks/07_EATGNN_Piezoelectric_Tensor_task_1.md)
- [11_DPF](../dataset_uses/11_DPF_JARVIS_Database_dataset_use_ffc007efd1c1.md): [11 DPF](../papers/11_DPF.md), [task](../tasks/11_DPF_task_1.md)
- [16_OOD_Generalization_Materials](../dataset_uses/16_OOD_Generalization_Materials_JARVIS_Database_dataset_use_cf5af77f0164.md): [16 OOD Generalization Materials](../papers/16_OOD_Generalization_Materials.md), [task](../tasks/16_OOD_Generalization_Materials_task_1.md)
- [21_ComFormer](../dataset_uses/21_ComFormer_JARVIS_Database_dataset_use_82bf6a79848a.md): [21 ComFormer](../papers/21_ComFormer.md), [task](../tasks/21_ComFormer_task_1.md)
- [28_JARVIS_Leaderboard](../dataset_uses/28_JARVIS_Leaderboard_JARVIS_Database_dataset_use_25fa570bba6f.md): [28 JARVIS Leaderboard](../papers/28_JARVIS_Leaderboard.md), [task](../tasks/28_JARVIS_Leaderboard_task_1.md)
- [38_Matformer](../dataset_uses/38_Matformer_JARVIS_Database_dataset_use_eb07f6f8d169.md): [38 Matformer](../papers/38_Matformer.md), [task](../tasks/38_Matformer_task_1.md)
- [41_Cross_Property_Transfer_Learning](../dataset_uses/41_Cross_Property_Transfer_Learning_JARVIS_Database_dataset_use_4b96eaf50f0b.md): [41 Cross Property Transfer Learning](../papers/41_Cross_Property_Transfer_Learning.md), [task](../tasks/41_Cross_Property_Transfer_Learning_task_1.md)
