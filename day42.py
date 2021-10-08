# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).


def squared_list():
    list_combined = list()
    for i in range(1, 21):
        list_combined.append(i ** 2)
    print(list_combined)


squared_list()