# Portfolio Optimization

## Overview
This project performs constrained portfolio optimization to maximize Sharpe ratio.
Using historical prices and SciPy optimization, it solves for asset allocations subject to:
- long-only allocations
- full investment constraint (weights sum to 1)

## Key Files
- `optimization.py`: optimizer and portfolio statistics
- `tests/grade_optimization.py`: system validation harness
- `Figure1.png`: normalized portfolio vs benchmark visualization

## Skills Demonstrated
- Numerical optimization for finance
- Risk-adjusted objective design (Sharpe ratio)
- Portfolio diagnostics (cumulative return, volatility, average daily return)

## Run
```bash
python optimization.py
```
