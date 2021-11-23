# Write a Pandas program to create a scatter plot of the trading volume/stock prices of Alphabet Inc. stock between two specific dates.

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1.set_index('Date')
x= ['Close']; y = ['Volume']
plt.figure(figsize=[15,10])
df2.plot.scatter(x, y, s=50);
plt.grid(True)
plt.title('Trading Volume/Price of Alphabet Inc. stock,\n01-04-2020 to 30-09-2020', fontsize=14, color='black')
plt.xlabel("Stock Price",fontsize=12, color='black')
plt.ylabel("Trading Volume", fontsize=12, color='black')
plt.show()