# Write a Pandas program to read the diamonds DataFrame and detect duplicate color.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.shape)

print("\nCount the duplicate items:")
print(diamonds.clarity.duplicated().sum())