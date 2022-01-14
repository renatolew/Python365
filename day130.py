# Write a Pandas program to set an existing column as the index of diamonds DataFrame and restore the index name, and move the index back to a column.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nNew Dataframe:")
diamonds.set_index('color', inplace=True)
print(diamonds.head())

print("\nNow restore the index name:")
diamonds.index.name = 'color'
diamonds.reset_index(inplace=True)
print(diamonds.head())