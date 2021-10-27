# Write a Python program to calculate the sum of the digits in an integer.

number_input = int(input("Input a four digit numbers: "))

first_digit  = number_input // 1000
second_digit = (number_input - first_digit * 1000)//100
third_digit = (number_input - first_digit * 1000 - second_digit * 100)//10
fourth_digit = number_input - first_digit * 1000 - second_digit * 100 - third_digit * 10


print(first_digit, second_digit, third_digit, fourth_digit)

print("The sum of digits in the number is", first_digit + second_digit + third_digit + fourth_digit)