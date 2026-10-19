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
- QM9 data set

## Observed material scopes

- molecules
- materials of technological interest

## Observed research tasks

- electron density prediction
- benchmarking of materials design methods
- accurate property prediction in both molecules and crystals

## Observed research stages

- data_acquisition
- data_preparation
- model_training
- model_evaluation
- candidate_generation

## Observed properties

- electron charge density
- energies
- internal energy at 0 K
- internal energy at room temperature
- enthalpy
- Gibbs free energy
- zero-point vibrational energy
- dipole moment
- isotropic polarizability
- electronic spatial extent
- heat capacity
- highest vibrational frequency
- HOMO energy
- LUMO energy
- band gap

## Observed fields

- atomic species
- atomic positions
- charge density grid
- energies
- atomic number
- chirality
- ring sizes
- hybridization
- acceptor
- donor
- aromatic
- bond type
- same ring
- graph distance
- expanded distance
- average atomic weight
- bonds per atom

## Usage evidence

- P025 (Higher-order equivariant neural networks for charge density prediction in materials): training in collecting DFT-computed charge density data — Train and validate ChargE3Net on organic molecules
- P028 (JARVIS-Leaderboard: a large scale benchmark of materials design methods): source in populate reference dataset — to generate a benchmark dataset with well-defined data splits
- P061 (Graph Networks as a Universal Machine Learning Framework for Molecules and Crystals): source in data collection from QM9 and Materials Project — Data collection for molecular property prediction
- P061 (Graph Networks as a Universal Machine Learning Framework for Molecules and Crystals): source in construction of crystal graphs and attribute assignment — Construction of molecular graphs with atomic, bond, and global state attributes
- P061 (Graph Networks as a Universal Machine Learning Framework for Molecules and Crystals): training in training of MEGNet models for multiple properties — Training MEGNet models for multiple molecular properties including internal energy, enthalpy, Gibbs free energy, band gap, and others
- P061 (Graph Networks as a Universal Machine Learning Framework for Molecules and Crystals): test in evaluation of model performance against benchmarks — Evaluation of MEGNet model performance against benchmarks for 13 molecular properties
- P061 (Graph Networks as a Universal Machine Learning Framework for Molecules and Crystals): training in unified free energy model development — Training unified free energy MEGNet model incorporating temperature, pressure, and entropy as global state inputs

## Dataset evidence

- P025, PDF page 2, Results: "We train and validate ChargE3Net on a diverse set of DFT-computed charge density data, including organic molecules (QM9)54–56, nickel manganese cobalt battery cathode materials (NMC)57, and inorganic materials collected from Materials Project (MP)49,58."
- P025, PDF page 7, Datasets: "The QM9 dataset56 contains VASP calculations of the 133,845 small organic molecules introduced by Ramakrishnan et al.55, with training, validation, and test splits of size 123,835, 50, and 10,000 respectively."
- P028, PDF page 10, Methods: "For atomic structure datasets, we use DFT datasets such as JARVIS-DFT70,71, Materials Project (MP)65, Tight binding three-body dataset (TB3)72, Quantum-Machine 9 (QM9)139,140."
- P118, PDF page 3: "The molecule data set used in this work is the QM9 data set33 processed by Faber et al.32 It contains the B3LYP/6-31G(2df,p)-level density functional theory (DFT) calculation results on 130 462 small organic molecules containing up to 9 heavy atoms."
