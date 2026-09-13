# Dataset: Interpolated OC22 oxide database

- Dataset ID: `D_P038_interpolated_oc22_oxide_database`
- Dataset type: `derived_subset`
- Source dataset: `D_open_catalyst_2022`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- Interpolated OC22 oxide database
- interpolated database
- database of the total energy predictions for all slabs and OER surface intermediates for 4119 oxide materials
- extrapolated database

## Observed material scopes

- oxide materials

## Observed research tasks

- Rational design of nanoscale stabilized oxide catalysts for OER

## Observed research stages

- candidate_generation
- candidate_screening
- computational_validation

## Observed properties

- total energy
- Gibbs adsorption energy
- overpotential
- Pourbaix decomposition energy
- Wulff shape
- nanoparticle formation energy

## Observed fields

- material_id
- slab
- intermediate
- energy
- gamma
- eta
- EPBX
- GNP_f

## Usage evidence

- P038 (Rational design of nanoscale stabilized oxide catalysts for OER with OC22): candidate_pool in Interpolating total energy predictions for slabs and surface intermediates — Provide total energy predictions for all slabs and OER surface intermediates for 4119 oxide materials to enable high-throughput screening.
- P038 (Rational design of nanoscale stabilized oxide catalysts for OER with OC22): screening in High-throughput screening with progressive criteria — Screen candidates using progressive criteria including Pourbaix stability, Wulff shape analysis, overpotential assessment, energy above hull, and material cost.
- P038 (Rational design of nanoscale stabilized oxide catalysts for OER with OC22): computational_validation in DFT validation of ML predictions — Validate ML-predicted Gibbs adsorption energies and overpotentials using DFT calculations.

## Dataset evidence

- P038, PDF page 1, Introduction: "In this work, we interpolated a database of the total energy predictions for all slabs and OER surface intermediates for 4119 oxide materials in the original OC22 dataset using pre-trained models from the OC22 framework."
- P038, PDF page 5, Results and discussion: "Using the previously developed ML models, we systematically extrapolated the total DFT energy of all terminations for all facets up to a MMI = 1 for all 4119 materials considered in this study."
