# Dataset: Alexandria

- Dataset ID: `D_alexandria`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Alexandria
- Alexandria PBE bulk materials dataset
- Alexandria dataset

## Observed material scopes

- inorganic materials
- crystals
- bulk crystalline materials
- inorganic bulk materials

## Observed research tasks

- training Machine Learning Interatomic Potentials (MLIPs) for inorganic materials
- developing universal interatomic potentials for atomistic modelling of materials

## Observed research stages

- data_acquisition

## Observed properties

- energies
- forces
- stresses
- optimization trajectories
- energy
- cell stress

## Observed fields

- energies
- forces
- stresses
- optimization trajectories
- energy
- cell stress
- atomic positions
- unit cell

## Usage evidence

- P053 (Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models): source in generation of diverse non-equilibrium structures via Boltzmann sampling, AIMD, and rattled relaxations — to obtain diverse non-equilibrium structures by sampling relaxed structures as input for Boltzmann sampling, AIMD, and rattled relaxations
- P063 (Orb: A Fast, Scalable Neural Network Potential): training in combining MPtraj and Alexandria datasets for finetuning — to obtain high-quality, consistent data for finetuning a universal interatomic potential

## Dataset evidence

- P120, PDF page 5, Datasets: "In comparison, for finetuning a UIP, data quality and consistency is of critical importance. Here, we follow previous work [62, 44] in combining MPtraj, the dataset constructed from the Materials Project and used to train CHGNet [38], with Alexandria [45], as both use PBE exchange-correlation functionals; Hubbard U corrections for transition metal oxides; no additional dispersion correction; and the same DFT software implementation (VASP) for geometry optimization."
- P110, PDF page 10, 4.1 OMat24 structure generation and sampling: "Input structure generation for the OMat24 dataset consists of three different processes intended to obtain diverse non-equilibrium structures: Boltzmann sampling of rattled (random Gaussian perturbations of atomic positions) structures, ab initio molecular dynamics (AIMD), and relaxations of rattled structures. In all three approaches, initial structures were obtained by randomly sampling the relaxed structures in the Alexandria PBE bulk materials dataset (3D compounds)20."
- P110, PDF page 10, 4.1 OMat24 structure generation and sampling: "The Alexandria dataset was chosen as a starting point because it was the largest openly available DFT dataset of equilibrium and near equilibrium structures (∼4.5 million materials)."
