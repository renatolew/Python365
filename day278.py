# Write a program to fetch only even values from a dictionary.

dict1 = {"val1": 10, "val2": 21, "val3": 34, "val4": 47}


for i in dict1.values():
    if i % 2 == 0:
        print(i, end = " ")
    else:
        pass

