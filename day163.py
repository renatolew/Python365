# Calculate the sum of all numbers from 1 to a given number


sum = 0
n = int(input("Enter the desired number: "))

for i in range(1, n + 1, 1):
    sum += i

print("\n")
print("The sum is: ", sum)