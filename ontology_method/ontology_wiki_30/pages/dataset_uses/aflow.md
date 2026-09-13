# AFLOW

## Ontology Type
DatasetUse

## Usage Description
AFLOW is a high-throughput computational database containing ~14,000 solid materials with stoichiometric compositions and associated property values derived from density functional theory calculations. It includes six curated properties: band gap, bulk modulus, Debye temperature, shear modulus, thermal conductivity, and thermal expansion (the latter four log-scaled). In this paper, AFLOW is used to train and evaluate OOD property predictors on composition-based regression tasks, specifically to assess zero-shot extrapolation performance beyond the upper range of training property values during virtual screening of high-performing solids.

## Dataset
- [AFLOW](../datasets/aflow.md)

## Task
- [17_Known_Unknowns_OOD.pdf](../tasks/17_known_unknowns_ood_pdf.md)

## Paper
- [17 Known Unknowns OOD](../papers/17_known_unknowns_ood.md)

## Provided Representations
- [composition](../representations/composition.md)
- [crystal graph](../representations/crystal_graph.md)
- [descriptor](../representations/descriptor.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)

## Evidence
- AFLOW is a high-throughput computational database containing ~14,000 solid materials with stoichiometric compositions and associated property values derived from density functional theory calculations. It includes six curated properties: band gap, bulk modulus, Debye temperature, shear modulus, thermal conductivity, and thermal expansion (the latter four log-scaled). In this paper, AFLOW is used to train and evaluate OOD property predictors on composition-based regression tasks, specifically to assess zero-shot extrapolation performance beyond the upper range of training property values during virtual screening of high-performing solids.

## Metadata
dataset_use_id: `dataset_use_7f67e60ee559`
link: https://aflowlib.org
