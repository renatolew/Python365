# Create a line plot of one column versus another column

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet_stock_data.csv")

start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-09-30')

df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date' ]>= start_date) & (df['Date' ]<= end_date)

df1 = df.loc[new_df]
df2 = df1.set_index('Date')

plt.figure(figsize=(5 ,5))
plt.suptitle('Stock prices of Alphabet Inc.,\n01-04-2020 to 30-09-2020', \
             fontsize=18, color='black')

plt.xlabel("Date" ,fontsize=16, color='black')
plt.ylabel("$ price", fontsize=16, color='black')

df2['Close'].plot(color='green');
plt.show()