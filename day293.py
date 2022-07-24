# Write a map function that returns the squares of the items in the list.


list1 = [10, 20, 30, 40, 50, 60]

list2 = list(map(lambda x: x**2, list1))

print(list2)