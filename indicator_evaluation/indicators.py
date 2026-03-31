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
5 Indicators Chosen:
    *EMA
    *RSI
    *Bollinger Bands
    *CCI
    *MACD
'''

def author(): 
    return 'ndaponte3'

def study_group():
   return 'ndaponte3' 

def compute_ema(df, span=30):
    ema_df = df.copy()
    ema_df['EMA'] = df['JPM'].ewm(span=span).mean()  

    plt.figure()
    plt.plot(ema_df.index, ema_df['JPM'], label='JPM')
    plt.plot(ema_df.index, ema_df['EMA'], label='EMA', color='red')
    plt.legend()
    plt.title('Exponential Moving Average (EMA)')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45) #Rotate x_labels
    plt.savefig('EMA.png')
    #plt.show()
    plt.close()

    return ema_df.dropna()

def compute_rsi(df, period=14):
    delta = df.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    rsi_df = pd.DataFrame(index=df.index)  # Create an empty DataFrame with the same index
    rsi_df['RSI'] = rsi

    plt.figure()
    plt.plot(rsi_df.index, rsi_df['RSI'], label='RSI')
    plt.axhline(70, color='r', linestyle='--', label='Overbought')
    plt.axhline(30, color='g', linestyle='--', label='Oversold')
    plt.legend()
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.savefig('RSI.png')
    #plt.show()
    plt.close()

    return rsi_df.dropna()

def compute_bollinger_bands(df, window=20):
    sma = df.rolling(window=window).mean()
    std = df.rolling(window=window).std()

    upper_band = sma + (2 * std)
    lower_band = sma - (2 * std)
    bbp = (df - lower_band) / (upper_band - lower_band)

    plt.figure(figsize=(10, 6))  # Adjust figure size as needed
    plt.plot(df.index, df, label='JPM')
    plt.plot(sma.index, sma, label='SMA', color='yellow')  # Plot SMA as black line
    plt.plot(upper_band.index, upper_band, label='Upper Band', color='red')  # Plot Upper Band as red line
    plt.plot(lower_band.index, lower_band, label='Lower Band', color='blue')  # Plot Lower Band as blue line
    plt.fill_between(df.index, lower_band.squeeze(), upper_band.squeeze(), color='grey', alpha=0.3)
    plt.legend()
    plt.title('Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Ensures labels fit nicely in the plot
    plt.savefig('Bollinger_Bands.png')
    #plt.show()
    plt.close()

    bb_df = pd.DataFrame(index=df.index)
    bb_df['Price'] = df.squeeze()
    bb_df['SMA'] = sma.squeeze()
    bb_df['Upper Band'] = upper_band.squeeze()
    bb_df['Lower Band'] = lower_band.squeeze()
    bb_df['BBP'] = bbp.squeeze()

    return bb_df.dropna()

def compute_cci(df, ndays=20):
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

    return cci_df.dropna()

def compute_macd(df, short_period=12, long_period=26, signal_period=9):
    short_ema = df.ewm(span=short_period, adjust=False).mean()
    long_ema = df.ewm(span=long_period, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_period, adjust=False).mean()

    macd_df = df.copy()
    macd_df['MACD'] = macd
    macd_df['Signal'] = signal

    plt.figure()
    plt.plot(macd_df.index, macd_df['MACD'], label='MACD')
    plt.plot(macd_df.index, macd_df['Signal'], label='Signal Line')
    plt.legend()
    plt.title('Moving Average Convergence Divergence (MACD)')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.ylabel('MACD Value')
    #plt.show()
    plt.savefig('MACD.png')
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
