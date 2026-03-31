""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: Nicholas Daponte  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import datetime as dt  		  	   		 	   			  		 			 	 	 		 		 	
import random  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import pandas as pd
import numpy as np  		  	   		 	   			  		 			 	 	 		 		 	
import util as ut  		  	   		 	   			  		 			 	 	 		 		 	
import RTLearner as rt
import BagLearner as bl
from indicators import compute_bollinger_bands, compute_cci, compute_rsi  	
from marketsimcode import compute_portvals	  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
class StrategyLearner(object):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param verbose: If â€œverboseâ€ is True, your code can print out information for debugging.  		  	   		 	   			  		 			 	 	 		 		 	
        If verbose = False your code should not generate ANY output.  		  	   		 	   			  		 			 	 	 		 		 	
    :type verbose: bool  		  	   		 	   			  		 			 	 	 		 		 	
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		 	   			  		 			 	 	 		 		 	
    :type impact: float  		  	   		 	   			  		 			 	 	 		 		 	
    :param commission: The commission amount charged, defaults to 0.0  		  	   		 	   			  		 			 	 	 		 		 	
    :type commission: float  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    # constructor  		  	   		 	   			  		 			 	 	 		 		 	
    def __init__(self, verbose=False, impact=0.005, commission=9.95):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        Constructor method  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        self.verbose = verbose  		  	   		 	   			  		 			 	 	 		 		 	
        self.impact = impact  		  	   		 	   			  		 			 	 	 		 		 	
        self.commission = commission
        self.learner = bl.BagLearner(learner = rt.RTLearner, kwargs = {"leaf_size":5}, bags = 20, boost = False, verbose = False)  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # this method should create a QLearner, and train it for trading  		  	   		 	   			  		 			 	 	 		 		 	
    def add_evidence(  		  	   		 	   			  		 			 	 	 		 		 	
        self,  		  	   		 	   			  		 			 	 	 		 		 	
        symbol="IBM",  		  	   		 	   			  		 			 	 	 		 		 	
        sd=dt.datetime(2008, 1, 1),  		  	   		 	   			  		 			 	 	 		 		 	
        ed=dt.datetime(2009, 1, 1),  		  	   		 	   			  		 			 	 	 		 		 	
        sv=10000,  		  	   		 	   			  		 			 	 	 		 		 	
    ):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        Trains your strategy learner over a given time frame.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        :param symbol: The stock symbol to train on  		  	   		 	   			  		 			 	 	 		 		 	
        :type symbol: str  		  	   		 	   			  		 			 	 	 		 		 	
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   			  		 			 	 	 		 		 	
        :type sd: datetime  		  	   		 	   			  		 			 	 	 		 		 	
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   			  		 			 	 	 		 		 	
        :type ed: datetime  		  	   		 	   			  		 			 	 	 		 		 	
        :param sv: The starting value of the portfolio  		  	   		 	   			  		 			 	 	 		 		 	
        :type sv: int  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        # add your code to do learning here  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        # example usage of the old backward compatible util function  		  	   		 	   			  		 			 	 	 		 		 	
        syms = symbol  		  	   		 	   			  		 			 	 	 		 		 	
        dates = pd.date_range(sd, ed)  		  	   		 	   			  		 			 	 	 		 		 	
        prices_all = ut.get_data([syms], dates)  # automatically adds SPY  		  	   		 	   			  		 			 	 	 		 		 	
        prices = prices_all.drop(columns=['SPY'])  		  	   		 	   			  		 			 	 	 		 		 	
       
        
        window = 5

        # Compute indicators
        bollinger_bands = compute_bollinger_bands(prices, window = window)[['bollinger']]
       
        rsi = compute_rsi(prices, period = window)[['RSI']] ##(PICK ANOTHER INIDACTOR)
        #cci pre work 
        ccd_df_high = ut.get_data([syms], dates, colname="High")
        ccd_df_high = ccd_df_high.drop(columns='SPY')
        ccd_df_low = ut.get_data([syms], dates,  colname="Low")
        ccd_df_low = ccd_df_low.drop(columns='SPY')
        ccd_df_close = ut.get_data([syms], dates,  colname="Adj Close")
        ccd_df_close = ccd_df_close.drop(columns='SPY')
        ccd_concat = pd.concat([ccd_df_high, ccd_df_low, ccd_df_close], axis=1)
        ccd_df_normalized = ccd_concat / ccd_concat.iloc[0]
    
        cci = compute_cci(ccd_df_normalized, ndays=5)  
        # Remove the first 3 columns
        cci = cci.iloc[:, 3:]
        # Create a DataFrame for indicators
        indicators = pd.concat([bollinger_bands, cci, rsi], axis=1)
        indicators.columns = ['bollinger', 'cci', 'rsi']
        indicators.fillna(0,inplace=True)
        indicators=indicators[:-5]
        
        trainX = indicators.values
        

        
        
        
        
        # Construct trainY
        trainY = []
        for i in range(prices.shape[0] - 5):
            ratio = (prices.iloc[i + 5, 0] - prices.iloc[i, 0]) / prices.iloc[i, 0]
            if ratio > (0.02 + self.impact):
                trainY.append(1)
            elif ratio < (-0.02 - self.impact):
                trainY.append(-1)
            else:
                trainY.append(0)
        trainY = np.array(trainY)
         
        # Training
        self.learner.add_evidence(trainX,trainY)
        
        
  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # this method should use the existing policy and test it against new data  		  	   		 	   			  		 			 	 	 		 		 	
    def testPolicy(  		  	   		 	   			  		 			 	 	 		 		 	
        self,  		  	   		 	   			  		 			 	 	 		 		 	
        symbol="IBM",  		  	   		 	   			  		 			 	 	 		 		 	
        sd=dt.datetime(2009, 1, 1),  		  	   		 	   			  		 			 	 	 		 		 	
        ed=dt.datetime(2010, 1, 1),  		  	   		 	   			  		 			 	 	 		 		 	
        sv=10000,  		  	   		 	   			  		 			 	 	 		 		 	
        ):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        Tests your learner using data outside of the training data  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        :param symbol: The stock symbol that you trained on on  		  	   		 	   			  		 			 	 	 		 		 	
        :type symbol: str  		  	   		 	   			  		 			 	 	 		 		 	
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   			  		 			 	 	 		 		 	
        :type sd: datetime  		  	   		 	   			  		 			 	 	 		 		 	
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   			  		 			 	 	 		 		 	
        :type ed: datetime  		  	   		 	   			  		 			 	 	 		 		 	
        :param sv: The starting value of the portfolio  		  	   		 	   			  		 			 	 	 		 		 	
        :type sv: int  		  	   		 	   			  		 			 	 	 		 		 	
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		 	   			  		 			 	 	 		 		 	
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		 	   			  		 			 	 	 		 		 	
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		 	   			  		 			 	 	 		 		 	
            long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		 	   			  		 			 	 	 		 		 	
        :rtype: pandas.DataFrame  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        syms = symbol	
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data([syms], dates)  # automatically adds SPY  		  	   		 	   			  		 			 	 	 		 		 	
        prices = prices_all.drop(columns=['SPY']) 
        
        window = 5

        # Compute indicators
        bollinger_bands = compute_bollinger_bands(prices, window = window)[['bollinger']]
        rsi = compute_rsi(prices, period = window)[['RSI']]
        # Compute indicators
        #cci pre work 
        ccd_df_high = ut.get_data([syms], dates, colname="High")
        ccd_df_high = ccd_df_high.drop(columns='SPY')
        ccd_df_low = ut.get_data([syms], dates,  colname="Low")
        ccd_df_low = ccd_df_low.drop(columns='SPY')
        ccd_df_close = ut.get_data([syms], dates,  colname="Adj Close")
        ccd_df_close = ccd_df_close.drop(columns='SPY')
        ccd_concat = pd.concat([ccd_df_high, ccd_df_low, ccd_df_close], axis=1)
        ccd_df_normalized = ccd_concat / ccd_concat.iloc[0]
    
        cci = compute_cci(ccd_df_normalized, ndays=window)  
        # Remove the first 3 columns
        cci = cci.iloc[:, 3:]
        
        # Create a DataFrame for indicators
        indicators = pd.concat([bollinger_bands, cci, rsi], axis=1)
        indicators.columns = ['bollinger', 'cci', 'rsi']
        # Create a DataFrame for indicators
        indicators = pd.concat([bollinger_bands, cci, rsi], axis=1)
        indicators.columns = ['bollinger', 'cci', 'rsi']
        indicators.fillna(0,inplace=True)
        indicators=indicators[:-5]
        
        
        # Predict trading signals
        predictions = self.learner.query(indicators.values)
        
       # Create DataFrame with the necessary columns
        df_trades = pd.DataFrame(index=prices_all.index, columns=['Symbol', 'Order', 'Shares'])
        df_trades['Symbol'] = symbol
        df_trades['Order'] = None  # Initialize to NaN
        df_trades['Shares'] = 0
        
        position = 0
        index = 0  # Index for df_trades
        for i in range(len(predictions)):
            if predictions[i] == 1 and position == 0:
                df_trades.loc[df_trades.index[index]] = [symbol, 'BUY', 1000]
                position = 1000
                index += 1
            elif predictions[i] == -1 and position == 0:
                df_trades.loc[df_trades.index[index]] = [symbol, 'SELL', 1000]
                position = -1000
                index += 1
            elif predictions[i] == 1 and position == -1000:
                df_trades.loc[df_trades.index[index]] = [symbol, 'BUY', 1000]
                position = 1000
                index += 1
            elif predictions[i] == -1 and position == 1000:
                df_trades.loc[df_trades.index[index]] = [symbol, 'SELL', 1000]
                position = -1000
                index += 1
        
        # Close positions at the end
        if position != 0:
            df_trades.loc[df_trades.index[index]] = [symbol, 'SELL' if position > 0 else 'BUY', abs(position)]

		 	   			  		 			 	 	 		 		 	
        # here we build a fake set of trades  		  	   		 	   			  		 			 	 	 		 		 	
        # your code should return the same sort of data  		  	   		 	   			  		 			 	 	 		 		 	
        # dates = pd.date_range(sd, ed)  		  	   		 	   			  		 			 	 	 		 		 	
        # prices_all = ut.get_data([symbol], dates)  # automatically adds SPY  		  	   		 	   			  		 			 	 	 		 		 	
        # trades = prices_all[[symbol,]]  # only portfolio symbols  		  	   		 	   			  		 			 	 	 		 		 	
        # trades_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		 	   			  		 			 	 	 		 		 	
        # trades.values[:, :] = 0  # set them all to nothing  		  	   		 	   			  		 			 	 	 		 		 	
        # trades.values[0, :] = 1000  # add a BUY at the start  		  	   		 	   			  		 			 	 	 		 		 	
        # trades.values[40, :] = -1000  # add a SELL  		  	   		 	   			  		 			 	 	 		 		 	
        # trades.values[41, :] = 1000  # add a BUY  		  	   		 	   			  		 			 	 	 		 		 	
        # trades.values[60, :] = -2000  # go short from long  		  	   		 	   			  		 			 	 	 		 		 	
        # trades.values[61, :] = 2000  # go long from short  		  	   		 	   			  		 			 	 	 		 		 	
        # trades.values[-1, :] = -1000  # exit on the last day  		  	   		 	   			  		 			 	 	 		 		 	
        # if self.verbose:  		  	   		 	   			  		 			 	 	 		 		 	
        #     print(type(trades))  # it better be a DataFrame!  		  	   		 	   			  		 			 	 	 		 		 	
        # if self.verbose:  		  	   		 	   			  		 			 	 	 		 		 	
        #     print(trades)  		  	   		 	   			  		 			 	 	 		 		 	
        # if self.verbose:  		  	   		 	   			  		 			 	 	 		 		 	
        #     print(prices_all)  
        df_trades = df_trades.dropna(subset=['Order'])	
        df_trades.reset_index(inplace=True)
        df_trades.rename(columns={'index': 'Date'}, inplace=True)
        df_trades['Date'] = df_trades['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))	
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
  		  	   		 	   			  		 			 	 	 		 		 	
# if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
#     print("One does not simply think up a strategy")  		  	   		 	   			  		 			 	 	 		 		 	
#     st = StrategyLearner()

#     st.add_evidence(symbol="AAPL",sd=dt.datetime(2009, 1, 1),ed=dt.datetime(2009,12,31),sv=100000)
   
#     df_trades = st.testPolicy(symbol="AAPL", sd=dt.datetime(2009, 1, 1), ed=dt.datetime(2010, 1, 1), sv=100000)
    
#     manual_strategy_portvals = compute_portvals(df_trades, start_val=100000, commission=9.95, impact=0.005)

#     manual_strategy_portvals = manual_strategy_portvals / manual_strategy_portvals[0]
    
    
    
    
    
    
    
