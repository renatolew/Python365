# Using map() function and len() function create a list that's consisted of lengths of each element in the first list.

list1=["Alpine", "Avalanche", "Powder", "Snowflake", "Summit"]

list2 = list(map(len, list1))

print(list2)