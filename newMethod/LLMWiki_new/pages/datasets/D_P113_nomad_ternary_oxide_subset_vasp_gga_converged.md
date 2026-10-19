# Dataset: NOMAD ternary oxide subset (VASP/GGA, converged)

- Dataset ID: `D_P113_nomad_ternary_oxide_subset_vasp_gga_converged`
- Dataset type: `derived_subset`
- Source dataset: `D_nomad_archive`
- Availability: public
- Recommendable: false
- Confidence: 1.0

## Raw names

- NOMAD ternary oxide subset (VASP/GGA, converged)
- ternary elements containing oxygen
- ternary oxides
- almost 8000 entries

## Observed material scopes

- ternary oxides

## Observed research tasks

- AI-based analysis of materials-science data

## Observed research stages

- data_acquisition
- data_preparation
- candidate_generation

## Observed properties

- atomic density

## Observed fields

- atoms
- atomic_density
- composition
- stoichiometric_ratio

## Usage evidence

- P056 (The NOMAD Artificial-Intelligence Toolkit: turning materials-science data into knowledge and understanding): training in Querying the NOMAD Archive via RESTful API — Training dataset for clustering analysis targeting atomic density.
- P056 (The NOMAD Artificial-Intelligence Toolkit: turning materials-science data into knowledge and understanding): label_source in Enriching retrieved data with atomic features — Source of atomic density values used to enrich the dataframe with atomic features.
- P056 (The NOMAD Artificial-Intelligence Toolkit: turning materials-science data into knowledge and understanding): candidate_pool in Generating candidate descriptors via SISSO — Source of materials for generating candidate descriptors (materials genes) via SISSO.

## Dataset evidence

- P113, PDF page 3, Querying the NOMAD Archive and performing AI modeling on retrieved data: "In the example notebook37, we use the NOMAD Python client library to retrieve ternary elements containing oxygen. We also request that the ab initio calculations were carried out with the VASP code, using exchange-correlation (xc) functionals from the generalized-gradient-approximation (GGA) family. In addition, to ensure that calculations have converged, we also set that the energy difference during geometry optimization has converged. As of April 2022, this query retrieves almost 8000 entries, which are the results of simulations carried out at different laboratories."
