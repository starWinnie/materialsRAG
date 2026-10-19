# Dataset: ICSD

- Dataset ID: `D_icsd`
- Dataset type: `public_database`
- Source dataset: None
- Availability: restricted
- Recommendable: true
- Confidence: 1.0

## Raw names

- ICSD
- ICSD database
- Inorganic Crystal Structure Database

## Observed material scopes

- crystal structures
- ternary inorganic crystal materials
- 20 space groups (5 crystal systems)

## Observed research tasks

- designing novel superconducting candidates
- generative design of crystal materials with symmetry constraints

## Observed research stages

- data_acquisition
- candidate_screening

## Observed properties

- structural validity
- space group
- lattice parameters
- fractional coordinates

## Observed fields

- ordered and disordered crystal structures
- chemical composition
- space group
- lattice parameter
- CIF
- element composition
- space group number
- lattice vectors
- fractional coordinates

## Usage evidence

- P031 (Learning Superconductivity from Ordered and Disordered Material Structures): source in constructing SuperCon3D dataset — source of ordered and disordered crystal structures for constructing SuperCon3D
- P031 (Learning Superconductivity from Ordered and Disordered Material Structures): candidate_pool in screening ICSD database using SODNet — screening the entire ICSD database to identify potential high-Tc superconductor candidates using trained SODNet
- P047 (PHYSICS GUIDED DEEP LEARNING FOR GENERATIVE DESIGN OF CRYSTAL MATERIALS WITH SYMMETRY CONSTRAINTS): source in collecting material data from MP, ICSD and OQMD — source database for curating ternary materials with 20 space groups

## Dataset evidence

- P031, PDF page 7, 5.1.1 SuperCon3D dataset.: "Additionally, over 200,000 ordered and disordered crystal structures were gathered from the ICSD database [3]."
- P031, PDF page 7, 5.1.1 SuperCon3D dataset.: "We then matched these 11,949 SuperCon entries with 208,425 ICSD entries based on chemical composition, space group and lattice parameter."
- P104, PDF page 3, Results and Discussion: "We collect our material data from MP [4], ICSD [1] and OQMD (v1.4) [5]. In total, 42,072 ternary materials with 20 space groups (5 crystal systems) are curated when we start this project..."
