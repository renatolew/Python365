# Write a Pandas program to display the movies (title, number of votes) that received specified number of votes.

import pandas as pd


df = pd.read_csv('movies_metadata.csv')
vote_count = 1000
small_df = df[['title', 'vote_count']]
result = small_df[small_df['vote_count'] >= vote_count]
print("List of movies longer than 30 minutes and shorter than 360 minutes:")
print(result)