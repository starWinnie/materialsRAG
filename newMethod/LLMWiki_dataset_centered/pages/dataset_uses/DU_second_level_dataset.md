# Dataset Use: second-level dataset

- DatasetUse ID: `DU_second_level_dataset`
- Dataset: second-level dataset (`D_second_level_dataset`)
- Papers: P008
- Usage records: 2

## Usage roles

- candidate_pool
- source

## Purposes

- Serve as the reduced search space for subsequent high-throughput calculation of κPET.
- Provide input structures for PET model-based high-throughput calculation of κPET at 300 K.

## Used fields

- structure
- composition

## Construction methods

- k-means clustering (k=7) on first-level dataset; selection of clusters C1 and C2 based on known low-κL materials

## Filter conditions

- C1 and C2 clusters

## Sample counts

- 704

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P008_03_second_level_dataset

- Paper: `P008` — Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity
- Task: identifying semiconductors with ultralow lattice thermal conductivity (`T_P008_01`)
- Stage: unsupervised learning for clustering materials with similar κL (`candidate_generation`, `S_P008_03`)
- Usage role: candidate_pool
- Purpose: Serve as the reduced search space for subsequent high-throughput calculation of κPET.
- Used fields: structure, composition
- Filter conditions: C1 and C2 clusters
- Construction method: k-means clustering (k=7) on first-level dataset; selection of clusters C1 and C2 based on known low-κL materials
- Sample count: 704
- Confidence: 1.0

Evidence:
- P008, PDF page 4: "Since the materials with a high likelihood of possessing relatively low κL tend to group into the two clusters of C1 and C2, the exploration scope for finding materials with low κL is reduced from 2675 materials to 704 materials, narrowing by approximately three-quarters. As a result, these two problem-speciﬁc clusters (C1 and C2) further constitute our second-level dataset."

### UR_P008_04_second_level_dataset

- Paper: `P008` — Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity
- Task: identifying semiconductors with ultralow lattice thermal conductivity (`T_P008_01`)
- Stage: high-throughput calculation of κPET values for second-level dataset (`label_generation`, `S_P008_04`)
- Usage role: source
- Purpose: Provide input structures for PET model-based high-throughput calculation of κPET at 300 K.
- Used fields: structure
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P008, PDF page 3, Results: "We use the phonon-elasticity-thermal (PET) model44 to perform low-cost HTC on the materials in the second-level dataset, establishing a local database based on the HTC results."

## Aggregated evidence

- , PDF page 4: "Since the materials with a high likelihood of possessing relatively low κL tend to group into the two clusters of C1 and C2, the exploration scope for finding materials with low κL is reduced from 2675 materials to 704 materials, narrowing by approximately three-quarters. As a result, these two problem-speciﬁc clusters (C1 and C2) further constitute our second-level dataset."
- , PDF page 3, Results: "We use the phonon-elasticity-thermal (PET) model44 to perform low-cost HTC on the materials in the second-level dataset, establishing a local database based on the HTC results."
