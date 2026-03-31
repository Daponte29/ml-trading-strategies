"""Bagged random-tree strategy learner for trade generation."""

import datetime as dt
import numpy as np
import pandas as pd
import util as ut
import RTLearner as rt
import BagLearner as bl
from indicators import compute_bollinger_bands, compute_cci, compute_rsi


class StrategyLearner(object):
    """Learn a mapping from indicators to {-1, 0, 1} trading signals."""

    def __init__(self, verbose=False, impact=0.005, commission=9.95):
        self.verbose = verbose
        self.impact = impact
        self.commission = commission
        self.learner = bl.BagLearner(
            learner=rt.RTLearner,
            kwargs={"leaf_size": 5},
            bags=20,
            boost=False,
            verbose=False,
        )

    def _build_indicators(self, symbol, sd, ed, window=5):
        dates = pd.date_range(sd, ed)
        prices = ut.get_data([symbol], dates).drop(columns=["SPY"])
        normed = prices / prices.iloc[0]

        bb = compute_bollinger_bands(normed, window=window)[["bollinger"]]
        rsi = compute_rsi(prices, period=window)[["RSI"]]

        high = ut.get_data([symbol], dates, colname="High").drop(columns=["SPY"])
        low = ut.get_data([symbol], dates, colname="Low").drop(columns=["SPY"])
        close = ut.get_data([symbol], dates, colname="Adj Close").drop(columns=["SPY"])
        cci_input = pd.concat([high, low, close], axis=1)
        cci = compute_cci(cci_input, ndays=window)[["CCI"]]

        indicators = pd.concat([bb, cci, rsi], axis=1)
        indicators.columns = ["bollinger", "cci", "rsi"]
        indicators = indicators.fillna(0.0)
        return prices, indicators

    def add_evidence(
        self,
        symbol="IBM",
        sd=dt.datetime(2008, 1, 1),
        ed=dt.datetime(2009, 1, 1),
        sv=10000,
    ):
        prices, indicators = self._build_indicators(symbol, sd, ed)

        lookahead = 5
        x_train = indicators.iloc[:-lookahead].values
        y_train = []

        for i in range(prices.shape[0] - lookahead):
            future_ret = (prices.iloc[i + lookahead, 0] - prices.iloc[i, 0]) / prices.iloc[i, 0]
            if future_ret > (0.02 + self.impact):
                y_train.append(1)
            elif future_ret < (-0.02 - self.impact):
                y_train.append(-1)
            else:
                y_train.append(0)

        self.learner.add_evidence(x_train, np.array(y_train))

    def testPolicy(
        self,
        symbol="IBM",
        sd=dt.datetime(2009, 1, 1),
        ed=dt.datetime(2010, 1, 1),
        sv=10000,
    ):
        prices, indicators = self._build_indicators(symbol, sd, ed)
        predictions = self.learner.query(indicators.values)

        trades = pd.DataFrame(0, index=prices.index, columns=[symbol], dtype=int)
        holdings = 0

        for i, day in enumerate(prices.index):
            signal = predictions[i]
            if signal > 0 and holdings <= 0:
                target = 1000
            elif signal < 0 and holdings >= 0:
                target = -1000
            else:
                target = holdings

            trades.at[day, symbol] = target - holdings
            holdings = target

        return trades

    def author(self):
        return "ndaponte3"

    def study_group(self):
        return "ndaponte3"
