"""Indicator helpers shared by manual and learned strategies."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def compute_rsi(df, period=14):
    """Compute RSI series for a single-symbol price DataFrame."""
    delta = df.diff(1)
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    result = pd.DataFrame(index=df.index)
    result["RSI"] = rsi
    return result


def compute_bollinger_bands(df, window=20):
    """Compute SMA, upper/lower bands, and normalized Bollinger value."""
    symbol = df.columns[0]
    rolling_mean = df[symbol].rolling(window).mean()
    rolling_std = df[symbol].rolling(window).std()
    upper = rolling_mean + 2 * rolling_std
    lower = rolling_mean - 2 * rolling_std
    value = (df[symbol] - rolling_mean) / (2 * rolling_std)

    return pd.DataFrame(
        {
            symbol: df[symbol],
            "SMA": rolling_mean,
            "bollinger_upper": upper,
            "bollinger_lower": lower,
            "bollinger": value,
        },
        index=df.index,
    )


def compute_cci(df, ndays=5):
    """Compute CCI from high/low/close input frame."""
    typical_price = (df.iloc[:, 0] + df.iloc[:, 1] + df.iloc[:, 2]) / 3
    sma = typical_price.rolling(window=ndays).mean()
    mad = typical_price.rolling(window=ndays).apply(lambda x: np.fabs(x - x.mean()).mean())
    cci = (typical_price - sma) / (0.015 * mad)

    out = df.copy()
    out["CCI"] = cci
    return out
