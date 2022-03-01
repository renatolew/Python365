# Write a program to display all prime numbers within a range

start = int(input("Type the first number of the interval: "))
end = int(input("Type the second number of the interval: "))
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)