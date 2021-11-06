# Write a NumPy program to calculate 2p for all elements in a given array.

import numpy as np

base_array = np.array([1., 3., 7., 9.], np.float32)
print("Original array: ")
print(base_array)


print("\n2^p for all the elements of the said array:")
r1 = np.exp2(base_array)
r2 = 2 ** base_array
assert np.allclose(r1, r2)
print(r1)