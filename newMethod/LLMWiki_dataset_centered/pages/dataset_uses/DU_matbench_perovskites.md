# Dataset Use: matbench_perovskites

- DatasetUse ID: `DU_matbench_perovskites`
- Dataset: matbench_perovskites (`D_matbench_perovskites`)
- Papers: P029
- Usage records: 6

## Usage roles

- source
- candidate_pool
- training
- test
- benchmark
- computational_validation

## Purposes

- To acquire structure-based materials property regression dataset for benchmarking.
- To generate five OOD test set splits (LOCO, SparseXsingle, SparseYsingle, SparseXcluster, SparseYcluster) by clustering in OFM feature space or property space.
- To train eight GNN models on training/validation splits of each OOD fold.
- To evaluate model performance using mean absolute error (MAE) on OOD test sets.
- To compare OOD MAE results against MatBench i.i.d. baselines.
- To computationally investigate latent physical spaces via t-SNE using perovskites formation energy dataset.

## Used fields

- crystal structure
- formation energy

## Construction methods

- k-means clustering on OFM features or kernel density estimation on t-SNE-reduced OFM features or property values
- For each fold, one cluster is selected as test set, rest as training and validation sets.
- Five OOD test set generation methods applied: LOCO, SparseXsingle, SparseYsingle, SparseXcluster, SparseYcluster.

## Filter conditions

- lowest structure density
- lowest property density
- leave-one-cluster-out

## Sample counts

- 18928

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P029_01_matbench_perovskites

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: selection of three benchmark datasets from MatBench (`data_acquisition`, `S_P029_01`)
- Usage role: source
- Purpose: To acquire structure-based materials property regression dataset for benchmarking.
- Used fields: crystal structure, formation energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 18928
- Confidence: 1.0

Evidence:
- P029, PDF page 2, Results: "We analyze eight GNN models for material property regression tasks using three datasets sourced from MatBench26 and mentioned in Table 1."
- P029, PDF page 4, Dataset: "Table 2 | Details of the three benchmark datasets used in this work Dataset Target property Total samples Original source MatBench best algorithm (MAE) Unit matbench_perovskites Formation energy 18928 Castelli et al.72 coGN36 (0.0269) eV/unit cell"

### UR_P029_02_matbench_perovskites

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: generation of five OOD test set splits per dataset (`data_preparation`, `S_P029_02`)
- Usage role: candidate_pool
- Purpose: To generate five OOD test set splits (LOCO, SparseXsingle, SparseYsingle, SparseXcluster, SparseYcluster) by clustering in OFM feature space or property space.
- Used fields: crystal structure, formation energy
- Filter conditions: lowest structure density, lowest property density, leave-one-cluster-out
- Construction method: k-means clustering on OFM features or kernel density estimation on t-SNE-reduced OFM features or property values
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P029, PDF page 4, OOD test set generation: "Leave-one-cluster-out (LOCO). Meredig et al.45 proposed this approach... Initially, we apply the k-means algorithm61 based on the orbital-field matrix (OFM) features62 to cluster the whole dataset into 50 clusters."
- P029, PDF page 4, OOD test set generation: "Single-point targets with the lowest structure density (SparseXsingle). In this method, we begin by converting material structures into the 1024-dimension OFM feature space. Subsequently, we apply the t-distributed stochastic neighbor embedding (t-SNE)64 for dimension reduction..."

### UR_P029_03_matbench_perovskites

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: training of eight GNN models on each OOD fold (`model_training`, `S_P029_03`)
- Usage role: training
- Purpose: To train eight GNN models on training/validation splits of each OOD fold.
- Used fields: crystal structure, formation energy
- Filter conditions: Not stated
- Construction method: For each fold, one cluster is selected as test set, rest as training and validation sets.
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P029, PDF page 3, OOD test set generation: "For each fold, we selected a cluster as the test set, and the rest as training and validation sets, and averaged the results over 50 folds to get the final result."

