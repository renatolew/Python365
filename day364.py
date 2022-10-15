# In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

ex_list = [1, 2, 3, 4, 5, 6]

def replace_first(list):
    replacer = list[0]
    list.append(replacer)
    list = list[1:]
    return list

print(replace_first(ex_list))
print(replace_first([1, 3, 5, 7]))
print(replace_first(["a", "b", "c"]))
print(replace_first(["I", "am", "hungry"]))
