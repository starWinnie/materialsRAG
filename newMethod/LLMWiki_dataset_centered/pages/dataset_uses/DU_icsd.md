# Dataset Use: ICSD

- DatasetUse ID: `DU_icsd`
- Dataset: ICSD (`D_icsd`)
- Papers: P031
- Usage records: 2

## Usage roles

- source
- candidate_pool

## Purposes

- source of ordered and disordered crystal structures for constructing SuperCon3D
- screening the entire ICSD database to identify potential high-Tc superconductors

## Used fields

- ordered and disordered crystal structures
- crystal structures

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 208425

## Availability

- Dataset: restricted
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P031_01_icsd

- Paper: `P031` — Learning Superconductivity from Ordered and Disordered Material Structures
- Task: designing high Tc superconductors (`T_P031_01`)
- Stage: constructing SuperCon3D dataset (`data_acquisition`, `S_P031_01`)
- Usage role: source
- Purpose: source of ordered and disordered crystal structures for constructing SuperCon3D
- Used fields: ordered and disordered crystal structures
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 208425
- Confidence: 1.0

Evidence:
- P031, PDF page 7, 5.1.1 SuperCon3D dataset.: "Additionally, over 200,000 ordered and disordered crystal structures were gathered from the ICSD database [3]. We then matched these 11,949 SuperCon entries with 208,425 ICSD entries based on chemical composition, space group and lattice parameter."

### UR_P031_04_icsd

- Paper: `P031` — Learning Superconductivity from Ordered and Disordered Material Structures
- Task: designing high Tc superconductors (`T_P031_01`)
- Stage: screening ICSD database with SODNet (`candidate_screening`, `S_P031_04`)
- Usage role: candidate_pool
- Purpose: screening the entire ICSD database to identify potential high-Tc superconductors
- Used fields: crystal structures
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P031, PDF page 9, 5.2.4 Potential Superconducting Materials.: "Using our model, we screened the ICSD database to identify potential high-Tc superconductors."

## Aggregated evidence

- , PDF page 7, 5.1.1 SuperCon3D dataset.: "Additionally, over 200,000 ordered and disordered crystal structures were gathered from the ICSD database [3]. We then matched these 11,949 SuperCon entries with 208,425 ICSD entries based on chemical composition, space group and lattice parameter."
- , PDF page 9, 5.2.4 Potential Superconducting Materials.: "Using our model, we screened the ICSD database to identify potential high-Tc superconductors."
