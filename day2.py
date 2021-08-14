# Create a function that takes an integer and returns the factorial of that integer.
# That is, the integer multiplied by all positive lower integers.


print('This program will return to you the factorial for any number!!')
int_num = input('Type the number you want to find the factorial for: \n')


def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        fac_num = 1
        count = 1
        while count <= number:
            fac_num = fac_num * count
            count += 1
        return fac_num

factorial_num = factorial(int(int_num))

print('The factorial for {} is {}'.format(int_num, factorial_num))