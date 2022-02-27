# Write a program to use for loop to print the reverse pattern for a number


number = int(input("Type the desired number: "))

n = number
k = number

for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()