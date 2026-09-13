# Dataset Use: List of 55 experimentally-reported chemical compositions

- DatasetUse ID: `DU_list_of_55_experimentally_reported_chemical_compositions`
- Dataset: List of 55 experimentally-reported chemical compositions (`D_list_of_55_experimentally_reported_chemical_compositions`)
- Papers: P037
- Usage records: 1

## Usage roles

- candidate_pool

## Purposes

- candidate pool for screening new TCM candidates

## Used fields

- chemical formula

## Construction methods

- search across MPDS, Pearson's Crystallographic Database, and ICSD for compounds containing Zn, Ga, Sn, Al, In

## Filter conditions

- oxide compounds with three cations from Zn, Ga, Sn, Al, In
- doped binary oxides (ZnO, SnO2, In2O3) with dopants not in training dataset

## Sample counts

- 55

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P037_06_list_of_55_experimentally_reported_chemical_compositions

- Paper: `P037` — Assessing data-driven predictions of band gap and electrical conductivity for transparent conducting materials
- Task: accelerating the discovery of new transparent conducting materials (TCMs) (`T_P037_01`)
- Stage: screening 55 compositions for TCM characteristics (`candidate_screening`, `S_P037_06`)
- Usage role: candidate_pool
- Purpose: candidate pool for screening new TCM candidates
- Used fields: chemical formula
- Filter conditions: oxide compounds with three cations from Zn, Ga, Sn, Al, In, doped binary oxides (ZnO, SnO2, In2O3) with dopants not in training dataset
- Construction method: search across MPDS, Pearson's Crystallographic Database, and ICSD for compounds containing Zn, Ga, Sn, Al, In
- Sample count: 55
- Confidence: 1.0

Evidence:
- P037, PDF page 12, Testing the search for new TCMs: "We conducted a search for oxide compounds containing combinations of three cations from Zn, Ga, Sn, Al, and In. We also include a small selection of five compositions across MPDS and ICSD of doped binary oxides (ZnO, SnO2 and In2O3), with dopants not present in the training dataset. We end up with a final list comprising 55 compositions shown in Table 4."

## Aggregated evidence

- , PDF page 12, Testing the search for new TCMs: "We conducted a search for oxide compounds containing combinations of three cations from Zn, Ga, Sn, Al, and In. We also include a small selection of five compositions across MPDS and ICSD of doped binary oxides (ZnO, SnO2 and In2O3), with dopants not present in the training dataset. We end up with a final list comprising 55 compositions shown in Table 4."
