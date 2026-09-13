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
- data_preparation
- model_training
- model_evaluation
- ablation_study
- candidate_screening

## Observed properties

- bandgap
- dielectric constants
- relative energies

## Observed fields

- organic cation
- inorganic cation (Ge, Sn, Pb)
- inorganic anion (F, Cl, Br, I)
- bandgap

## Usage evidence

- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): source in acquisition of polymer and perovskite datasets — Acquisition of computational perovskite property data for training and evaluation.
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): training in descriptor generation and dataset partitioning — Descriptor generation (MPNN embedding) and episodic partitioning for extrapolative training.
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): training in training MNNs via extrapolative episodic training (E2T) — Training MNNs via extrapolative episodic training (E2T) using episodes with extrapolative relationships.
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): test in evaluation of extrapolative prediction performance — Evaluation of extrapolative prediction performance on unseen perovskite compositions (HOIP-GeF and HOIP-PbI).
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): benchmark in hyperparameter sensitivity analysis for E2T — Ablation study to investigate hyperparameter sensitivity (|S_train|, |S_infer|, λ) for E2T performance.
- P015 (Advancing extrapolative predictions of material properties through learning to learn using extrapolative episodic training): candidate_pool in fine-tuning for downstream extrapolative domains — Fine-tuning pretrained E2T models on target-domain perovskite subsets (HOIP-GeF and HOIP-PbI) with limited samples.

## Dataset evidence

- P015, PDF page 10, Methods: "The HOIP dataset40,41 contains 1345 perovskite compounds and their properties, including bandgaps, dielectric constants, and relative energies, calculated using the density functional theory."
- P015, PDF page 4, unknown: "To verify the generalizability of E2T, we conducted another experiment using a hybrid organic–inorganic perovskite (HOIP) dataset40,41, which includes 1345 perovskite structures and their properties, including bandgaps, as calculated through the density functional theory."
