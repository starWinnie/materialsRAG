# HiBoFL Local Database (PET-derived)

## Ontology Type
DatasetUse

## Usage Description
A custom-built, MongoDB-stored local database containing 661 semiconductors from clusters C1 and C2 (selected via unsupervised learning on the Materials Project data), each annotated with lattice thermal conductivity values (κPET) at 300 K computed using the phonon-elasticity-thermal (PET) empirical model. It includes derived elastic properties (bulk/shear moduli), crystal system, formula type, and elemental composition. This dataset is used to train and validate the supervised CatBoost classifier for ultralow κL prediction (κPET ≤ 2 W/mK), enable statistical analysis of low-κL trends, and prioritize candidates (e.g., Cs2SnSe3, Cs2GeSe3) for first-principles validation.

## Dataset
- [HiBoFL Local Database (PET-derived)](../datasets/hibofl_local_database_pet_derived.md)

## Task
- [08_HiBoFL_Thermal_Conductivity.pdf](../tasks/08_hibofl_thermal_conductivity_pdf.md)

## Paper
- [08 HiBoFL Thermal Conductivity](../papers/08_hibofl_thermal_conductivity.md)

## Provided Representations
- [composition](../representations/composition.md)
- [descriptor](../representations/descriptor.md)

## Supported R&D Stages
- [Dataset Selection](../stages/dataset_selection.md)
- [Representation / Feature Construction](../stages/representation_feature_construction.md)
- [Model Training](../stages/model_training.md)
- [Screening / Prediction](../stages/screening_prediction.md)
- [Validation](../stages/validation.md)

## Evidence
- A custom-built, MongoDB-stored local database containing 661 semiconductors from clusters C1 and C2 (selected via unsupervised learning on the Materials Project data), each annotated with lattice thermal conductivity values (κPET) at 300 K computed using the phonon-elasticity-thermal (PET) empirical model. It includes derived elastic properties (bulk/shear moduli), crystal system, formula type, and elemental composition. This dataset is used to train and validate the supervised CatBoost classifier for ultralow κL prediction (κPET ≤ 2 W/mK), enable statistical analysis of low-κL trends, and prioritize candidates (e.g., Cs2SnSe3, Cs2GeSe3) for first-principles validation.

## Metadata
dataset_use_id: `dataset_use_d80d5b12b3a5`
link: None
