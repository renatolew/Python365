# Write a Pandas program to sort movies on runtime in descending order.

import pandas as pd

df = pd.read_csv('movies_metadata.csv')
small_df = df[['title', 'release_date', 'budget', 'revenue', 'runtime']]


#Sort Movies based on runtime (in descending order)
result = small_df.sort_values('runtime', ascending=False)
print("DataFrame sort on Runtime.")
print(result.head())