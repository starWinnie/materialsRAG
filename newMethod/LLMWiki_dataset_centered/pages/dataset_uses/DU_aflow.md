# Dataset Use: AFLOW

- DatasetUse ID: `DU_aflow`
- Dataset: AFLOW (`D_aflow`)
- Papers: P017, P028
- Usage records: 2

## Usage roles

- source

## Purposes

- solid materials property prediction benchmark
- reference benchmark dataset for ES methods

## Used fields

- material composition
- property values
- id
- structure
- formation_energy
- bandgap
- elastic_tensor

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 14123

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P017_01_aflow

- Paper: `P017` — Known Unknowns: Out-of-Distribution Property Prediction in Materials and Molecules
- Task: Out-of-Distribution Property Prediction (`T_P017_01`)
- Stage: Dataset collection for solids and molecules (`data_acquisition`, `S_P017_01`)
- Usage role: source
- Purpose: solid materials property prediction benchmark
- Used fields: material composition, property values
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 14123
- Confidence: 1.0

Evidence:
- P017, PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- P017, PDF page 2, Results: "The datasets vary in size, ranging from approximately 300 to 14,000 samples."
- P017, PDF page 3, Table 1: "AFLOW30 Band Gap [eV] 14123"

### UR_P028_01_aflow

- Paper: `P028` — JARVIS-Leaderboard: a large scale benchmark of materials design methods
- Task: benchmarking of materials design methods (`T_P028_01`)
- Stage: populating reference benchmark datasets (`data_acquisition`, `S_P028_01`)
- Usage role: source
- Purpose: reference benchmark dataset for ES methods
- Used fields: id, structure, formation_energy, bandgap, elastic_tensor
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P028, PDF page 7: "PBE87 data from Open Quantum Materials Database (OQMD)88,89, AFLOW90 and Materials Project65 compare well with each other."

## Aggregated evidence

- , PDF page 2, Results: "We evaluate the extrapolation capability of Bilinear Transduction on three widely used benchmarks for solid materials property prediction, AFLOW, Matbench, and the Materials Project (MP), covering 12 distinct prediction tasks of various classes of materials properties: electronic, mechanical, thermal, etc."
- , PDF page 2, Results: "The datasets vary in size, ranging from approximately 300 to 14,000 samples."
- , PDF page 3, Table 1: "AFLOW30 Band Gap [eV] 14123"
- , PDF page 7: "PBE87 data from Open Quantum Materials Database (OQMD)88,89, AFLOW90 and Materials Project65 compare well with each other."
