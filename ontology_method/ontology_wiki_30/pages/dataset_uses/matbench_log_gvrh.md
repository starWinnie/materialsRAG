# matbench_log_gvrh

## Ontology Type
DatasetUse

## Usage Description
A dataset of 10,987 inorganic crystals from the Materials Project, with log10-transformed shear modulus (log10(GPa)) as the target property. In this paper, it is split into five OOD test configurations using OFM-based t-SNE density estimation and k-means clustering to isolate samples with lowest structural or property density; these splits enable benchmarking of GNNs’ extrapolative capability for elastic property prediction on materials dissimilar to the training set.

## Dataset
- [matbench_log_gvrh](../datasets/matbench_log_gvrh.md)

## Task
- [29_Structure_OOD_Benchmark.pdf](../tasks/29_structure_ood_benchmark_pdf.md)

## Paper
- [29 Structure OOD Benchmark](../papers/29_structure_ood_benchmark.md)

## Provided Representations
- [crystal structure](../representations/crystal_structure.md)
- [crystal graph](../representations/crystal_graph.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Benchmarking / Evaluation](../stages/benchmarking_evaluation.md)

## Evidence
- A dataset of 10,987 inorganic crystals from the Materials Project, with log10-transformed shear modulus (log10(GPa)) as the target property. In this paper, it is split into five OOD test configurations using OFM-based t-SNE density estimation and k-means clustering to isolate samples with lowest structural or property density; these splits enable benchmarking of GNNs’ extrapolative capability for elastic property prediction on materials dissimilar to the training set.

## Metadata
dataset_use_id: `dataset_use_e3365bf03dac`
link: https://matbench.materialsproject.org/
