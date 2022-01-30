# Write a Pandas program to get the true memory usage by diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nTrue memory usage by diamonds DataFrame:")
print(diamonds.info(memory_usage='deep'))