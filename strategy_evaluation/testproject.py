# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:57:26 2024

@author: nolot
"""
from experiment1 import compute_benchmark, print_stats, plot_portfolio_values
from experiment2 import compute_benchmark2, print_stats2, plot_portfolio_values2

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

def author():
    return 'ndaponte3'

def study_group():
   return 'ndaponte3'    




if __name__ == "__main__":
    # Define parameters IN SAMPLE
    symbol = 'JPM'  # List of symbols
    sd = dt.datetime(2008, 1, 1)  # Start date
    ed = dt.datetime(2009, 12, 31)  # End date
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
    benchmark_portvals = compute_benchmark(sd, ed, sv, symbol) #(FIXXXXXXXXX MAIN THING LEFT BEFORE REPORT BUT USE OTHER GRAPHS)
    
    plot_portfolio_values(manual_strategy_portvals, ML_strategy_portvals, benchmark_portvals, sample = 'IN_SAMPLE', save_filename = 'IN_1.png')
    benchmark_portvals = pd.Series(benchmark_portvals.iloc[:, 0])
    manual_strategy_portvals = pd.Series(manual_strategy_portvals.iloc[:, 0])







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
    manual_strategy_portvals_2 = compute_portvals(df_trades_manual_2, sv, commission=9.95, impact=0.005)
    manual_strategy_portvals_2 = manual_strategy_portvals_2 / manual_strategy_portvals_2.iloc[0]
    # Create instance of StrategyLearner IN SAMPLE
    #st_2 = StrategyLearner()
    #Train Learner
    #st_2.add_evidence(symbol=symbol,sd=sd,ed=ed,sv=100000)
    #Get Trades Output
    df_trades_ML_2 = st.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=100000)
    
    ML_strategy_portval_2s = compute_portvals(df_trades_ML_2, sv, commission=9.95, impact=0.005)

    ML_strategy_portval_2s = ML_strategy_portval_2s / ML_strategy_portval_2s.iloc[0]
  
    #Benchmark Portvals
    #benchmark_portvals_2 = compute_benchmark(sd, ed, sv, symbol)
    
    plot_portfolio_values(manual_strategy_portvals_2, ML_strategy_portval_2s, benchmark_portvals, sample = 'OUT_SAMPLE', save_filename = 'OUT_1.png')
    #benchmark_portvals = pd.Series(benchmark_portvals)
    #manual_strategy_portvals = pd.Series(manual_strategy_portvals.iloc[:, 0])
    print_stats(benchmark_portvals, manual_strategy_portvals, 'out_sample_stats.txt')
    
    
    
    '''Experiment 2'''
   
# Define parameters IN SAMPLE
symbol = 'JPM'  # List of symbols
sd = dt.datetime(2008, 1, 1)  # Start date
ed = dt.datetime(2009, 12, 31)  # End date
sv = 100000  # Starting value of portfolio

# Define different impact values
impacts = [0.000, 0.005, 0.010]  # Example: low, medium, high impact values

for impact in impacts:
    # Create instance of StrategyLearner
    st = StrategyLearner(verbose=False, impact=impact, commission=9.95)
    # Train Learner
    st.add_evidence(symbol=symbol, sd=sd, ed=ed, sv=100000)
    # Get Trades Output
    df_trades = st.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=100000)
    
    # Compute portfolio values
    ML_strategy_portvals = compute_portvals(df_trades, sv, commission=9.95, impact=impact)
    ML_strategy_portvals = ML_strategy_portvals / ML_strategy_portvals.iloc[0]
  
    # Benchmark Portvals
    benchmark_portvals = compute_benchmark(sd, ed, sv, impact=impact)
    
    # Plot portfolio values
    plot_filename = f'IN_{impact}.png'
    plot_portfolio_values(ML_strategy_portvals, benchmark_portvals, sample='IN_SAMPLE', save_filename=plot_filename)
    
    # Print stats
    stats_filename = f'{impact}_impact.txt'
    print_stats(benchmark_portvals, ML_strategy_portvals, stats_filename)
