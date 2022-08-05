# This time use the sorted() function to sort the list in ascending order with lambda.

list1 = [100, 10, 10000, 1, 9, 999, 99]

list1 = sorted(list1, key = lambda x: x)

print(list1)