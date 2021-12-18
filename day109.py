# Write a Python program to remove multiple spaces in a string

import re

text1 = 'Python      exercises    are                   fun'


print("Original string:",text1)
print("Without extra spaces:",re.sub(' +',' ',text1))
