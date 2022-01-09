# Write a Pandas program to create a bar plot of the 'value_counts' for the 'cut' series of diamonds DataFrame.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

print("\nBar plot of the 'value_counts' for the ‘cut’ series of diamonds DataFrame:")
diamonds.cut.value_counts().plot(kind='bar')