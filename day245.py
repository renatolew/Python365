# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)
exponent(8, 2)
exponent(9, 6)