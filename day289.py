# Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}.


list1=["NY", "FL", "CA", "VT"]

dict1 = {i:i for i in list1}


print(dict1)