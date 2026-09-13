# Inorganic Crystal Structure Database

## Metadata

- Dataset ID: `dataset_0d530002ad88`
- Aliases: ICSD (Inorganic Crystal Structure Database), Inorganic Crystal Structure Database (ICSD)
- Links: https://icsd.fiz-karlsruhe.de, https://icsd.products.fiz-karlsruhe.de/
- Used by papers: 4
- Dataset usage records: 4

## Description Examples

- The ICSD contains over 200,000 experimentally determined ordered and disordered inorganic crystal structures. In this paper, it serves two roles: (1) as the source of structural data used to construct SuperCon3D via matching with SuperCon entries; and (2) as the external candidate pool for high-Tc screening — SODNet is applied to predict Tc for ~200k ICSD entries (including disordered ones), yielding 27 prioritized candidates (e.g., Ba1.1432Co0.1429O3.0009Rh0.8574, ErH3) for experimental follow-up. Thus, ICSD supports both dataset construction and real-world superconductor screening.
- A curated collection of experimentally determined inorganic crystal structures, containing over 200,000 entries with detailed structural information (atomic positions, lattice parameters, space groups) and chemical formulae. In this paper, it is used to (1) define uniqueness by filtering out generated formulae already present in ICSD, (2) support the high-level heuristic Rhi via a uniqueness checker against known structures, and (3) form part of the reference set for match rate evaluation alongside Materials Project.
- An experimental database of ~300,000 manually curated, peer-reviewed crystal structures determined by X-ray and neutron diffraction. Used to train the data-mined substitution prediction (DMSP) algorithm that guides ion exchange substitutions via conditional probabilities (pDMSP) based on observed ionic substitution patterns in real synthesized materials; also used as an external benchmark for novelty assessment (alongside MP and Alexandria).
- A repository of experimentally determined crystal structures. In this paper, ICSD is cited as the source of experimentally validated lattice parameters (e.g., for TiNi, CuZr, RuNb in Fig. 5C) used to benchmark the accuracy of SSPM’s predicted lattice parameters p(X|A,B,Y) for B2, D03, and L12 structures. It supports validation of structural predictions but is not used for model training.

## Uses

- [31_Superconductivity_Ordered_Disordered](../dataset_uses/31_Superconductivity_Ordered_Disordered_Inorganic_Crystal_Structure_Database_dataset_use_e.md): [31 Superconductivity Ordered Disordered](../papers/31_Superconductivity_Ordered_Disordered.md), [task](../tasks/31_Superconductivity_Ordered_Disordered_task_1.md)
- [67_Generative Hierarchical Materials Search](../dataset_uses/67_Generative_Hierarchical_Materials_Search_Inorganic_Crystal_Structure_Database_dataset_u.md): [67 Generative Hierarchical Materials Search](../papers/67_Generative_Hierarchical_Materials_Search.md), [task](../tasks/67_Generative_Hierarchical_Materials_Search_task_1.md)
- [72_Establishing baselines for generative discovery of inorganic crystals](../dataset_uses/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals_Inorganic_Crystal.md): [72 Establishing baselines for generative discovery of inorganic crystals](../papers/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals.md), [task](../tasks/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals_task_1.md)
- [98_Self-supervised probabilistic models for exploring shape memory alloys](../dataset_uses/98_Self-supervised_probabilistic_models_for_exploring_shape_memory_alloys_Inorganic_Crysta.md): [98 Self-supervised probabilistic models for exploring shape memory alloys](../papers/98_Self-supervised_probabilistic_models_for_exploring_shape_memory_alloys.md), [task](../tasks/98_Self-supervised_probabilistic_models_for_exploring_shape_memory_alloys_task_1.md)
