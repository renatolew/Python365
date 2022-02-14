# Concatenate two lists index-wise

list1 = ["M", "na", "i", "Sl", "Sh"]
list2 = ["y", "me", "s", "im", "ady"]

list3 = [i + j for i, j in zip(list1, list2)]

print(list3)