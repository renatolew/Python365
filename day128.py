# Write a Pandas program to check the number of rows and columns and drop those row if 'any' values are missing in a row of diamonds

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("Number of rows and columns:")
print(diamonds.shape)

print("After droping those rows where values are missing:")
print(diamonds.dropna(how='any').shape)