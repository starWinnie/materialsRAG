# Dataset: OpenKIM 178 FCC Interatomic Potentials

- Dataset ID: `D_openkim_178_fcc_interatomic_potentials`
- Dataset type: `public_subset`
- Source dataset: `D_openkim_repository`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- OpenKIM 178 FCC Interatomic Potentials
- 178 IPs
- 178 IP models
- 178 IPs for nine FCC metals

## Observed material scopes

- FCC metals

## Observed research tasks

- predicting plastic flow strength from small-scale indicator properties

## Observed research stages

- data_acquisition
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

- P014 (Cross-scale covariance for material property prediction): candidate_pool in collecting interatomic potential models and their precomputed properties — Provide initial pool of interatomic potentials for MD simulations and small-scale property analysis
- P014 (Cross-scale covariance for material property prediction): screening in screening IP models for numerical and physical validity — Identify and remove IP models with numerical instabilities or physical anomalies

## Dataset evidence

- P014, PDF page 7, MD simulations of plastic strength: "Out of the many IPs available and documented in the OpenKIM repository, 178 IPs previously developed for nine FCC metals were selected."
- P014, PDF page 1, unknown: "Here we explore covariance between predictions of metal plasticity, from 178 large-scale (~108 atoms) molecular dynamics (MD) simulations, and a variety of indicator properties computed at small-scales (≤102 atoms). All simulations use the same 178 IPs."
