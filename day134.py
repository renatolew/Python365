# Write a Pandas program to read specified rows and all columns of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("First 7 rows:")
print(diamonds.head(7))

print("\nAll columns:")
print(diamonds.loc[0, :])