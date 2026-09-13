# Dataset Use: NMC

- DatasetUse ID: `DU_nmc`
- Dataset: NMC (`D_nmc`)
- Papers: P025
- Usage records: 1

## Usage roles

- training

## Purposes

- Train and validate ChargE3Net on nickel manganese cobalt battery cathode materials

## Used fields

- atomic species
- atomic positions
- charge density grid points

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 1450

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P025_01_nmc

- Paper: `P025` — Higher-order equivariant neural networks for charge density prediction in materials
- Task: charge density prediction (`T_P025_01`)
- Stage: collecting DFT-computed charge density data (`data_acquisition`, `S_P025_01`)
- Usage role: training
- Purpose: Train and validate ChargE3Net on nickel manganese cobalt battery cathode materials
- Used fields: atomic species, atomic positions, charge density grid points
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 1450
- Confidence: 1.0

Evidence:
- P025, PDF page 2, Results: "We train and validate ChargE3Net on a diverse set of DFT-computed charge density data, including organic molecules (QM9)54–56, nickel manganese cobalt battery cathode materials (NMC)57, and inorganic materials collected from Materials Project (MP)49,58."
- P025, PDF page 7, Datasets: "The NMC dataset57 consists of VASP calculations of 2000 randomly sampled nickel manganese cobalt oxides containing varying levels of lithium content, with training, validation, and test splits of size 1450, 50, and 500 respectively."

## Aggregated evidence

- , PDF page 2, Results: "We train and validate ChargE3Net on a diverse set of DFT-computed charge density data, including organic molecules (QM9)54–56, nickel manganese cobalt battery cathode materials (NMC)57, and inorganic materials collected from Materials Project (MP)49,58."
- , PDF page 7, Datasets: "The NMC dataset57 consists of VASP calculations of 2000 randomly sampled nickel manganese cobalt oxides containing varying levels of lithium content, with training, validation, and test splits of size 1450, 50, and 500 respectively."
