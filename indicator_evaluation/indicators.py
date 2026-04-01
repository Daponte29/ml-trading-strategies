"""Technical indicators used by indicator and strategy evaluation projects."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def _single_symbol(df):
    """Return the single symbol column name for one-asset indicator inputs."""
    if len(df.columns) != 1:
        raise ValueError("Expected a single-symbol DataFrame input.")
    return df.columns[0]


def compute_ema(df, span=30):
    """Compute and plot Exponential Moving Average."""
    symbol = _single_symbol(df)
    ema_df = df.copy()
    ema_df["EMA"] = ema_df[symbol].ewm(span=span).mean()

    plt.figure()
    plt.plot(ema_df.index, ema_df[symbol], label=symbol)
    plt.plot(ema_df.index, ema_df["EMA"], label="EMA", color="red")
    plt.legend()
    plt.title(f"Exponential Moving Average (EMA) - {symbol}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.savefig("EMA.png")
    plt.close()

    return ema_df.dropna()


def compute_rsi(df, period=14):
    """Compute and plot Relative Strength Index."""
    delta = df.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    rsi_df = pd.DataFrame(index=df.index)
    rsi_df["RSI"] = rsi

    plt.figure()
    plt.plot(rsi_df.index, rsi_df["RSI"], label="RSI")
    plt.axhline(70, color="r", linestyle="--", label="Overbought")
    plt.axhline(30, color="g", linestyle="--", label="Oversold")
    plt.legend()
    plt.title("Relative Strength Index (RSI)")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.savefig("RSI.png")
    plt.close()

    return rsi_df.dropna()


def compute_bollinger_bands(df, window=20):
    """Compute and plot Bollinger Bands plus BBP."""
    symbol = _single_symbol(df)
    sma = df.rolling(window=window).mean()
    std = df.rolling(window=window).std()
    upper_band = sma + (2 * std)
    lower_band = sma - (2 * std)
    bbp = (df - lower_band) / (upper_band - lower_band)

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df[symbol], label=symbol)
    plt.plot(sma.index, sma, label="SMA", color="yellow")
    plt.plot(upper_band.index, upper_band, label="Upper Band", color="red")
    plt.plot(lower_band.index, lower_band, label="Lower Band", color="blue")
    plt.fill_between(df.index, lower_band.squeeze(), upper_band.squeeze(), color="grey", alpha=0.3)
    plt.legend()
    plt.title("Bollinger Bands")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Bollinger_Bands.png")
    plt.close()

    bb_df = pd.DataFrame(index=df.index)
    bb_df["Price"] = df[symbol]
    bb_df["SMA"] = sma.squeeze()
    bb_df["Upper Band"] = upper_band.squeeze()
    bb_df["Lower Band"] = lower_band.squeeze()
    bb_df["BBP"] = bbp.squeeze()
    return bb_df.dropna()


def compute_cci(df, ndays=20):
    """Compute and plot Commodity Channel Index from high/low/close frame."""
    typical_price = (df.iloc[:, 0] + df.iloc[:, 1] + df.iloc[:, 2]) / 3
    sma = typical_price.rolling(window=ndays).mean()
    mad = typical_price.rolling(window=ndays).apply(lambda x: np.fabs(x - x.mean()).mean())
    cci = (typical_price - sma) / (0.015 * mad)

    cci_df = df.copy()
    cci_df["CCI"] = cci

    plt.figure()
    plt.plot(cci_df.index, cci_df["CCI"], label="CCI")
    plt.axhline(100, color="r", linestyle="--", label="Overbought")
    plt.axhline(-100, color="g", linestyle="--", label="Oversold")
    plt.legend()
    plt.title("Commodity Channel Index (CCI)")
    plt.xlabel("Date")
    plt.ylabel("CCI Value")
    plt.xticks(rotation=45)
    plt.savefig("CCI.png")
    plt.close()

    return cci_df.dropna()


def compute_macd(df, short_period=12, long_period=26, signal_period=9):
    """Compute and plot MACD and signal line."""
    symbol = _single_symbol(df)
    short_ema = df.ewm(span=short_period, adjust=False).mean()
    long_ema = df.ewm(span=long_period, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_period, adjust=False).mean()

    macd_df = df.copy()
    macd_df["MACD"] = macd
    macd_df["Signal"] = signal

    plt.figure()
    plt.plot(macd_df.index, macd_df["MACD"], label="MACD")
    plt.plot(macd_df.index, macd_df["Signal"], label="Signal Line")
    plt.legend()
    plt.title(f"Moving Average Convergence Divergence (MACD) - {symbol}")
    plt.xlabel("Date")
    plt.ylabel("MACD Value")
    plt.xticks(rotation=45)
    plt.savefig("MACD.png")
    plt.close()

    return macd_df.dropna()
#Example Usage and Test
# if __name__ == "__main__":
#     dates = pd.date_range('2008-01-01', '2009-12-31')
#     symbols = ['JPM']
#     df = get_data(symbols, dates)
#     df = df.drop(columns='SPY')
#     normalized = df / df.iloc[0]  # Normalize JPM price
#     #Indicator 1
#     ema_df = compute_ema(normalized)
#     #Indicator 2
#     rsi_df = compute_rsi(normalized)
#     #Indicator 3
#     bollinger_df = compute_bollinger_bands(normalized)
#     #Indicator 4
#     ccd_df_high = get_data(symbols, dates, colname="High")
#     ccd_df_high = ccd_df_high.drop(columns='SPY')
#     ccd_df_low = get_data(symbols, dates,  colname="Low")
#     ccd_df_low = ccd_df_low.drop(columns='SPY')
#     ccd_df_close = get_data(symbols, dates,  colname="Adj Close")
#     ccd_df_close = ccd_df_close.drop(columns='SPY')
#     ccd_concat = pd.concat([ccd_df_high, ccd_df_low, ccd_df_close], axis=1)
#     ccd_df_normalized = ccd_concat / ccd_concat.iloc[0]
#     cci_df = compute_cci(ccd_df_normalized)
    
#     #Indicator 5
#     macd_df = compute_macd(normalized)
