# Write a Pandas program to read rows in positions 0 through 4, columns in positions 1 through 4 of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nRows in positions 0 through 4, columns in positions 1 through 4:")
print(diamonds.iloc[0:4, 1:4])