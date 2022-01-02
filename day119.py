# Write a Pandas program to display the unique values in cut series of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nDisplay the unique values in cut series of diamonds DataFrame:")
print(diamonds.cut.unique())