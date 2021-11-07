#  Write a NumPy program to round array elements to the given number of decimals.

import numpy as np

x = np.round([1.4588, 1.5001, 1.5523], decimals=3)
print(x)

x = np.round([0.28, .50, .64], decimals=1)
print(x)

x = np.round([.6, 1.4, 2.5, 3.2, 4.8])
print(x)