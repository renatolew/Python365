# Write a Pandas program to filter the DataFrame rows to only show carat weight at least 0.3.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head(20))

print("\nRows to only show carat weight at least 0.3:")
target = []
for w in diamonds.carat:
   if w >= .3:
       target.append(True)
   else:
       target.append(False)

print(target[0:25])