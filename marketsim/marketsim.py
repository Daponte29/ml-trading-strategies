""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""MC2-P1: Market simulator.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: Nicholas Daponte  		  	   		 	   			  		 			 	 	 		 		 	
IMPORTANT NOTE: Course Retake Resubmission 	   		 	   			  		 			 	 	 		 		 	
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
    orders_file="./orders/orders.csv",
    start_val=1000000,
    commission=9.95,
    impact=0.005,
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
    Orders = pd.read_csv(orders_file, index_col='Date', parse_dates=True).sort_index()
    Orders_Dates = sorted(list(set(Orders.index)))
    SYMB = list(set(Orders['Symbol']))

    Prices = get_data(SYMB, pd.date_range(Orders_Dates[0], Orders_Dates[-1]))
    if "SPY" not in SYMB:
        Prices = Prices.drop('SPY', axis=1)  # Drop SPY if not in Orders
    Prices['Money'] = 1  # Initializing Money for transactions
    Trades = Prices.copy()
    Trades[:] = 0  # Start with empty trades before entering from Order Book raw data file
        
    Holdings = Trades.copy()  # Total holdings that will be summed for Portfolio Value
    
    COMM = {i: 0 for i in Orders_Dates}  # Dictionary of commission and impact tracking for each date
    
    for index, col in Orders.iterrows():
        if col['Order'] == 'SELL':
            Trades.loc[index, col['Symbol']] += col['Shares'] * -1  # Trading shares
        else:
            Trades.loc[index, col['Symbol']] += col['Shares']  # Buying Shares so positive number of shares
     
        COMM[index] -= commission + (col['Shares'] * Prices.loc[index, col['Symbol']] * impact)
          
    for date in Orders_Dates:
        Trades.iloc[Trades.index.get_loc(date), -1] += -1 * (Trades.iloc[Trades.index.get_loc(date), :-1].multiply(Prices.iloc[Prices.index.get_loc(date), :-1]).sum()) + COMM[date]
    
    Holdings.iloc[0, -1] = start_val + Trades.iloc[0, -1]
    Holdings.iloc[0, :-1] = Trades.iloc[0, :-1]
    
    for i in range(1, Holdings.shape[0]):
        Holdings.iloc[i, :] = Trades.iloc[i, :] + Holdings.iloc[i - 1, :]
    
    Amount = Holdings.multiply(Prices)
    portvals = Amount.sum(axis=1)
    
    return portvals
    
    
    
    
    
    
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # In the template, instead of computing the value of the portfolio, we just  		  	   		 	   			  		 			 	 	 		 		 	
    # read in the value of IBM over 6 months -------------------template commented below
 		  	   		 	   			  		 			 	 	 		 		 	
    # start_date = dt.datetime(2008, 1, 1)  		  	   		 	   			  		 			 	 	 		 		 	
    # end_date = dt.datetime(2008, 6, 1)  		  	   		 	   			  		 			 	 	 		 		 	
    # portvals = get_data(["IBM"], pd.date_range(start_date, end_date))  		  	   		 	   			  		 			 	 	 		 		 	
    # portvals = portvals[["IBM"]]  # remove SPY  		  	   		 	   			  		 			 	 	 		 		 	
    # rv = pd.DataFrame(index=portvals.index, data=portvals.values)  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # return rv  		  	   		 	   			  		 			 	 	 		 		 	
    return portvals  # 1-col dataframe of portfolio values indexed by date		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def test_code():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Helper function to test code  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    # this is a helper function you can use to test your code  		  	   		 	   			  		 			 	 	 		 		 	
    # note that during autograding his function will not be called.  		  	   		 	   			  		 			 	 	 		 		 	
    # Define input parameters  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    of = r"C:\Users\nolot\Desktop\ML4T\ML4T_2024Summer\marketsim\additional_orders\additional_orders\orders2.csv" #Orders rawdata	
     	   		 	   			  		 			 	 	 		 		 	
    sv = 1000000  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Process orders function 		  	   		 	   			  		 			 	 	 		 		 	
    portvals = compute_portvals(orders_file=of, start_val=sv)  		  	   		 	   			  		 			 	 	 		 		 	
    if isinstance(portvals, pd.DataFrame):  		  	   		 	   			  		 			 	 	 		 		 	
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		 	   			  		 			 	 	 		 		 	
    else:  		  	   		 	   			  		 			 	 	 		 		 	
        "warning, code did not return a DataFrame"  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Get portfolio stats  		  	   		 	   			  		 			 	 	 		 		 	
    # Here we just fake the data. you should use your code from previous assignments.  		  	   		 	   			  		 			 	 	 		 		 	
    start_date = dt.datetime(2008, 1, 1)  		  	   		 	   			  		 			 	 	 		 		 	
    end_date = dt.datetime(2008, 6, 1)  		  	   		 	   			  		 			 	 	 		 		 	
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [  		  	   		 	   			  		 			 	 	 		 		 	
        0.2,  		  	   		 	   			  		 			 	 	 		 		 	
        0.01,  		  	   		 	   			  		 			 	 	 		 		 	
        0.02,  		  	   		 	   			  		 			 	 	 		 		 	
        1.5,  		  	   		 	   			  		 			 	 	 		 		 	
    ]  		  	   		 	   			  		 			 	 	 		 		 	
    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [  		  	   		 	   			  		 			 	 	 		 		 	
        0.2,  		  	   		 	   			  		 			 	 	 		 		 	
        0.01,  		  	   		 	   			  		 			 	 	 		 		 	
        0.02,  		  	   		 	   			  		 			 	 	 		 		 	
        1.5,  		  	   		 	   			  		 			 	 	 		 		 	
    ]  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Compare portfolio against $SPX  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Date Range: {start_date} to {end_date}")  		  	   		 	   			  		 			 	 	 		 		 	
    print()  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Sharpe Ratio of SPY : {sharpe_ratio_SPY}")  		  	   		 	   			  		 			 	 	 		 		 	
    print()  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Cumulative Return of SPY : {cum_ret_SPY}")  		  	   		 	   			  		 			 	 	 		 		 	
    print()  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Standard Deviation of SPY : {std_daily_ret_SPY}")  		  	   		 	   			  		 			 	 	 		 		 	
    print()  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Average Daily Return of SPY : {avg_daily_ret_SPY}")  		  	   		 	   			  		 			 	 	 		 		 	
    print()  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Final Portfolio Value: {portvals[-1]}")  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    test_code()  		  	   		 	   			  		 			 	 	 		 		 	
