# Write a Python program to print all primes (Sieve_of_Eratosthenes) smaller than or equal to a specified number.

def prime_checker(num):
    limit_num = num+1
    not_prime_num = set()
    prime_nums = []

    for i in range(2, limit_num):
        if i in not_prime_num:
            continue

        for f in range(i * 2, limit_num, i):
            not_prime_num.add(f)

        prime_nums.append(i)

    return prime_nums

print(prime_checker(100));
print(prime_checker(150));
print(prime_checker(50));