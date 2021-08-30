#  Write a Python program to test whether all numbers of a list is greater than a certain number.

num_comparison = int(input('Type the number you want to compare to the number list: '))

num_list = [15, 18, 19, 22, 23, 25, 27, 31, 33, 35]

def greater_than_list_checker(number, list):
    count = 0
    for element in list:
        if number >= element:
            count += 1

    if count > 0:
        return 'There is at least one number equal to or smaller than your number in this list.'
    else:
        return 'Your number is smaller than every number on the list.'

print(greater_than_list_checker(num_comparison, num_list))