# Write a Pandas program to calculate the multiply of length, width and depth for each cut of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nMultiply of length, width and depth for each cut:")
print((diamonds.x*diamonds.y*diamonds.z).head())