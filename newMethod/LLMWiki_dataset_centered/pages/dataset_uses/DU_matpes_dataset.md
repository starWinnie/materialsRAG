# Dataset Use: MATPES dataset

- DatasetUse ID: `DU_matpes_dataset`
- Dataset: MATPES dataset (`D_matpes_dataset`)
- Papers: P035
- Usage records: 1

## Usage roles

- pretraining

## Purposes

- Train the foundational MLIP PET-OMATPES model at the r2SCAN level, enabling zero-shot formation energy predictions on DFT-relaxed geometries.

## Used fields

- energies
- forces

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- None stated

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P035_03_matpes_dataset

- Paper: `P035` — Correcting DFT formation energies towards experimental accuracy using foundational MLIPs and latent-feature delta-learning
- Task: Correcting DFT formation energies towards experimental accuracy (`T_P035_01`)
- Stage: Evaluating zero-shot fMLIP formation energies (`model_evaluation`, `S_P035_03`)
- Usage role: pretraining
- Purpose: Train the foundational MLIP PET-OMATPES model at the r2SCAN level, enabling zero-shot formation energy predictions on DFT-relaxed geometries.
- Used fields: energies, forces
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P035, PDF page 3, RESULTS: "Fig. 2b shows that zero-shot formation energies [62] from the PET-OMATPES model [63, 64]—one of the top-performing models in community benchmarks at the time of publication [65], trained on the OMAT [66] and MATPES [37] datasets at the r2SCAN level—reduce the MAE by more than 40% when evaluated at the DFT (GGA) relaxed geometry."

## Aggregated evidence

- , PDF page 3, RESULTS: "Fig. 2b shows that zero-shot formation energies [62] from the PET-OMATPES model [63, 64]—one of the top-performing models in community benchmarks at the time of publication [65], trained on the OMAT [66] and MATPES [37] datasets at the r2SCAN level—reduce the MAE by more than 40% when evaluated at the DFT (GGA) relaxed geometry."
