# 07_EATGNN_Piezoelectric_Tensor - JARVIS Database

## Dataset Use

The Joint Automated Repository for Various Integrated Simulations (JARVIS) is a DFT-based materials database that includes piezoelectric tensor data derived from high-throughput calculations. The paper explicitly states bulk material data was sourced from both the Materials Project and JARVIS; JARVIS contributes additional piezoelectric tensor entries—particularly from the referenced high-throughput study (Choudhary et al., npj Comput. Mater. 6, 64, 2020)—to expand coverage and improve model generalization for bulk crystal tensor prediction.

## Links

- Paper: [07 EATGNN Piezoelectric Tensor](../papers/07_EATGNN_Piezoelectric_Tensor.md)
- Task: [task page](../tasks/07_EATGNN_Piezoelectric_Tensor_task_1.md)
- Dataset: [JARVIS Database](../datasets/JARVIS_Database.md)
- Dataset URL: https://jarvis.nist.gov/

## Task Context

Predicting the complete third-rank piezoelectric stress tensor (eᵢⱼₖ) for crystalline materials — including all 18 independent Voigt components — while respecting crystal symmetry, rotational equivariance, and coordinate-frame independence, to enable accurate characterization of longitudinal, transverse, and shear piezoelectric effects across arbitrary crystallographic orientations.

## Metadata

- Dataset use ID: `dataset_use_98325f79e378`
- Original dataset title: JARVIS Database
- Tags: piezoelectric tensor prediction, equivariant learning, crystal symmetry-aware modeling
