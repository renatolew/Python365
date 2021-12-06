# Write a Pandas program to access those movies released after 1995-01-01.

import pandas as pd

df = pd.read_csv('movies_metadata.csv')

# Create a smaller dataframe
small_df = df[['title', 'release_date', 'budget', 'revenue', 'runtime']]
result = small_df[small_df['release_date'] > '1995-01-01']

print("DataFrame based on release date>'1995-01-01'.")
print(result)