# Write a Pandas program to create a plot of Open, High, Low, Close, Adjusted Closing prices and Volume of Alphabet Inc. between two specific dates.

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
stock_data = df1.set_index('Date')
stock_data.plot(subplots = True, figsize = (8, 8));
plt.legend(loc = 'best')
plt.suptitle('Open,High,Low,Close,Adj Close prices & Volume of Alphabet Inc., From 01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.show()