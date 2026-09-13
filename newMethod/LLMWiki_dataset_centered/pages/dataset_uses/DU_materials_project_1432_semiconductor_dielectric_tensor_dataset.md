# Dataset Use: Materials Project 1432-semiconductor dielectric tensor dataset

- DatasetUse ID: `DU_materials_project_1432_semiconductor_dielectric_tensor_dataset`
- Dataset: Materials Project 1432-semiconductor dielectric tensor dataset (`D_materials_project_1432_semiconductor_dielectric_tensor_dataset`)
- Papers: P003
- Usage records: 5

## Usage roles

- source
- training
- validation
- computational_validation

## Purposes

- ab initio calculation of frequency-dependent dielectric tensors via OpenMX and Kubo formula
- spherical-harmonics decomposition of Cartesian dielectric tensors into ℓ=0 and ℓ=2 channels
- training TSENN to predict ℓ=0 and ℓ=2 spherical-harmonics coefficients from crystal graphs
- evaluation of dielectric tensor prediction accuracy using MAE and other metrics on full-tensor and per-component levels
- Kramers–Kronig reconstruction of real parts from predicted imaginary parts and symmetry validation via masking

## Used fields

- crystal structure
- bandgap
- energy above hull
- space group
- dielectric tensor (real and imaginary parts)
- spherical-harmonics coefficients (ℓ=0 and ℓ=2)
- predicted dielectric tensors
- ground-truth dielectric tensors
- predicted imaginary dielectric spectra
- ground-truth dielectric tensors (for symmetry validation)

## Construction methods

- selection from Materials Project based on bandgap (0.3–3 eV), energy above hull (<0.02 eV/atom), element count (<3), atom count per unit cell (<10), exclusion of magnetic materials and f-element-containing materials; symmetrization of structures; first-principles DFT calculations using OpenMX; dielectric tensors computed via Kubo formula over 0–30 eV at 0.01 eV resolution

## Filter conditions

- bandgap between 0.3 and 3 eV
- energy above hull < 0.02 eV/atom
- fewer than three elements
- fewer than ten atoms per unit cell
- nonmagnetic
- no f-electron elements

## Sample counts

- 1432

## Availability

- Dataset: public
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P003_01_materials_project_1432_semiconductor_dielectric_tensor_dataset

- Paper: `P003` — Accurate prediction of tensorial spectra using equivariant graph neural network
- Task: prediction of tensorial spectra (`T_P003_01`)
- Stage: ab initio calculations of dielectric tensors (`data_acquisition`, `S_P003_01`)
- Usage role: source
- Purpose: ab initio calculation of frequency-dependent dielectric tensors via OpenMX and Kubo formula
- Used fields: crystal structure, bandgap, energy above hull, space group
- Filter conditions: bandgap between 0.3 and 3 eV, energy above hull < 0.02 eV/atom, fewer than three elements, fewer than ten atoms per unit cell, nonmagnetic, no f-electron elements
- Construction method: selection from Materials Project based on bandgap (0.3–3 eV), energy above hull (<0.02 eV/atom), element count (<3), atom count per unit cell (<10), exclusion of magnetic materials and f-element-containing materials; symmetrization of structures; first-principles DFT calculations using OpenMX; dielectric tensors computed via Kubo formula over 0–30 eV at 0.01 eV resolution
- Sample count: 1432
- Confidence: 1.0

Evidence:
- P003, PDF page 2, Results: "We demonstrate the capabilities of TSENN by considering the frequency-dependent dielectric tensors of a dataset of 1432 nonmagnetic semiconductors calculated via first-principles methods using OpenMX."
- P003, PDF page 2, Results: "With our focus on small bandgap semiconductors in mind, we selected materials from the Materials Project41 with bandgaps ranging from 0.3 to 3 eV... To maintain structural stability, we imposed an energy-above-hull threshold of 0.02 eV/atom. For computational efficiency, we limited our selection to materials with fewer than three elements and fewer than ten atoms per unit cell. Additionally, we excluded magnetic materials as well as materials containing elements with f electrons..."
- P003, PDF page 2, Results: "For each entry, we first symmetrized the structure by following the procedure of ref. 44 and performed first-principles calculations using OpenMX. The dielectric tensors were computed using the Kubo formula for photon energies ranging from 0 to 30 eV, with an increment of 0.01 eV, resulting in 1432 frequency-dependent dielectric tensors satisfying the symmetry constraints of the crystal systems considered."

### UR_P003_02_materials_project_1432_semiconductor_dielectric_tensor_dataset

- Paper: `P003` — Accurate prediction of tensorial spectra using equivariant graph neural network
- Task: prediction of tensorial spectra (`T_P003_01`)
- Stage: spherical-harmonics decomposition of dielectric tensors (`data_preparation`, `S_P003_02`)
- Usage role: source
- Purpose: spherical-harmonics decomposition of Cartesian dielectric tensors into ℓ=0 and ℓ=2 channels
- Used fields: dielectric tensor (real and imaginary parts)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P003, PDF page 2, Results: "To predict the dielectric tensor using an equivariant neural network, we express it in the spherical-harmonics basis, which naturally encodes rotational symmetry. The dielectric tensor is symmetric under the permutation of Cartesian indices, εij = εji, and therefore admits the decomposition εij = Tαβ Y α 1 Y β 1 = ε(0)  ε(2) = ∑ ‘2f0, 2g ∑ ‘ m = ‘ εm (‘) Y m ‘ , (1) which separates the scalar trace component (ℓ= 0) from the traceless symmetric tensor component (ℓ= 2)."
- P003, PDF page 2, Results: "Since we are dealing with frequency-dependent tensors, we take the Cartesian tensor at each photon energy, perform this change-of-basis operation, and obtain the frequency-dependent spherical-harmonic coefficients as our target, as shown in Fig. 2."

