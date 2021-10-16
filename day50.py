# Write a Python program to compute the product of a list of integers (without using for loop).


from functools import reduce

nums = [5, 10, 15,]

print("Original list numbers:")
print(nums)

nums_product = reduce( (lambda x, y: x * y), nums)

print("\nProduct of the said numbers (without using for loop):",nums_product)
