# Write a Pandas program to read rows 0 through 2 (inclusive), columns 'color' and 'price' of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nRows 0 through 2 (inclusive), columns ‘color’ and ‘price’:")
print(diamonds.loc[0:2, ['color', 'price']])