# In-house DFT-relaxed novel structures dataset

## Ontology Type
DatasetUse

## Usage Description
A custom dataset of 751 novel crystalline structures generated and DFT-relaxed internally by the authors. It contains ground-truth formation energies and energies above the convex hull computed via first-principles methods. This dataset is used exclusively for out-of-distribution evaluation—testing the model’s generalization capability on materials not present in the Materials Project—by predicting Ef and EHull and reporting parity plots, Pearson correlations (0.894 and 0.931), and MAEs (0.0318 and 0.0294 eV/atom), thereby validating real-world applicability for new material discovery.

## Dataset
- [In-house DFT-relaxed novel structures dataset](../datasets/in_house_dft_relaxed_novel_structures_dataset.md)

## Task
- [13_CrysCo.pdf](../tasks/13_crysco_pdf.md)

## Paper
- [13 CrysCo](../papers/13_crysco.md)

## Provided Representations
- [crystal structure](../representations/crystal_structure.md)
- [crystal graph](../representations/crystal_graph.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Benchmarking / Evaluation](../stages/benchmarking_evaluation.md)

## Evidence
- A custom dataset of 751 novel crystalline structures generated and DFT-relaxed internally by the authors. It contains ground-truth formation energies and energies above the convex hull computed via first-principles methods. This dataset is used exclusively for out-of-distribution evaluation—testing the model’s generalization capability on materials not present in the Materials Project—by predicting Ef and EHull and reporting parity plots, Pearson correlations (0.894 and 0.931), and MAEs (0.0318 and 0.0294 eV/atom), thereby validating real-world applicability for new material discovery.

## Metadata
dataset_use_id: `dataset_use_2a8c8d9c10db`
link: None
