# Write a Pandas program to print a concise summary of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nConcise summary of diamonds DataFrame:")
print(diamonds.info())