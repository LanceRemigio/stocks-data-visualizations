import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
bank_stocks = pd.read_csv('bank_stocks.csv')
returns = pd.read_csv('returns.csv')

# Grabs Close Prices for each bank
closePrice = bank_stocks.xs(key = 'Close', axis = 1 , level = 'Stock Info')

# grabs max close price for the entire time period

# print(
#         closePrice.max()  
#         )

# Pairplot for each bank's close price  

# sns.pairplot(data = closePrice)

print(returns.idxmax()) # Returns best single day returns of each bank as a series
print(returns.idxmin()) # returns worst single day returns of each bank as a series

# standard deviation of returns

print(
        returns.loc['2015'].std()
        )


# closePrice = bank_stocks.xs(key = 'Close', axis = 1, level = "Stock Info")
# closePriceBAC = bank_stocks.xs(key = 'Close', axis = 1, level = "Stock Info")['BAC'].loc['2008']
# closePriceBAC = bank_stocks.xs(key = 'Close', axis = 1, level = "Stock Info")['BAC'].loc['2015']
# closePriceBAC = bank_stocks.xs(key = 'Close', axis = 1 , level = 'Stock Info')['BAC'].loc['2008']
closePriceBAC = bank_stocks.xs(key = 'Close', axis = 1 , level = 'Stock Info')['BAC'].loc['2008']
rollingAvg = closePriceBAC.rolling(30).mean()

# sns.clustermap(data = closePrice.corr(), annot = True)
# plt.savefig('./plots/clustermapClosePrice.png')

# part 2 (Optional)

# dataBAC = bank_stocks['BAC'].loc['2015': '2016']
# dataBAC.iplot(kind = 'candle')
# dataMS = closePrice['MS'].loc['2015']
# dataMS.ta_plot(study = 'sma')
# dataSMA = bank_stocks['BAC'].loc['2015']
# dataSMA.ta_plot(study = 'sma')
# dataSMA.iplot(study = 'boll')

# -- plots -- 

# sns.heatmap(data = closePrice.corr(), annot = True)
# sns.clustermap(data = closePrice.corr(), annot = True)





# sns.lineplot(data = closePriceBAC)
# sns.lineplot(data = rollingAvg)
# plt.savefig('./plots/clustermapClosePrice.png')
plt.show()


# sns.displot(data = returns['MS Returns'].loc['2015'], kde = True, bins = 60)


# sns.displot(data = returns['C Returns'].loc['2008'], kde = True, bins = 50)


# plt.show()


# print(
#         bank_stocks.xs('Bank')
#         )


# print(maxClosePrice)

# data = pdr.get_data_yahoo(tickerList, start, end)


# print(bank_stocks.head())




