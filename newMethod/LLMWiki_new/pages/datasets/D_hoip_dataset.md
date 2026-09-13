# Dataset: HOIP dataset

- Dataset ID: `D_hoip_dataset`
- Dataset type: `public_database`
- Source dataset: None
- Availability: public
- Recommendable: true
- Confidence: 1.0

## Raw names

- HOIP dataset
- hybrid organic–inorganic perovskite (HOIP) dataset
- 1345 perovskite compounds

## Observed material scopes

- hybrid organic–inorganic perovskites

## Observed research tasks

- extrapolative prediction of material properties

## Observed research stages

- data_acquisition
- candidate_generation
- model_training
- model_evaluation
- candidate_screening

## Observed properties

- bandgap
- dielectric constants
- relative energies

## Observed fields

- organic cation
- inorganic cation
- inorganic anion
- bandgap

## Usage evidence

- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): source in acquisition of polymer and perovskite datasets — Acquisition of computational property data for hybrid organic–inorganic perovskites (bandgaps)
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): candidate_pool in generation of extrapolative episodes — Generation of extrapolative episodes where test instances lie outside training domain (e.g., perovskites containing Ge+F or Pb+I excluded from training)
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): training in meta-training of MNNs via extrapolative episodic training (E2T) — Meta-training of MNNs via extrapolative episodic training (E2T)
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): test in evaluation of extrapolative prediction performance — Evaluation of extrapolative prediction performance on unseen perovskite compositions (HOIP-GeF and HOIP-PbI)
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): experimental_validation in fine-tuning for downstream extrapolative domains — Fine-tuning pretrained meta-learners to target perovskite domains (HOIP-GeF and HOIP-PbI) using limited data

## Dataset evidence

- P015, PDF page 10, unknown: "The HOIP dataset40,41 contains 1345 perovskite compounds and their properties, including bandgaps, dielectric constants, and relative energies, calculated using the density functional theory."
- P015, PDF page 4, unknown: "To verify the generalizability of E2T, we conducted another experiment using a hybrid organic–inorganic perovskite (HOIP) dataset40,41, which includes 1345 perovskite structures and their properties, including bandgaps, as calculated through the density functional theory."
