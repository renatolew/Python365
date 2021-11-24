# Write a Pandas program to create a histogram to visualize daily return distribution of Alphabet Inc. stock price between two specific dates.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Date', 'Adj Close']]
df3 = df2.set_index('Date')
daily_changes = df3.pct_change(periods=1)
sns.distplot(daily_changes['Adj Close'].dropna(),bins=100,color='purple')
plt.suptitle('Daily % return of Alphabet Inc. stock price,\n01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.grid(True)
plt.show()