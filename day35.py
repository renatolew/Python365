# Write a Python program to find  the greatest common divisor (gcd) of two integers.

a = int(input('Type the first number to have gcd checked: '))
b = int(input('Type the second number to have gcd checked: '))

def recurse_gcd(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return recurse_gcd(low, high%low)

print(recurse_gcd(a,b))