### UR_P029_04_matbench_perovskites

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: evaluation of model performance using mean absolute error (MAE) (`model_evaluation`, `S_P029_04`)
- Usage role: test
- Purpose: To evaluate model performance using mean absolute error (MAE) on OOD test sets.
- Used fields: formation energy
- Filter conditions: Not stated
- Construction method: Five OOD test set generation methods applied: LOCO, SparseXsingle, SparseYsingle, SparseXcluster, SparseYcluster.
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P029, PDF page 12, Evaluation criterion: "We use the mean absolute error (MAE) metric, which is a standard evaluation criterion for regression-based materials property prediction problems."
- P029, PDF page 6, MEGNet: "Results on the perovskites dataset are summarized in Table 5."

### UR_P029_05_matbench_perovskites

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: comparison of OOD performance against MatBench i.i.d. baselines (`ablation_study`, `S_P029_05`)
- Usage role: benchmark
- Purpose: To compare OOD MAE results against MatBench i.i.d. baselines.
- Used fields: formation energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P029, PDF page 9, Comparison of OOD performance with baseline i.i.d. performance: "Here we aim to check how the evaluated GNNs’ performances degrade when changing their test sets from i.i.d to OOD. The i.i.d. baseline MAEs for all GNN algorithms can be found on the MatBench leaderboard37, while the OOD test set performances... can be found in Tables 3, 4, and 5, respectively."

### UR_P029_06_matbench_perovskites

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: analysis of latent physical spaces via t-SNE (`computational_validation`, `S_P029_06`)
- Usage role: computational_validation
- Purpose: To computationally investigate latent physical spaces via t-SNE using perovskites formation energy dataset.
- Used fields: crystal structure, formation energy
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P029, PDF page 10, Physical insights: "We utilized t-distributed stochastic neighbor embedding (t-SNE)64... to investigate specific insights into the materials’ physics... Our objective is to visualize the distribution of latent representations learned through the training of different models."
- P029, PDF page 10, Physical insights: "t-SNE diagrams for (a) CGCNN, (b) ALIGNN, (c) DeeperGATGNN, (d) coGN, and (e) coNGN were plotted after training with the perovskites dataset and retrieving latent representation of the first layer after the final graph convolution layer."

## Aggregated evidence

- , PDF page 2, Results: "We analyze eight GNN models for material property regression tasks using three datasets sourced from MatBench26 and mentioned in Table 1."
- , PDF page 4, Dataset: "Table 2 | Details of the three benchmark datasets used in this work Dataset Target property Total samples Original source MatBench best algorithm (MAE) Unit matbench_perovskites Formation energy 18928 Castelli et al.72 coGN36 (0.0269) eV/unit cell"
- , PDF page 4, OOD test set generation: "Leave-one-cluster-out (LOCO). Meredig et al.45 proposed this approach... Initially, we apply the k-means algorithm61 based on the orbital-field matrix (OFM) features62 to cluster the whole dataset into 50 clusters."
- , PDF page 4, OOD test set generation: "Single-point targets with the lowest structure density (SparseXsingle). In this method, we begin by converting material structures into the 1024-dimension OFM feature space. Subsequently, we apply the t-distributed stochastic neighbor embedding (t-SNE)64 for dimension reduction..."
- , PDF page 3, OOD test set generation: "For each fold, we selected a cluster as the test set, and the rest as training and validation sets, and averaged the results over 50 folds to get the final result."
- , PDF page 12, Evaluation criterion: "We use the mean absolute error (MAE) metric, which is a standard evaluation criterion for regression-based materials property prediction problems."
- , PDF page 6, MEGNet: "Results on the perovskites dataset are summarized in Table 5."
- , PDF page 9, Comparison of OOD performance with baseline i.i.d. performance: "Here we aim to check how the evaluated GNNs’ performances degrade when changing their test sets from i.i.d to OOD. The i.i.d. baseline MAEs for all GNN algorithms can be found on the MatBench leaderboard37, while the OOD test set performances... can be found in Tables 3, 4, and 5, respectively."
- , PDF page 10, Physical insights: "We utilized t-distributed stochastic neighbor embedding (t-SNE)64... to investigate specific insights into the materials’ physics... Our objective is to visualize the distribution of latent representations learned through the training of different models."
- , PDF page 10, Physical insights: "t-SNE diagrams for (a) CGCNN, (b) ALIGNN, (c) DeeperGATGNN, (d) coGN, and (e) coNGN were plotted after training with the perovskites dataset and retrieving latent representation of the first layer after the final graph convolution layer."
