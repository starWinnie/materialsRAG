# Dataset Use: matbench_dielectric

- DatasetUse ID: `DU_matbench_dielectric`
- Dataset: matbench_dielectric (`D_matbench_dielectric`)
- Papers: P029
- Usage records: 5

## Usage roles

- source
- candidate_pool
- training
- test
- benchmark

## Purposes

- To acquire structure-based materials property regression dataset for benchmarking.
- To generate five OOD test set splits (LOCO, SparseXsingle, SparseYsingle, SparseXcluster, SparseYcluster) by clustering in OFM feature space or property space.
- To train eight GNN models on training/validation splits of each OOD fold.
- To evaluate model performance using mean absolute error (MAE) on OOD test sets.
- To compare OOD MAE results against MatBench i.i.d. baselines.

## Used fields

- crystal structure
- refractive index

## Construction methods

- k-means clustering on OFM features or kernel density estimation on t-SNE-reduced OFM features or property values
- For each fold, one cluster is selected as test set, rest as training and validation sets.
- Five OOD test set generation methods applied: LOCO, SparseXsingle, SparseYsingle, SparseXcluster, SparseYcluster.

## Filter conditions

- lowest structure density
- lowest property density
- leave-one-cluster-out

## Sample counts

- 4764

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P029_01_matbench_dielectric

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: selection of three benchmark datasets from MatBench (`data_acquisition`, `S_P029_01`)
- Usage role: source
- Purpose: To acquire structure-based materials property regression dataset for benchmarking.
- Used fields: crystal structure, refractive index
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 4764
- Confidence: 1.0

Evidence:
- P029, PDF page 2, Results: "We analyze eight GNN models for material property regression tasks using three datasets sourced from MatBench26 and mentioned in Table 1."
- P029, PDF page 4, Dataset: "Table 2 | Details of the three benchmark datasets used in this work Dataset Target property Total samples Original source MatBench best algorithm (MAE) Unit matbench_dielectric Refractive index 4764 Materials Project40,70 MODNet71 (0.2711) Unitless"

### UR_P029_02_matbench_dielectric

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: generation of five OOD test set splits per dataset (`data_preparation`, `S_P029_02`)
- Usage role: candidate_pool
- Purpose: To generate five OOD test set splits (LOCO, SparseXsingle, SparseYsingle, SparseXcluster, SparseYcluster) by clustering in OFM feature space or property space.
- Used fields: crystal structure, refractive index
- Filter conditions: lowest structure density, lowest property density, leave-one-cluster-out
- Construction method: k-means clustering on OFM features or kernel density estimation on t-SNE-reduced OFM features or property values
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P029, PDF page 4, OOD test set generation: "Leave-one-cluster-out (LOCO). Meredig et al.45 proposed this approach... Initially, we apply the k-means algorithm61 based on the orbital-field matrix (OFM) features62 to cluster the whole dataset into 50 clusters."
- P029, PDF page 4, OOD test set generation: "Single-point targets with the lowest structure density (SparseXsingle). In this method, we begin by converting material structures into the 1024-dimension OFM feature space. Subsequently, we apply the t-distributed stochastic neighbor embedding (t-SNE)64 for dimension reduction..."

### UR_P029_03_matbench_dielectric

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: training of eight GNN models on each OOD fold (`model_training`, `S_P029_03`)
- Usage role: training
- Purpose: To train eight GNN models on training/validation splits of each OOD fold.
- Used fields: crystal structure, refractive index
- Filter conditions: Not stated
- Construction method: For each fold, one cluster is selected as test set, rest as training and validation sets.
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P029, PDF page 3, OOD test set generation: "For each fold, we selected a cluster as the test set, and the rest as training and validation sets, and averaged the results over 50 folds to get the final result."

### UR_P029_04_matbench_dielectric

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: evaluation of model performance using mean absolute error (MAE) (`model_evaluation`, `S_P029_04`)
- Usage role: test
- Purpose: To evaluate model performance using mean absolute error (MAE) on OOD test sets.
- Used fields: refractive index
- Filter conditions: Not stated
- Construction method: Five OOD test set generation methods applied: LOCO, SparseXsingle, SparseYsingle, SparseXcluster, SparseYcluster.
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P029, PDF page 12, Evaluation criterion: "We use the mean absolute error (MAE) metric, which is a standard evaluation criterion for regression-based materials property prediction problems."
- P029, PDF page 4, Performance comparison on OOD test sets: "The results of the dielectric dataset for five different OOD target generation methods are summarized in Table 3."

### UR_P029_05_matbench_dielectric

- Paper: `P029` — Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study
- Task: structure-based out-of-distribution (OOD) materials property prediction (`T_P029_01`)
- Stage: comparison of OOD performance against MatBench i.i.d. baselines (`ablation_study`, `S_P029_05`)
- Usage role: benchmark
- Purpose: To compare OOD MAE results against MatBench i.i.d. baselines.
- Used fields: refractive index
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P029, PDF page 9, Comparison of OOD performance with baseline i.i.d. performance: "Here we aim to check how the evaluated GNNs’ performances degrade when changing their test sets from i.i.d to OOD. The i.i.d. baseline MAEs for all GNN algorithms can be found on the MatBench leaderboard37, while the OOD test set performances... can be found in Tables 3, 4, and 5, respectively."

## Aggregated evidence

- , PDF page 2, Results: "We analyze eight GNN models for material property regression tasks using three datasets sourced from MatBench26 and mentioned in Table 1."
- , PDF page 4, Dataset: "Table 2 | Details of the three benchmark datasets used in this work Dataset Target property Total samples Original source MatBench best algorithm (MAE) Unit matbench_dielectric Refractive index 4764 Materials Project40,70 MODNet71 (0.2711) Unitless"
- , PDF page 4, OOD test set generation: "Leave-one-cluster-out (LOCO). Meredig et al.45 proposed this approach... Initially, we apply the k-means algorithm61 based on the orbital-field matrix (OFM) features62 to cluster the whole dataset into 50 clusters."
- , PDF page 4, OOD test set generation: "Single-point targets with the lowest structure density (SparseXsingle). In this method, we begin by converting material structures into the 1024-dimension OFM feature space. Subsequently, we apply the t-distributed stochastic neighbor embedding (t-SNE)64 for dimension reduction..."
- , PDF page 3, OOD test set generation: "For each fold, we selected a cluster as the test set, and the rest as training and validation sets, and averaged the results over 50 folds to get the final result."
- , PDF page 12, Evaluation criterion: "We use the mean absolute error (MAE) metric, which is a standard evaluation criterion for regression-based materials property prediction problems."
- , PDF page 4, Performance comparison on OOD test sets: "The results of the dielectric dataset for five different OOD target generation methods are summarized in Table 3."
- , PDF page 9, Comparison of OOD performance with baseline i.i.d. performance: "Here we aim to check how the evaluated GNNs’ performances degrade when changing their test sets from i.i.d to OOD. The i.i.d. baseline MAEs for all GNN algorithms can be found on the MatBench leaderboard37, while the OOD test set performances... can be found in Tables 3, 4, and 5, respectively."
