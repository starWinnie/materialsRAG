# Dataset: argyrodite-type test set

- Dataset ID: `D_P041_argyrodite_type_test_set`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- argyrodite-type test set
- 126 argyrodite-type test materials
- argyrodite test set

## Observed material scopes

- argyrodite-type Li solid-state electrolytes
- Li24+xM4S20X4 compounds

## Observed research tasks

- fine-tuning pretrained universal machine-learning interatomic potentials

## Observed research stages

- model_evaluation
- experimental_validation

## Observed properties

- energy
- force
- softening scale
- Li diffusivity
- quasi-melting behavior

## Observed fields

- atomic configurations
- DFT energies
- forces
- MSD data

## Usage evidence

- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): test in evaluating PES accuracy on argyrodite and non-argyrodite Li SSE test sets — evaluating PES accuracy on argyrodite and non-argyrodite Li SSE test sets
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): experimental_validation in validating dynamical properties via MD simulations and comparison to DFT benchmarks — validating dynamical properties via MD simulations and comparison to DFT benchmarks

## Dataset evidence

- P041, PDF page 6, PES evaluation of Li SSEs: "For the argyrodite-type test set, we consider compounds with the chemical formula Li24+xM4S20X4, where M represents tetravalent (Si, Ge, or Sn) and pentavalent (P, As, or Sb) cations, and X is a halide anion such as Cl, Br, or I. In addition, we account for high-entropy systems in which more than two different non-Li cations and halides are incorporated (e.g., Li26P2Si2S20Cl2I2). In this case, assuming that S and X are S2−and X−ions, respectively, the number of Li atoms is adjusted to maintain charge neutrality. The combination of non-Li cations and halides yields a total of 1890 possible compositions. Among them, considering the high computational cost of DFT calculations to produce reference data for comparison, we select 126 representative compounds, which cover diverse chemistries, for the test set (see Supplementary Table 1 for detailed compositions)."
