# Write a Python program to extract values between quotation marks of a string.

import re

text_test = '"Python", "Exercise", "365"'

print(re.findall(r'"(.*?)"', text_test))