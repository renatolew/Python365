# Print All Toyota Cars details

import pandas as pd

df = pd.read_csv("Automobile_data.csv")

manufacturers = df.groupby('company')

print(manufacturers.get_group('toyota'))
