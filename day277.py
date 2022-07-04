# Write a program to filter even and odd number from a list.

list = [10, 15, 20, 25, 30, 32, 34, 35, 37, 38, 40, 50, 60, 65]
even = []
odd = []

for i in range (len(list)):
    if list[i] % 2 == 0:
        even.append(list[i])
    else:
        odd.append(list[i])

print("Even numbers are: ", even)
print("Odd numbers are: ", odd)