# Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on.
# Continues this operation until the number is no longer positive.

def subtract_own_digits(num):
  qty_op = 0
  num_str = str(num)
  while (num > 0):
    num -= sum([int(i) for i in list(num_str)])
    num_str = list(str(num))
    qty_op += 1
  return qty_op


print(subtract_own_digits(10))
print(subtract_own_digits(25))
print(subtract_own_digits(121))