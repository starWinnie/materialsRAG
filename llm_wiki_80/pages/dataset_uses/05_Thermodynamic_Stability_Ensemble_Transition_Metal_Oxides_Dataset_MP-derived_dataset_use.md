# 05_Thermodynamic_Stability_Ensemble - Transition Metal Oxides Dataset (MP-derived)

## Dataset Use

A subset of 7,137 transition metal oxides (1,211 stable) extracted from MP, with all samples withheld from training to form an out-of-distribution test set. Used to assess ECSG’s generalization to Fe- and Mn-containing oxides — representing another unknown space — and to confirm robust stability prediction under moderate class imbalance (17.0% stable).

## Links

- Paper: [05 Thermodynamic Stability Ensemble](../papers/05_Thermodynamic_Stability_Ensemble.md)
- Task: [task page](../tasks/05_Thermodynamic_Stability_Ensemble_task_1.md)
- Dataset: [Transition Metal Oxides Dataset (MP-derived)](../datasets/Transition_Metal_Oxides_Dataset_MP-derived.md)
- Dataset URL: None

## Task Context

Predicting the thermodynamic stability of inorganic compounds by classifying them as stable or unstable based on decomposition energy (ΔHd), where compounds with ΔHd ≤ 0 meV/atom (or relaxed thresholds of 25/40 meV/atom) are labeled stable — enabling high-throughput screening of viable candidates in unexplored compositional spaces.

## Metadata

- Dataset use ID: `dataset_use_4ca1b02de040`
- Original dataset title: Transition Metal Oxides Dataset (MP-derived)
- Tags: thermodynamic stability prediction, compound stability classification, decomposition energy estimation
