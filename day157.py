# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

for x, y in zip(list1, list2[::-1]):
    print(x, y)