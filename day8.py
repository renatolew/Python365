# Create a function that takes two number strings and returns their sum as a string.

print('This program calculates the sum of two numbers from string inputs: ')
num_str1 = input('Type the first number to be summed: ')
num_str2 = input('Type the second number to be summed: ')
print('\nCalculating...')

def sum_strings(str1, str2):
    try:
        num_1 = int(str1)
        num_2 = int(str2)
        sum_nums = num_1 + num_2
        sum_returned = str(sum_nums)
        return sum_returned
    except ValueError:
        return 'invalid, because you didnt type two valid numbers'

print('The summed value is {}.'.format(sum_strings(num_str1, num_str2)))
print(type(sum_strings(num_str1, num_str2)))