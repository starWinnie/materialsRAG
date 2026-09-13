# Dataset: labeled local database

- Dataset ID: `D_labeled_local_database`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- labeled local database
- local database
- 661 materials with κPET values

## Observed material scopes

- semiconductors

## Observed research tasks

- identifying semiconductors with ultralow lattice thermal conductivity

## Observed research stages

- candidate_screening
- computational_validation
- model_training
- model_evaluation

## Observed properties

- κPET at 300 K

## Observed fields

- κPET
- formula
- structure
- crystal system
- shear modulus
- bulk modulus

## Usage evidence

- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): screening in statistical analysis and candidate selection from labeled local database — Enable statistical analysis and candidate selection (e.g., Cs2SnSe3, Cs2GeSe3) based on κPET ≤ 2 W/mK threshold.
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): computational_validation in first-principles validation of selected candidates — Provide candidate list (Cs2SnSe3, Cs2GeSe3) selected from κPET-ranked materials for first-principles validation.
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): training in training interpretable supervised classification model — Train interpretable CatBoost classifier to predict ultralow κL (κPET ≤ 2 W/mK).
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): validation in evaluation of classification model performance — Evaluate trained CatBoost model performance via stratified tenfold cross-validation.

## Dataset evidence

- P008, PDF page 4: "Given the success of unsupervised learning in signiﬁcantly reducing the broad material search space, it has become feasible to further extend the second-level dataset into a labeled repository of thermal conductivity through HTC at affordable computational costs."
