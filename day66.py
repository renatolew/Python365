# Write a NumPy program to calculate the difference between the maximum and the minimum values of a given array along the second axis.

import numpy as np

test_array = np.arange(14).reshape((2, 7))
print("\nOriginal array:")
print(test_array)

r1 = np.ptp(test_array, 1)
r2 = np.amax(test_array, 1) - np.amin(test_array, 1)
assert np.allclose(r1, r2)

print("\nDifference between the maximum and the minimum values of the said array:")
print(r1)