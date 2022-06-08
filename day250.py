# Write a Python program to find the circumference and area of a circle with a given radius

import math

r = float(input("Input the radius of the circle: "))

c = 2 * math.pi * r
area = math.pi * r * r

print("The circumference of the circle is: ", c)
print("The area of the circle is: ", area)