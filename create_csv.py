from pandas_datareader import data
import datetime  
import pandas as pd

# Creating start time and end time
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

# create the keys for the our new dataframe
tickers = ['BAC', 'MS', 'C', 'WFC', 'GS' , 'JPM' ]

# Reading in and storing each bank's stock data in a list
listOfBanks = [
        data.DataReader(item, 'stooq', start, end) for item in tickers
        ] 

# concatenating the dataframes together into one
bank_stocks = pd.concat(listOfBanks , axis = 1 , keys = tickers)

bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']

# creates a new data frame based on the stock returns of each bank
returns = pd.DataFrame()

for ticker in tickers:
    returns[ticker  + ' Returns'] = bank_stocks[ticker]['Close'].pct_change()

# exports dataframes as csv files
bank_stocks.to_csv('bank_stocks.csv') 

returns.to_csv('returns.csv')



