# Assess Learners

## Overview

This project benchmarks supervised learning approaches for stock/market-style tabular data.
It implements and compares:

* Decision Trees (`DTLearner`)
* Random Trees (`RTLearner`)
* Bagging ensembles (`BagLearner`)
* A high-ensemble composite learner (`InsaneLearner`)
* Linear Regression baseline (`LinRegLearner`)

The analysis script sweeps leaf sizes and compares in-sample vs out-of-sample performance using error metrics and plots.

## Key Files

* `testlearner.py`: main experiment driver and figure generation
* `DTLearner.py`, `RTLearner.py`: tree learners
* `BagLearner.py`, `InsaneLearner.py`: ensemble learners
* `LinRegLearner.py`: regression baseline
* `grade_learners.py`: course grading harness

## Skills Demonstrated

* Supervised learning model design from scratch
* Bias/variance analysis via hyperparameter sweeps
* Ensemble methods (bootstrap aggregation)
* Experimental rigor with train/test splits and reproducibility

## Run

```bash
python testlearner.py Data/Istanbul.csv
```

## Outputs

* `Q1_new_alternative_metrics.png`
* `Q2_new_alternative_metrics.png`
* `Q3_new_alternative_metrics.png`


