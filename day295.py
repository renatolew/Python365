# Using map() function and lambda add each elements of two lists together. Use a lambda with two arguments.

list1 = [100, 200, 300, 400, 500]
list2 = [1, 10, 100, 1000, 10000]



list3 = list(map(lambda x,y: x+y, list1, list2))


print(list3)