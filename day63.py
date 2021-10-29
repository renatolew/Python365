# Write a NumPy program to test whether any of the elements of a given array is non-zero.

import numpy as np


first_array = np.array([1, 0, 0, 0])
print("Original array:")
print(first_array)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(first_array))


second_array = np.array([0, 0, 0, 0])
print("\nOriginal array:")
print(second_array)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(second_array))