# Write a Pandas program to create a histogram of the 'carat' Series (distribution of a numerical variable) of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nHistogram of the 'carat' Series (distribution of a numerical variable) of diamonds DataFrame.")
diamonds.carat.plot(kind='hist')