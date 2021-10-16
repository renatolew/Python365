# Write a Python program to add two objects if both objects are an integer type.

def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "Inputs must be integers!"
   return a + b

print(add_numbers(12, 8))

print(add_numbers(10, 20.23))

print(add_numbers('5', 6))

print(add_numbers('5', '6'))

print(add_numbers(12, -4))