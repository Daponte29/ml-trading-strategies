"""Experiment 1 utilities for comparing manual, learner, and benchmark strategies."""

import pandas as pd
import matplotlib.pyplot as plt
from marketsimcode import compute_portvals
from util import get_data


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def compute_benchmark(sd, ed, sv, symbol="JPM", impact=0.005):
    """Buy 1000 shares on first trading day and hold."""
    prices = get_data([symbol], pd.date_range(sd, ed))
    first_day = prices.index.min()

    trades = pd.DataFrame(0, index=prices.index, columns=[symbol], dtype=int)
    trades.at[first_day, symbol] = 1000

    vals = compute_portvals(trades, start_val=sv, commission=9.95, impact=impact)
    return vals / vals.iloc[0]


def print_stats(benchmark_series, strategy_series, filename):
    """Write cumulative return and daily-return stats to file."""
    if isinstance(benchmark_series, pd.DataFrame):
        benchmark_series = benchmark_series.iloc[:, 0]
    if isinstance(strategy_series, pd.DataFrame):
        strategy_series = strategy_series.iloc[:, 0]

    cr_b = benchmark_series.iloc[-1] / benchmark_series.iloc[0] - 1
    cr_s = strategy_series.iloc[-1] / strategy_series.iloc[0] - 1

    dr_b = benchmark_series.pct_change().dropna()
    dr_s = strategy_series.pct_change().dropna()

    with open(filename, "w") as fh:
        fh.write("[Strategy]\n")
        fh.write(f"Cumulative Return: {cr_s}\n")
        fh.write(f"Std Daily Return: {dr_s.std()}\n")
        fh.write(f"Avg Daily Return: {dr_s.mean()}\n\n")
        fh.write("[Benchmark]\n")
        fh.write(f"Cumulative Return: {cr_b}\n")
        fh.write(f"Std Daily Return: {dr_b.std()}\n")
        fh.write(f"Avg Daily Return: {dr_b.mean()}\n")


def plot_portfolio_values(manual_vals, learner_vals, benchmark_vals, sample="IN_SAMPLE", save_filename="IN_1.png"):
    """Save normalized portfolio comparison plot."""
    plt.figure(figsize=(12, 6))
    plt.plot(manual_vals.index, manual_vals, label="Manual", color="red")
    plt.plot(learner_vals.index, learner_vals, label="Learner", color="blue")
    plt.plot(benchmark_vals.index, benchmark_vals, label="Benchmark", color="purple")
    plt.title(f"Portfolio Value Comparison {sample}")
    plt.xlabel("Date")
    plt.ylabel("Normalized Value")
    plt.legend()
    plt.grid(True)
    plt.savefig(save_filename)
    plt.close()
