# Dataset Use: first-level dataset

- DatasetUse ID: `DU_first_level_dataset`
- Dataset: first-level dataset (`D_first_level_dataset`)
- Papers: P008
- Usage records: 2

## Usage roles

- candidate_pool
- source

## Purposes

- Serve as the filtered input for unsupervised clustering after applying thermodynamic, electronic, structural, and compositional criteria.
- Provide featurized input (composition + structure descriptors) for k-means clustering to identify problem-specific clusters.

## Used fields

- Ehull
- Eg
- Natoms
- Nelements
- structure
- composition

## Construction methods

- Filtering MP database on Ehull ≤ 0.05 eV/atom, 0.1 eV ≤ Eg ≤ 2 eV, Natoms < 20, Nelements < 4, excluding H/lanthanides/actinides

## Filter conditions

- Ehull ≤ 0.05 eV/atom
- 0.1 eV ≤ Eg ≤ 2 eV
- Natoms < 20
- Nelements < 4
- exclude H, lanthanides, actinides

## Sample counts

- 2675

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P008_02_first_level_dataset

- Paper: `P008` — Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity
- Task: identifying semiconductors with ultralow lattice thermal conductivity (`T_P008_01`)
- Stage: preliminary high-throughput screening (`data_preparation`, `S_P008_02`)
- Usage role: candidate_pool
- Purpose: Serve as the filtered input for unsupervised clustering after applying thermodynamic, electronic, structural, and compositional criteria.
- Used fields: Ehull, Eg, Natoms, Nelements, structure
- Filter conditions: Ehull ≤ 0.05 eV/atom, 0.1 eV ≤ Eg ≤ 2 eV, Natoms < 20, Nelements < 4, exclude H, lanthanides, actinides
- Construction method: Filtering MP database on Ehull ≤ 0.05 eV/atom, 0.1 eV ≤ Eg ≤ 2 eV, Natoms < 20, Nelements < 4, excluding H/lanthanides/actinides
- Sample count: 2675
- Confidence: 1.0

Evidence:
- P008, PDF page 3, Preliminary high-throughput screening: "Ultimately, through excluding the materials containing hydrogen, lanthanides, and actinides, and conducting structural analysis, we further obtain 2675 three-dimensional (3D) crystal structures without calculation errors. These materials constitute the first-level dataset for our in-depth investigations."

### UR_P008_03_first_level_dataset

- Paper: `P008` — Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity
- Task: identifying semiconductors with ultralow lattice thermal conductivity (`T_P008_01`)
- Stage: unsupervised learning for clustering materials with similar κL (`candidate_generation`, `S_P008_03`)
- Usage role: source
- Purpose: Provide featurized input (composition + structure descriptors) for k-means clustering to identify problem-specific clusters.
- Used fields: structure, composition
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P008, PDF page 3, Unsupervised learning for identifying materials with similar κL: "Following the generation of the first-level dataset as input, the materials should be transformed into the length-fixed vectors as the so-called descriptors... composition-based features and structure-based features... each material can generate a total of 273 descriptors automatically..."

## Aggregated evidence

- , PDF page 3, Preliminary high-throughput screening: "Ultimately, through excluding the materials containing hydrogen, lanthanides, and actinides, and conducting structural analysis, we further obtain 2675 three-dimensional (3D) crystal structures without calculation errors. These materials constitute the first-level dataset for our in-depth investigations."
- , PDF page 3, Unsupervised learning for identifying materials with similar κL: "Following the generation of the first-level dataset as input, the materials should be transformed into the length-fixed vectors as the so-called descriptors... composition-based features and structure-based features... each material can generate a total of 273 descriptors automatically..."
