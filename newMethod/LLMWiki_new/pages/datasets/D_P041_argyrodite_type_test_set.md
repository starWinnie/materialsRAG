# Dataset: argyrodite-type test set

- Dataset ID: `D_P041_argyrodite_type_test_set`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- argyrodite-type test set
- argyrodite test set

## Observed material scopes

- argyrodite-type materials

## Observed research tasks

- fine-tuning pretrained universal machine-learning interatomic potentials

## Observed research stages

- model_evaluation
- computational_validation

## Observed properties

- potential energy
- atomic forces
- Li-ion diffusivity
- quasi-melting behavior

## Observed fields

- atomic positions
- cell parameters
- energies
- forces
- MSD
- quasi-melting ratio

## Usage evidence

- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): benchmark in evaluating PES accuracy on argyrodite and non-argyrodite test sets — quantify improvements in energy/force prediction accuracy and softening scales across argyrodite-type Li SSEs
- P041 (An efficient forgetting-aware fine-tuning framework for pretrained universal machine-learning interatomic potentials): computational_validation in performing MD simulations to assess dynamical properties (Li diffusivity and quasi-melting behavior) — validate that the fine-tuned MLIP accurately describes finite-temperature atomic motion and associated dynamical properties for argyrodite-type materials

## Dataset evidence

- P041, PDF page 6: "To generate a speciﬁc test dataset, we ﬁrst optimize the structures of the selected materials at 0 K and then perform ab initio molecular dynamics (AIMD) simulations for 100 ps under the NVT ensemble. Each system is gradually heated from 300 to 1200 K to probe the PES across the temperature range typically used for simulating Li diffusion in SSEs. Test conﬁgurations are sampled every 200 fs, resulting in 500 structures per material."
