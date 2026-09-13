# Dataset Use: Mendeleev-nr

- DatasetUse ID: `DU_mendeleev_nr`
- Dataset: Mendeleev-nr (`D_mendeleev_nr`)
- Papers: P026
- Usage records: 1

## Usage roles

- training

## Purposes

- Training set for composition-based ML models (Roost, CrabNet) under redundancy control

## Used fields

- compositions
- formation energy
- band gap

## Construction methods

- MD-HIT-composition algorithm with Mendeleev similarity threshold

## Filter conditions

- Mendeleev distance thresholds: 0.5, 0.8, 1, 1.5, 2, 2.5, 3

## Sample counts

- 3177

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P026_04_mendeleev_nr

- Paper: `P026` — MD-HIT: Machine learning for material property prediction with dataset redundancy control
- Task: dataset redundancy control for material property prediction (`T_P026_01`)
- Stage: evaluate ML model performance on redundancy-controlled splits (`model_evaluation`, `S_P026_04`)
- Usage role: training
- Purpose: Training set for composition-based ML models (Roost, CrabNet) under redundancy control
- Used fields: compositions, formation energy, band gap
- Filter conditions: Mendeleev distance thresholds: 0.5, 0.8, 1, 1.5, 2, 2.5, 3
- Construction method: MD-HIT-composition algorithm with Mendeleev similarity threshold
- Sample count: 3177
- Confidence: 1.0

Evidence:
- P026, PDF page 4, Datasets generation: "For Mendeleev similarity, we used distance thresholds of 0.5, 0.8, 1, 1.5, 2, 2.5, and 3 to generate seven non-redundant datasets (Mendeleev-nr). The dataset sizes range from 86,740 to 3177."

## Aggregated evidence

- , PDF page 4, Datasets generation: "For Mendeleev similarity, we used distance thresholds of 0.5, 0.8, 1, 1.5, 2, 2.5, and 3 to generate seven non-redundant datasets (Mendeleev-nr). The dataset sizes range from 86,740 to 3177."
