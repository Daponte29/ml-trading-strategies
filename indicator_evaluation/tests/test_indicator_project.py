import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

"""Run indicator generation and compare TOS against benchmark."""

import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from util import get_data
from indicators import compute_bollinger_bands, compute_cci, compute_ema, compute_macd, compute_rsi
import TheoreticallyOptimalStrategy as TOS
from marketsimcode import compute_portvals


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


if __name__ == "__main__":
    sd = dt.date(2008, 1, 1)
    ed = dt.date(2009, 12, 31)
    dates = pd.date_range(sd, ed)
    symbol = "JPM"

    prices = get_data([symbol], dates).drop(columns="SPY")
    normalized = prices / prices.iloc[0]

    compute_ema(normalized)
    compute_rsi(normalized)
    compute_bollinger_bands(normalized)

    high = get_data([symbol], dates, colname="High").drop(columns="SPY")
    low = get_data([symbol], dates, colname="Low").drop(columns="SPY")
    close = get_data([symbol], dates, colname="Adj Close").drop(columns="SPY")
    cci_input = pd.concat([high, low, close], axis=1)
    compute_cci(cci_input / cci_input.iloc[0])

    compute_macd(normalized)

    trades = TOS.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=100000)
    orders = pd.DataFrame(index=trades.index, columns=["Symbol", "Order", "Shares"])
    orders["Symbol"] = symbol
    orders["Order"] = trades[symbol].apply(lambda x: "BUY" if x > 0 else ("SELL" if x < 0 else "HOLD"))
    orders["Shares"] = trades[symbol].abs()
    orders = orders[orders["Order"] != "HOLD"]

    portvals = compute_portvals(orders, start_val=100000, commission=0.0, impact=0.0)
    portvals = portvals / portvals.iloc[0]

    benchmark = 1000 * get_data([symbol], dates, colname="Adj Close").drop(columns="SPY")
    benchmark = benchmark / benchmark.iloc[0, 0]

    fig = plt.figure()
    plt.plot(benchmark.index, benchmark[symbol], color="purple", label="Benchmark")
    plt.plot(portvals.index, portvals, color="red", label="TOS")
    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Normalized Value")
    plt.title("TOS Portfolio vs Benchmark")
    plt.xticks(rotation=45)
    plt.savefig("TOS Portfolio vs Benchmark.png")
    plt.close(fig)

