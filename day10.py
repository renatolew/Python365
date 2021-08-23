# Your job is to create a function, that takes 3 numbers: a, b, c and returns True if the last digit of a * b = the last digit of c.
# Check the examples below for an explanation.


numb_1 = input('Type the first number: ')
numb_2 = input('Type the second number: ')
numb_3 = input('Type the third number: ')

list_numb_1 = list(numb_1)
list_numb_2 = list(numb_2)
list_numb_3 = list(numb_3)

def last_digit_ultimate(num1, num2, num3):
    if int(num1[-1]) * int(num2[-1]) == int(num3[-1]):
        return True
    else:
        return False


print(last_digit_ultimate(list_numb_1, list_numb_2, list_numb_3))