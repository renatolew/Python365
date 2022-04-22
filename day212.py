# Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10

import numpy


sample_array = numpy.arange(100, 200, 10)
print(sample_array)

sample_array = sample_array.reshape(5,2)
print(sample_array)