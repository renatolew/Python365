# Write a Pandas program to read rows in positions 0 through 4 (exclusive) and all columns of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nRows in positions 0 through 4 (exclusive) and all columns :")
print(diamonds.iloc[0:5, :])