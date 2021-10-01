# Write a Python program that invoke a given function after specific milliseconds.

from time import sleep
import math

def delay_func(fn, ms, *args):
  sleep(ms / 2000)
  return fn(*args)

print("Square root after specific miliseconds:")

print(delay_func(lambda x: math.sqrt(x), 100, 25))
print(delay_func(lambda x: math.sqrt(x), 1000, 100))
print(delay_func(lambda x: math.sqrt(x), 2000, 225))