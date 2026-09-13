# Dataset: Materials Project cleaned subset (6648 structures)

- Dataset ID: `D_P019_materials_project_cleaned_subset_6648_structures`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- Materials Project cleaned subset (6648 structures)
- cleaned dataset
- 6648 structures
- 6648 structures retained for model training

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

- P019 (Dielectric tensor prediction for inorganic materials using latent information from preferred potential): training in Dataset cleaning and filtering — Clean the raw MP dataset by restricting dielectric constant ranges and filtering out unsupported elements.
- P019 (Dielectric tensor prediction for inorganic materials using latent information from preferred potential): test in Benchmarking against state-of-the-art models — Evaluate DTNet performance using MAEten, MAEmean-diag, MAEdiag, and MAEoff-diag metrics.

## Dataset evidence

- P019, PDF page 3, unknown: "We clean up the dataset by restricting the element in total dielectric constants εij ∈[−10, 100] for ∀i, j∈{1,2,3} and filtering out structures that contain elements not supported by PFP. Finally there are 6648 structures retained for model training."
- P019, PDF page 11, Methods: "We clean up the dataset by filtering out dielectric constants that contain any element out of the range of [−10, 100]. Structures that contain elements not supported by PFP (shown in Fig. 4c) are cleaned up, and finally there are 6,648 structures retained for model training."
