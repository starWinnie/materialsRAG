# Dataset: EmbeddingOOD

- Dataset ID: `D_embeddingood`
- Dataset type: `paper_specific`
- Source dataset: None
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- EmbeddingOOD
- EmbeddingOOD test set

## Observed material scopes

- inorganic crystalline materials

## Observed research tasks

- dataset redundancy control for material property prediction

## Observed research stages

- computational_validation

## Observed properties

- formation energy

## Observed fields

- latent representations
- pairwise distances

## Usage evidence

- P026 (MD-HIT: Machine learning for material property prediction with dataset redundancy control): experimental_validation in validate OOD generalization improvement — Out-of-distribution test set to validate OOD generalization improvement

## Dataset evidence

- P026, PDF page 8: "To compare the true OOD performance of models trained on non-redundant and redundant dataset, we prepared another OOD test set named EmbeddingOOD. First, we used a pretrained Roost model as an encoder to obtain the latent representations for all samples in the entire dataset (86,740 samples). We then calculated the pairwise distances of all samples using their latent representations and selected 1000 OOD samples that are furthest away on average from their three nearest neighbors, forming our EmbeddingOOD test set."
