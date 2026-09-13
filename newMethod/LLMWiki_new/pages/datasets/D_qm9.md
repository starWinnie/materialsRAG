# Dataset: QM9

- Dataset ID: `D_qm9`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- QM9
- organic molecules (QM9)
- Quantum-Machine 9 (QM9)

## Observed material scopes

- molecules
- materials of technological interest

## Observed research tasks

- electron density prediction
- benchmarking of materials design methods

## Observed research stages

- data_acquisition

## Observed properties

- electron charge density
- energies

## Observed fields

- atomic species
- atomic positions
- charge density grid
- energies

## Usage evidence

- P025 (Higher-order equivariant neural networks for charge density prediction in materials): training in collecting DFT-computed charge density data — Train and validate ChargE3Net on organic molecules
- P028 (JARVIS-Leaderboard: a large scale benchmark of materials design methods): source in populate reference dataset — to generate a benchmark dataset with well-defined data splits

## Dataset evidence

- P025, PDF page 2, Results: "We train and validate ChargE3Net on a diverse set of DFT-computed charge density data, including organic molecules (QM9)54–56, nickel manganese cobalt battery cathode materials (NMC)57, and inorganic materials collected from Materials Project (MP)49,58."
- P025, PDF page 7, Datasets: "The QM9 dataset56 contains VASP calculations of the 133,845 small organic molecules introduced by Ramakrishnan et al.55, with training, validation, and test splits of size 123,835, 50, and 10,000 respectively."
- P028, PDF page 10, Methods: "For atomic structure datasets, we use DFT datasets such as JARVIS-DFT70,71, Materials Project (MP)65, Tight binding three-body dataset (TB3)72, Quantum-Machine 9 (QM9)139,140."
