# Using map() function, first return a new list with absolute values of existing list. Then for ans_1, find the total sum of the new list's elements.


list1 = [99.3890,-3.5, 5, -0.7123, -9, -0.003]

new_list = list(map(abs, list1))
print(new_list)

ans_1 = sum(new_list)
print(ans_1)