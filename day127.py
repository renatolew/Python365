# Write a Pandas program to count the number of missing values in each Series of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nNumber of missing values in each Series of diamonds DataFrame:")
print(diamonds.isnull().sum())