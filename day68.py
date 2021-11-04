# Write a NumPy program to check two random arrays are equal or not.

import numpy as np

first_array = np.random.randint(0,2,6)
print("First array:")
print(first_array)

second_array = np.random.randint(0,2,6)
print("Second array:")
print(second_array)

print("Test above two arrays are equal or not!")
array_equal = np.allclose(first_array, second_array)
print(array_equal)