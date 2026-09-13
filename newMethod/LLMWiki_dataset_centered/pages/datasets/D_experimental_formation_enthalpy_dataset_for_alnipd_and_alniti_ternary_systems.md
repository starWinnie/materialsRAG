# Dataset: Experimental formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems

- Dataset ID: `D_experimental_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 0.98

## Raw names

- Experimental formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems
- experimental values of the enthalphy of formation
- reliable experimental values of the enthalphy of formation
- experimental values of the heat of formation
- experimental data (Hexpt)

## Observed material scopes

- Al–Ni–Pd system
- Al–Ni–Ti system
- binary alloys
- ternary alloys
- intermetallic compounds

## Observed research tasks

- correcting DFT-calculated formation enthalpy errors

## Observed research stages

- data_acquisition
- label_generation
- model_training
- model_evaluation
- candidate_screening

## Observed properties

- formation enthalpy

## Observed fields

- chemical formula
- elemental concentrations
- enthalpy of formation

## Usage evidence

- P043 (Machine learning for improved density functional theory thermodynamics): label_source in acquiring experimental formation enthalpy data — Serve as ground truth labels for training and evaluation of the ML correction model.
- P043 (Machine learning for improved density functional theory thermodynamics): label_source in calculating enthalpy correction labels (Hcorr) — Compute enthalpy correction labels Hcorr = HDFT − Hexpt.
- P043 (Machine learning for improved density functional theory thermodynamics): training in training neural network regressor — Provide target labels (Hcorr) for supervised training of the neural network regressor.
- P043 (Machine learning for improved density functional theory thermodynamics): test in evaluating model performance with cross-validation — Evaluate model performance via cross-validation on held-out data.
- P043 (Machine learning for improved density functional theory thermodynamics): screening in comparing linear vs. neural network correction models — Compare linear vs. neural network correction models by computing RMSE against experimental Hcorr.

## Dataset evidence

- P043, PDF page 3: "A training dataset of reliable experimental values of the enthalphy of formation is initially filtered to exclude missing or unreliable enthalpy values, ensuring that only well-defined data points are used for training of the neural network."
- P043, PDF page 4, Results and discussion: "We have performed DFT calculations, as described above, for all the known enthalpies of formation of the two ternary phase diagrams, for Al–Ni–Pd and Al–Ni–Ti, at ambient conditions, resulting in a total of 34 systems."
- P043, PDF page 6: "For completeness, we list in Table 1 of the Appendix all experimental values of the heat of formation used in this investigation, together with the predicted values using Eqs. 9 and 10."
