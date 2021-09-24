# Write a Python program to combine two dictionary adding values for common keys.

from collections import Counter


dict1 = {'a': 20, 'b': 50, 'c':35, 'd':5}
dict2 = {'a': 30, 'b': 20, 'c':40, 'e':12}


dict_final = Counter(dict1) + Counter(dict2)


print(dict_final)