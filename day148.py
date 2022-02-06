# Write a Pandas program to count the duplicate rows of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.shape)

print("\nDuplicate rows of diamonds DataFrame:")
print(diamonds.duplicated().sum())