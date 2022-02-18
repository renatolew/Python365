# Add new item to a list after a specified item inside another list

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]


list1[2][2].append(7000)
print(list1)