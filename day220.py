# Find the average mileage of each car making company

import pandas as pd

df = pd.read_csv("Automobile_data.csv")

manufacturers = df.groupby('company')

print(manufacturers['company','average-mileage'].mean())
