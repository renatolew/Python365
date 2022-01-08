# Write a Pandas program to calculate various summary statistics of cut series of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nVarious summary statistics of diamonds DataFrame:")
print(diamonds.carat.describe())