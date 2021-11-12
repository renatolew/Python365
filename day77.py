# Write a NumPy program to get the number of nonzero elements in an array.

import numpy as np

x = np.array([[0, 10, 20], [20, 30, 40]])

print("Original array:")
print(x)

print("Number of non zero elements in the above array:")
print(np.count_nonzero(x))