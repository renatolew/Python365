# Write a NumPy program to repeat all the elements three times of a given array of string

import numpy as np

test_array = np.array(['Python', 'NumPy', 'Exercicing', 'Everyday'], dtype=np.str)
print("Original Array:")
print(test_array)

repeated_array = np.char.multiply(test_array, 3)
print("New array:")
print(repeated_array)