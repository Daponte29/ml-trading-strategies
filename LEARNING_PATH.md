# ML4T Relearning Path

Use this guide to revisit each project quickly and rebuild intuition from fundamentals to applied trading workflows.

## 1. Start Here

1. Read the root README for project map and setup.
2. Install dependencies from the root package metadata:
   1. `pip install -e .`
3. Run one project at a time from its folder.

## 2. Recommended Order

1. `martingale`
Reason: builds simulation mindset and probability intuition.

2. `marketsim`
Reason: establishes order processing, holdings, cash accounting, and portfolio valuation.

3. `optimize_something`
Reason: introduces objective functions, constraints, and optimizer workflows.

4. `assess_learners`
Reason: covers bias/variance, supervised learners, and bagging.

5. `defeat_learners`
Reason: reinforces model behavior by designing adversarial synthetic data.

6. `qlearning_robot`
Reason: transitions into reinforcement learning and Dyna-Q acceleration.

7. `indicator_evaluation`
Reason: applies feature engineering to technical indicators and strategy analysis.

8. `strategy_evaluation`
Reason: capstone integration of indicators, learners, backtesting, and evaluation.

## 3. What To Focus On In Code

1. Inputs/outputs at each boundary:
   1. CSV -> DataFrame
   2. Signals -> trades
   3. Trades -> portfolio values

2. Core algorithms:
   1. Tree splitting and leaf conditions
   2. Bootstrap sampling and aggregation
   3. Q update rule and exploration decay
   4. Sharpe-ratio objective and constraints

3. Experiment design:
   1. in-sample vs out-of-sample separation
   2. fixed random seeds
   3. plotting and interpretation of metrics

## 4. Presentability Checklist

1. Keep each project README updated with:
   1. overview
   2. key files
   3. run command
2. Prefer clear module docstrings and descriptive function names.
3. Keep generated figures in project folders where they are created.
4. Avoid committing temporary notebooks or scratch scripts.
