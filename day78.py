# Write a NumPy program to make all the elements of a given string to a numeric string of 5 digits with zeros on its left.

import numpy as np

test_array = np.array(['7', '14', '198', '6753', '53241'], dtype=np.str)

print("\nOriginal Array:")
print(test_array)

standarized_array = np.char.zfill(test_array, 5)
print("\nNumeric string of 5 digits with zeros:")
print(standarized_array)