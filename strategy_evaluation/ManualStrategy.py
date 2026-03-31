# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:06:10 2024

@author: nolot
"""
import pandas as pd
import numpy as np
import datetime as dt
from util import get_data, plot_data
from marketsimcode import compute_portvals
from indicators import compute_bollinger_bands, compute_cci , compute_rsi
import matplotlib.pyplot as plt







class ManualStrategy:
    def __init__(self):
        pass

    def testPolicy(self, symbol, sd, ed, sv):
        # Setup
        # symbol = symbol[0]
        dates = pd.date_range(sd, ed)
        prices = get_data([symbol], dates)
        prices = prices.drop(columns=['SPY'])
        normalized = prices / prices.iloc[0]
        
        # Compute indicators
        #cci pre work 
        ccd_df_high = get_data([symbol], dates, colname="High")
        ccd_df_high = ccd_df_high.drop(columns='SPY')
        ccd_df_low = get_data([symbol], dates,  colname="Low")
        ccd_df_low = ccd_df_low.drop(columns='SPY')
        ccd_df_close = get_data([symbol], dates,  colname="Adj Close")
        ccd_df_close = ccd_df_close.drop(columns='SPY')
        ccd_concat = pd.concat([ccd_df_high, ccd_df_low, ccd_df_close], axis=1)
        ccd_df_normalized = ccd_concat / ccd_concat.iloc[0]
        
        cci = compute_cci(ccd_df_normalized, ndays=5)
        bollinger = compute_bollinger_bands(normalized, window=5)
        rsi = compute_rsi(prices ,period=5)
        
        # Initialize
        df_trades = pd.DataFrame(columns=['Date', 'Symbol', 'Order', 'Shares'])
        flag = 0  # Flag: 1 - long, -1 - short, 0 - neutral
        index = 0

        for i in range(len(normalized) - 1):
            today = normalized.index[i]
            next_day = normalized.index[i + 1]
            
            # Get indicator values
            cci_today = cci.loc[today, 'CCI']
            bollinger_today = bollinger.loc[today]
            rsi_today = rsi.loc[today, 'RSI']
            # Get the stock price for today
            today_value = normalized.loc[today, symbol]
        
           # Trading logic
            if flag == 0:
                # Buy conditions
                if today_value < bollinger_today['bollinger'] and cci_today < -100 and rsi_today < 30:
                    df_trades.loc[index] = [today.strftime('%Y-%m-%d'), symbol, 'BUY', 1000]
                    flag = 1
                    index += 1
                # Sell conditions
                elif today_value > bollinger_today['bollinger'] and cci_today > 100 and rsi_today > 70:
                    df_trades.loc[index] = [today.strftime('%Y-%m-%d'), symbol, 'SELL', 1000]
                    flag = -1
                    index += 1
            elif flag == 1:
                # Sell conditions for existing long position
                if today_value > bollinger_today['bollinger'] and cci_today > 100 and rsi_today > 70:
                    df_trades.loc[index] = [today.strftime('%Y-%m-%d'), symbol, 'SELL', 1000]
                    flag = 0
                    index += 1
            elif flag == -1:
                # Buy conditions for existing short position
                if today_value < bollinger_today['bollinger'] and cci_today < -100 and rsi_today < 30:
                    df_trades.loc[index] = [today.strftime('%Y-%m-%d'), symbol, 'BUY', 1000]
                    flag = 0
                    index += 1
        
        # Closing position if open
        if flag == 1:
            df_trades.loc[index] = [normalized.index[-1].strftime('%Y-%m-%d'), symbol, 'SELL', 1000]
        elif flag == -1:
            df_trades.loc[index] = [normalized.index[-1].strftime('%Y-%m-%d'), symbol, 'BUY', 1000]
        #Fix error:
        df_trades['Date'] = pd.to_datetime(df_trades['Date'])
        df_trades.set_index('Date', inplace=True)
        df_trades['Shares'] = df_trades.apply(lambda row: row['Shares'] if row['Order'] == 'BUY' else -row['Shares'], axis=1)
        df_trades.drop(columns=['Symbol', 'Order'], inplace=True)
        df_trades.rename(columns={'Shares': symbol}, inplace=True)

        return df_trades
        
             
                
     
        
     
        
     
        def author(self):
        def study_group(self):
           return 'ndaponte3'
#---------------------------------------OUT OF CLASS-------------------------------------------------------------
def compute_benchmark(sd, ed, sv):
    # Get the first trading day in the range
    dates = pd.date_range(sd, ed)
    prices = get_data(['JPM'], dates)
    first_trading_day = prices.index.min()

    # Create a DataFrame for the buy and hold strategy
    df_trades = pd.DataFrame(columns=['Date', 'Symbol', 'Order', 'Shares'])
    df_trades.loc[0] = [first_trading_day.strftime('%Y-%m-%d'), 'JPM', 'BUY', 1000]

    # Compute portfolio values
    portvals = compute_portvals(df_trades, sv, commission=9.95, impact=0.005)
    
    return portvals / portvals[0]

def print_stats(benchmark, manual_strategy):
    benchmark = benchmark['Value']
    manual_strategy = manual_strategy['Value']

    # Cumulative Return
    cr_ben = benchmark.iloc[-1] / benchmark.iloc[0] - 1
    cr_the = manual_strategy.iloc[-1] / manual_strategy.iloc[0] - 1

    # Daily Returns
    dr_ben = (benchmark / benchmark.shift(1)) - 1
    dr_the = (manual_strategy / manual_strategy.shift(1)) - 1

    # Stats
    sddr_ben = dr_ben.std()
    sddr_the = dr_the.std()
    adr_ben = dr_ben.mean()
    adr_the = dr_the.mean()

    print("\n[Manual Strategy]")
    print("Cumulative Return: {:.2f}".format(cr_the))
    print("Standard Deviation of Daily Returns: {:.2f}".format(sddr_the))
    print("Average Daily Return: {:.2f}".format(adr_the))
    print("\n[Benchmark]")
    print("Cumulative Return: {:.2f}".format(cr_ben))
    print("Standard Deviation of Daily Returns: {:.2f}".format(sddr_ben))
    print("Average Daily Return: {:.2f}".format(adr_ben))

def plot_portfolios(benchmark_portvals, manual_strategy_portvals):
    # Plotting the portfolio values
    plt.figure(figsize=(10, 6))
    
    # Plot benchmark
    plt.plot(benchmark_portvals, label='Benchmark', color='purple')
    
    # Plot manual strategy
    plt.plot(manual_strategy_portvals, label='Manual Strategy', color='red')
    
    # Adding title and labels
    plt.title('Portfolio Values: Manual Strategy vs Benchmark')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    
    # Adding a legend
    plt.legend()
    
    # Display the plot
    plt.grid()
    plt.show()
    
    
# if __name__ == "__main__":
#     # Define parameters
#     symbol = ['JPM']  # List of symbols
#     sd = dt.datetime(2008, 1, 1)  # Start date
#     ed = dt.datetime(2009, 12, 31)  # End date
#     sv = 100000  # Starting value of portfolio
    
#     # Create instance of ManualStrategy
#     manual_strategy = ManualStrategy()

#     # Test the manual strategy
#     df_trades = manual_strategy.testPolicy(symbol, sd, ed, sv)

#     # Compute benchmark
#     benchmark_portvals = compute_benchmark(sd, ed, sv)

#     # Compute portfolio values for manual strategy
#     manual_strategy_portvals = compute_portvals(df_trades, sv, commission=9.95, impact=0.005)
#     manual_strategy_portvals = manual_strategy_portvals / manual_strategy_portvals[0]
#     # Print statistics
#     #print_stats(benchmark_portvals, manual_strategy_portvals)

#     # Plot results
#     plot_portfolios(benchmark_portvals, manual_strategy_portvals)
