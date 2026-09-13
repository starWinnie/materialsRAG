# Dataset: second-level dataset

- Dataset ID: `D_P008_second_level_dataset`
- Dataset type: `derived_subset`
- Source dataset: `D_P008_first_level_dataset`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- second-level dataset
- problem-speciﬁc clusters (C1 and C2)
- 704 materials

## Observed material scopes

- semiconductors

## Observed research tasks

- identifying semiconductors with ultralow lattice thermal conductivity

## Observed research stages

- candidate_generation
- computational_validation

## Observed properties

- κPET at 300 K
- cluster assignment (C1 or C2)

## Observed fields

- κPET
- cluster

## Usage evidence

- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): candidate_pool in unsupervised learning to identify problem-specific clusters with similar κL — group materials into clusters based on compositional and structural similarity to prioritize those likely exhibiting low κL
- P008 (Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity): source in high-throughput calculation (HTC) of κPET on problem-specific clusters — assign approximate κL labels to materials in C1 and C2 using the low-cost PET empirical model

## Dataset evidence

- P008, PDF page 4: "Since the materials with a high likelihood of possessing relatively low κL tend to group into the two clusters of C1 and C2, the exploration scope for ﬁnding materials with low κL is reduced from 2675 materials to 704 materials, narrowing by approximately three-quarters. As a result, these two problem-speciﬁc clusters (C1 and C2) further constitute our second-level dataset."
