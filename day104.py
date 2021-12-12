# Write a Pandas program to find the diamonds that are either Premium or Ideal.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nDiamonds that are either Premium or Ideal:")
result = diamonds[(diamonds.cut == 'Premium') | (diamonds.cut == 'Ideal')]
print(result.head())