# Write a Python program to find out the average of a set of integers (no libraries allowed)

count = int(input("Enter the count of numbers: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    sum = sum + x
avg = sum/count
print(" The average is: ", avg)