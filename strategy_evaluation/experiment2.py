# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:36:29 2024

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



def compute_benchmark2(sd, ed, sv, impact = None):
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

def print_stats2(benchmark, ML_strategy, filename):
    # Ensure that 'benchmark' and 'manual_strategy' are Series
    if not isinstance(benchmark, pd.Series):
        raise ValueError("benchmark should be a pandas Series.")
    if not isinstance(ML_strategy, pd.Series):
        raise ValueError("manual_strategy should be a pandas Series.")
    
    # Cumulative Return
    cr_ben = benchmark.iloc[-1] / benchmark.iloc[0] - 1
    cr_the = ML_strategy.iloc[-1] / ML_strategy.iloc[0] - 1

    # Daily Returns
    dr_ben = benchmark.pct_change().dropna()
    dr_the = ML_strategy.pct_change().dropna()

    # Stats
    sddr_ben = dr_ben.std()
    sddr_the = dr_the.std()
    adr_ben = dr_ben.mean()
    adr_the = dr_the.mean()

    # Write the statistics to a file
    with open(filename, 'w') as f:
        f.write("[ML_strategy]\n")
        f.write(f"Cumulative Return: {cr_the}\n")
        f.write(f"Standard Deviation of Daily Returns: {sddr_the}\n")
        f.write(f"Average Daily Return: {adr_the}\n")
        f.write("\n[Benchmark]\n")
        f.write(f"Cumulative Return: {cr_ben}\n")
        f.write(f"Standard Deviation of Daily Returns: {sddr_ben}\n")
        f.write(f"Average Daily Return: {adr_ben}\n")

def plot_portfolio_values2(ML_strategy_portvals, benchmark_portvals, sample = None, save_filename='portfolio_values_comparison.png'):
    # Plot the portfolio values
    plt.figure(figsize=(12, 6))
    
 
    
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
    
    
   
    
def author():
    return 'ndaponte3'

def study_group():
   return 'ndaponte3'    
    
    
# if __name__ == "__main__":
#     # Define parameters IN SAMPLE
#     symbol = 'JPM'  # List of symbols
#     sd = dt.datetime(2008, 1, 1)  # Start date
#     ed = dt.datetime(2009, 12, 31)  # End date
#     sv = 100000  # Starting value of portfolio
    
#     # Define different impact values
#     impacts = [0.000, 0.005, 0.010]  # Example: low, medium, high impact values
    
#     for impact in impacts:
#         # Create instance of StrategyLearner
#         st = StrategyLearner(verbose=False, impact=impact, commission=9.95)
#         # Train Learner
#         st.add_evidence(symbol=symbol, sd=sd, ed=ed, sv=100000)
#         # Get Trades Output
#         df_trades = st.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=100000)
        
#         # Compute portfolio values
#         ML_strategy_portvals = compute_portvals(df_trades, sv, commission=9.95, impact=impact)
#         ML_strategy_portvals = ML_strategy_portvals / ML_strategy_portvals.iloc[0]
      
#         # Benchmark Portvals
#         benchmark_portvals = compute_benchmark(sd, ed, sv, impact=impact)
        
#         # Plot portfolio values
#         plot_filename = f'IN_{impact}.png'
#         plot_portfolio_values(ML_strategy_portvals, benchmark_portvals, sample='IN_SAMPLE', save_filename=plot_filename)
        
#         # Print stats
#         stats_filename = f'{impact}_impact.txt'
#         print_stats(benchmark_portvals, ML_strategy_portvals, stats_filename)
    
    
    
    
    
    
    
    
    
