"""Market simulator helper for indicator evaluation workflows."""

import pandas as pd
from util import get_data


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def compute_portvals(orders, start_val=100000, commission=0.0, impact=0.0):
    """Compute portfolio values from orders DataFrame with Symbol/Order/Shares."""
    if orders.empty:
        return pd.Series(dtype=float)

    orders = orders.sort_index().copy()
    symbols = sorted(orders["Symbol"].unique().tolist())

    dates = pd.date_range(orders.index.min(), orders.index.max())
    prices = get_data(symbols, dates)
    if "SPY" in prices.columns and "SPY" not in symbols:
        prices = prices.drop(columns=["SPY"])

    prices["Cash"] = 1.0
    trades = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)

    for date, row in orders.iterrows():
        symbol = row["Symbol"]
        shares = float(row["Shares"])
        signed = shares if row["Order"] == "BUY" else -shares
        px = prices.at[date, symbol]

        trades.at[date, symbol] += signed
        trades.at[date, "Cash"] -= signed * px
        trades.at[date, "Cash"] -= commission
        trades.at[date, "Cash"] -= abs(signed) * px * impact

    holdings = trades.cumsum()
    holdings["Cash"] += start_val

    values = holdings * prices
    return values.sum(axis=1)
