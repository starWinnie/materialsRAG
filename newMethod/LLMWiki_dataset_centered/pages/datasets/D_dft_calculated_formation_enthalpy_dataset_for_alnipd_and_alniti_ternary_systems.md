# Dataset: DFT-calculated formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems

- Dataset ID: `D_dft_calculated_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 0.97

## Raw names

- DFT-calculated formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems
- DFT-calculated formation enthalpies
- HDFT
- DFT total energy
- DFT-calculated and experimentally measured enthalpies
- DFT-calculated heat of formation values

## Observed material scopes

- Al–Ni–Pd system
- Al–Ni–Ti system
- binary alloys
- ternary alloys
- intermetallic compounds

## Observed research tasks

- correcting DFT-calculated formation enthalpy errors

## Observed research stages

- label_generation
- model_training
- model_evaluation

## Observed properties

- formation enthalpy

## Observed fields

- chemical formula
- elemental concentrations
- DFT formation enthalpy

## Usage evidence

- P043 (Machine learning for improved density functional theory thermodynamics): source in calculating enthalpy correction labels (Hcorr) — Compute enthalpy correction labels Hcorr = HDFT − Hexpt.
- P043 (Machine learning for improved density functional theory thermodynamics): training in training neural network regressor — Provide input features (via derived Hcorr labels) for supervised training of the neural network regressor.
- P043 (Machine learning for improved density functional theory thermodynamics): test in evaluating model performance with cross-validation — Evaluate model performance via cross-validation on held-out data (to compute Hpred and compare against Hexpt).

## Dataset evidence

- P043, PDF page 1: "A neural network model has been trained to predict the discrepancy between DFT-calculated and experimentally measured enthalpies for binary and ternary alloys and compounds."
- P043, PDF page 4, Results and discussion: "We have performed DFT calculations, as described above, for all the known enthalpies of formation of the two ternary phase diagrams, for Al–Ni–Pd and Al–Ni–Ti, at ambient conditions, resulting in a total of 34 systems."
- P043, PDF page 4: "The total DFT corrected enthalpy is given by  Hpred = HDFT − Hcorr,"
