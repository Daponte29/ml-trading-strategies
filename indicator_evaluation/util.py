"""Shared utility helpers for reading data files used across projects."""

import os

import pandas as pd


def symbol_to_path(symbol, base_dir=None):
    """Return CSV file path for a ticker symbol."""
    if base_dir is None:
        base_dir = os.environ.get("MARKET_DATA_DIR", "../data/")
    return os.path.join(base_dir, f"{symbol}.csv")


def get_data(symbols, dates, addSPY=True, colname="Adj Close"):
    """Read stock data for symbols over dates using a selected column name."""
    df = pd.DataFrame(index=dates)

    symbols = list(symbols)
    if addSPY and "SPY" not in symbols:
        symbols = ["SPY"] + symbols

    for symbol in symbols:
        df_temp = pd.read_csv(
            symbol_to_path(symbol),
            index_col="Date",
            parse_dates=True,
            usecols=["Date", colname],
            na_values=["nan"],
        )
        df_temp = df_temp.rename(columns={colname: symbol})
        df = df.join(df_temp)

        if symbol == "SPY":
            df = df.dropna(subset=["SPY"])

    return df


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot a DataFrame with consistent axis labels."""
    import matplotlib.pyplot as plt

    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def get_orders_data_file(basefilename):
    return open(os.path.join(os.environ.get("ORDERS_DATA_DIR", "orders/"), basefilename))


def get_learner_data_file(basefilename):
    return open(
        os.path.join(os.environ.get("LEARNER_DATA_DIR", "Data/"), basefilename),
        "r",
    )


def get_robot_world_file(basefilename):
    return open(os.path.join(os.environ.get("ROBOT_WORLDS_DIR", "testworlds/"), basefilename))
