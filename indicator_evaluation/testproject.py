# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:17:09 2024

@author: nolot
"""

from util import get_data
from indicators import compute_bollinger_bands, compute_cci, compute_ema, compute_macd, compute_rsi
import TheoreticallyOptimalStrategy as TOS
from marketsimcode import compute_portvals
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt


def author(): 
        return 'ndaponte3'

def study_group():
   return 'ndaponte3' 










if __name__ == "__main__":
    '''Technical Indicators'''
    sd = dt.date(2008, 1, 1)
    ed = dt.date(2009, 12, 31)
    dates = pd.date_range(sd, ed)
    symbols = ["JPM"]
    
    df = get_data(symbols, dates)
    df = df.drop(columns='SPY')
    normalized = df / df.iloc[0]  # Normalize JPM price
    
    #Indicator 1--------------------------
    ema_df = compute_ema(normalized)
    #Indicator 2-------------------------
    rsi_df = compute_rsi(normalized)
    #Indicator 3-----------------------
    bollinger_df = compute_bollinger_bands(normalized)
    #Indicator 4----------------------------
    ccd_df_high = get_data(symbols, dates, colname="High")
    ccd_df_high = ccd_df_high.drop(columns='SPY')
    ccd_df_low = get_data(symbols, dates,  colname="Low")
    ccd_df_low = ccd_df_low.drop(columns='SPY')
    ccd_df_close = get_data(symbols, dates,  colname="Adj Close")
    ccd_df_close = ccd_df_close.drop(columns='SPY')
    ccd_concat = pd.concat([ccd_df_high, ccd_df_low, ccd_df_close], axis=1)
    ccd_df_normalized = ccd_concat / ccd_concat.iloc[0]
    cci_df = compute_cci(ccd_df_normalized)
    
    #Indicator 5-----------------------------
    macd_df = compute_macd(normalized)
    
    
    ''' TOS '''
    #Get trades
    df_trades = TOS.testPolicy(symbol="JPM", sd=sd, ed=ed, sv=100000)
    
    #Create orders
    orders = pd.DataFrame(index=df_trades.index.values, columns=["JPM", "Order", "Shares"])
    orders["Order"] = df_trades.where(df_trades > 0, "BUY").where(df_trades < 0, "SELL")
    orders["Shares"] = abs(df_trades)
    
    #Portfolio Value
    port_value = compute_portvals(orders, start_val=100000, commission=0.0, impact=0.000)
    port_value = port_value / port_value.iloc[0]
    #Compare to Benchmark
    
    bench_data = 1000 * get_data(symbols, pd.date_range(sd, ed), colname="Adj Close").drop(columns="SPY") # 1000 shares hold
    bench_data["Benchmark"] = bench_data / bench_data.iloc[0, 0]
    bench_data["Portfolio"] = port_value
    
    #Generate Chart of Portfolio Vs. Benchmark for this Strategy of Trading
    fig = plt.figure()
    plt.plot(bench_data.Benchmark, 'purple')
    plt.plot(bench_data.Portfolio, 'r')
    plt.legend(["Benchmark", "Portfolio"])
    plt.xlabel("Date")
    plt.xticks(rotation=45) #Rotate x_labels
    plt.ylabel("Portfolio Value")
    plt.title("TOS Portfolio vs Benchmark")
    #plt.show()
    plt.savefig("TOS Portfolio vs Benchmark.png")
    plt.close()
    
    #Generate some stats on the Portfolio and Benchmark
    daily_rets = bench_data.diff().dropna()
    # Bench
    
    bench_std = round(daily_rets.Benchmark.std(), 3)
    bench_cum_rets = round(daily_rets.Benchmark.sum(), 3)
    bench_avg_rets = round(daily_rets.Benchmark.mean(), 3)
    
    # TOS
    port_std = round(daily_rets.Portfolio.std(), 3)
    port_cum_rets = round(daily_rets.Portfolio.sum(), 3)
    port_avg_rets = round(daily_rets.Portfolio.mean(), 34)

    # Output
    headers = ['Portfolio', 'STD', 'Cumulative Rets', 'Average Rets']
    rows = [['Benchmark', bench_std, bench_cum_rets, bench_avg_rets],
            ['TOS', port_std, port_cum_rets, port_avg_rets]]

    df = pd.DataFrame(data=rows, columns=headers)
    df.to_csv(r'P6_Table.txt', header=True, index=None, sep='\t', mode='a')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
