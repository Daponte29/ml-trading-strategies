# Market Simulator

## Overview

This project implements a vectorized market simulator that converts an order stream into daily portfolio values.
It supports transaction costs through:

* fixed per-trade commission
* proportional market impact (slippage)

## Key Files

* `marketsim.py`: core simulator (`compute_portvals`)
* `orders/`: sample order files
* `additional_orders/`: additional test scenarios
* `tests/grade_marketsim.py`: course grading harness

## Skills Demonstrated

* Time-indexed portfolio accounting
* Transaction cost modeling
* Robust handling of multi-day trades and holdings propagation

## Run

```bash
python marketsim.py
```


