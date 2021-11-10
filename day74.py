# Write a NumPy program to compute the histogram of nums against the bins.

import numpy as np
import matplotlib.pyplot as plt


nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1, 0.6, 1.1, 1.4, 2.2, 8.5])
bins = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("nums: ",nums)
print("bins: ",bins)
print("Result:", np.histogram(nums, bins))

plt.hist(nums, bins=bins)
plt.show()