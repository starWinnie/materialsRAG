# Dataset Use: Open Catalyst 2022

- DatasetUse ID: `DU_open_catalyst_2022`
- Dataset: Open Catalyst 2022 (`D_open_catalyst_2022`)
- Papers: P038
- Usage records: 1

## Usage roles

- training

## Purposes

- Fine-tuning the pre-trained S2EF-Total model for oxide surfaces and OER intermediates.

## Used fields

- relaxation_trajectory
- total_energy
- forces
- adsorbate

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 62331

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P038_02_open_catalyst_2022

- Paper: `P038` — Rational design of nanoscale stabilized oxide catalysts for OER with OC22
- Task: Rational design of nanoscale stabilized oxide catalysts for OER (`T_P038_01`)
- Stage: Fine-tuning OC22 S2EF-Total model (`model_training`, `S_P038_02`)
- Usage role: training
- Purpose: Fine-tuning the pre-trained S2EF-Total model for oxide surfaces and OER intermediates.
- Used fields: relaxation_trajectory, total_energy, forces, adsorbate
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 62331
- Confidence: 1.0

Evidence:
- P038, PDF page 2, 2.2 DFT and machine learning settings: "which was subsequently fine-tuned with the OC22 dataset (62331 DFT relaxations) to better predict the total energies of oxide surfaces and surface intermediates."

## Aggregated evidence

- , PDF page 2, 2.2 DFT and machine learning settings: "which was subsequently fine-tuned with the OC22 dataset (62331 DFT relaxations) to better predict the total energies of oxide surfaces and surface intermediates."
