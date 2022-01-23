# Write a Pandas program to read rows in which the 'cut' is 'Premium', column 'color' of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nRows in which the ‘cut’  is ‘Premium’, column ‘color’:")
print(diamonds.loc[diamonds.cut=='Premium', 'color'])