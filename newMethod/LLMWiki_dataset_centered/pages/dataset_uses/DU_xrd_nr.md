# Dataset Use: XRD-nr

- DatasetUse ID: `DU_xrd_nr`
- Dataset: XRD-nr (`D_xrd_nr`)
- Papers: P026
- Usage records: 1

## Usage roles

- training

## Purposes

- Training set for structure-based ML models (ALIGNN, DeeperGATGNN) under redundancy control

## Used fields

- CIF files
- formation energy per atom
- band gaps

## Construction methods

- MD-HIT-structure algorithm with XRD feature distance threshold

## Filter conditions

- XRD distance thresholds: 0.5, 0.6, 0.8, 0.9

## Sample counts

- None stated

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P026_04_xrd_nr

- Paper: `P026` — MD-HIT: Machine learning for material property prediction with dataset redundancy control
- Task: dataset redundancy control for material property prediction (`T_P026_01`)
- Stage: evaluate ML model performance on redundancy-controlled splits (`model_evaluation`, `S_P026_04`)
- Usage role: training
- Purpose: Training set for structure-based ML models (ALIGNN, DeeperGATGNN) under redundancy control
- Used fields: CIF files, formation energy per atom, band gaps
- Filter conditions: XRD distance thresholds: 0.5, 0.6, 0.8, 0.9
- Construction method: MD-HIT-structure algorithm with XRD feature distance threshold
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P026, PDF page 6: "For XRD-based non-redundant datasets (XRD-nr), we used thresholds of 0.5, 0.6, 0.8, and 0.9."

## Aggregated evidence

- , PDF page 6: "For XRD-based non-redundant datasets (XRD-nr), we used thresholds of 0.5, 0.6, 0.8, and 0.9."
