# matbench_dielectric

## Ontology Type
DatasetUse

## Usage Description
A benchmark subset of Materials Project structures curated for dielectric property prediction, where the target property is the refractive index η (related to the electronic dielectric constant via η = √ε∞). The dataset includes ~1,000–2,000 structures (exact size not specified but drawn from MP) and is used exclusively for out-of-distribution benchmarking—evaluating DTNet’s generalization by predicting ε∞ and computing η from predicted tensors. It supports model validation and leaderboard comparison against state-of-the-art methods like MODNet.

## Dataset
- [matbench_dielectric](../datasets/matbench_dielectric.md)

## Task
- [19_DTNet_Dielectric_Tensor.pdf](../tasks/19_dtnet_dielectric_tensor_pdf.md)

## Paper
- [19 DTNet Dielectric Tensor](../papers/19_dtnet_dielectric_tensor.md)

## Provided Representations
- [crystal structure](../representations/crystal_structure.md)
- [spectrum or tensor](../representations/spectrum_or_tensor.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Validation](../stages/validation.md)
- [Benchmarking / Evaluation](../stages/benchmarking_evaluation.md)

## Evidence
- A benchmark subset of Materials Project structures curated for dielectric property prediction, where the target property is the refractive index η (related to the electronic dielectric constant via η = √ε∞). The dataset includes ~1,000–2,000 structures (exact size not specified but drawn from MP) and is used exclusively for out-of-distribution benchmarking—evaluating DTNet’s generalization by predicting ε∞ and computing η from predicted tensors. It supports model validation and leaderboard comparison against state-of-the-art methods like MODNet.

## Metadata
dataset_use_id: `dataset_use_a9c60cb9113f`
link: https://matbench.materialsvirtuallab.org/
