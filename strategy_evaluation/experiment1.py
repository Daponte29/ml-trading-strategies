# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:08:13 2024

@author: nolot
"""

import datetime as dt
import pandas as pd
import util as ut
import random
import numpy as np
from StrategyLearner import StrategyLearner
from marketsimcode import compute_portvals
from util import get_data, plot_data
import matplotlib.pyplot as plt
from ManualStrategy import ManualStrategy



def compute_benchmark(sd, ed, sv, symbol, impact):
    # Get the first trading day in the range
    dates = pd.date_range(sd, ed)
    prices = get_data(['JPM'], dates)
    first_trading_day = prices.index.min()

    # Create a DataFrame for the buy and hold strategy
    df_trades = pd.DataFrame(columns=['Date', 'Symbol', 'Order', 'Shares'])
    df_trades.loc[0] = [first_trading_day.strftime('%Y-%m-%d'), 'JPM', 'BUY', 1000]
    df_trades['Date'] = pd.to_datetime(df_trades['Date'])
    df_trades.set_index('Date', inplace=True)
    df_trades['Shares'] = df_trades.apply(lambda row: row['Shares'] if row['Order'] == 'BUY' else -row['Shares'], axis=1)
    df_trades.drop(columns=['Symbol', 'Order'], inplace=True)
    df_trades.rename(columns={'Shares': symbol}, inplace=True)
    # Compute portfolio values
    portvals = compute_portvals(df_trades, sv, commission=9.95, impact=0.005)
    
    return portvals / portvals.iloc[0]

def print_stats(benchmark, manual_strategy, filename):
    # Ensure that 'benchmark' and 'manual_strategy' are Series
    if not isinstance(benchmark, pd.Series):
        raise ValueError("benchmark should be a pandas Series.")
    if not isinstance(manual_strategy, pd.Series):
        raise ValueError("manual_strategy should be a pandas Series.")
    
    # Cumulative Return
    cr_ben = benchmark.iloc[-1] / benchmark.iloc[0] - 1
    cr_the = manual_strategy.iloc[-1] / manual_strategy.iloc[0] - 1

    # Daily Returns
    dr_ben = benchmark.pct_change().dropna()
    dr_the = manual_strategy.pct_change().dropna()

    # Stats
    sddr_ben = dr_ben.std()
    sddr_the = dr_the.std()
    adr_ben = dr_ben.mean()
    adr_the = dr_the.mean()

    # Write the statistics to a file
    with open(filename, 'w') as f:
        f.write("[Manual Strategy]\n")
        f.write(f"Cumulative Return: {cr_the}\n")
        f.write(f"Standard Deviation of Daily Returns: {sddr_the}\n")
        f.write(f"Average Daily Return: {adr_the}\n")
        f.write("\n[Benchmark]\n")
        f.write(f"Cumulative Return: {cr_ben}\n")
        f.write(f"Standard Deviation of Daily Returns: {sddr_ben}\n")
        f.write(f"Average Daily Return: {adr_ben}\n")

def plot_portfolio_values(manual_strategy_portvals, ML_strategy_portvals, benchmark_portvals, sample = None, save_filename='portfolio_values_comparison.png'):
    # Plot the portfolio values
    plt.figure(figsize=(12, 6))
    
    # Plot Manual Strategy
    plt.plot(manual_strategy_portvals.index, manual_strategy_portvals, color='red', label='Manual Strategy')
    
    # Plot ML Strategy
    plt.plot(ML_strategy_portvals.index, ML_strategy_portvals, color='blue', label='ML Strategy')
    
    # Plot Benchmark
    plt.plot(benchmark_portvals.index, benchmark_portvals, color='purple', label='Benchmark')
    if sample == 'IN_SAMPLE':
        # Formatting the plot
        plt.title('Portfolio Value Comparison IN_SAMPLE')
    elif sample == 'OUT_SAMPLE':
        plt.title('Portfolio Value Comparison OUT_SAMPLE')
        
    plt.xlabel('Date')
    plt.ylabel('Normalized Portfolio Value')
    plt.legend()
    plt.grid(True)
    # Save the plot
    plt.savefig(save_filename)
    # Show plot
    #plt.show()
    
    
   
    
def author(self):
def study_group(self):
   return 'ndaponte3'  

    

'''
pre>--- Summary ---
Tests passed: 0 out of 4

--- Details ---
Test #0: failed 
Test case description: ML4T-220
Traceback:
  File "grade_strategy_learner.py", line 443, in test_strategy
    raise IncorrectOutput(
IncorrectOutput: Test failed on one or more output criteria.
  Inputs:
    insample_args: {'symbol': 'ML4T-220', 'sd': datetime.datetime(2008, 1, 1, 0, 0), 'ed': datetime.datetime(2009, 12, 31, 0, 0), 'sv': 100000}
    outsample_args: {'symbol': 'ML4T-220', 'sd': datetime.datetime(2010, 1, 1, 0, 0), 'ed': datetime.datetime(2011, 12, 31, 0, 0), 'sv': 100000}
    benchmark_type: clean
    benchmark: 1.0
    train_time: 25
    test_time: 5
    max_time: 60
    seed: 1481090000

  Failures:
  First insample trades DF has invalid shape: (35, 4)
'''    
    
if __name__ == "__main__":
    # Define parameters IN SAMPLE
    symbol = 'JPM'  # List of symbols
    sd = dt.datetime(2008, 1, 1, 0, 0)  # Start date
    ed = dt.datetime(2009, 12, 31, 0, 0)  # End date
    sv = 100000  # Starting value of portfolio
    
    # Create instance of ManualStrategy IN SAMPLE----------------------------------
    manual_strategy = ManualStrategy()

    # Test the manual strategy
    df_trades_manual = manual_strategy.testPolicy(symbol, sd, ed, sv)
    # Compute portfolio values for manual strategy
    manual_strategy_portvals = compute_portvals(df_trades_manual, sv, commission=9.95, impact=0.005)
    manual_strategy_portvals = manual_strategy_portvals / manual_strategy_portvals.iloc[0]
    # Create instance of StrategyLearner IN SAMPLE
    st = StrategyLearner()
    #Train Learner
    st.add_evidence(symbol=symbol,sd=sd,ed=ed,sv=100000)
    #Get Trades Output
    df_trades_ML = st.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=100000)
    
    ML_strategy_portvals = compute_portvals(df_trades_ML, sv, commission=9.95, impact=0.005)

    ML_strategy_portvals = ML_strategy_portvals / ML_strategy_portvals.iloc[0]
  
    #Benchmark Portvals
    benchmark_portvals = compute_benchmark(sd, ed, sv)
    
    plot_portfolio_values(manual_strategy_portvals, ML_strategy_portvals, benchmark_portvals, sample = 'IN_SAMPLE', save_filename = 'IN_1.png')
    print_stats(benchmark_portvals, manual_strategy_portvals, 'in_sample_stats.txt')






    # Define parameters OUT SAMPLE-----------------------------------------------
    symbol = 'JPM'  # List of symbols
    sd = dt.datetime(2010, 1, 1)  # Start date
    ed = dt.datetime(2011, 12, 31)  # End date
    sv = 100000  # Starting value of portfolio
    
    # Create instance of ManualStrategy IN SAMPLE
   

    # Test the manual strategy
    df_trades_manual_2 = manual_strategy.testPolicy(symbol, sd, ed, sv)
    # Compute portfolio values for manual strategy
    manual_strategy_portvals_2 = compute_portvals(df_trades_manual_2, sv, commission=9.95, impact=0.005,sd=sd, ed=ed)
    manual_strategy_portvals_2 = manual_strategy_portvals_2 / manual_strategy_portvals_2[0]
    # Create instance of StrategyLearner IN SAMPLE
    #st_2 = StrategyLearner()
    #Train Learner
    #st_2.add_evidence(symbol=symbol,sd=sd,ed=ed,sv=100000)
    #Get Trades Output
    df_trades_ML_2 = st.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=100000)
    
    ML_strategy_portval_2s = compute_portvals(df_trades_ML_2, sv, commission=9.95, impact=0.005, sd=sd, ed=ed)

    ML_strategy_portval_2s = ML_strategy_portval_2s / ML_strategy_portval_2s[0]
  
    #Benchmark Portvals
    benchmark_portvals_2 = compute_benchmark(sd, ed, sv)
    
    plot_portfolio_values(manual_strategy_portvals_2, ML_strategy_portval_2s, benchmark_portvals_2, sample = 'OUT_SAMPLE', save_filename = 'OUT_1.png')
    print_stats(benchmark_portvals_2, manual_strategy_portvals_2, 'out_sample_stats.txt')
    
    ####HAVE SHORT AND LONG entry points [    ]
    
    
    
    
