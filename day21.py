# Write a Python program to find the digits which are absent in a given mobile number.


num_input = input('Type the mobile number to be checked: ')
list_input = list(num_input)


def absent_digits(n):
    all_nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    n = set([int(i) for i in n])
    n = n.symmetric_difference(all_nums)
    n = sorted(n)

    return n

print(absent_digits(list_input))