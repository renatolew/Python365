# Sort all cars by Price column

import pandas as pd

cars_df = pd.read_csv("Automobile_data.csv")

cars_df = cars_df.sort_values(by=['price', 'horsepower'], ascending=False)

print(cars_df.head(5))