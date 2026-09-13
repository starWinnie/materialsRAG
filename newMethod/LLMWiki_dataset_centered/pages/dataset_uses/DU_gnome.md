# Dataset Use: GNoME

- DatasetUse ID: `DU_gnome`
- Dataset: GNoME (`D_gnome`)
- Papers: P025
- Usage records: 1

## Usage roles

- computational_validation

## Purposes

- Evaluate generalization capabilities of ChargE3Net on out-of-distribution materials

## Used fields

- atomic species
- atomic positions
- charge density grid points

## Construction methods

- None stated

## Filter conditions

- 5 or 6 unique species

## Sample counts

- 1924

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P025_01_gnome

- Paper: `P025` — Higher-order equivariant neural networks for charge density prediction in materials
- Task: charge density prediction (`T_P025_01`)
- Stage: collecting DFT-computed charge density data (`data_acquisition`, `S_P025_01`)
- Usage role: computational_validation
- Purpose: Evaluate generalization capabilities of ChargE3Net on out-of-distribution materials
- Used fields: atomic species, atomic positions, charge density grid points
- Filter conditions: 5 or 6 unique species
- Construction method: Not stated
- Sample count: 1924
- Confidence: 1.0

Evidence:
- P025, PDF page 4, experimental: "To examine the generalization capabilities of ChargE3Net on out-of-distribution data, we analyze a random subset of 1924 materials published by GNoME50 with 5 or more unique species to differentiate it from the MP distribution."
- P025, PDF page 8, Data availability: "In addition to a held-out test set randomly sampled from the Materials Project, we obtain a random set of 2000 published structures from GNoME50 as a second test set. Speciﬁcally, we choose a random set of materials from GNoME with 5 or 6 unique species as these are less well-represented in the Materials Project training data. DFT calculations were set up using pymatgen71 and otherwise using the same methodology as detailed in Section4.4.76calculationsfailed,leaving1924materialsforanalysis,1510of which were non-magnetic."

## Aggregated evidence

- , PDF page 4, experimental: "To examine the generalization capabilities of ChargE3Net on out-of-distribution data, we analyze a random subset of 1924 materials published by GNoME50 with 5 or more unique species to differentiate it from the MP distribution."
- , PDF page 8, Data availability: "In addition to a held-out test set randomly sampled from the Materials Project, we obtain a random set of 2000 published structures from GNoME50 as a second test set. Speciﬁcally, we choose a random set of materials from GNoME with 5 or 6 unique species as these are less well-represented in the Materials Project training data. DFT calculations were set up using pymatgen71 and otherwise using the same methodology as detailed in Section4.4.76calculationsfailed,leaving1924materialsforanalysis,1510of which were non-magnetic."
