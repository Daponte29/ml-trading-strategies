# Defeat Learners

## Overview
This project creates synthetic datasets designed to favor one learner over another.
It generates:
- data where Linear Regression outperforms Decision Trees
- data where Decision Trees outperform Linear Regression

This demonstrates understanding of model inductive bias and how data-generating processes affect generalization.

## Key Files
- `gen_data.py`: synthetic data generators (`best_4_lin_reg`, `best_4_dt`)
- `tests/testbest4.py`: experiment and validation script
- `DTLearner.py`, `LinRegLearner.py`: learner implementations used for comparison
- `tests/grade_best4.py`: course grading harness

## Skills Demonstrated
- Synthetic data design for controlled ML experiments
- Bias-aware model evaluation
- Reproducibility via seeded generation

## Run
```bash
python tests/testbest4.py
```
