# ML4T Trading and Learning Lab

Personal project repository for machine learning, reinforcement learning, market simulation, and algorithmic trading experiments.

## Highlights

* Implemented multiple learners from scratch: decision tree, random tree, bagging ensemble, and Q-learning with Dyna-Q.
* Built end-to-end trading pipelines: indicators, strategy generation, portfolio simulation, and benchmark comparison.
* Ran optimization and simulation experiments for Sharpe ratio maximization and risk analysis.

## Project Map

* `assess_learners`: compare supervised learners and ensembles on predictive performance
* `defeat_learners`: generate synthetic datasets that expose model inductive bias
* `indicator_evaluation`: engineer and visualize technical indicators + theoretically optimal strategy
* `marketsim`: compute portfolio values from trade orders with commission and impact
* `martingale`: Monte Carlo analysis of betting strategy behavior under bankroll constraints
* `optimize_something`: constrained portfolio allocation optimization via Sharpe ratio
* `qlearning_robot`: tabular Q-learning and Dyna-Q for sequential decision making
* `strategy_evaluation`: manual strategy vs ML strategy comparison (in-sample/out-of-sample)

## Quick Start


1. Create and activate a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Run each project from its own folder using its local `README.md` instructions.

## Notes

* Historical price data used by projects is stored under `data/`.
* Most projects are self-contained and include their own `README.md` and `pyproject.toml`.


