# Strategy Evaluation

## Overview
This capstone-style trading project compares:
- a manual, indicator-based strategy
- an ML-driven strategy learner
- a benchmark buy-and-hold baseline

It includes in-sample and out-of-sample evaluation and sensitivity experiments for market impact.

## Key Files
- `StrategyLearner.py`: learning-based trading policy
- `ManualStrategy.py`: rule-based strategy
- `experiment1.py`, `experiment2.py`: evaluation experiments
- `tests/test_strategy_project.py`: orchestrates training, testing, plotting, and stats output
- `marketsimcode.py`: portfolio simulation with costs

## Skills Demonstrated
- End-to-end strategy pipeline (features, learner, backtest, diagnostics)
- Financial ML experimentation with transaction cost awareness
- Comparative evaluation and regime generalization checks

## Run
```bash
python tests/test_strategy_project.py
```

## Outputs
- In-sample and out-of-sample comparison plots
- Impact sensitivity plots and statistics files
