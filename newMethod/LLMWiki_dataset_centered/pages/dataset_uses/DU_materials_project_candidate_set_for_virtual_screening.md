# Dataset Use: Materials Project candidate set for virtual screening

- DatasetUse ID: `DU_materials_project_candidate_set_for_virtual_screening`
- Dataset: Materials Project candidate set for virtual screening (`D_materials_project_candidate_set_for_virtual_screening`)
- Papers: P019
- Usage records: 2

## Usage roles

- candidate_pool
- computational_validation

## Purposes

- Virtual screening of thermodynamically stable non-metal materials
- DFPT validation of top candidates identified through virtual screening

## Used fields

- structure
- Ehull

## Construction methods

- Selecting non-metal materials with Ehull = 0 from MP database

## Filter conditions

- Ehull = 0
- non-metal materials

## Sample counts

- 14375

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

0.95

## Usage records

### UR_P019_05_materials_project_candidate_set_for_virtual_screening

- Paper: `P019` — Dielectric tensor prediction for inorganic materials using latent information from preferred potential
- Task: Dielectric tensor prediction for inorganic materials (`T_P019_01`)
- Stage: Preparation of candidate structures for virtual screening (`candidate_generation`, `S_P019_05`)
- Usage role: candidate_pool
- Purpose: Virtual screening of thermodynamically stable non-metal materials
- Used fields: structure, Ehull
- Filter conditions: Ehull = 0, non-metal materials
- Construction method: Selecting non-metal materials with Ehull = 0 from MP database
- Sample count: 14375
- Confidence: 1.0

Evidence:
- P019, PDF page 8, unknown: "To prepare the candidate set for screening, we downloaded 14,375 non-metal materials from the MP database. These materials are specifically selected based on the energy above convex hull Ehull = 0 to estimate their thermodynamic stability, so that only stable materials are included in the candidate set."

### UR_P019_07_materials_project_candidate_set_for_virtual_screening

- Paper: `P019` — Dielectric tensor prediction for inorganic materials using latent information from preferred potential
- Task: Dielectric tensor prediction for inorganic materials (`T_P019_01`)
- Stage: DFPT validation of screened candidates (`computational_validation`, `S_P019_07`)
- Usage role: computational_validation
- Purpose: DFPT validation of top candidates identified through virtual screening
- Used fields: structure
- Filter conditions: Ehull = 0, non-metal materials
- Construction method: Selecting non-metal materials with Ehull = 0 from MP database
- Sample count: Not stated
- Confidence: 0.95

Evidence:
- P019, PDF page 9, unknown: "To validate the promising materials identiﬁed by DTNet, we conducted a three-round active exploration, with each round proposing 20 top candidates for validation."

## Aggregated evidence

- , PDF page 8, unknown: "To prepare the candidate set for screening, we downloaded 14,375 non-metal materials from the MP database. These materials are specifically selected based on the energy above convex hull Ehull = 0 to estimate their thermodynamic stability, so that only stable materials are included in the candidate set."
- , PDF page 9, unknown: "To validate the promising materials identiﬁed by DTNet, we conducted a three-round active exploration, with each round proposing 20 top candidates for validation."
