# Write a Pandas program to set an existing column as the index of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nNew Dataframe:")
diamonds.set_index('color', inplace=True)

print(diamonds.head())