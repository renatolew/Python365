# Write a NumPy program to create a new shape to an array without changing its data.

import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
print("Original array:")
print(x)

y = np.reshape(x,(3,2))
print("Reshaping 3x2:")
print(y)

z = np.reshape(x,(2,3))
print("Reshaping 2x3:")
print(z)