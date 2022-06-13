# Python program to display all integers within the range 100-200 whose sum of digits is an even number

for i in range(100,200):
    num = i
    sum = 0
    while(num != 0):
        digit = num % 10
        sum = sum + digit
        num = num//10
    if(sum % 2 == 0):
        print(i)