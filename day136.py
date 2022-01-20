# Write a Pandas program to read rows 2 through 5 and all columns of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nRows 2 through 5 and all columns :")
print(diamonds.loc[1:4, :])