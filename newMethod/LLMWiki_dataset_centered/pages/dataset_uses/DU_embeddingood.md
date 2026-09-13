# Dataset Use: EmbeddingOOD

- DatasetUse ID: `DU_embeddingood`
- Dataset: EmbeddingOOD (`D_embeddingood`)
- Papers: P026
- Usage records: 1

## Usage roles

- experimental_validation

## Purposes

- Out-of-distribution test set to validate OOD generalization improvement

## Used fields

- formation energy

## Construction methods

- Selected 1000 OOD samples furthest from three nearest neighbors in Roost latent representation space

## Filter conditions

- None stated

## Sample counts

- 1000

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P026_05_embeddingood

- Paper: `P026` — MD-HIT: Machine learning for material property prediction with dataset redundancy control
- Task: dataset redundancy control for material property prediction (`T_P026_01`)
- Stage: validate OOD generalization improvement (`computational_validation`, `S_P026_05`)
- Usage role: experimental_validation
- Purpose: Out-of-distribution test set to validate OOD generalization improvement
- Used fields: formation energy
- Filter conditions: Not stated
- Construction method: Selected 1000 OOD samples furthest from three nearest neighbors in Roost latent representation space
- Sample count: 1000
- Confidence: 1.0

Evidence:
- P026, PDF page 8: "To compare the true OOD performance of models trained on non-redundant and redundant dataset, we prepared another OOD test set named EmbeddingOOD. First, we used a pretrained Roost model as an encoder to obtain the latent representations for all samples in the entire dataset (86,740 samples). We then calculated the pairwise distances of all samples using their latent representations and selected 1000 OOD samples that are furthest away on average from their three nearest neighbors, forming our EmbeddingOOD test set."

## Aggregated evidence

- , PDF page 8: "To compare the true OOD performance of models trained on non-redundant and redundant dataset, we prepared another OOD test set named EmbeddingOOD. First, we used a pretrained Roost model as an encoder to obtain the latent representations for all samples in the entire dataset (86,740 samples). We then calculated the pairwise distances of all samples using their latent representations and selected 1000 OOD samples that are furthest away on average from their three nearest neighbors, forming our EmbeddingOOD test set."
