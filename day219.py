# Find each company’s Higesht price car

import pandas as pd

df = pd.read_csv("Automobile_data.csv")

manufacturers = df.groupby('company')

print(manufacturers['company','price'].max())
