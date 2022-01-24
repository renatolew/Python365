# Write a Pandas program to read rows in positions 0 and 1, columns in positions 0 and 3 of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nRows in positions 0 and 1, columns in positions 0 and 3 :")
print(diamonds.iloc[[0, 1], [0, 3]])