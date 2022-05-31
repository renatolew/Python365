# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number = int(input("Type the number to be reversed: "))
print("Number to be reversed: ", number)

while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end=" ")