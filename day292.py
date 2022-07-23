# Write a map function that adds plus 5 to each item in the list.


list1 = [10, 20, 30, 40, 50, 60]

list2 = list(map(lambda x: x+5, list1))

print(list2)
