# Write a NumPy program to compute the mean, standard deviation, and variance of a given array along the second axis.

import numpy as np


test_array = [16, 11, 12, 13, 14, 11, 16, 13, 18, 19, 10, 11, 9, 13, 12]
print("\nOriginal array:")
print(test_array)

mean = np.mean(test_array)
average = np.average(test_array)
assert np.allclose(mean, average)
print("\nMean: ", mean)


str_var = np.std(test_array)
sqrt_var = np.sqrt(np.mean((test_array - np.mean(test_array)) ** 2 ))
assert np.allclose(str_var, sqrt_var)
print("\nStandart Variation: ", str_var)


variance = np.var(test_array)
mean = np.mean((test_array - np.mean(test_array)) ** 2 )
assert np.allclose(variance, mean)
print("\nVariance: ", variance)