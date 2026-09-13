# 37_CrysGNN - Task 1

## Task Description

Predicting multiple physical and electronic properties of crystalline materials—including formation energy, bandgap, total energy, bulk modulus, shear modulus, Ehull, spillage, SLME, and dielectric-related properties—using graph neural network models enhanced by distilled knowledge from a pre-trained GNN on unlabeled crystal structures.

## Metadata

- Task ID: `task_c0c958c88b9f`
- Source paper: [37 CrysGNN](../papers/37_CrysGNN.md)
- Tags: property prediction, crystal structure modeling, knowledge distillation

## Supporting Datasets

### [Materials Project](../datasets/Materials_Project.md)

- Usage page: [usage note](../dataset_uses/37_CrysGNN_Materials_Project_dataset_use_b2263e9f177d.md)
- Original title in paper: Materials Project (MP) 2018.6.1
- Link: https://materialsproject.org/

A DFT-calculated dataset containing 69,239 crystalline materials with two key properties: formation energy and optical bandgap. It is used as a property-tagged downstream dataset for training and evaluating distilled SOTA property predictors (e.g., CGCNN, ALIGNN). The paper explicitly states this version is a subset of the pre-training data and serves as a benchmark for measuring MAE improvements from knowledge distillation.

### [JARVIS-DFT](../datasets/JARVIS-DFT.md)

- Usage page: [usage note](../dataset_uses/37_CrysGNN_JARVIS-DFT_dataset_use_ba0c2a957168.md)
- Original title in paper: JARVIS-DFT (2021.8.18)
- Link: https://jarvis.nist.gov/

A DFT-based materials database comprising 55,722 crystalline materials with 19 computed properties—including formation energy, bandgap (MBJ and OPT), total energy, bulk modulus, shear modulus, Ehull, spillage, SLME, and electronic properties like epsilon_x/y/z and n-Seebeck. Used as an independent downstream evaluation dataset (not seen during pre-training) to assess generalization of distilled models across diverse structural and electronic properties.

### [Open Quantum Materials Database](../datasets/Open_Quantum_Materials_Database.md)

- Usage page: [usage note](../dataset_uses/37_CrysGNN_Open_Quantum_Materials_Database_dataset_use_3cec11bf24e2.md)
- Original title in paper: OQMD-EXP
- Link: https://oqmd.org/

A small experimental dataset of 1,500 materials with measured formation energy values, derived from the Open Quantum Materials Database. It is used specifically to evaluate how distilled knowledge from CrysGNN helps mitigate DFT-induced bias—by training models on mixed DFT + experimental data and testing on held-out experimental data—to quantify reduction in MAE against ground-truth experimental measurements.

### [CrysGNN Curated Dataset (800K crystal graphs)](../datasets/CrysGNN_Curated_Dataset_800K_crystal_graphs.md)

- Usage page: [usage note](../dataset_uses/37_CrysGNN_CrysGNN_Curated_Dataset_800K_crystal_graphs_dataset_use_edfdc1bcda1b.md)
- Original title in paper: CrysGNN Curated Dataset (800K crystal graphs)
- Link: https://github.com/kdmsit/crysgnn

An author-curated, unlabeled dataset of 800,000 crystal graphs assembled from OQMD (661K) and Materials Project (139K), represented as multi-graphs with node features (electronegativity, valence electrons, covalent radius), edge features (bond lengths), space group numbers, and crystal system labels. Used exclusively for self-supervised pre-training of CrysGNN via node-level reconstruction (features & connectivity) and graph-level objectives (space group classification and contrastive learning over crystal systems).

<!-- RD_STAGES_START -->
## R&D Stages

This task is mapped to the following R&D stages:

- Problem Definition
- Dataset Selection
- Model Training
- Screening / Prediction
<!-- RD_STAGES_END -->
