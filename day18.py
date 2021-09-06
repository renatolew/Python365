# Write a Python program to split fractional and integer parts of a floating point number (up to 2 decimal places).

num_input = input('Type the number to be splited: ')

num_float = float(num_input)

def float_split(num):
    int_num = int(num)

    float_part = num - int(num)

    return print('The integer part of this number is {} and the float part is {:.2f}.'.format(int_num, float_part))


float_split(num_float)