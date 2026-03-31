# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:17:11 2024

@author: nolot
"""
import pandas as pd
import numpy as np
from util import get_data
import matplotlib.dates as mdates
import datetime as dt
import matplotlib.pyplot as plt
#--------------------------------------------------

'''
Using Indicators:
    *CCI(Commodity Channel Index)
    *RSI
    *Bollinger Bands
For Project 8
'''
 




def compute_rsi(df, period=14):
    # Calculate price changes
    delta = df.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Compute rolling averages of gains and losses
    avg_gain = gain.rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()

    # Calculate RS and RSI
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    # Create DataFrame for RSI
    rsi_df = pd.DataFrame(index=df.index)
    rsi_df['RSI'] = rsi

    # Plot RSI
    plt.figure()
    plt.plot(rsi_df.index, rsi_df['RSI'], label='RSI')
    plt.axhline(70, color='r', linestyle='--', label='Overbought')
    plt.axhline(30, color='g', linestyle='--', label='Oversold')
    plt.legend()
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    #plt.savefig('RSI.png')
    #plt.show()
    plt.close()

    return rsi_df

def compute_bollinger_bands(df, window=20):
    symbol = df.columns[0]
    rolling_mean = df[symbol].rolling(window).mean()
    rolling_std = df[symbol].rolling(window).std()
    bollinger_upper = rolling_mean + (rolling_std * 2)
    bollinger_lower = rolling_mean - (rolling_std * 2)
    bollinger_value = (df[symbol] - rolling_mean) / (rolling_std * 2)
    return pd.DataFrame({
        symbol: df[symbol], 
        'SMA': rolling_mean, 
        'bollinger_upper': bollinger_upper, 
        'bollinger_lower': bollinger_lower, 
        'bollinger': bollinger_value
    }, index=df.index)


def compute_cci(df, ndays=5):
    tp = (df.iloc[:, 0] + df.iloc[:, 1] + df.iloc[:, 2]) / 3 
    sma = tp.rolling(window=ndays).mean()
    mad = tp.rolling(window=ndays).apply(lambda x: np.fabs(x - x.mean()).mean())

    cci = (tp - sma) / (0.015 * mad)

    cci_df = df.copy()
    cci_df['CCI'] = cci

    plt.figure()
    plt.plot(cci_df.index, cci_df['CCI'], label='CCI')
    plt.axhline(100, color='r', linestyle='--', label='Overbought')
    plt.axhline(-100, color='g', linestyle='--', label='Oversold')
    plt.legend()
    plt.title('Commodity Channel Index (CCI)')
    plt.xlabel('Date')
    plt.xticks(rotation=45) #Rotate x_labels
    plt.ylabel('CCI Value')
    plt.savefig('CCI.png')  # Save the figure before showing
    #plt.show()
    plt.close()

    return cci_df






def author():
    return 'ndaponte3'

def study_group():
   return 'ndaponte3'

#Example Usage and Test
# if __name__ == "__main__":
#     dates = pd.date_range('2008-01-01', '2009-12-31')
#     symbols = ['JPM']
#     df = get_data(symbols, dates)
#     df = df.drop(columns='SPY')
#     normalized = df / df.iloc[0]  # Normalize JPM price
#     # #Indicator 1
#     # ema_df = compute_ema(normalized)
#     # #Indicator 2
#     # rsi_df = compute_rsi(normalized)
#     # #Indicator 3
#     # bollinger_df = compute_bollinger_bands(normalized)
#      #Indicator 4
#     ccd_df_high = get_data(symbols, dates, colname="High")
#     ccd_df_high = ccd_df_high.drop(columns='SPY')
#     ccd_df_low = get_data(symbols, dates,  colname="Low")
#     ccd_df_low = ccd_df_low.drop(columns='SPY')
#     ccd_df_close = get_data(symbols, dates,  colname="Adj Close")
#     ccd_df_close = ccd_df_close.drop(columns='SPY')
#     ccd_concat = pd.concat([ccd_df_high, ccd_df_low, ccd_df_close], axis=1)
#     ccd_df_normalized = ccd_concat / ccd_concat.iloc[0]
#     cci_df = compute_cci(ccd_df_normalized,ndays=5)
