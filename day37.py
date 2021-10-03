# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).


def sum_series(number):
  if number < 1:
    return 0
  else:
    return number + sum_series(number - 2)

print(sum_series(15))
print(sum_series(32))