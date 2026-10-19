# Dataset: WBM Test split

- Dataset ID: `D_P110_wbm_test_split`
- Dataset type: `derived_subset`
- Source dataset: `D_open_materials_2024_omat24`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- WBM Test split
- WBM Test

## Observed material scopes

- inorganic bulk materials

## Observed research tasks

- training Machine Learning Interatomic Potentials (MLIPs) for inorganic materials

## Observed research stages

- data_preparation

## Observed properties

- energy
- forces
- cell stress

## Observed fields

- energy
- forces
- cell stress
- atomic positions
- unit cell

## Usage evidence

- P053 (Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models): test in creation of explicit training, validation and test splits — to ensure that the training dataset does not overlap with the Matbench Discovery leaderboard created from the WBM dataset

## Dataset evidence

- P110, PDF page 3: "The WBM Test split was created using the AFLOW structure prototype labels35 in the aviary package36. The prototype label of a structure is a standardized way to classify crystal structures by elemental stoichiometry, space group, Pearson symbol, and Wyckoff positions35. The split includes all OMat24 structures that were generated starting from an Alexandria relaxed structure with a prototype label matching any of prototype labels from the initial or relaxed structures included in the WBM dataset. Additionally, all OMat24 structures with a prototype label matching an initial or relaxed WBM structure are also included in the WBM Test split. The WBM Test split includes a total of 5.3 million structures."
