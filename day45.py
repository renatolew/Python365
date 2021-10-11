# Write a Python program to remove all whitespaces from a string.

import re

test_string = ' Testing    Regex   Now'

print("Original string: ",test_string)

print("Removing whitespaces: ",re.sub(r'\s+', '',test_string))