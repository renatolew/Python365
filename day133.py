# Write a Pandas program to concatenate the diamonds DataFrame with the 'color' Series.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nConcatenate the 'diamonds' DataFrame with the 'color' Series:")
print(pd.concat([diamonds, diamonds.color], axis=1).head())