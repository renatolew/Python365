# Calculate the cube of all numbers from 1 to a given number

num = int(input("Type the desired number: "))

def cube(num):
    for i in range(1, num +1):
        print("The cube of ", i, "is", i*i*i)

cube(num)