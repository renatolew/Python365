# Write a NumPy program (using NumPy) to sum of all the multiples of 3 or 5 below 100.

import numpy as np

test_array = np.arange(1, 100)

# find multiple numbers of 3 or 5
mult_n = test_array[(test_array % 3 == 0) | (test_array % 5 == 0)]
print(mult_n[:1000])

# print sum of the numbers found
print(mult_n.sum())