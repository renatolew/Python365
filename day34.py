# Write a Python program to convert a float to ratio.


from fractions import Fraction

float_num = 8.4

print(Fraction(float_num).limit_denominator())