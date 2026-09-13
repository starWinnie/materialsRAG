# Dataset Use: labeled local database

- DatasetUse ID: `DU_labeled_local_database`
- Dataset: labeled local database (`D_labeled_local_database`)
- Papers: P008
- Usage records: 4

## Usage roles

- screening
- computational_validation
- training
- validation

## Purposes

- Enable statistical analysis and candidate selection (e.g., Cs2SnSe3, Cs2GeSe3) based on κPET ≤ 2 W/mK threshold.
- Provide candidate list (Cs2SnSe3, Cs2GeSe3) selected from κPET-ranked materials for first-principles validation.
- Train interpretable CatBoost classifier to predict ultralow κL (κPET ≤ 2 W/mK).
- Evaluate trained CatBoost model performance via stratified tenfold cross-validation.

## Used fields

- κPET
- formula
- crystal system
- shear modulus
- bulk modulus
- 273 descriptors (Magpie + Voronoi)

## Construction methods

- None stated

## Filter conditions

- κPET ≤ 2 W/mK
- lowest κPET values
- unreported materials
- κPET ≤ 2 W/mK → label 1
- κPET > 2 W/mK → label 0

## Sample counts

- 2

## Availability

- Dataset: not_directly_available
- Recommendable: false

## Confidence

1.0

## Usage records

### UR_P008_05_labeled_local_database

- Paper: `P008` — Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity
- Task: identifying semiconductors with ultralow lattice thermal conductivity (`T_P008_01`)
- Stage: statistical analysis and candidate selection from labeled local database (`candidate_screening`, `S_P008_05`)
- Usage role: screening
- Purpose: Enable statistical analysis and candidate selection (e.g., Cs2SnSe3, Cs2GeSe3) based on κPET ≤ 2 W/mK threshold.
- Used fields: κPET, formula, crystal system, shear modulus, bulk modulus
- Filter conditions: κPET ≤ 2 W/mK
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P008, PDF page 5: "Of particular note is that nearly 70% of these semiconductors exhibit the κPET values no greater than 2 W/mK (left panel in Fig. 4a), with a considerable portion of these materials remaining unreported to date. These materials also constitute a list of candidate materials with potential applications in the TE ﬁeld (Table S2)..."

### UR_P008_06_labeled_local_database

- Paper: `P008` — Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity
- Task: identifying semiconductors with ultralow lattice thermal conductivity (`T_P008_01`)
- Stage: first-principles validation of selected candidates (`computational_validation`, `S_P008_06`)
- Usage role: computational_validation
- Purpose: Provide candidate list (Cs2SnSe3, Cs2GeSe3) selected from κPET-ranked materials for first-principles validation.
- Used fields: κPET, formula
- Filter conditions: lowest κPET values, unreported materials
- Construction method: Not stated
- Sample count: 2
- Confidence: 1.0

Evidence:
- P008, PDF page 5: "To further validate the results and conduct in-depth analysis of the phonon thermal transport mechanisms, we calculate more precise κL values according to ﬁrst-principles derived force constants and Boltzmann transport theory for the unreported materials Cs2SnSe3 and Cs2GeSe3, which are screened out based on the formula type ranking among the materials with the lowest κPET values."

### UR_P008_07_labeled_local_database

- Paper: `P008` — Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity
- Task: identifying semiconductors with ultralow lattice thermal conductivity (`T_P008_01`)
- Stage: training interpretable supervised classification model (`model_training`, `S_P008_07`)
- Usage role: training
- Purpose: Train interpretable CatBoost classifier to predict ultralow κL (κPET ≤ 2 W/mK).
- Used fields: κPET, 273 descriptors (Magpie + Voronoi)
- Filter conditions: κPET ≤ 2 W/mK → label 1, κPET > 2 W/mK → label 0
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P008, PDF page 7, Interpretable supervised learning for predicting ultralow κL: "After labeling the materials in the second-level dataset based on our HTC framework to obtain the local database, we develop interpretable supervised classiﬁcation models to predict ultralow κL for efﬁciently by-passing the complex ab initio calculations..."
- P008, PDF page 7, Interpretable supervised learning for predicting ultralow κL: "Here, materials with κPET not exceeding 2 W/mK are labeled as 1, which are considered to possess ultralow κL; otherwise, they are labeled as 0, signifying non-ultralow κL."

### UR_P008_08_labeled_local_database

- Paper: `P008` — Hierarchy-boosted funnel learning for identifying semiconductors with ultralow lattice thermal conductivity
- Task: identifying semiconductors with ultralow lattice thermal conductivity (`T_P008_01`)
- Stage: evaluation of classification model performance (`model_evaluation`, `S_P008_08`)
- Usage role: validation
- Purpose: Evaluate trained CatBoost model performance via stratified tenfold cross-validation.
- Used fields: κPET, 273 descriptors (Magpie + Voronoi)
- Filter conditions: Not stated
- Construction method: Not stated
- Sample count: Not stated
- Confidence: 1.0

Evidence:
- P008, PDF page 7, Interpretable supervised learning for predicting ultralow κL: "As a result, the performances of the optimal CatBoost classiﬁcation model are characterized by the ROC curve and the confusion matrix (Fig. 6b), showing its great ability in classifying semiconductors with ultralow κL due to the high ROC AUC (0.94), accuracy (0.90), precision (0.89), recall (0.90) and F1-score (0.89)."

## Aggregated evidence

- , PDF page 5: "Of particular note is that nearly 70% of these semiconductors exhibit the κPET values no greater than 2 W/mK (left panel in Fig. 4a), with a considerable portion of these materials remaining unreported to date. These materials also constitute a list of candidate materials with potential applications in the TE ﬁeld (Table S2)..."
- , PDF page 5: "To further validate the results and conduct in-depth analysis of the phonon thermal transport mechanisms, we calculate more precise κL values according to ﬁrst-principles derived force constants and Boltzmann transport theory for the unreported materials Cs2SnSe3 and Cs2GeSe3, which are screened out based on the formula type ranking among the materials with the lowest κPET values."
- , PDF page 7, Interpretable supervised learning for predicting ultralow κL: "After labeling the materials in the second-level dataset based on our HTC framework to obtain the local database, we develop interpretable supervised classiﬁcation models to predict ultralow κL for efﬁciently by-passing the complex ab initio calculations..."
- , PDF page 7, Interpretable supervised learning for predicting ultralow κL: "Here, materials with κPET not exceeding 2 W/mK are labeled as 1, which are considered to possess ultralow κL; otherwise, they are labeled as 0, signifying non-ultralow κL."
- , PDF page 7, Interpretable supervised learning for predicting ultralow κL: "As a result, the performances of the optimal CatBoost classiﬁcation model are characterized by the ROC curve and the confusion matrix (Fig. 6b), showing its great ability in classifying semiconductors with ultralow κL due to the high ROC AUC (0.94), accuracy (0.90), precision (0.89), recall (0.90) and F1-score (0.89)."
