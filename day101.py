# Write a Pandas program to sort the entire diamonds DataFrame by the 'carat' Series in ascending and descending order.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nSort the entire diamonds DataFrame by the 'carat' Series in ascending order")
result = diamonds.sort_values('carat')
print(result)

print("\nSort the entire diamonds DataFrame by the 'carat' Series in descending  order")
result = diamonds.sort_values('carat', ascending=False)
print(result)