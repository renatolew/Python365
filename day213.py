# Following is the provided numPy array. Return array of items by taking the third column from all rows

import numpy

sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

print("Printing Input Array")
print(sampleArray)

print("\n Printing array of items in the third column from all rows")
res_array = sampleArray[...,2]
print(res_array)