# Dataset: Materials Project v2023.11.1 dielectric dataset

- Dataset ID: `D_materials_project_v2023_11_1_dielectric_dataset`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- Materials Project v2023.11.1 dielectric dataset
- Materials Project
- MP
- MP v2023.11.1
- Materials Project (v2023.11.1)

## Observed material scopes

- inorganic materials

## Observed research tasks

- Dielectric tensor prediction for inorganic materials

## Observed research stages

- data_acquisition
- model_evaluation

## Observed properties

- dielectric tensor
- electronic dielectric tensor
- ionic dielectric tensor
- total dielectric tensor
- band gap

## Observed fields

- structure
- atomic numbers and positions
- ε∞ij
- ε0ij
- εij
- Ehull
- Eg

## Usage evidence

- P019 (Dielectric tensor prediction for inorganic materials using latent information from preferred potential): source in Data acquisition from Materials Project — Source for acquiring training structures with dielectric constants.
- P019 (Dielectric tensor prediction for inorganic materials using latent information from preferred potential): benchmark in Benchmarking DTNet against state-of-the-art algorithms — Benchmarking DTNet against state-of-the-art algorithms.

## Dataset evidence

- P019, PDF page 3, unknown: "Data preparation. We leverage on one of the largest open databases of DFT-calculated crystal structure properties, Materials Project38, to obtain a wide range of training structures. The dataset (MP v2023.11.1) contains 7277 relaxed materials along with calculated dielectric constants."
- P019, PDF page 11, Methods: "The Materials Project (v2023.11.1) contains a dataset of 7277 dielectric tensors. The dielectric properties are calculated using the Vienna Ab-Initio Simulation Package (VASP version 5.3.4), employing the generalized gradient approximation GGA/PBE exchange-correlation functional57 with the +U correction58,59 to account for electron-electron interactions within the transition metal orbitals."
