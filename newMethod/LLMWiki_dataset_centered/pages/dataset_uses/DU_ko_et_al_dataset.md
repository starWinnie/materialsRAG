# Dataset Use: Ko et al. dataset

- DatasetUse ID: `DU_ko_et_al_dataset`
- Dataset: Ko et al. dataset (`D_ko_et_al_dataset`)
- Papers: P039
- Usage records: 3

## Usage roles

- benchmark
- test
- candidate_pool

## Purposes

- Validate framework capability in capturing different charge states and long-range interactions
- Benchmark model performance on diverse charge-state systems
- Screen candidate systems for finetuning to achieve ab initio accuracy

## Used fields

- atomic coordinates
- atomic types
- energies
- forces

## Construction methods

- None stated

## Filter conditions

- Na8/9Cl8+ clusters
- Au2 dimers on MgO surfaces

## Sample counts

- None stated

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P039_01_ko_et_al_dataset

- Paper: `P039` — A foundation machine learning potential with polarizable long-range interactions for materials modelling
- Task: Develop a foundation machine learning interatomic potential with explicit polarizable long-range interactions (`T_P039_01`)
- Stage: Acquire training datasets including diverse charge-state systems and periodic table elements (`data_acquisition`, `S_P039_01`)
- Usage role: benchmark
- Purpose: Validate framework capability in capturing different charge states and long-range interactions
- Used fields: atomic coordinates, atomic types, energies, forces
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P039, PDF page 3, Validation on diverse charge-state datasets: "To evaluate the capability of our framework in capturing different charge states and long-range interactions, we validated our framework against the dataset developed by Ko et al.28 and Maruf et al.38, which encompass various charge states and charge transfer systems."

### UR_P039_04_ko_et_al_dataset

- Paper: `P039` — A foundation machine learning potential with polarizable long-range interactions for materials modelling
- Task: Develop a foundation machine learning interatomic potential with explicit polarizable long-range interactions (`T_P039_01`)
- Stage: Benchmark model performance on diverse charge-state datasets and physical properties (`model_evaluation`, `S_P039_04`)
- Usage role: test
- Purpose: Benchmark model performance on diverse charge-state systems
- Used fields: atomic coordinates, atomic types, energies, forces
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P039, PDF page 3, Validation on diverse charge-state datasets: "To evaluate the capability of our framework in capturing different charge states and long-range interactions, we validated our framework against the dataset developed by Ko et al.28 and Maruf et al.38, which encompass various charge states and charge transfer systems."

### UR_P039_07_ko_et_al_dataset

- Paper: `P039` — A foundation machine learning potential with polarizable long-range interactions for materials modelling
- Task: Develop a foundation machine learning interatomic potential with explicit polarizable long-range interactions (`T_P039_01`)
- Stage: Screen candidate systems for finetuning to achieve ab initio accuracy (`candidate_screening`, `S_P039_07`)
- Usage role: candidate_pool
- Purpose: Screen candidate systems for finetuning to achieve ab initio accuracy
- Used fields: atomic coordinates, atomic types, energies, forces
- Filter conditions: Na8/9Cl8+ clusters, Au2 dimers on MgO surfaces
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P039, PDF page 7, Finetuning for enhanced accuracy: "Using Na8/9Cl8+ clusters and Au2 dimers on MgO surfaces from Ko et al.28 as test cases, we performed targeted finetuning using 20% subsets of configurations and mean squared force error as the sole loss function."

## Aggregated evidence

- , PDF page 3, Validation on diverse charge-state datasets: "To evaluate the capability of our framework in capturing different charge states and long-range interactions, we validated our framework against the dataset developed by Ko et al.28 and Maruf et al.38, which encompass various charge states and charge transfer systems."
- , PDF page 3, Validation on diverse charge-state datasets: "To evaluate the capability of our framework in capturing different charge states and long-range interactions, we validated our framework against the dataset developed by Ko et al.28 and Maruf et al.38, which encompass various charge states and charge transfer systems."
- , PDF page 7, Finetuning for enhanced accuracy: "Using Na8/9Cl8+ clusters and Au2 dimers on MgO surfaces from Ko et al.28 as test cases, we performed targeted finetuning using 20% subsets of configurations and mean squared force error as the sole loss function."
