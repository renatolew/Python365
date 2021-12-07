# Remove multiple rows at once from diamonds dataframe

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nRemove multiple rows:")
diamonds.drop([2, 4, 5], axis=0, inplace=True)
print(diamonds.head())