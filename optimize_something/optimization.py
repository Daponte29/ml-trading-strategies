""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""MC1-P2: Optimize a portfolio.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: Nicholas Daponte  		  	   		 	   			  		 			 	 	 		 		 	
Summer 2024 Resubmission - Course Retake - Nicholas Daponte  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
def author():
    return 'ndaponte3'

def study_group():
    return 'None'  		  	   		 	   			  		 			 	 	 		 		 	
#packages///////////////////////  		  	   		 	   			  		 			 	 	 		 		 	
import datetime as dt  		  	   		 	   			  		 			 	 	 		 		 	  		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np  		  	   		 	   			  		 			 	 	 		 		 			  	   		 	   			  		 			 	 	 		 		 	
import matplotlib.pyplot as plt  		  	   		 	   			  		 			 	 	 		 		 	
import pandas as pd  
import scipy.optimize as sp		  	   		 	   			  		 			 	 	 		 		 	
from util import get_data, plot_data  		  	   		 	   			  		 			 	 	 		 		 	
  #/////////////////////////////////		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
# This is the function that will be tested by the autograder  		  	   		 	   			  		 			 	 	 		 		 	
# The student must update this code to properly implement the functionality  		  	   		 	   			  		 			 	 	 		 		 	
def optimize_portfolio(  		  	   		 	   			  		 			 	 	 		 		 	
    sd=dt.datetime(2008, 1, 1),  		  	   		 	   			  		 			 	 	 		 		 	
    ed=dt.datetime(2009, 1, 1),  		  	   		 	   			  		 			 	 	 		 		 	
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		 	   			  		 			 	 	 		 		 	
    gen_plot=False,  		  	   		 	   			  		 			 	 	 		 		 	
):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe  		  	   		 	   			  		 			 	 	 		 		 	
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of  		  	   		 	   			  		 			 	 	 		 		 	
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take  		  	   		 	   			  		 			 	 	 		 		 	
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and  		  	   		 	   			  		 			 	 	 		 		 	
    statistics.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   			  		 			 	 	 		 		 	
    :type sd: datetime  		  	   		 	   			  		 			 	 	 		 		 	
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   			  		 			 	 	 		 		 	
    :type ed: datetime  		  	   		 	   			  		 			 	 	 		 		 	
    :param syms: A list of symbols that make up the portfolio (note that your code should support any  		  	   		 	   			  		 			 	 	 		 		 	
        symbol in the data directory)  		  	   		 	   			  		 			 	 	 		 		 	
    :type syms: list  		  	   		 	   			  		 			 	 	 		 		 	
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		 	   			  		 			 	 	 		 		 	
        code with gen_plot = False.  		  	   		 	   			  		 			 	 	 		 		 	
    :type gen_plot: bool  		  	   		 	   			  		 			 	 	 		 		 	
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,  		  	   		 	   			  		 			 	 	 		 		 	
        standard deviation of daily returns, and Sharpe ratio  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: tuple  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Read in adjusted closing prices for given symbols, date range  		  	   		 	   			  		 			 	 	 		 		 	
    dates = pd.date_range(sd, ed)  		  	   		 	   			  		 			 	 	 		 		 	
    prices_all = get_data(syms, dates)  # automatically adds SPY  		  	   		 	   			  		 			 	 	 		 		 	
    prices = prices_all[syms]  # only portfolio symbols  		  	   		 	   			  		 			 	 	 		 		 	
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # find the allocations for the optimal portfolio  		  	   		 	   			  		 			 	 	 		 		 	
    # note that the values here ARE NOT meant to be correct for a test case  		  	   		 	   			  		 			 	 	 		 		 	
    #Allocations
    num_stocks = len(syms)
    initial_guess = [1.0/num_stocks] * num_stocks #equally distributed as initital guess
    bounds = [(0.0,1.0)] * num_stocks
    constraints = { 'type' : 'eq' , 'fun': lambda allocs: 1.0 - np.sum(allocs)}
    allocs = sp.minimize(min_sharpe_ratio, initial_guess, args = (prices) , bounds = bounds, constraints = constraints).x #scipy minimize the negative gives maximum of sharpe ratio
    	
    port_val, cr, adr, sddr, sr = assess_portfolio(allocs, prices)  	   		 	   			  		 			 	 	 		 		 	
      	   		 	   			  		 			 	 	 		 		 	
    # Compare daily portfolio value with SPY using a normalized plot  		  	   		 	   			  		 			 	 	 		 		 	
    if gen_plot:
        df_temp = pd.concat([port_val, prices_SPY / prices_SPY.iloc[0]], keys=['Portfolio', 'SPY'], axis=1)
        ax = df_temp.plot()
        ax.set_title('Normalized Daily Portfolio Value (IBM, X, GLD, JPM) and SPY')
        ax.set_ylabel('Price')
        ax.set_xlabel('Date')
        plt.grid(True)
        plt.savefig('Figure1.png')  # Save the plot as a PNG file
        #plt.show()  	   		 	   
      	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    return allocs, cr, adr, sddr, sr  		  	   		 	   			  		 			 	 	 		 		 	

def min_sharpe_ratio(allocs, prices):
    return -assess_portfolio(allocs, prices)[4] #add negative sign for maximization

def assess_portfolio(allocs, prices):
    # Get daily portfolio value
    normed = prices / prices.iloc[0]
    alloced = normed * allocs
    port_val = alloced.sum(axis=1)
   
    # Calculate daily returns
    daily_rets = port_val / port_val.shift(1) - 1
    daily_rets.iloc[0] = 0  # Set the first daily return to 0
    
    # Cumulative return
    cr = (port_val[-1] / port_val[0]) - 1

    # AVG daily return
    adr = daily_rets.mean()

    # Standard deviation of daily return
    sddr = daily_rets.std()

    # Sharpe Ratio w/ risk adjusted (0%) return
    sr = (adr - 0) / sddr
    sr *= 252**0.5  # adjustment for daily sampling (for annual measure)

    return port_val, cr, adr, sddr, sr 	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def test_code():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    This function WILL NOT be called by the auto grader.  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    start_date = dt.datetime(2008, 6, 1)  		  	   		 	   			  		 			 	 	 		 		 	
    end_date = dt.datetime(2009, 6, 1)  		  	   		 	   			  		 			 	 	 		 		 	
    symbols = ["IBM", "X", "GLD", "JPM"]  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Assess the portfolio  		  	   		 	   			  		 			 	 	 		 		 	
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		 	   			  		 			 	 	 		 		 	
        sd=start_date, ed=end_date, syms=symbols, gen_plot=True  		  	   		 	   			  		 			 	 	 		 		 	
    )  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Print statistics  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Start Date: {start_date}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"End Date: {end_date}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Symbols: {symbols}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Allocations:{allocations}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Sharpe Ratio: {sr}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Volatility (stdev of daily returns): {sddr}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Average Daily Return: {adr}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Cumulative Return: {cr}")  		  	   		 	   			  		 			 	 	 		 		 	
    # Generate the graph to save to report 2
  		  	   		 	   			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    # This code WILL NOT be called by the auto grader  		  	   		 	   			  		 			 	 	 		 		 	
    # Do not assume that it will be called  		  	   		 	   			  		 			 	 	 		 		 	
    test_code()  		  	   		 	   			  		 			 	 	 		 		 	
