# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:17:10 2024

@author: nolot
"""
import datetime as dt  		  	   		 	   			  		 			 	 	 		 		 	
import os  		  	   		 	   			  		 			 	 	 		 		 		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np  		  	   		 	   			  		 			 	 	 		 		 	 		  	   		 	   			  		 			 	 	 		 		 	
import pandas as pd  		  	   		 	   			  		 			 	 	 		 		 	
from util import get_data, plot_data 
#////Libraries////////////////////////////


def author(): 
    return 'ndaponte3'

def study_group():
   return 'ndaponte3' 

def compute_portvals(
    Orders,
    start_val=100000,
    commission=0.00,
    impact=0.000,
):
    """
    Computes the portfolio values.

    :param orders_file: Path of the order file or the file object
    :type orders_file: str or file object
    :param start_val: The starting value of the portfolio
    :type start_val: int
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)
    :type commission: float
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction
    :type impact: float
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.
    :rtype: pandas.DataFrame
    """
    
    # Read in Orders data and Prices Data
    # Orders = pd.read_csv(orders_file, index_col='Date', parse_dates=True).sort_index()
    Orders_Dates = sorted(list(set(Orders.index)))
    SYMB = ['JPM']
    #########
    sd = dt.date(2008, 1, 1)
    ed = dt.date(2009, 12, 31)
    dates = pd.date_range(sd, ed)
    symbols = ["JPM"]
    ########
    Prices = get_data(symbols,dates )
    Prices = Prices.drop('SPY', axis=1)  # Drop SPY 
    
    Prices['Money'] = 1  # Initializing Money for transactions
    Trades = Prices.copy()
    Trades[:] = 0  # Start with empty trades before entering from Order Book raw data file
        
    Holdings = Trades.copy()  # Total holdings that will be summed for Portfolio Value
    
    COMM = {i: 0 for i in Orders_Dates}  # Dictionary of commission and impact tracking for each date
    
    for index, col in Orders.iterrows():
        if col['Order'] == 'SELL':
            Trades.loc[index, 'JPM'] += col['Shares'] * -1  # Trading shares
        else:
            Trades.loc[index, 'JPM'] += col['Shares']  # Buying Shares so positive number of shares
     
        # COMM[index] -= commission + (col['Shares'] * Prices.loc[index, col['Symbol']] * impact)
          
    for date in Orders_Dates:
        Trades.iloc[Trades.index.get_loc(date), -1] += -1 * (Trades.iloc[Trades.index.get_loc(date), :-1].multiply(Prices.iloc[Prices.index.get_loc(date), :-1]).sum()) + 0
    
    Holdings.iloc[0, -1] = start_val + Trades.iloc[0, -1]
    Holdings.iloc[0, :-1] = Trades.iloc[0, :-1]
    
    for i in range(1, Holdings.shape[0]):
        Holdings.iloc[i, :] = Trades.iloc[i, :] + Holdings.iloc[i - 1, :]
    
    Amount = Holdings.multiply(Prices)
    portvals = Amount.sum(axis=1)
    
    return portvals		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
# def test_code():  		  	   		 	   			  		 			 	 	 		 		 	
#     """  		  	   		 	   			  		 			 	 	 		 		 	
#     Helper function to test code  		  	   		 	   			  		 			 	 	 		 		 	
#     """  		  	   		 	   			  		 			 	 	 		 		 	
#     # this is a helper function you can use to test your code  		  	   		 	   			  		 			 	 	 		 		 	
#     # note that during autograding his function will not be called.  		  	   		 	   			  		 			 	 	 		 		 	
#     # Define input parameters  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
#     of = r"C:\Users\nolot\Desktop\ML4T\ML4T_2024Summer\marketsim\additional_orders\additional_orders\orders2.csv" #Orders rawdata	
     	   		 	   			  		 			 	 	 		 		 	
#     sv = 1000000  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
#     # Process orders function 		  	   		 	   			  		 			 	 	 		 		 	
#     portvals = compute_portvals(orders_file=of, start_val=sv)  		  	   		 	   			  		 			 	 	 		 		 	
#     if isinstance(portvals, pd.DataFrame):  		  	   		 	   			  		 			 	 	 		 		 	
#         portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		 	   			  		 			 	 	 		 		 	
#     else:  		  	   		 	   			  		 			 	 	 		 		 	
#         "warning, code did not return a DataFrame"  		
