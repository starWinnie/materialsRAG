# Dataset Use: MP21 Energy Above Convex Hull Dataset

- DatasetUse ID: `DU_mp21_energy_above_convex_hull_dataset`
- Dataset: MP21 Energy Above Convex Hull Dataset (`D_mp21_energy_above_convex_hull_dataset`)
- Papers: P013
- Usage records: 2

## Usage roles

- benchmark
- pretraining

## Purposes

- Benchmark CrysCo's performance on energy above convex hull prediction
- Pretrain CrysCoT models on energy above convex hull for transfer learning to data-scarce properties

## Used fields

- material compositions
- crystal structures

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 126785

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P013_04_mp21_energy_above_convex_hull_dataset

- Paper: `P013` — Accelerating materials property prediction via a hybrid Transformer Graph framework that leverages four body interactions
- Task: materials property prediction (`T_P013_01`)
- Stage: transfer learning for data-scarce properties (`model_training`, `S_P013_04`)
- Usage role: pretraining
- Purpose: Pretrain CrysCoT models on energy above convex hull for transfer learning to data-scarce properties
- Used fields: material compositions, crystal structures
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 126785
- Confidence: 1.0

Evidence:
- P013, PDF page 6, unknown: "We ﬁrst trained parent models on primary properties (Eg, Ef, and EHull), with dataset sizes ranging from 126,728 to 126,785 entries from MP21."

### UR_P013_05_mp21_energy_above_convex_hull_dataset

- Paper: `P013` — Accelerating materials property prediction via a hybrid Transformer Graph framework that leverages four body interactions
- Task: materials property prediction (`T_P013_01`)
- Stage: benchmarking CrysCo's performance (`model_evaluation`, `S_P013_05`)
- Usage role: benchmark
- Purpose: Benchmark CrysCo's performance on energy above convex hull prediction
- Used fields: material compositions, crystal structures
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 126785
- Confidence: 1.0

Evidence:
- P013, PDF page 4, unknown: "Table 1 | The eight datasets derived from the MP21 database and used in the present study Dataset name	Source	Material property	# Crystal structures MP_ehull (EHull)	MP21	Energy above the convex hull (eV/atom)	126,785"

## Aggregated evidence

- , PDF page 4, unknown: "Table 1 | The eight datasets derived from the MP21 database and used in the present study Dataset name	Source	Material property	# Crystal structures MP_ehull (EHull)	MP21	Energy above the convex hull (eV/atom)	126,785"
- , PDF page 6, unknown: "We ﬁrst trained parent models on primary properties (Eg, Ef, and EHull), with dataset sizes ranging from 126,728 to 126,785 entries from MP21."
