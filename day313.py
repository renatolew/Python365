# Place msg = "You're out of list range" to avoid IndexError.

list1 = [5, 10, 20]

try:
    print(list1[5])
except IndexError as error:
    msg = "You're out of list range"


print(msg)

