# Write a Pandas program to display the movies (title, runtime) longer than 80 minutes and shorter than 360 minutes.

import pandas as pd

df = pd.read_csv('movies_metadata.csv')
small_df = df[['title', 'runtime']]
result = small_df[(small_df['runtime'] >= 80) & (small_df['runtime'] <= 360)]
print("List of movies longer than 80 minutes and shorter than 360 minutes:")
print(result)