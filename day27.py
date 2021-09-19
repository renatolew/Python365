# Write a Python program to returns sum of all divisors of a number.

def sum_div(number):
    divisors = [1]
    for n in range(2, number):
        if (number % n) == 0:
            divisors.append(n)
    return sum(divisors)


print(sum_div(15))
print(sum_div(22))