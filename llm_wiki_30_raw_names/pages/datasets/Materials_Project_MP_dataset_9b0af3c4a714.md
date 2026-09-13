# Materials Project (MP)

## Metadata

- Dataset ID: `dataset_9b0af3c4a714`
- Aliases: Materials Project (MP)
- Links: https://materialsproject.org, https://materialsproject.org/
- Used by papers: 7
- Dataset usage records: 7

## Description Examples

- A large-scale DFT-computed database containing thermodynamic properties (e.g., formation energy, decomposition energy) for 85,014 inorganic crystalline compounds, including experimentally observed and hypothetical materials. Used as the primary training and benchmarking dataset to train and evaluate the ECSG ensemble model for binary classification of compound stability; also used to construct convex hulls for ΔHd labeling and to extract composition-only samples for sample efficiency analysis.
- A large-scale database of ~69,239 synthetically feasible crystalline materials, providing DFT-calculated properties including formation energy, PBE bandgap, bulk modulus, and shear modulus. In this paper, it is used for crystal property prediction across four regression tasks using standardized data splits (60,000 / 5,000 / 4,239 for formation energy and bandgap; ~4,664 / ~393 / ~393 for moduli), enabling comparison against state-of-the-art models and validation of generalization beyond JARVIS.
- A database of ~146k ab initio–computed inorganic crystalline materials, containing formation energies, band gaps, bulk moduli, crystal structures (space groups, point groups, crystal systems), and chemical compositions. In this paper, it is used to construct over 700 OOD tasks—including leave-one-element-out, leave-one-period-out, leave-one-group-out, leave-one-space-group-out, and leave-one-crystal-system-out splits—to evaluate ML model generalization on formation energy prediction and assess representational domain coverage via UMAP embedding analysis.
- The Materials Project is a high-throughput computational database providing thermodynamic and mechanical properties for over 100,000 inorganic compounds, derived from DFT calculations. The paper uses a subset of 6,184–6,331 entries focused on bulk modulus, shear modulus, and elastic anisotropy — retaining the lowest-formation-enthalpy entry for duplicate compositions. This dataset supports the OOD property prediction task by enabling evaluation on large-scale, composition-driven mechanical property extrapolation under realistic database screening conditions.
- A large-scale computational materials database containing over 100,000+ DFT-optimized crystal structures, each annotated with structural metadata (space group, lattice parameters, atomic positions) and computed properties. In this paper, MP contributes ~800K untagged crystal graph data (i.e., structures without property labels) used solely for self-supervised pre-training of CrysDiff via crystal structure reconstruction — enabling learning of latent marginal distributions p(F, L | A) without supervision.

## Uses

- [05_Thermodynamic_Stability_Ensemble](../dataset_uses/05_Thermodynamic_Stability_Ensemble_Materials_Project_MP_dataset_use_set_use_8d0cb093180d.md): [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble_paper_dfa00819e2d0.md), [task](../tasks/05_Thermodynamic_Stability_Ensemble_task_1_task_134b6e57d77b.md)
- [10_CrystalFramer](../dataset_uses/10_CrystalFramer_Materials_Project_MP_dataset_use_f5d1c7f17083_set_use_f5d1c7f17083.md): [10 CrystalFramer](../papers/10_CrystalFramer_paper_376c54bdb055.md), [task](../tasks/10_CrystalFramer_task_1_task_f4a8c4f8f856.md)
- [16_OOD_Generalization_Materials](../dataset_uses/16_OOD_Generalization_Materials_Materials_Project_MP_dataset_use_678f_set_use_678f2345f1c3.md): [16 OOD Generalization Materials](../papers/16_OOD_Generalization_Materials_paper_cd925085a1df.md), [task](../tasks/16_OOD_Generalization_Materials_task_1_task_49a79df78a99.md)
- [17_Known_Unknowns_OOD](../dataset_uses/17_Known_Unknowns_OOD_Materials_Project_MP_dataset_use_c7404036124f_set_use_c7404036124f.md): [17 Known Unknowns OOD](../papers/17_Known_Unknowns_OOD_paper_0accd46e95fd.md), [task](../tasks/17_Known_Unknowns_OOD_task_1_task_e097cf9a59e5.md)
- [23_CrysDiff](../dataset_uses/23_CrysDiff_Materials_Project_MP_dataset_use_fc830baee0aa_set_use_fc830baee0aa.md): [23 CrysDiff](../papers/23_CrysDiff_paper_0010b7688bb5.md), [task](../tasks/23_CrysDiff_task_1_task_1f1a85917ec8.md)
- [24_Structure_Aware_Transfer_Learning](../dataset_uses/24_Structure_Aware_Transfer_Learning_Materials_Project_MP_dataset_use_set_use_d0e53778f61f.md): [24 Structure Aware Transfer Learning](../papers/24_Structure_Aware_Transfer_Learning_paper_a9ca0fbfd8f7.md), [task](../tasks/24_Structure_Aware_Transfer_Learning_task_1_task_25b6baf65d50.md)
- [26_MD_HIT](../dataset_uses/26_MD_HIT_Materials_Project_MP_dataset_use_822072fb5acc_set_use_822072fb5acc.md): [26 MD HIT](../papers/26_MD_HIT_paper_364d763e5978.md), [task](../tasks/26_MD_HIT_task_1_task_e55c8a4f2b28.md)
