# Write a Pandas program to create a side-by-side bar plot of the diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nSide-by-side bar plot of the diamonds DataFrame:")
diamonds.groupby('cut').mean().plot(kind='bar')