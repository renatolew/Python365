# Write a Pandas program to calculate the number of votes garnered by the 70% movie.

import pandas as pd

df = pd.read_csv('movies_metadata.csv')
result = df['vote_count'].quantile(0.70)
print(result)