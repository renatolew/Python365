# Write a Pandas program to read rows 0, 5, 7 and all columns of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nRows 0, 5, 7 and all columns:")
print(diamonds.loc[[0, 5, 7], :])