# Given dictionary is consisted of vehicles and their weights in kilograms.
# Contruct a list of the names of vehicles with weight below 5000 kilograms.
# In the same list comprehension make the key names all upper case.

dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

list1 = [i.upper() for i in dict1 if dict1[i]<5000]

print(list1)