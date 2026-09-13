# Dataset: Experimental formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems

- Dataset ID: `D_P043_experimental_formation_enthalpy_dataset_for_alnipd_and_alniti_ternary_systems`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 0.98

## Raw names

- Experimental formation enthalpy dataset for Al–Ni–Pd and Al–Ni–Ti ternary systems
- experimental values of the enthalphy of formation
- known enthalpies of formation of the two ternary phase diagrams, for Al–Ni–Pd and Al–Ni–Ti

## Observed material scopes

- Al–Ni–Pd system
- Al–Ni–Ti system
- ternary alloys
- binary alloys
- intermetallic compounds

## Observed research tasks

- ML-based correction of DFT formation enthalpy errors for improved phase stability prediction

## Observed research stages

- data_acquisition
- label_generation
- model_training
- model_evaluation
- candidate_screening
- computational_validation

## Observed properties

- formation enthalpy (Hf)

## Observed fields

- chemical formula
- elemental concentrations
- valence electron count
- experimental formation enthalpy (Hexpt)

## Usage evidence

- P043 (Machine learning for improved density functional theory thermodynamics): label_source in Collection of experimental formation enthalpy data — Provide ground-truth experimental formation enthalpies (Hexpt) to construct training labels Hcorr = HDFT − Hexpt
- P043 (Machine learning for improved density functional theory thermodynamics): label_source in Calculation of DFT-experiment discrepancy (Hcorr) — Compute target labels Hcorr = HDFT − Hexpt for supervised learning
- P043 (Machine learning for improved density functional theory thermodynamics): training in Supervised training of neural network regressor — Train neural network to predict Hcorr using experimental ground truth
- P043 (Machine learning for improved density functional theory thermodynamics): test in Performance evaluation using cross-validation — Evaluate model performance on unseen experimental data via LOOCV and k-fold cross-validation
- P043 (Machine learning for improved density functional theory thermodynamics): screening in Comparison of linear vs. neural network correction models — Compare linear vs. neural network correction models by evaluating RMSE on same experimental reference
- P043 (Machine learning for improved density functional theory thermodynamics): computational_validation in Application of ML-corrected enthalpies to phase stability assessment — Validate utility of ML-corrected enthalpies (Hpred) for phase stability assessment by comparing against experimental ground truth

## Dataset evidence

- P043, PDF page 3: "A training dataset of reliable experimental values of the enthalphy of formation is initially filtered to exclude missing or unreliable enthalpy values, ensuring that only well-defined data points are used for training of the neural network."
- P043, PDF page 4, Results and discussion: "We have performed DFT calculations, as described above, for all the known enthalpies of formation of the two ternary phase diagrams, for Al–Ni–Pd and Al–Ni–Ti, at ambient conditions, resulting in a total of 34 systems."
- P043, PDF page 6: "For completeness, we list in Table 1 of the Appendix all experimental values of the heat of formation used in this investigation, together with the predicted values using Eqs. 9 and 10."
