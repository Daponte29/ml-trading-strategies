"""Experiment 2 utilities for analyzing strategy learner sensitivity to impact."""

import pandas as pd
import matplotlib.pyplot as plt
from marketsimcode import compute_portvals
from util import get_data


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def compute_benchmark2(sd, ed, sv, symbol="JPM", impact=0.005):
    prices = get_data([symbol], pd.date_range(sd, ed))
    first_day = prices.index.min()
    trades = pd.DataFrame(0, index=prices.index, columns=[symbol], dtype=int)
    trades.at[first_day, symbol] = 1000
    vals = compute_portvals(trades, start_val=sv, commission=9.95, impact=impact)
    return vals / vals.iloc[0]


def print_stats2(benchmark_series, learner_series, filename):
    if isinstance(benchmark_series, pd.DataFrame):
        benchmark_series = benchmark_series.iloc[:, 0]
    if isinstance(learner_series, pd.DataFrame):
        learner_series = learner_series.iloc[:, 0]

    cr_b = benchmark_series.iloc[-1] / benchmark_series.iloc[0] - 1
    cr_l = learner_series.iloc[-1] / learner_series.iloc[0] - 1
    dr_b = benchmark_series.pct_change().dropna()
    dr_l = learner_series.pct_change().dropna()

    with open(filename, "w") as fh:
        fh.write("[Learner]\n")
        fh.write(f"Cumulative Return: {cr_l}\n")
        fh.write(f"Std Daily Return: {dr_l.std()}\n")
        fh.write(f"Avg Daily Return: {dr_l.mean()}\n\n")
        fh.write("[Benchmark]\n")
        fh.write(f"Cumulative Return: {cr_b}\n")
        fh.write(f"Std Daily Return: {dr_b.std()}\n")
        fh.write(f"Avg Daily Return: {dr_b.mean()}\n")


def plot_portfolio_values2(learner_vals, benchmark_vals, sample="IN_SAMPLE", save_filename="IN_impact.png"):
    plt.figure(figsize=(12, 6))
    plt.plot(learner_vals.index, learner_vals, color="blue", label="Learner")
    plt.plot(benchmark_vals.index, benchmark_vals, color="purple", label="Benchmark")
    plt.title(f"Portfolio Value Comparison {sample}")
    plt.xlabel("Date")
    plt.ylabel("Normalized Value")
    plt.legend()
    plt.grid(True)
    plt.savefig(save_filename)
    plt.close()
