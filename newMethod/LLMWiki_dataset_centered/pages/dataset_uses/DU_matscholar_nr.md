# Dataset Use: Matscholar-nr

- DatasetUse ID: `DU_matscholar_nr`
- Dataset: Matscholar-nr (`D_matscholar_nr`)
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

- MD-HIT-composition algorithm with Matscholar similarity threshold

## Filter conditions

- Matscholar distance thresholds: 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4

## Sample counts

- None stated

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P026_04_matscholar_nr

- Paper: `P026` — MD-HIT: Machine learning for material property prediction with dataset redundancy control
- Task: dataset redundancy control for material property prediction (`T_P026_01`)
- Stage: evaluate ML model performance on redundancy-controlled splits (`model_evaluation`, `S_P026_04`)
- Usage role: training
- Purpose: Training set for composition-based ML models (Roost, CrabNet) under redundancy control
- Used fields: compositions, formation energy, band gap
- Filter conditions: Matscholar distance thresholds: 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4
- Construction method: MD-HIT-composition algorithm with Matscholar similarity threshold
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P026, PDF page 4, Datasets generation: "Similarly, we generated eight Matscholar non-redundant datasets (Matscholar-nr) with percentages of the total range from 50.82% to 2.33%."

## Aggregated evidence

- , PDF page 4, Datasets generation: "Similarly, we generated eight Matscholar non-redundant datasets (Matscholar-nr) with percentages of the total range from 50.82% to 2.33%."
