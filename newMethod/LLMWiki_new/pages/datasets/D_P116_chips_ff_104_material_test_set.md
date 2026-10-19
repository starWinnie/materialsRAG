# Dataset: CHIPS-FF 104-material test set

- Dataset ID: `D_P116_chips_ff_104_material_test_set`
- Dataset type: `derived_subset`
- Source dataset: `D_jarvis_dft`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- CHIPS-FF 104-material test set
- set of 104 materials
- test set of 104 materials
- 104 structures

## Observed material scopes

- metals
- semiconductors
- insulators

## Observed research tasks

- benchmarking machine learning force fields (MLFFs)

## Observed research stages

- data_preparation
- computational_validation

## Observed properties

- lattice parameters
- elastic tensor
- phonon band structure
- surface energy
- vacancy formation energy
- work of adhesion
- radial distribution function

## Observed fields

- lattice constants a, b, c
- volume
- bulk modulus
- C11
- C44
- phonon band structure
- surface energy
- vacancy formation energy
- work of adhesion
- radial distribution function

## Usage evidence

- P059 (CHIPS-FF: Evaluating Universal Machine Learning Force Fields for Material Properties): candidate_pool in generating supercell structures for surfaces and defects — generate supercell structures for surfaces, defects, and interfaces
- P059 (CHIPS-FF: Evaluating Universal Machine Learning Force Fields for Material Properties): benchmark in computing material properties and error metrics — compute and evaluate target properties (elastic tensor, phonons, surface energy, vacancy formation, work of adhesion, RDF) using uMLFFs

## Dataset evidence

- P116, PDF page 3: "For our benchmarking study, we chose a set of 104 materials most commonly found in semiconductor devices and interfaces. This test set contains metals, semiconductors and insulators to be representative of the various parts and interfaces of integrated circuits."
- P116, PDF page 3: "For each of the 104 structures, we performed structural relaxations, fitting of the energy vs volume curve (equation of state), calculation of the elastic tensor, calculation of the phonon band structure, relaxation of all nonpolar surfaces..., and relaxation of each type of point defect in the material."
