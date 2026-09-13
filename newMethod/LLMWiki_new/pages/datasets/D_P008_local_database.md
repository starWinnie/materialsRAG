# Dataset: local database

- Dataset ID: `D_P008_local_database`
- Dataset type: `derived_subset`
- Source dataset: `D_P008_second_level_dataset`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- local database
- labeled repository of thermal conductivity
- 661 labeled materials with κPET values

## Observed material scopes

- semiconductors

## Observed research tasks

- identifying semiconductors with ultralow lattice thermal conductivity

## Observed research stages

- model_training
- model_evaluation
- label_generation

## Observed properties

- κPET at 300 K
- binary label (ultralow/non-ultralow κL)

## Observed fields

- κPET
- label

## Usage evidence

- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): training in training CatBoost classifier on labeled local database — Train supervised classification model to predict ultralow κL (κPET ≤ 2 W/mK)
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): validation in evaluating CatBoost classifier performance — Assess predictive accuracy and robustness of the trained model
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): label_source in assigning binary labels (ultralow/non-ultralow κL) based on κPET threshold — Generate training labels for supervised classification

## Dataset evidence

- P008, PDF page 4: "Given the success of unsupervised learning in signiﬁcantly reducing the broad material search space, it has become feasible to further extend the second-level dataset into a labeled repository of thermal conductivity through HTC at affordable computational costs. Based on the PET empirical equation within the high-throughput framework, we derive the κPET values at 300 K ignoring the anisotropy for materials in the second-level dataset..."
