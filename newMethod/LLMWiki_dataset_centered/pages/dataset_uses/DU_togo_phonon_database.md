# Dataset Use: Togo phonon database

- DatasetUse ID: `DU_togo_phonon_database`
- Dataset: Togo phonon database (`D_togo_phonon_database`)
- Papers: P027
- Usage records: 4

## Usage roles

- source
- screening
- computational_validation

## Purposes

- Source of phonon dispersion data for complex materials with large unit cells
- Complex-material test set for evaluating generalizability on large-unit-cell systems
- Validation set for assessing performance on complex materials beyond training domain
- Validation on alloy systems and high-entropy alloys using phonon data derived from Togo database or analogous DFPT/VCA methods

## Used fields

- phonon dispersion along highly symmetric paths
- POSCAR
- FORCE_SET
- phonopy.config files
- Γ-phonon spectra
- phonon dispersion at high-symmetry points
- phonon dispersion

## Construction methods

- random selection with quality filtering (lowest Γ-phonon > −0.07 cm⁻¹, >40 atoms/unit cell)
- filtered and randomly selected subset (156 materials)

## Filter conditions

- lowest Γ-phonon band > −0.07 cm⁻¹
- more than 40 atoms per unit cell
- random selection of 156 materials

## Sample counts

- 156

## Availability

- Dataset: public
- Recommendable: true

## Confidence

0.95

## Usage records

### UR_P027_01_togo_phonon_database

- Paper: `P027` — Virtual Node Graph Neural Network for Full Phonon Prediction
- Task: phonon spectra and bandstructure prediction (`T_P027_01`)
- Stage: acquisition of ab initio phonon data (`data_acquisition`, `S_P027_01`)
- Usage role: source
- Purpose: Source of phonon dispersion data for complex materials with large unit cells
- Used fields: phonon dispersion along highly symmetric paths, POSCAR, FORCE_SET, phonopy.config files
- Filter conditions: lowest Γ-phonon band > −0.07 cm⁻¹, more than 40 atoms per unit cell
- Construction method: Not stated
- Sample count: 156
- Confidence: 1.0

Evidence:
- P027, PDF page 9, Methods: "We also got phonon dispersion of complex (more number of atoms per unit cell) materials from Atsushi Togo’s phonon database31."
- P027, PDF page 9, Methods: "To quality control the data, we selected materials whose lowest Γ-phonon band is higher than −0.07 cm−1. We also ﬁltered the material to get only the ones with more than 40 atoms per unit cell. Finally, we randomly selected 156 (the same as the number of data in the testing set for ease of comparison) out of 505 ﬁltered materials. We used them as our complex material data set."

### UR_P027_02_togo_phonon_database

- Paper: `P027` — Virtual Node Graph Neural Network for Full Phonon Prediction
- Task: phonon spectra and bandstructure prediction (`T_P027_01`)
- Stage: phonon data preparation and splitting (`data_preparation`, `S_P027_02`)
- Usage role: screening
- Purpose: Complex-material test set for evaluating generalizability on large-unit-cell systems
- Used fields: phonon dispersion along highly symmetric paths, Γ-phonon spectra
- Filter conditions: lowest Γ-phonon band > −0.07 cm⁻¹, more than 40 atoms per unit cell, random selection of 156 materials
- Construction method: random selection with quality filtering (lowest Γ-phonon > −0.07 cm⁻¹, >40 atoms/unit cell)
- Sample count: 156
- Confidence: 1.0

Evidence:
- P027, PDF page 9, Methods: "To quality control the data, we selected materials whose lowest Γ-phonon band is higher than −0.07 cm−1. We also ﬁltered the material to get only the ones with more than 40 atoms per unit cell. Finally, we randomly selected 156 (the same as the number of data in the testing set for ease of comparison) out of 505 ﬁltered materials. We used them as our complex material data set."

### UR_P027_04_togo_phonon_database

- Paper: `P027` — Virtual Node Graph Neural Network for Full Phonon Prediction
- Task: phonon spectra and bandstructure prediction (`T_P027_01`)
- Stage: evaluation of phonon prediction accuracy (`model_evaluation`, `S_P027_04`)
- Usage role: computational_validation
- Purpose: Validation set for assessing performance on complex materials beyond training domain
- Used fields: Γ-phonon spectra, phonon dispersion at high-symmetry points
- Filter conditions: lowest Γ-phonon band > −0.07 cm⁻¹, more than 40 atoms per unit cell
- Construction method: filtered and randomly selected subset (156 materials)
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P027, PDF page 9, Methods: "We used them as our complex material data set."

### UR_P027_05_togo_phonon_database

- Paper: `P027` — Virtual Node Graph Neural Network for Full Phonon Prediction
- Task: phonon spectra and bandstructure prediction (`T_P027_01`)
- Stage: validation on alloy systems and complex materials (`computational_validation`, `S_P027_05`)
- Usage role: computational_validation
- Purpose: Validation on alloy systems and high-entropy alloys using phonon data derived from Togo database or analogous DFPT/VCA methods
- Used fields: phonon dispersion, Γ-phonon spectra
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 0.95

Evidence:
- P027, PDF page 6, Discussion: "Additional tests on SiGe alloys, FeCoNi alloys, and other high-energy alloys are performed, which agree well with existing literature (Supplementary Information VI)."

## Aggregated evidence

- , PDF page 9, Methods: "We also got phonon dispersion of complex (more number of atoms per unit cell) materials from Atsushi Togo’s phonon database31."
- , PDF page 9, Methods: "To quality control the data, we selected materials whose lowest Γ-phonon band is higher than −0.07 cm−1. We also ﬁltered the material to get only the ones with more than 40 atoms per unit cell. Finally, we randomly selected 156 (the same as the number of data in the testing set for ease of comparison) out of 505 ﬁltered materials. We used them as our complex material data set."
- , PDF page 9, Methods: "To quality control the data, we selected materials whose lowest Γ-phonon band is higher than −0.07 cm−1. We also ﬁltered the material to get only the ones with more than 40 atoms per unit cell. Finally, we randomly selected 156 (the same as the number of data in the testing set for ease of comparison) out of 505 ﬁltered materials. We used them as our complex material data set."
- , PDF page 9, Methods: "We used them as our complex material data set."
- , PDF page 6, Discussion: "Additional tests on SiGe alloys, FeCoNi alloys, and other high-energy alloys are performed, which agree well with existing literature (Supplementary Information VI)."
