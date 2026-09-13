# Dataset: OpenKIM 163 FCC Interatomic Potentials (screened)

- Dataset ID: `D_P014_openkim_163_fcc_interatomic_potentials_screened`
- Dataset type: `derived_subset`
- Source dataset: `D_openkim_178_fcc_interatomic_potentials`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- OpenKIM 163 FCC Interatomic Potentials (screened)
- 163 IPs
- remaining 163 IPs

## Observed material scopes

- FCC metals

## Observed research tasks

- predicting plastic flow strength from small-scale indicator properties

## Observed research stages

- data_preparation
- candidate_screening

## Observed properties

- plastic flow strength (MD)
- small-scale indicator properties

## Observed fields

- IP identifier
- metal species
- plastic flow strength
- C44
- rVFPE
- uSFE
- iSFE
- SE 111 FCC
- lattice constant
- vacancy migration energy
- relaxed vacancy formation energy
- unrelaxed vacancy formation energy
- vacancy formation volume

## Usage evidence

- P014 (Cross-scale covariance for material property prediction): training in cleaning and imputing missing or unreliable small-scale property data — Provide cleaned dataset for covariance analysis and regression modeling
- P014 (Cross-scale covariance for material property prediction): screening in identifying and excluding SF-jammed IP models — Identify and exclude SF-jammed IP models to ensure statistical homogeneity

## Dataset evidence

- P014, PDF page 2, Results and discussion: "MD simulations using one particular IP could not be completed due to numerical instabilities encountered irrespective of the integration time step. Another 14 IPs were excluded after subsequent analyzes revealed anomalies or irregularities in crystal response to straining, such as crystal rotation, phase transformations, and formation of amorphous phases, or voids (see the Supplementary Information (SI) for the full list of IPs and details on which were removed from consideration)."
- P014, PDF page 2, Results and discussion: "At the same time, inspection of small-scale indicator properties of the remaining 163 IPs, precomputed in the OpenKIM repository, revealed some missing or out-of-bounds values deemed unreliable."
