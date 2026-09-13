# Dataset: local database

- Dataset ID: `D_P008_local_database`
- Dataset type: `derived_subset`
- Source dataset: `D_P008_second_level_dataset`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- local database
- labeled local database
- 661 materials with κPET values at 300 K

## Observed material scopes

- semiconductors

## Observed research tasks

- identifying semiconductors with ultralow lattice thermal conductivity

## Observed research stages

- label_generation
- model_training
- model_evaluation

## Observed properties

- κPET at 300 K
- binary label (ultralow κL: 1, non-ultralow κL: 0)

## Observed fields

- κPET
- label

## Usage evidence

- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): label_source in labeling materials as ultralow or non-ultralow κL based on κPET threshold — generate binary classification labels for supervised learning using κPET ≤2 W/mK as cutoff
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): training in training CatBoost classifier on labeled local database — train robust supervised classification model to predict ultralow κL directly from descriptors
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): validation in evaluating CatBoost model performance — assess classification accuracy and robustness using standard metrics

## Dataset evidence

- P008, PDF page 3, Results: "We use the phonon-elasticity-thermal (PET) model44 to perform low-cost HTC on the materials in the second-level dataset, establishing a local database based on the HTC results."
- P008, PDF page 7, Interpretable supervised learning for predicting ultralow κL: "Here, materials with κPET not exceeding 2 W/mK are labeled as 1, which are considered to possess ultralow κL; otherwise, they are labeled as 0, signifying non-ultralow κL."
