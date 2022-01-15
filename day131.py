# Write a Pandas program to access a specified Series index and the Series values of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nAccess the Series index:")
print(diamonds.carat.value_counts().index)

print("\nAccess the Series values:")
print(diamonds.carat.value_counts().values)