# Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.
#
# (Hint: lambda will be passed to sort method's key parameter as argument)


list1 = [100, 10, 10000, 1, 9, 999, 99]
list1.sort(key = lambda x: 100/x)


print(list1)