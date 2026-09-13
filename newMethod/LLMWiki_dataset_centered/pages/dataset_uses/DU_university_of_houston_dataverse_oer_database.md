# Dataset Use: University of Houston Dataverse OER database

- DatasetUse ID: `DU_university_of_houston_dataverse_oer_database`
- Dataset: University of Houston Dataverse OER database (`D_university_of_houston_dataverse_oer_database`)
- Papers: P038
- Usage records: 3

## Usage roles

- computational_validation
- screening

## Purposes

- Primary database used for high-throughput screening and nanoscale stability assessment.
- Used as input to the high-throughput screening framework applying progressive criteria (bulk Pourbaix stability, Wulff shape, overpotential, energy above hull, material cost).
- Used to compute nanoparticle formation energy (GNP_f) for nanoscale stability assessment.

## Used fields

- overpotential
- EPBX
- GNP_f
- Wulff_shape
- material_cost
- e_above_hull

## Construction methods

- Interpolated using fine-tuned OC22 S2EF-Total model on 4119-oxide subset; includes 6,068,572 total energy predictions.

## Filter conditions

- EPBX ≤ 0.5 eV/atom
- η < 0.75 V
- Ehull ≤ 0.1 eV/atom
- material cost < $8346/kg
- 10–100 nm nanoparticle radius

## Sample counts

- 190
- 886
- 6068572

## Availability

- Dataset: public
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P038_04_university_of_houston_dataverse_oer_database

- Paper: `P038` — Rational design of nanoscale stabilized oxide catalysts for OER with OC22
- Task: Rational design of nanoscale stabilized oxide catalysts for OER (`T_P038_01`)
- Stage: Interpolation of total energies for OER intermediates (`candidate_generation`, `S_P038_04`)
- Usage role: computational_validation
- Purpose: Primary database used for high-throughput screening and nanoscale stability assessment.
- Used fields: overpotential, EPBX, GNP_f, Wulff_shape, material_cost
- Filter conditions: Not stated
- Construction method: Interpolated using fine-tuned OC22 S2EF-Total model on 4119-oxide subset; includes 6,068,572 total energy predictions.
- Sample count: 6068572
- Confidence: 1.0

Evidence:
- P038, PDF page 5, unknown: "Table 1 Summary of database scope Predictions: 6068572 Materials: 4119 Ave. # slabs per material: 47 OH* O* OOH* * 1,972,166 667,266 3,237,238 191,902"

### UR_P038_05_university_of_houston_dataverse_oer_database

- Paper: `P038` — Rational design of nanoscale stabilized oxide catalysts for OER with OC22
- Task: Rational design of nanoscale stabilized oxide catalysts for OER (`T_P038_01`)
- Stage: High-throughput screening with progressive criteria (`candidate_screening`, `S_P038_05`)
- Usage role: screening
- Purpose: Used as input to the high-throughput screening framework applying progressive criteria (bulk Pourbaix stability, Wulff shape, overpotential, energy above hull, material cost).
- Used fields: overpotential, EPBX, e_above_hull, material_cost
- Filter conditions: EPBX ≤ 0.5 eV/atom, η < 0.75 V, Ehull ≤ 0.1 eV/atom, material cost < $8346/kg
- Construction method: Not stated
- Sample count: 190
- Confidence: 1.0

Evidence:
- P038, PDF page 8, 3.4 Alternative screening frameworks: "In total we have identified 190 candidates (122 bulk – and 68 nanostable) with 145 distinct chemical systems when considering all the different screening frameworks listed in Table 2."

### UR_P038_06_university_of_houston_dataverse_oer_database

- Paper: `P038` — Rational design of nanoscale stabilized oxide catalysts for OER with OC22
- Task: Rational design of nanoscale stabilized oxide catalysts for OER (`T_P038_01`)
- Stage: Nanoscale stability assessment via nanoparticle formation energy (`computational_validation`, `S_P038_06`)
- Usage role: computational_validation
- Purpose: Used to compute nanoparticle formation energy (GNP_f) for nanoscale stability assessment.
- Used fields: EPBX, GNP_f, Wulff_shape
- Filter conditions: 10–100 nm nanoparticle radius
- Construction method: Not stated
- Sample count: 886
- Confidence: 1.0

Evidence:
- P038, PDF page 8, 3.4 Alternative screening frameworks: "Using our nanoscale stability diagrams (see Fig. 2), we were able to identify 2778 Pourbaix stable materials with 886 stabilizing at the nanoscale regime (10 to 100 nm)."

## Aggregated evidence

- , PDF page 5, unknown: "Table 1 Summary of database scope Predictions: 6068572 Materials: 4119 Ave. # slabs per material: 47 OH* O* OOH* * 1,972,166 667,266 3,237,238 191,902"
- , PDF page 8, 3.4 Alternative screening frameworks: "In total we have identified 190 candidates (122 bulk – and 68 nanostable) with 145 distinct chemical systems when considering all the different screening frameworks listed in Table 2."
- , PDF page 8, 3.4 Alternative screening frameworks: "Using our nanoscale stability diagrams (see Fig. 2), we were able to identify 2778 Pourbaix stable materials with 886 stabilizing at the nanoscale regime (10 to 100 nm)."
