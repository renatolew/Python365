# Write a Pandas program to find the details of the diamonds where length>5, width>5 and depth>5.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nDiamonds where length>5, width>5 and depth>5:")
result = diamonds[(diamonds.x>5) & (diamonds.y>5) & (diamonds.z>5)]
print(result.head())