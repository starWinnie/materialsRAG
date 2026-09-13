# Dataset Use: QM9

- DatasetUse ID: `DU_qm9`
- Dataset: QM9 (`D_qm9`)
- Papers: P025, P028
- Usage records: 2

## Usage roles

- training
- source

## Purposes

- Train and validate ChargE3Net on organic molecules
- reference benchmark dataset for AI methods

## Used fields

- atomic species
- atomic positions
- charge density grid points
- id
- smiles
- geometry
- energy
- forces
- dipole_moment
- polarizability
- homo
- lumo
- gap
- zpve
- u0
- u298
- h298
- g298
- cv

## Construction methods

- None stated

## Filter conditions

- None stated

## Sample counts

- 123835

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P025_01_qm9

- Paper: `P025` — Higher-order equivariant neural networks for charge density prediction in materials
- Task: charge density prediction (`T_P025_01`)
- Stage: collecting DFT-computed charge density data (`data_acquisition`, `S_P025_01`)
- Usage role: training
- Purpose: Train and validate ChargE3Net on organic molecules
- Used fields: atomic species, atomic positions, charge density grid points
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: 123835
- Confidence: 1.0

Evidence:
- P025, PDF page 2, Results: "We train and validate ChargE3Net on a diverse set of DFT-computed charge density data, including organic molecules (QM9)54–56, nickel manganese cobalt battery cathode materials (NMC)57, and inorganic materials collected from Materials Project (MP)49,58."
- P025, PDF page 7, Datasets: "The QM9 dataset56 contains VASP calculations of the 133,845 small organic molecules introduced by Ramakrishnan et al.55, with training, validation, and test splits of size 123,835, 50, and 10,000 respectively."

### UR_P028_01_qm9

- Paper: `P028` — JARVIS-Leaderboard: a large scale benchmark of materials design methods
- Task: benchmarking of materials design methods (`T_P028_01`)
- Stage: populating reference benchmark datasets (`data_acquisition`, `S_P028_01`)
- Usage role: source
- Purpose: reference benchmark dataset for AI methods
- Used fields: id, smiles, geometry, energy, forces, dipole_moment, polarizability, homo, lumo, gap, zpve, u0, u298, h298, g298, cv
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P028, PDF page 10, Methods: "DFT datasets such as JARVIS-DFT70,71, Materials Project (MP)65, Tight binding three-body dataset (TB3)72, Quantum-Machine 9 (QM9)139,140."

## Aggregated evidence

- , PDF page 2, Results: "We train and validate ChargE3Net on a diverse set of DFT-computed charge density data, including organic molecules (QM9)54–56, nickel manganese cobalt battery cathode materials (NMC)57, and inorganic materials collected from Materials Project (MP)49,58."
- , PDF page 7, Datasets: "The QM9 dataset56 contains VASP calculations of the 133,845 small organic molecules introduced by Ramakrishnan et al.55, with training, validation, and test splits of size 123,835, 50, and 10,000 respectively."
- , PDF page 10, Methods: "DFT datasets such as JARVIS-DFT70,71, Materials Project (MP)65, Tight binding three-body dataset (TB3)72, Quantum-Machine 9 (QM9)139,140."
