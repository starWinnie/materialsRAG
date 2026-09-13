# Dataset: matbench_dielectric

- Dataset ID: `D_matbench_dielectric`
- Dataset type: `public_subset`
- Source dataset: `D_matbench`
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- matbench_dielectric
- dielectric dataset

## Observed material scopes

- inorganic materials
- crystalline solids
- dielectric materials

## Observed research tasks

- Structure-based out-of-distribution (OOD) materials property prediction

## Observed research stages

- data_acquisition
- data_preparation
- candidate_generation
- model_training
- model_evaluation
- computational_validation

## Observed properties

- refractive index

## Observed fields

- crystal structures
- refractive index

## Usage evidence

- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): source in Selecting three benchmark datasets from MatBench — Acquire structure-property dataset suitable for OOD evaluation
- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): pretraining in Preprocessing crystal structures into OFM feature space and applying t-SNE — Convert raw crystal structures into low-dimensional representations for clustering-based OOD test set generation
- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): candidate_pool in Generating five types of OOD test sets via clustering and density estimation — Generate five types of OOD test sets via clustering and density estimation
- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): training in Training eight GNN models on each fold using OOD train/val splits — Train eight GNN models on each fold using OOD train/val splits
- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): test in Evaluating model performance using MAE on OOD test sets — Evaluating model performance using MAE on OOD test sets
- P029 (Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study): benchmark in Comparing OOD MAEs against MatBench i.i.d. baselines and analyzing latent spaces — Comparing OOD MAEs against MatBench i.i.d. baselines and analyzing latent spaces

## Dataset evidence

- P029, PDF page 4, Dataset: "Table 2 | Details of the three benchmark datasets used in this work Dataset Target property Total samples Original source MatBench best algorithm (MAE) Unit matbench_dielectric Refractive index 4764 Materials Project40,70 MODNet71 (0.2711) Unitless"
