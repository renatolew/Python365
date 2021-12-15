# Write a Pandas program to calculate the mean and median of each numeric column of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nMean of each numeric column of diamonds DataFrame:")
print(diamonds.mean())

print("\nMedian of each numeric column of diamonds DataFrame:")
print(diamonds.median())