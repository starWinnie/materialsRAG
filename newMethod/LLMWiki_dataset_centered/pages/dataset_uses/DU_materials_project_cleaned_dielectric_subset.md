# Dataset Use: Materials Project cleaned dielectric subset

- DatasetUse ID: `DU_materials_project_cleaned_dielectric_subset`
- Dataset: Materials Project cleaned dielectric subset (`D_materials_project_cleaned_dielectric_subset`)
- Papers: P019
- Usage records: 2

## Usage roles

- training
- benchmark

## Purposes

- Model training after cleaning and filtering / Validation during model training / Model evaluation on held-out test set
- Benchmarking DTNet against state-of-the-art models

## Used fields

- structure
- ε∞ij
- ε0ij
- εij

## Construction methods

- Filtering dielectric constants εij ∈ [−10, 100] and removing structures with elements unsupported by PFP

## Filter conditions

- εij ∈ [−10, 100]
- elements supported by PFP

## Sample counts

- 6648

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P019_02_materials_project_cleaned_dielectric_subset

- Paper: `P019` — Dielectric tensor prediction for inorganic materials using latent information from preferred potential
- Task: Dielectric tensor prediction for inorganic materials (`T_P019_01`)
- Stage: Dataset cleaning and filtering (`data_preparation`, `S_P019_02`)
- Usage role: training
- Purpose: Model training after cleaning and filtering / Validation during model training / Model evaluation on held-out test set
- Used fields: structure, ε∞ij, ε0ij, εij
- Filter conditions: εij ∈ [−10, 100], elements supported by PFP
- Construction method: Filtering dielectric constants εij ∈ [−10, 100] and removing structures with elements unsupported by PFP
- Sample count: 6648
- Confidence: 1.0

Evidence:
- P019, PDF page 3, unknown: "We clean up the dataset by restricting the element in total dielectric constants εij ∈[−10, 100] for ∀i, j∈{1,2,3} and filtering out structures that contain elements not supported by PFP. Finally there are 6648 structures retained for model training."
- P019, PDF page 3, unknown: "The above dataset was partitioned into training, validation, and test subsets in a 0.8:0.1:0.1 ratio for the experimental analysis."
- P019, PDF page 3, unknown: "The above dataset was partitioned into training, validation, and test subsets in a 0.8:0.1:0.1 ratio for the experimental analysis."

### UR_P019_04_materials_project_cleaned_dielectric_subset

- Paper: `P019` — Dielectric tensor prediction for inorganic materials using latent information from preferred potential
- Task: Dielectric tensor prediction for inorganic materials (`T_P019_01`)
- Stage: Benchmarking DTNet against state-of-the-art models (`model_evaluation`, `S_P019_04`)
- Usage role: benchmark
- Purpose: Benchmarking DTNet against state-of-the-art models
- Used fields: structure, ε∞ij, ε0ij, εij
- Filter conditions: εij ∈ [−10, 100], elements supported by PFP
- Construction method: Filtering dielectric constants εij ∈ [−10, 100] and removing structures with elements unsupported by PFP
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P019, PDF page 2, Results: "To evaluate the performance of DTNet, we compared it against existing methods, PaiNN31, M3GNet36 and MatTen37, on the dataset obtained from Materials Project (MP)38."

## Aggregated evidence

- , PDF page 3, unknown: "We clean up the dataset by restricting the element in total dielectric constants εij ∈[−10, 100] for ∀i, j∈{1,2,3} and filtering out structures that contain elements not supported by PFP. Finally there are 6648 structures retained for model training."
- , PDF page 3, unknown: "The above dataset was partitioned into training, validation, and test subsets in a 0.8:0.1:0.1 ratio for the experimental analysis."
- , PDF page 3, unknown: "The above dataset was partitioned into training, validation, and test subsets in a 0.8:0.1:0.1 ratio for the experimental analysis."
- , PDF page 2, Results: "To evaluate the performance of DTNet, we compared it against existing methods, PaiNN31, M3GNet36 and MatTen37, on the dataset obtained from Materials Project (MP)38."
