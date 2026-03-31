"""Portfolio simulator for strategy evaluation projects."""

import pandas as pd
from util import get_data


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def compute_portvals(trades_df, start_val=1000000, commission=0.0, impact=0.0):
    """Compute portfolio value series from a signed-share trades DataFrame."""
    trades_df = trades_df.sort_index().copy()
    symbols = trades_df.columns.tolist()

    dates = pd.date_range(trades_df.index.min(), trades_df.index.max())
    prices = get_data(symbols, dates)
    prices = prices[symbols]
    prices["Cash"] = 1.0

    trades = trades_df.reindex(prices.index).fillna(0.0)
    trades["Cash"] = 0.0

    for date in trades.index:
        for symbol in symbols:
            shares = trades.at[date, symbol]
            if shares == 0:
                continue
            px = prices.at[date, symbol]
            trades.at[date, "Cash"] -= shares * px
            trades.at[date, "Cash"] -= commission
            trades.at[date, "Cash"] -= abs(shares) * px * impact

    holdings = trades.cumsum()
    holdings["Cash"] += start_val

    values = holdings * prices
    portvals = values.sum(axis=1)
    return portvals.to_frame(name="Value")
