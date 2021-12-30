# Write a Pandas program to display percentages of each value of cut series occurs in diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nPercentages instead of raw counts in cut series of diamonds DataFrame:")
print(diamonds.cut.value_counts(normalize=True))