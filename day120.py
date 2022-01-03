# Write a Pandas program to count the number of unique values in cut series of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nNumber of unique values in cut series of diamonds DataFrame:")
print(diamonds.cut.nunique())