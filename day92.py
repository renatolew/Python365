# Write a Pandas program to plot the volatility over a period of time of Alphabet Inc. stock price between two specific dates.

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Date', 'Close']]
df3 = df2.set_index('Date')
data_filled = df3.asfreq('D', method='ffill')
data_returns = data_filled.pct_change()
data_std = data_returns.rolling(window=30, min_periods=30).std()
plt.figure(figsize=(20,20))
data_std.plot();
plt.suptitle('Volatility over a period of time  of Alphabet Inc. stock price,\n01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.grid(True)
plt.show()