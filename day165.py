# Write a program to display only those numbers from a list that satisfy the following conditions:
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop


numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)