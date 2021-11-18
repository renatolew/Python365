# Create a dataframe of ten rows, four columns with random values.
# Write a Pandas program to highlight the negative numbers red and positive numbers black.

import pandas as pd
import numpy as np


np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))], axis=1)

print("Original array:")
print(df)

def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

print("\nNegative numbers red and positive numbers black:")
df.style.applymap(color_negative_red)
