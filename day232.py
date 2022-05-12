# Given two integer numbers return their product only if the product is greater than 1000, else return their sum.

def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

func_return = multiplication_or_sum(10, 20)
print(func_return)

func_return = multiplication_or_sum(55, 35)
print(func_return)