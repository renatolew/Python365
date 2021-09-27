# Write a Python program to remove the intersection of a 2nd set from the 1st set.

set1 = {1, 3, 5, 7, 9, 11, 13, 15}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("Original sets:")
print(set1)
print(set2)

print("\nRemove the intersection of a 2nd set from the 1st set using difference_update():")

set1.difference_update(set2)

print("set1: ",set1)
print("set2: ",set2)



print("------------------------------------------")

set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}

print("Original sets:")
print(set3)
print(set4)

print("\nRemove the intersection of a 2nd set from the 1st set using -= operator:")

set3 -= set4

print("set3: ",set3)
print("set4: ",set4)