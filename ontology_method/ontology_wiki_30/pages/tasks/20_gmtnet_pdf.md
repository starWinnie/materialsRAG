# 20_GMTNet.pdf

## Ontology Type
Task

## Task Description
Predicting crystal tensor properties—including dielectric tensors (order-2), piezoelectric tensors (order-3), and elastic tensors (order-4)—in matrix form while ensuring predictions are equivariant under O(3) transformations (rotations/reflections) and invariant under the crystal’s space group symmetries, so that predicted tensors respect zero-element patterns, mutual element dependencies, and physical transformation rules dictated by intrinsic crystal symmetry.

## Material Systems
None

## Target Properties
- [dielectric property](../target_properties/dielectric_property.md)

## Representations
- [space group](../representations/space_group.md)
- [spectrum or tensor](../representations/spectrum_or_tensor.md)

## Methods
- [equivariant neural network](../methods/equivariant_neural_network.md)

## Supporting Dataset Uses
- [JARVIS-DFT](../dataset_uses/jarvis_dft_4.md)

## Datasets
- [JARVIS-DFT](../datasets/jarvis_dft.md)

## Source Papers
- [20 GMTNet](../papers/20_gmtnet.md)

## Metadata
task_id: `task_78314418eccc`
tags: tensor prediction; crystal symmetry enforcement; O(3) equivariance
