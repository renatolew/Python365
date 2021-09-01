# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


raw_list = [1, 1, 2, 3, 4, 5, 5, 6, 8, 9, 12, 12, 13, 14, 15, 15, 16]
raw_list2 = ['a', 'b', 'b', 'c', 1, 3, 4, 1, 'a']


def unique_items(list):
    unique_list = []
    for element in list:
        if element in unique_list:
            continue
        else:
            unique_list.append(element)
    return unique_list


print(unique_items(raw_list))
print(unique_items(raw_list2))