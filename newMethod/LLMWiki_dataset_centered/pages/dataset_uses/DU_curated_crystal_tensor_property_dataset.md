# Dataset Use: Curated Crystal Tensor Property Dataset

- DatasetUse ID: `DU_curated_crystal_tensor_property_dataset`
- Dataset: Curated Crystal Tensor Property Dataset (`D_curated_crystal_tensor_property_dataset`)
- Papers: P020
- Usage records: 1

## Usage roles

- training

## Purposes

- training, validation, and test data for GMTNet across dielectric, piezoelectric, and elastic tensor prediction tasks

## Used fields

- crystal structure M = (A, P, L)
- tensor property values

## Construction methods

- extracting both the tensor property values and corresponding crystal structures directly from the DFT calculation files of JARVIS-DFT

## Filter conditions

- congruence between properties and structures
- consistent DFT core computation

## Sample counts

- None stated

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P020_01_curated_crystal_tensor_property_dataset

- Paper: `P020` — A Space Group Symmetry Informed Network for O(3) Equivariant Crystal Tensor Prediction
- Task: crystal tensor property prediction (`T_P020_01`)
- Stage: curating a dataset encompassing dielectric, piezoelectric, and elastic tensors (`data_acquisition`, `S_P020_01`)
- Usage role: training
- Purpose: training, validation, and test data for GMTNet across dielectric, piezoelectric, and elastic tensor prediction tasks
- Used fields: crystal structure M = (A, P, L), tensor property values
- Filter conditions: congruence between properties and structures, consistent DFT core computation
- Construction method: extracting both the tensor property values and corresponding crystal structures directly from the DFT calculation files of JARVIS-DFT
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P020, PDF page 7, 5.1. Curated Crystal Tensor Property Dataset: "In our research, a dataset is curated specifically focusing on crystal tensor properties, including dielectric, piezoelectric, and elastic tensors, sourced from the JARVIS-DFT database (Choudhary et al., 2020). This dataset has been constructed with a keen emphasis on ensuring congruence between the properties and structures, achieved by extracting both the tensor property values and corresponding crystal structures directly from the DFT calculation files. This approach guarantees that the symmetry of the properties aligns with that of the structures. Notably, each tensor property within this dataset is computed using a consistent DFT core, ensuring uniformity in the calculation method."
- P020, PDF page 7, 5.1. Curated Crystal Tensor Property Dataset: "Table 1. Dataset statistics. Fnorm denotes Frobenius norm. Dataset # Samples Fnorm Mean Fnorm STD # Elem. Unit Dielectric 4713 14.7 18.2 87 Unitless Piezo 4998 0.43 3.09 87 C/m2 Elastic 14220 327 249 87 GPa"

## Aggregated evidence

- , PDF page 7, 5.1. Curated Crystal Tensor Property Dataset: "In our research, a dataset is curated specifically focusing on crystal tensor properties, including dielectric, piezoelectric, and elastic tensors, sourced from the JARVIS-DFT database (Choudhary et al., 2020). This dataset has been constructed with a keen emphasis on ensuring congruence between the properties and structures, achieved by extracting both the tensor property values and corresponding crystal structures directly from the DFT calculation files. This approach guarantees that the symmetry of the properties aligns with that of the structures. Notably, each tensor property within this dataset is computed using a consistent DFT core, ensuring uniformity in the calculation method."
- , PDF page 7, 5.1. Curated Crystal Tensor Property Dataset: "Table 1. Dataset statistics. Fnorm denotes Frobenius norm. Dataset # Samples Fnorm Mean Fnorm STD # Elem. Unit Dielectric 4713 14.7 18.2 87 Unitless Piezo 4998 0.43 3.09 87 C/m2 Elastic 14220 327 249 87 GPa"
