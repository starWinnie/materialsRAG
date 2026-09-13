# Dataset: second-level dataset

- Dataset ID: `D_second_level_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_first_level_dataset`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- second-level dataset
- C1 and C2
- 704 materials

## Observed material scopes

- semiconductors

## Observed research tasks

- identifying semiconductors with ultralow lattice thermal conductivity

## Observed research stages

- candidate_generation
- label_generation

## Observed properties

- Ehull
- Eg
- Natoms
- Nelements
- structure

## Observed fields

- Ehull
- Eg
- Natoms
- Nelements
- structure

## Usage evidence

- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): candidate_pool in unsupervised learning for clustering materials with similar κL — Serve as the reduced search space for subsequent high-throughput calculation of κPET.
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): source in high-throughput calculation of κPET values for second-level dataset — Provide input structures for PET model-based high-throughput calculation of κPET at 300 K.

## Dataset evidence

- P008, PDF page 4: "Since the materials with a high likelihood of possessing relatively low κL tend to group into the two clusters of C1 and C2, the exploration scope for finding materials with low κL is reduced from 2675 materials to 704 materials, narrowing by approximately three-quarters. As a result, these two problem-speciﬁc clusters (C1 and C2) further constitute our second-level dataset."
