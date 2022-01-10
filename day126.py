# Write a Pandas program to create a DataFrame of booleans (True if missing, False if not missing) from diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nDataFrame of booleans:")
print(diamonds.isnull().head(50))