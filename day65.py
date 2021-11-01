# Write a NumPy program to replace all numbers in a given array which is equal, less and greater to a given number.

import numpy as np


nums_array = np.array([[5.54, 3.38, 7.99],
              [3.54, 8.55, 6.99],
              [1.54, 2.39, 9.29]])

print("Original array:")
print(nums_array)

n = 8.55
r = 18.95

print("\nReplace elements of the said array which are equal to ",n,"with",r)
print(np.where(nums_array == n, r, nums_array))
print("\nReplace elements with of the said array which are less than",n,"with",r)
print(np.where(nums_array < n, r, nums_array))
print("\nReplace elements with of the said array which are greater than",n,"with",r)
print(np.where(nums_array > n, r, nums_array))