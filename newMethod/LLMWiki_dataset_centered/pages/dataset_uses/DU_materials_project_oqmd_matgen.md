# Dataset Use: Materials Project, OQMD, Matgen

- DatasetUse ID: `DU_materials_project_oqmd_matgen`
- Dataset: Materials Project, OQMD, Matgen (`D_materials_project_oqmd_matgen`)
- Papers: P031
- Usage records: 1

## Usage roles

- pretraining

## Purposes

- pre-training DiffCSP-SC on large-scale crystal structures to manage vast feature space

## Used fields

- 3D crystals

## Construction methods

- deduplication of crystal structures from Materials Project, OQMD, Matgen, and ICSD

## Filter conditions

- excluding molecular crystals

## Sample counts

- None stated

## Availability

- Dataset: public
- Recommendable: true

## Confidence

1.0

## Usage records

### UR_P031_03_materials_project_oqmd_matgen

- Paper: `P031` — Learning Superconductivity from Ordered and Disordered Material Structures
- Task: designing high Tc superconductors (`T_P031_01`)
- Stage: training DiffCSP-SC (`model_training`, `S_P031_03`)
- Usage role: pretraining
- Purpose: pre-training DiffCSP-SC on large-scale crystal structures to manage vast feature space
- Used fields: 3D crystals
- Filter conditions: excluding molecular crystals
- Construction method: deduplication of crystal structures from Materials Project, OQMD, Matgen, and ICSD
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P031, PDF page 7, 4.2.3 Pre-training: "We pre-trained our model on approximately 1.14 million unique 3D crystals sourced from existing databases, including Materials Project, OQMD, ICSD and Matgen."

## Aggregated evidence

- , PDF page 7, 4.2.3 Pre-training: "We pre-trained our model on approximately 1.14 million unique 3D crystals sourced from existing databases, including Materials Project, OQMD, ICSD and Matgen."
