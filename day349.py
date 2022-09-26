# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

def max_of_three(a, b, c):
    max_3 = 0
    if a > b:
        if a > c:
            max_3 = a
        else:
            max_3 = c
    else:
        if b > c:
            max_3 = b
        else:
            max_3 = c
    return print(max_3)


max_of_three(1, 5, 10)
max_of_three(10, 5, 22)
max_of_three(1, 50, 8)
max_of_three(80, 50, 44)