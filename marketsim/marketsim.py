"""Market simulator for processing historical orders into portfolio values."""

import pandas as pd
from util import get_data


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def compute_portvals(
    orders_file="./orders/orders.csv",
    start_val=1000000,
    commission=9.95,
    impact=0.005,
):
    """Compute daily portfolio values from an orders CSV file."""
    orders = pd.read_csv(orders_file, index_col="Date", parse_dates=True).sort_index()

    symbols = sorted(orders["Symbol"].unique().tolist())
    dates = pd.date_range(orders.index.min(), orders.index.max())
    prices = get_data(symbols, dates)
    if "SPY" not in symbols and "SPY" in prices.columns:
        prices = prices.drop(columns=["SPY"])

    prices["Cash"] = 1.0
    trades = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)

    for trade_date, row in orders.iterrows():
        symbol = row["Symbol"]
        shares = float(row["Shares"])
        signed_shares = shares if row["Order"] == "BUY" else -shares
        trade_price = prices.loc[trade_date, symbol]

        trades.loc[trade_date, symbol] += signed_shares
        cash_change = -(signed_shares * trade_price)
        cash_change -= commission
        cash_change -= abs(signed_shares) * trade_price * impact
        trades.loc[trade_date, "Cash"] += cash_change

    holdings = trades.cumsum()
    holdings.loc[holdings.index[0], "Cash"] += start_val
    holdings["Cash"] = holdings["Cash"].ffill()

    values = holdings * prices
    portvals = values.sum(axis=1)
    return portvals


def test_code():
    """Simple local sanity run."""
    vals = compute_portvals()
    print(vals.head())
    print(vals.tail())


if __name__ == "__main__":
    test_code()
