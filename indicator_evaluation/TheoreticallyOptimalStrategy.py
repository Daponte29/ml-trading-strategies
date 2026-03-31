# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:17:10 2024

@author: nolot
"""
import pandas as pd
import datetime as dt
from util import get_data , plot_data 
#------------------------------
def author(): 
    return 'ndaponte3'

def study_group():
   return 'ndaponte3' 


def testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000):
    symbols = [symbol]
    # Get dates for the specified date range
    dates = pd.date_range(sd, ed)
    
    # Get Data for the specified symbol and date range
    data = get_data(symbols, dates)
    data = data.drop(columns=['SPY'])  # Drop 'SPY' column if it exists
    
    # Get Returns
    rets = data.diff()
    
    # Create trades DataFrame
    df_trades = pd.DataFrame(index=data.index, columns=[symbol], data=0.0)
    
    # Initialize trade signals based on future price movements
    for i in range(1, len(data)):
        if rets.iloc[i - 1][symbol] > 0:
            df_trades.iloc[i][symbol] = 1000.0  # Buy 1000 shares if the price is expected to rise
        elif rets.iloc[i - 1][symbol] < 0:
            df_trades.iloc[i][symbol] = -1000.0  # Sell 1000 shares if the price is expected to fall
    
    return df_trades

# # Example usage:
# if __name__ == "__main__":
#     symbol = "JPM"
#     start_date = dt.datetime(2008, 1, 1)
#     end_date = dt.datetime(2009, 12, 31)
#     starting_value = 100000
    
#     # Call the testPolicy function to get trades
#     trades = testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=starting_value)
    
#     # Display the trades generated
#     print("Trades generated for TOS strategy:")
#     print(trades)
