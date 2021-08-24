# Given two integers a and b, return how many times a can be halved while still being greater than b.

input_a = input('Type the integer A: ')
input_b = input('Type the integer B: ')

int_a = int(input_a)
int_b = int(input_b)

def halve_and_halve(int1, int2):
    count = 0
    while (int1 / 2 > int2):
        int1 = int1 / 2
        count += 1
    return count


print('The amount of times {} can be halved while still being greater than {} is {}.'.format(input_a, input_b, halve_and_halve(int_a, int_b)))
