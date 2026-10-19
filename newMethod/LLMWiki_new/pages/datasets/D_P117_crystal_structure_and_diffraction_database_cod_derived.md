# Dataset: Crystal Structure and Diffraction Database (COD-derived)

- Dataset ID: `D_P117_crystal_structure_and_diffraction_database_cod_derived`
- Dataset type: `derived_subset`
- Source dataset: `D_crystallography_open_database`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- Crystal Structure and Diffraction Database (COD-derived)
- crystal structure database
- Crystal Structure and Diffraction database
- large-scale crystal structure database[51]
- experimental crystal structures

## Observed material scopes

- condensed matter materials
- crystal structures

## Observed research tasks

- deep fusion of experimental and theoretical data in condensed matter physics

## Observed research stages

- data_acquisition
- data_preparation
- candidate_generation
- candidate_screening
- computational_validation

## Observed properties

- crystal structures
- diffraction patterns

## Observed fields

- chemical formula
- space group
- lattice parameters
- atomic positions
- diffraction data

## Usage evidence

- P060 (MaterialsGalaxy: A Platform Fusing Experimental and Theoretical Data in Condensed Matter Physics): source in Data Acquisition and Standardization Layer — serving as the experimental cornerstone of the collection, providing nearly 500,000 crystal structure entries for ingestion and harmonization
- P060 (MaterialsGalaxy: A Platform Fusing Experimental and Theoretical Data in Condensed Matter Physics): training in Data Standardization — providing standardized crystal structures for canonical representation and symmetry resolution using pymatgen and spglib
- P060 (MaterialsGalaxy: A Platform Fusing Experimental and Theoretical Data in Condensed Matter Physics): candidate_pool in Structure vectorization — providing standardized crystal structures for transformation into structural fingerprints using SiteStatsFingerprint featurizer
- P060 (MaterialsGalaxy: A Platform Fusing Experimental and Theoretical Data in Condensed Matter Physics): screening in Vector database and similarity search — enabling high-speed similarity searches to dynamically link disparate data records based on structural fingerprints
- P060 (MaterialsGalaxy: A Platform Fusing Experimental and Theoretical Data in Condensed Matter Physics): computational_validation in Application example: Data fusion for CrGeTe3 — providing experimental crystal structure for horizontal integration with theoretical electronic band structure in CrGeTe3 case study

## Dataset evidence

- P117, PDF page 3, Data Sources and Integration Strategy: "The experimental cornerstone of our collection is a large-scale crystal structure database[51] comprising nearly 500,000 entries derived from the Crystallography Open Database (COD)[2, 3] and supplemented by literature mining."
