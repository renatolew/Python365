# Write a Pandas program to drop all non-numeric columns from diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nChecking variable type in each column:")
print(diamonds.dtypes)

print("\nDrop all non-numeric columns of diamonds DataFrame:")
num_diamonds = diamonds.drop(diamonds.select_dtypes(include=[object]),axis=1)
print(num_diamonds.head())