# Write a NumPy program compare two given arrays.

import numpy as np

array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([4, 5, 1, 4, 8])

print("Array a: ",array_a)
print("Array b: ",array_b)
print("a > b")
print(np.greater(array_a, array_b))

print("a >= b")
print(np.greater_equal(array_a, array_b))

print("a < b")
print(np.less(array_a, array_b))

print("a <= b")
print(np.less_equal(array_a, array_b))