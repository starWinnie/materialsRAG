# OQMD (Open Quantum Materials Database)

## Metadata

- Dataset ID: `dataset_9dcd35cc7ac5`
- Aliases: OQMD (Open Quantum Materials Database)
- Links: https://oqmd.org, https://oqmd.org/, https://www.oqmd.org
- Used by papers: 3
- Dataset usage records: 3

## Description Examples

- A large-scale ab initio database of ~1M predicted stable and metastable inorganic compounds, with formation energies, crystal structures, and elemental compositions. Its scale (~10× larger than MP) enables rigorous scaling analysis: the paper uses it to validate learning curves (training set size and time effects) on representationally OOD tasks (e.g., leave-H-out), confirm domain misidentification biases, and demonstrate adverse scaling behavior where increased data degrades OOD performance.
- A high-throughput DFT database containing ~400,000+ predicted crystal structures and their computed thermodynamic properties (e.g., formation energy). Like MP, it provides full 3D structural representations (A, F, L) but no experimental property labels. In this paper, OQMD contributes the remaining portion (~800K total) of unlabelled crystal structures used for pre-training CrysDiff, alongside MP. It serves the same role as MP: enabling unsupervised learning of crystal geometry distributions via diffusion-based reconstruction.
- A database of computationally predicted stable and metastable inorganic crystal structures (~300k+ entries at time of publication), used jointly with Materials Project, Matgen, and ICSD to assemble the ~1.14 million-structure pre-training corpus for DiffCSP-SC. Its inclusion ensures broad coverage of elemental combinations and structural motifs beyond experimentally synthesized superconductors, thereby improving the generative model’s capacity to sample chemically plausible and structurally valid crystals during high-Tc-targeted inverse design.

## Uses

- [16_OOD_Generalization_Materials](../dataset_uses/16_OOD_Generalization_Materials_OQMD_Open_Quantum_Materials_Database_set_use_2d998e4fb5bd.md): [16 OOD Generalization Materials](../papers/16_OOD_Generalization_Materials_paper_cd925085a1df.md), [task](../tasks/16_OOD_Generalization_Materials_task_1_task_49a79df78a99.md)
- [23_CrysDiff](../dataset_uses/23_CrysDiff_OQMD_Open_Quantum_Materials_Database_dataset_use_b4ed6b4f_set_use_b4ed6b4facca.md): [23 CrysDiff](../papers/23_CrysDiff_paper_0010b7688bb5.md), [task](../tasks/23_CrysDiff_task_1_task_1f1a85917ec8.md)
- [31_Superconductivity_Ordered_Disordered](../dataset_uses/31_Superconductivity_Ordered_Disordered_OQMD_Open_Quantum_Materials_D_set_use_bf4439f0a864.md): [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered_paper_3d03cb8978f0.md), [task](../tasks/31_Superconductivity_Ordered_Disordered_task_1_task_e583c77ddbb2.md)
