# Merge two data frames using the following condition
#
# Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.
#
#
# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
# car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_price_df = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
cars_horsepower_df = pd.DataFrame.from_dict(car_Horsepower)

cars_df = pd.merge(car_price_df, cars_horsepower_df, on="Company")

print(cars_df)