# 33_DenseGNN - Task 1

## Task Description

Predicting material properties—including formation energy, band gap, bulk modulus, phonon frequencies, dielectric constant, and perovskite formation energy—for crystals, molecules, and catalytic materials using graph neural networks, with emphasis on achieving high accuracy on both large-scale computational datasets and small experimental datasets while maintaining scalability and training efficiency.

## Metadata

- Task ID: `task_012e70d922bd`
- Source paper: [33 DenseGNN](../papers/33_DenseGNN.md)
- Tags: property prediction, materials informatics, graph neural network

## Supporting Datasets

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/33_DenseGNN_JARVIS-DFT_dataset_use_e40b11d77764.md)
- Original title in paper: JARVIS-DFT
- Link: https://jarvis.nist.gov/

A dataset of ~67,000 inorganic crystal structures with DFT-calculated properties (e.g., formation energy, band gap, dielectric, piezoelectric, exfoliation energy) computed using OptB88vdW and TBmBJ functionals; used to train and evaluate DenseGNN for crystal property prediction, particularly on formation energy and bandgap tasks, with an 80:10:10 train/validation/test split.

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/33_DenseGNN_Materials_Project_dataset_use_c9795fce5b7f.md)
- Original title in paper: Materials Project
- Link: https://materialsproject.org/

A database of over 132,000 computationally derived inorganic crystal structures and their DFT-predicted properties; specifically used in this paper to extract ~8,970 silicon-containing compounds for structural distinction evaluation via pre-trained embeddings, benchmarking DenseGNN’s ability to discriminate crystal structures against XRD standards.

### [QM9](../datasets/QM9.md)

- Usage page: [usage note](../dataset_uses/33_DenseGNN_QM9_dataset_use_65bbfad150c2.md)
- Original title in paper: QM9
- Link: https://doi.org/10.6084/m9.figshare.978910

A molecular dataset containing 130,829 stable small organic molecules with 19 DFT-computed quantum chemical properties (e.g., HOMO, LUMO, energy gap, dipole moment, zero-point energy); used to evaluate DenseGNN’s performance on molecular property regression tasks, especially for electronic properties sensitive to local geometry.

### [LipopDataset](../datasets/LipopDataset.md)

- Usage page: [usage note](../dataset_uses/33_DenseGNN_LipopDataset_dataset_use_34bccb473a1a.md)
- Original title in paper: LipopDataset
- Link: https://www.ebi.ac.uk/chembl/

A curated experimental dataset of 4,200 compounds with measured octanol/water partition coefficients (logD at pH 7.4), sourced from ChEMBL; used to assess DenseGNN’s ability to predict lipophilicity—a key pharmaceutical property—demonstrating its generalization to small-molecule solubility-related tasks.

### [FreeSolvDataset](../datasets/FreeSolvDataset.md)

- Usage page: [usage note](../dataset_uses/33_DenseGNN_FreeSolvDataset_dataset_use_aa09b82e2582.md)
- Original title in paper: FreeSolvDataset
- Link: https://github.com/deepchem/deepchem/tree/master/deepchem/datasets/freesolv

A dataset of experimental and computed solvation free energies in water for ~600 small molecules, extended here with SMILES strings and experimental values; used to benchmark DenseGNN’s predictive accuracy for aqueous solvation thermodynamics, supporting drug discovery–relevant property screening.

### [ESOLDataset](../datasets/ESOLDataset.md)

- Usage page: [usage note](../dataset_uses/33_DenseGNN_ESOLDataset_dataset_use_87a2ca584b3b.md)
- Original title in paper: ESOLDataset
- Link: https://github.com/deepchem/deepchem/tree/master/deepchem/datasets/esol

The Delaney (ESOL) dataset containing water solubility measurements (log S) for 1,128 compounds, encoded as SMILES strings; used to evaluate DenseGNN’s capacity to directly regress solubility from molecular structure, serving as a standard test for generalizability on sparse, experimentally derived small-molecule property data.

### [OC22](../datasets/OC22.md)

- Usage page: [usage note](../dataset_uses/33_DenseGNN_OC22_dataset_use_8a74c72752cc.md)
- Original title in paper: OC22
- Link: https://opencatalystproject.org/

The Open Catalyst 2022 dataset comprising ~1.2 million DFT total energy calculations for oxide electrocatalyst surfaces and adsorbates; used to validate DenseGNN on catalysis-relevant property prediction (e.g., S2EF-Total, IS2RE-Total), demonstrating its applicability to heterogeneous catalysis and surface chemistry beyond bulk materials.

### [Matbench](../datasets/Matbench.md)

- Usage page: [usage note](../dataset_uses/33_DenseGNN_Matbench_dataset_use_40ccd45b11bf.md)
- Original title in paper: Matbench
- Link: https://matbench.materialsproject.org/

An automated benchmark platform with 13 rigorously curated, domain-diverse solid-state materials property prediction tasks (e.g., phonons, dielectric, perovskites, jdft2d), covering sample sizes from 312 to 132,000 and spanning DFT and experimental sources; used as the primary benchmark to evaluate DenseGNN’s universality, scalability, and performance across materials science domains, including ablation and cross-model fusion studies.

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Model Training
- Screening / Prediction
- Validation
<!-- RD_STAGES_END -->
