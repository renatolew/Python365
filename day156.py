# Concatenate two lists in different orders and combinations

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]

print(res)