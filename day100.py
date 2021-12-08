# Write a Pandas program to rename all the columns of the diamonds Dataframe.

import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Original Dataframe:")
print(diamonds.head())

diamonds_cols = ['new_carat', 'new_cut', 'new_color', 'new_clarity', 'new_depth', 'new_table', 'new_price', 'new_x', 'new_y', 'new_z']
diamonds.columns = diamonds_cols

print("\nAfter renaming all the columns of the said dataframe:")
diamonds.rename(columns={'color':'diamond_color', 'clarity':'dimaond_clarity'}, inplace=True)
print(diamonds.head())