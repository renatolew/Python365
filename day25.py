# Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.


num_test = int(input('Type the number to be tested: '))


def prime_test(num):
    if (num == 1):
        return False
    elif (num == 2):
        return True;
    else:
        for x in range(2, num):
            if(num % x == 0):
                return False
        return True

print(prime_test(num_test))