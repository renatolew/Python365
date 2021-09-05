# Write a Python program to check whether a given number is a Disarium number or unhappy number.


num_check = input('Type the number you want to check: ')

num_int = int(num_check)

def check_disarium(num):
    sum = 0
    for i in range(len(str(num))):
        sum += int(str(num)[i]) ** (i + 1)
    return sum

if check_disarium(num_int) == num_int:
    print('This number is a Disarium!')
else:
    print('This number is unhappy...')