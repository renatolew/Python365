# First, create a range from 100 to 161 with steps of 10.
# Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value.

range1 = range(100, 161, 10)
dict1 = {i:i/100 for i in range1}

print(dict1)