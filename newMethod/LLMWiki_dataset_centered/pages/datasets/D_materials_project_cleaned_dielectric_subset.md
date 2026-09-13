# Dataset: Materials Project cleaned dielectric subset

- Dataset ID: `D_materials_project_cleaned_dielectric_subset`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project_v2023_11_1_dielectric_dataset`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- Materials Project cleaned dielectric subset
- cleaned dataset
- 6648 structures
- 6648 cleaned structures
- refined MP dataset

## Observed material scopes

- inorganic materials

## Observed research tasks

- Dielectric tensor prediction for inorganic materials

## Observed research stages

- data_preparation
- model_evaluation

## Observed properties

- dielectric tensor
- electronic dielectric tensor
- ionic dielectric tensor
- total dielectric tensor

## Observed fields

- structure
- ε∞ij
- ε0ij
- εij

## Usage evidence

- P019 (Dielectric tensor prediction for inorganic materials using latent information from preferred potential): training in Dataset cleaning and filtering — Model training after cleaning and filtering / Validation during model training / Model evaluation on held-out test set
- P019 (Dielectric tensor prediction for inorganic materials using latent information from preferred potential): benchmark in Benchmarking DTNet against state-of-the-art models — Benchmarking DTNet against state-of-the-art models

## Dataset evidence

- P019, PDF page 3, unknown: "We clean up the dataset by restricting the element in total dielectric constants εij ∈[−10, 100] for ∀i, j∈{1,2,3} and filtering out structures that contain elements not supported by PFP. Finally there are 6648 structures retained for model training."
- P019, PDF page 11, Methods: "We clean up the dataset by filtering out dielectric constants that contain any element out of the range of [−10, 100]. Structures that contain elements not supported by PFP (shown in Fig. 4c) are cleaned up, and finally there are 6,648 structures retained for model training."
