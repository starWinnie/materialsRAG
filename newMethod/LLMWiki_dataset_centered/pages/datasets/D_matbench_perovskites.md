# Dataset: matbench_perovskites

- Dataset ID: `D_matbench_perovskites`
- Dataset type: `public_subset`
- Source dataset: `D_matbench`
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- matbench_perovskites
- perovskites dataset

## Observed material scopes

- inorganic crystalline materials

## Observed research tasks

- structure-based out-of-distribution (OOD) materials property prediction

## Observed research stages

- data_acquisition
- data_preparation
- model_training
- model_evaluation
- ablation_study
- computational_validation

## Observed properties

- formation energy

## Observed fields

- crystal structure
- formation energy

## Usage evidence

- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): source in selection of three benchmark datasets from MatBench — To acquire structure-based materials property regression dataset for benchmarking.
- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): candidate_pool in generation of five OOD test set splits per dataset — To generate five OOD test set splits (LOCO, SparseXsingle, SparseYsingle, SparseXcluster, SparseYcluster) by clustering in OFM feature space or property space.
- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): training in training of eight GNN models on each OOD fold — To train eight GNN models on training/validation splits of each OOD fold.
- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): test in evaluation of model performance using mean absolute error (MAE) — To evaluate model performance using mean absolute error (MAE) on OOD test sets.
- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): benchmark in comparison of OOD performance against MatBench i.i.d. baselines — To compare OOD MAE results against MatBench i.i.d. baselines.
- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): computational_validation in analysis of latent physical spaces via t-SNE — To computationally investigate latent physical spaces via t-SNE using perovskites formation energy dataset.

## Dataset evidence

- P029, PDF page 2, Results: "We analyze eight GNN models for material property regression tasks using three datasets sourced from MatBench26 and mentioned in Table 1."
- P029, PDF page 4, Dataset: "Table 2 | Details of the three benchmark datasets used in this work Dataset Target property Total samples Original source MatBench best algorithm (MAE) Unit matbench_perovskites Formation energy 18928 Castelli et al.72 coGN36 (0.0269) eV/unit cell"
