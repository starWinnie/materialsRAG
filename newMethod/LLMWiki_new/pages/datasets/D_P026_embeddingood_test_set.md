# Dataset: EmbeddingOOD test set

- Dataset ID: `D_P026_embeddingood_test_set`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- EmbeddingOOD test set
- EmbeddingOOD

## Observed material scopes

- inorganic crystalline materials

## Observed research tasks

- dataset redundancy control for material property prediction

## Observed research stages

- candidate_screening

## Observed properties

- formation energy

## Observed fields

- composition
- formation energy
- latent representation

## Usage evidence

- P026 (MD-HIT: Machine learning for material property prediction with dataset redundancy control): test in construct OOD test sets via density-based sampling — Out-of-distribution test set for evaluating extrapolative capability in latent space

## Dataset evidence

- P026, PDF page 8: "First, we used a pretrained Roost model as an encoder to obtain the latent representations for all samples in the entire dataset (86,740 samples). We then calculated the pairwise distances of all samples using their latent representations and selected 1000 OOD samples that are furthest away on average from their three nearest neighbors, forming our EmbeddingOOD test set."
