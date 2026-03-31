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




def compute_portvals(
        trades_df,
        initial_cash=1000000,
        commission=0.0,
        impact=0.0
):
    """
    Computes the portfolio values.

    :param trades_df: DataFrame containing trades
    :type trades_df: pd.DataFrame
    :param initial_cash: The starting value of the portfolio
    :type initial_cash: int
    :param commission_fee: The fixed amount in dollars charged for each transaction (both entry and exit)
    :type commission_fee: float
    :param market_impact: The amount the price moves against the trader compared to the historical data at each transaction
    :type market_impact: float
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.
    :rtype: pandas.DataFrame
    """

    # Sort trades by date
    trades_df = trades_df.sort_index()

    start_date = trades_df.index.min()
    end_date = trades_df.index.max()

    # Get stock symbols from trades
    stock_symbols = trades_df.columns.tolist()

    # Generate date range for the period of interest
    date_range = pd.date_range(start_date, end_date)
    price_data = get_data(stock_symbols, date_range)
    price_data = price_data[stock_symbols]
    price_data['Cash'] = 1.0
    # Initialize trades DataFrame
    trades_df['Cash'] = 0.0
    trades_df.loc[start_date, 'Cash'] = initial_cash
    # Process trades
    for date, trade in trades_df.iterrows():
        shares = float(trade.iloc[0])
        price = price_data.loc[date, stock_symbols]
        trade['Cash'] -= (price * shares) * (1 + impact) + commission
        trades_df.at[date, 'Cash'] = trade['Cash']
    # Compute cumulative holdings
    cumulative_holdings = trades_df.cumsum()

    # Compute values
    portfolio_values = cumulative_holdings * price_data

    # Compute total portfolio value
    total_portfolio_value = portfolio_values.sum(axis=1)

    return total_portfolio_value.to_frame(name='Portfolio Value')
	 	   			  		 			 	
    	   			  	

	 			 	 	 		 		 	
def author(self):
def study_group(self):
   return 'ndaponte3'  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
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
