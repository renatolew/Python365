# Python program to generate the prime numbers from 1 to N

num = int(input("Enter the number of the range limit: "))
for n in range(2,num):
    for i in range(2,n):
        if(n % i == 0):
            break
    else:
        print(n)