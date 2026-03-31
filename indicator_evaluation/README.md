# Indicator Evaluation

## Overview
This project builds and evaluates technical indicators for algorithmic trading research.
It computes indicators and compares a Theoretically Optimal Strategy (TOS) against a benchmark portfolio.

Indicators used include:
- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- Bollinger Bands / Bollinger Band Percentage
- Commodity Channel Index (CCI)
- MACD and signal line

## Key Files
- `indicators.py`: indicator implementations
- `TheoreticallyOptimalStrategy.py`: optimal hindsight strategy logic
- `marketsimcode.py`: portfolio simulation engine
- `testproject.py`: project runner that generates figures and summary table

## Skills Demonstrated
- Feature engineering for financial time series
- Trading signal intuition and indicator diagnostics
- Strategy-vs-benchmark backtesting workflow

## Run
```bash
python testproject.py
```

## Outputs
- Indicator figures (`EMA.png`, `RSI.png`, `MACD.png`, `CCI.png`, `Bollinger_Bands.png`)
- Strategy comparison plot (`TOS Portfolio vs Benchmark.png`)
- Summary table (`P6_Table.txt`)