### UR_P003_03_materials_project_1432_semiconductor_dielectric_tensor_dataset

- Paper: `P003` — Accurate prediction of tensorial spectra using equivariant graph neural network
- Task: prediction of tensorial spectra (`T_P003_01`)
- Stage: training TSENN on spherical-harmonics coefficients (`model_training`, `S_P003_03`)
- Usage role: training
- Purpose: training TSENN to predict ℓ=0 and ℓ=2 spherical-harmonics coefficients from crystal graphs
- Used fields: crystal structure, spherical-harmonics coefficients (ℓ=0 and ℓ=2)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P003, PDF page 2, Results: "By training TSENN on the aforementioned dataset, we achieve a mean absolute error (MAE) of 0.127 in the predicted imaginary part of the dielectric tensor."
- P003, PDF page 3, unknown: "To train the model, we define a composite loss function L, which separately evaluates the scalar and tensor components of the predicted optical spectra."

### UR_P003_04_materials_project_1432_semiconductor_dielectric_tensor_dataset

- Paper: `P003` — Accurate prediction of tensorial spectra using equivariant graph neural network
- Task: prediction of tensorial spectra (`T_P003_01`)
- Stage: evaluation of dielectric tensor prediction accuracy (`model_evaluation`, `S_P003_04`)
- Usage role: validation
- Purpose: evaluation of dielectric tensor prediction accuracy using MAE and other metrics on full-tensor and per-component levels
- Used fields: predicted dielectric tensors, ground-truth dielectric tensors
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P003, PDF page 4, unknown: "To evaluate the model’s performance, the most direct measure is the MAE of the dielectric tensor, MAE = 1 6nω ∑ ω ∑ α ≤β |bε αβ(ω) − εαβ(ω)|."

### UR_P003_05_materials_project_1432_semiconductor_dielectric_tensor_dataset

- Paper: `P003` — Accurate prediction of tensorial spectra using equivariant graph neural network
- Task: prediction of tensorial spectra (`T_P003_01`)
- Stage: Kramers–Kronig reconstruction and symmetry validation (`computational_validation`, `S_P003_05`)
- Usage role: computational_validation
- Purpose: Kramers–Kronig reconstruction of real parts from predicted imaginary parts and symmetry validation via masking
- Used fields: predicted imaginary dielectric spectra, ground-truth dielectric tensors (for symmetry validation)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P003, PDF page 6, unknown: "With the accurately predicted imaginary parts, we used K–K relations to obtain the real parts of the dielectric tensors."
- P003, PDF page 8, unknown: "To further confirm symmetry preservation, we applied a symmetry-based masking procedure to the predicted tensor at each photon energy."

## Aggregated evidence

- , PDF page 2, Results: "We demonstrate the capabilities of TSENN by considering the frequency-dependent dielectric tensors of a dataset of 1432 nonmagnetic semiconductors calculated via first-principles methods using OpenMX."
- , PDF page 2, Results: "With our focus on small bandgap semiconductors in mind, we selected materials from the Materials Project41 with bandgaps ranging from 0.3 to 3 eV... To maintain structural stability, we imposed an energy-above-hull threshold of 0.02 eV/atom. For computational efficiency, we limited our selection to materials with fewer than three elements and fewer than ten atoms per unit cell. Additionally, we excluded magnetic materials as well as materials containing elements with f electrons..."
- , PDF page 2, Results: "For each entry, we first symmetrized the structure by following the procedure of ref. 44 and performed first-principles calculations using OpenMX. The dielectric tensors were computed using the Kubo formula for photon energies ranging from 0 to 30 eV, with an increment of 0.01 eV, resulting in 1432 frequency-dependent dielectric tensors satisfying the symmetry constraints of the crystal systems considered."
- , PDF page 2, Results: "To predict the dielectric tensor using an equivariant neural network, we express it in the spherical-harmonics basis, which naturally encodes rotational symmetry. The dielectric tensor is symmetric under the permutation of Cartesian indices, εij = εji, and therefore admits the decomposition εij = Tαβ Y α 1 Y β 1 = ε(0)  ε(2) = ∑ ‘2f0, 2g ∑ ‘ m = ‘ εm (‘) Y m ‘ , (1) which separates the scalar trace component (ℓ= 0) from the traceless symmetric tensor component (ℓ= 2)."
- , PDF page 2, Results: "Since we are dealing with frequency-dependent tensors, we take the Cartesian tensor at each photon energy, perform this change-of-basis operation, and obtain the frequency-dependent spherical-harmonic coefficients as our target, as shown in Fig. 2."
- , PDF page 2, Results: "By training TSENN on the aforementioned dataset, we achieve a mean absolute error (MAE) of 0.127 in the predicted imaginary part of the dielectric tensor."
- , PDF page 3, unknown: "To train the model, we define a composite loss function L, which separately evaluates the scalar and tensor components of the predicted optical spectra."
- , PDF page 4, unknown: "To evaluate the model’s performance, the most direct measure is the MAE of the dielectric tensor, MAE = 1 6nω ∑ ω ∑ α ≤β |bε αβ(ω) − εαβ(ω)|."
- , PDF page 6, unknown: "With the accurately predicted imaginary parts, we used K–K relations to obtain the real parts of the dielectric tensors."
- , PDF page 8, unknown: "To further confirm symmetry preservation, we applied a symmetry-based masking procedure to the predicted tensor at each photon energy."
