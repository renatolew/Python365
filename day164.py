# Write a program to print multiplication table of a given number

number = int(input("Type the chosen number: "))

for i in range(1, 11, 1):
    product = number * i
    print(product)