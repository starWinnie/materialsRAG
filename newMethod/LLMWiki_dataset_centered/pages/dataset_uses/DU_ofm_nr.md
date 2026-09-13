# Dataset Use: OFM-nr

- DatasetUse ID: `DU_ofm_nr`
- Dataset: OFM-nr (`D_ofm_nr`)
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

- MD-HIT-structure algorithm with OFM feature distance threshold

## Filter conditions

- OFM distance thresholds: 0.15, 0.2, 0.45, 0.7

## Sample counts

- None stated

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P026_04_ofm_nr

- Paper: `P026` — MD-HIT: Machine learning for material property prediction with dataset redundancy control
- Task: dataset redundancy control for material property prediction (`T_P026_01`)
- Stage: evaluate ML model performance on redundancy-controlled splits (`model_evaluation`, `S_P026_04`)
- Usage role: training
- Purpose: Training set for structure-based ML models (ALIGNN, DeeperGATGNN) under redundancy control
- Used fields: CIF files, formation energy per atom, band gaps
- Filter conditions: OFM distance thresholds: 0.15, 0.2, 0.45, 0.7
- Construction method: MD-HIT-structure algorithm with OFM feature distance threshold
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P026, PDF page 7, Structure based material property prediction with redundancy control: "We further evaluated the impact of OFM-controlled data redundancy on the algorithms’ performance (Fig. 6)."

## Aggregated evidence

- , PDF page 7, Structure based material property prediction with redundancy control: "We further evaluated the impact of OFM-controlled data redundancy on the algorithms’ performance (Fig. 6)."
