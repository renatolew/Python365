# Write a Pandas program to create a histograms plot of opening, closing, high, low stock prices of Alphabet Inc. between two specific dates.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Open','Close','High','Low']]
#df3 = df2.set_index('Date')
plt.figure(figsize=(25,25))
df2.plot.hist(alpha=0.5)
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc.,\n From 01-04-2020 to 30-09-2020', fontsize=12, color='blue')
plt.show()