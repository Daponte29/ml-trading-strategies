"""Portfolio optimization via Sharpe ratio maximization."""

import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.optimize as spo
from util import get_data


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def assess_portfolio(allocs, prices):
    """Return normalized portfolio value and common performance statistics."""
    normed = prices / prices.iloc[0]
    alloced = normed * allocs
    port_val = alloced.sum(axis=1)

    daily_returns = port_val.pct_change().dropna()
    cr = port_val.iloc[-1] / port_val.iloc[0] - 1
    adr = daily_returns.mean()
    sddr = daily_returns.std()
    sr = np.sqrt(252) * (adr / sddr) if sddr != 0 else 0.0

    return port_val, cr, adr, sddr, sr


def min_sharpe_ratio(allocs, prices):
    """Objective for optimizer: minimize negative Sharpe ratio."""
    return -assess_portfolio(allocs, prices)[4]


def optimize_portfolio(
    sd=dt.datetime(2008, 1, 1),
    ed=dt.datetime(2009, 1, 1),
    syms=None,
    gen_plot=False,
):
    """Find allocation vector that maximizes Sharpe ratio."""
    if syms is None:
        syms = ["GOOG", "AAPL", "GLD", "XOM"]

    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)
    prices = prices_all[syms]
    prices_spy = prices_all["SPY"]

    n_assets = len(syms)
    guess = np.ones(n_assets) / n_assets
    bounds = [(0.0, 1.0)] * n_assets
    constraints = ({"type": "eq", "fun": lambda allocs: 1.0 - np.sum(allocs)},)

    result = spo.minimize(
        min_sharpe_ratio,
        guess,
        args=(prices,),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )
    allocs = result.x

    port_val, cr, adr, sddr, sr = assess_portfolio(allocs, prices)

    if gen_plot:
        comparison = pd.concat(
            [port_val / port_val.iloc[0], prices_spy / prices_spy.iloc[0]],
            axis=1,
            keys=["Portfolio", "SPY"],
        )
        ax = comparison.plot(title="Normalized Daily Portfolio Value vs SPY")
        ax.set_xlabel("Date")
        ax.set_ylabel("Normalized Value")
        plt.grid(True)
        plt.savefig("Figure1.png")
        plt.close()

    return allocs, cr, adr, sddr, sr


def test_code():
    allocs, cr, adr, sddr, sr = optimize_portfolio(
        sd=dt.datetime(2008, 6, 1),
        ed=dt.datetime(2009, 6, 1),
        syms=["IBM", "X", "GLD", "JPM"],
        gen_plot=True,
    )
    print("Allocations:", allocs)
    print("CR:", cr, "ADR:", adr, "SDDR:", sddr, "SR:", sr)


if __name__ == "__main__":
    test_code()
