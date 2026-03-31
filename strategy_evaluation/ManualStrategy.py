"""Rule-based manual strategy using CCI, RSI, and Bollinger value."""

import pandas as pd
from util import get_data
from indicators import compute_bollinger_bands, compute_cci, compute_rsi


class ManualStrategy(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def testPolicy(self, symbol="JPM", sd=None, ed=None, sv=100000):
        """Generate signed-share trades constrained to holdings in {-1000,0,1000}."""
        dates = pd.date_range(sd, ed)
        prices = get_data([symbol], dates).drop(columns=["SPY"])
        normed = prices / prices.iloc[0]

        high = get_data([symbol], dates, colname="High").drop(columns=["SPY"])
        low = get_data([symbol], dates, colname="Low").drop(columns=["SPY"])
        close = get_data([symbol], dates, colname="Adj Close").drop(columns=["SPY"])
        cci_input = pd.concat([high, low, close], axis=1)

        cci = compute_cci(cci_input, ndays=5)["CCI"]
        bb = compute_bollinger_bands(normed, window=5)["bollinger"]
        rsi = compute_rsi(prices, period=5)["RSI"]

        trades = pd.DataFrame(0, index=prices.index, columns=[symbol], dtype=int)
        position = 0

        for day in prices.index:
            cci_val = cci.loc[day]
            bb_val = bb.loc[day]
            rsi_val = rsi.loc[day]

            buy_signal = bb_val < -0.5 and cci_val < -100 and rsi_val < 30
            sell_signal = bb_val > 0.5 and cci_val > 100 and rsi_val > 70

            if buy_signal and position <= 0:
                target = 1000
            elif sell_signal and position >= 0:
                target = -1000
            else:
                target = position

            trades.at[day, symbol] = target - position
            position = target

        return trades


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"
