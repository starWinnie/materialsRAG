# 72_Establishing baselines for generative discovery of inorganic crystals - Task 1

## Task Description

Predicting and generating novel, thermodynamically stable inorganic crystal structures with targeted properties (e.g., electronic band gap near 3 eV or high bulk modulus), while balancing structural novelty, compositional diversity, and synthetic feasibility — using generative AI models and baseline methods grounded in charge balance and ion substitution heuristics.

## Metadata

- Task ID: `task_5cdb3d3479b6`
- Source paper: [72 Establishing baselines for generative discovery of inorganic crystals](../papers/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals.md)
- Tags: crystal structure generation, thermodynamic stability prediction, property-targeted materials discovery

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals_Materials_Project.md)
- Original title in paper: Materials Project (MP)
- Link: https://materialsproject.org

A database of ~200,000 DFT-calculated inorganic compounds containing formation energies, band gaps, bulk moduli, crystal structures (CIFs), and decomposition energies relative to the convex hull. In this paper, it serves as the primary source for stable parent structures for ion exchange, training data for generative models (MP-20 subset), ground-truth stability labels (DEd ≤ 0), novelty assessment (exclusion criterion), and phase diagram construction for stability evaluation.

### [AFLOW Crystallographic Prototypes Library](../datasets/AFLOW_Crystallographic_Prototypes_Library.md)

- Usage page: [usage note](../dataset_uses/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals_AFLOW_Crystallogr.md)
- Original title in paper: AFLOW Crystallographic Prototypes Library
- Link: https://aflowlib.org/crystallographic_prototypes

A curated collection of 1,783 experimentally derived and theoretically validated crystal structure prototypes (e.g., spinel, perovskite), each with space group, Wyckoff positions, and site symmetry. Used in the random enumeration baseline to assign elements to prototype sites and generate candidate structures; also serves as the reference database for assessing 'prototype novelty' (i.e., whether a generated structure can be indexed to any known AFLOW prototype).

### [Inorganic Crystal Structure Database](../datasets/Inorganic_Crystal_Structure_Database.md)

- Usage page: [usage note](../dataset_uses/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals_Inorganic_Crystal.md)
- Original title in paper: Inorganic Crystal Structure Database (ICSD)
- Link: https://icsd.fiz-karlsruhe.de

An experimental database of ~300,000 manually curated, peer-reviewed crystal structures determined by X-ray and neutron diffraction. Used to train the data-mined substitution prediction (DMSP) algorithm that guides ion exchange substitutions via conditional probabilities (pDMSP) based on observed ionic substitution patterns in real synthesized materials; also used as an external benchmark for novelty assessment (alongside MP and Alexandria).

### [Alexandria Database](../datasets/Alexandria_Database.md)

- Usage page: [usage note](../dataset_uses/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals_Alexandria_Databa.md)
- Original title in paper: Alexandria Database
- Link: https://alexandria.chem.umn.edu

A large-scale computational database containing over 4.5 million DFT-relaxed inorganic crystal structures, including many not present in the Materials Project. Used in this work to extend training sets for generative models (e.g., MatterGen and CrystaLLM) to improve stability rates, and as an additional external source for novelty evaluation (i.e., checking whether generated materials appear in Alexandria beyond MP).

### [MP-20 dataset](../datasets/MP-20_dataset.md)

- Usage page: [usage note](../dataset_uses/72_Establishing_baselines_for_generative_discovery_of_inorganic_crystals_MP-20_Dataset_dat.md)
- Original title in paper: MP-20 Dataset
- Link: https://doi.org/10.1039/d5mh00010f

A curated subset of the Materials Project containing 45,231 stable (convex hull–stable) inorganic crystal structures, used as the standard training dataset for all four evaluated generative models (CrystaLLM, FTCP, CDVAE, MatterGen) to ensure consistent benchmarking; also used to train the CGCNN band gap and bulk modulus predictors and the CHGNet interatomic potential.
