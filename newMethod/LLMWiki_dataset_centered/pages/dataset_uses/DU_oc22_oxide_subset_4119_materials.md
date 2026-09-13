# Dataset Use: OC22 oxide subset (4119 materials)

- DatasetUse ID: `DU_oc22_oxide_subset_4119_materials`
- Dataset: OC22 oxide subset (4119 materials) (`D_oc22_oxide_subset_4119_materials`)
- Papers: P038
- Usage records: 1

## Usage roles

- candidate_pool

## Purposes

- Source of 4119 oxide materials for interpolation of slab and OER intermediate total energies.

## Used fields

- slab_structure
- intermediate

## Construction methods

- Subset of OC22 restricted to 4119 in-domain oxides with unit cells < 100 atoms; excludes 609 materials due to convergence issues.

## Filter conditions

- in-domain materials observed during OC22 training
- unit cell < 100 atoms
- slab atom count ≤ 200

## Sample counts

- 4119

## Availability

- Dataset: public
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P038_04_oc22_oxide_subset_4119_materials

- Paper: `P038` — Rational design of nanoscale stabilized oxide catalysts for OER with OC22
- Task: Rational design of nanoscale stabilized oxide catalysts for OER (`T_P038_01`)
- Stage: Interpolation of total energies for OER intermediates (`candidate_generation`, `S_P038_04`)
- Usage role: candidate_pool
- Purpose: Source of 4119 oxide materials for interpolation of slab and OER intermediate total energies.
- Used fields: slab_structure, intermediate
- Filter conditions: in-domain materials observed during OC22 training, unit cell < 100 atoms, slab atom count ≤ 200
- Construction method: Subset of OC22 restricted to 4119 in-domain oxides with unit cells < 100 atoms; excludes 609 materials due to convergence issues.
- Sample count: 4119
- Confidence: 1.0

Evidence:
- P038, PDF page 1, Introduction: "In this work, we interpolated a database of the total energy predictions for all slabs and OER surface intermediates for 4119 oxide materials in the original OC22 dataset using pre-trained models from the OC22 framework."

## Aggregated evidence

- , PDF page 1, Introduction: "In this work, we interpolated a database of the total energy predictions for all slabs and OER surface intermediates for 4119 oxide materials in the original OC22 dataset using pre-trained models from the OC22 framework."
