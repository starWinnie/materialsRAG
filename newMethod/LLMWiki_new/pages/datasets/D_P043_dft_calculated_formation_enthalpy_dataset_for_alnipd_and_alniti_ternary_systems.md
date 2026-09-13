# Dataset: DFT-calculated formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems

- Dataset ID: `D_P043_dft_calculated_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 0.98

## Raw names

- DFT-calculated formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems
- DFT-calculated formation enthalpies
- HDFT
- DFT total energy
- heat of formation [...] calculated at the theoretical equilibrium volume

## Observed material scopes

- Al–Ni–Pd system
- Al–Ni–Ti system
- ternary alloys
- binary alloys
- intermetallic compounds

## Observed research tasks

- ML-based correction of DFT formation enthalpy errors for improved phase stability prediction

## Observed research stages

- model_training

## Observed properties

- formation enthalpy (Hf)
- total energy
- equilibrium lattice parameter
- atomic volume

## Observed fields

- chemical formula
- elemental concentrations
- ground-state structure
- DFT-calculated formation enthalpy (HDFT)

## Usage evidence

- P043 (Machine learning for improved density functional theory thermodynamics): source in Supervised training of neural network regressor — Provide DFT-calculated formation enthalpies (HDFT) to compute Hcorr labels and later generate Hpred = HDFT − Hcorr

## Dataset evidence

- P043, PDF page 4, Results and discussion: "We have performed DFT calculations, as described above, for all the known enthalpies of formation of the two ternary phase diagrams, for Al–Ni–Pd and Al–Ni–Ti, at ambient conditions, resulting in a total of 34 systems."
- P043, PDF page 3: "The error inherent in DFT calculations (that has its origin from the approximation used for the exchange and correlation functional) can be quantified as the difference between the experimental and theoretical determined enthalpy of formation. Hence, we introduce the term Hcorr as Hcorr = HDFT − Hexpt"
- P043, PDF page 4, Results and discussion: "The total DFT corrected enthalpy is given by Hpred = HDFT − Hcorr, where HDFT is the enthalpy from DFT calculations."
