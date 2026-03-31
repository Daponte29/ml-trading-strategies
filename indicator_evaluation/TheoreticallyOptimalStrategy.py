"""Theoretically optimal strategy that looks one day ahead."""

import datetime as dt
import pandas as pd
from util import get_data


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000):
    prices = get_data([symbol], pd.date_range(sd, ed)).drop(columns=["SPY"])
    daily_change = prices.diff()

    trades = pd.DataFrame(0.0, index=prices.index, columns=[symbol])
    holdings = 0

    for i in range(1, len(prices)):
        if daily_change.iloc[i - 1, 0] > 0:
            target = 1000
        elif daily_change.iloc[i - 1, 0] < 0:
            target = -1000
        else:
            target = holdings

        trades.iloc[i, 0] = target - holdings
        holdings = target

    return trades
