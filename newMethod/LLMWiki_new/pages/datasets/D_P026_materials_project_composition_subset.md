# Dataset: Materials Project composition subset

- Dataset ID: `D_P026_materials_project_composition_subset`
- Dataset type: `derived_subset`
- Source dataset: `D_materials_project`
- Availability: not_directly_available
- Recommendable: false
- Confidence: 1.0

## Raw names

- Materials Project composition subset
- MP composition dataset
- 86,740 samples
- 86,741 samples

## Observed material scopes

- inorganic crystalline materials

## Observed research tasks

- dataset redundancy control for material property prediction

## Observed research stages

- data_preparation

## Observed properties

- formation energy
- band gap

## Observed fields

- composition
- formation energy
- band gap

## Usage evidence

- P026 (MD-HIT: Machine learning for material property prediction with dataset redundancy control): source in redundancy reduction using MD-HIT-composition — Input for MD-HIT-composition redundancy reduction algorithm

## Dataset evidence

- P026, PDF page 4, Datasets generation: "We downloaded 125,619 cif files with material structures from the Materials Project database, which includes 89,354 materials with unique compositions. In cases where compositions corresponded to multiple polymorphs, we adopted average material property values by default, with the exception of formation energy property, for which we used the minimum value. Additionally, we excluded mp-101974 (HeSiO2) due to issues with calculating Matscholar features. After eliminating formulas with over 50 atoms, we obtained a non-duplicate composition dataset with 86,741 samples..."
- P026, PDF page 5, Composition based material property prediction with redundancy control: "We conducted experiments using datasets filtered by Mendeleev and Matscholar distances. We evaluated two state-of-the-art composition-based property prediction algorithms, Roost and CrabNet... on non-redundant datasets derived from the MP composition dataset with 86,740 samples..."
