# Place result="You can't divide with 0" to the right place so that program avoids ZeroDivisionError.



a = 5
b = 0

try:
    result = a/b
except ZeroDivisionError:
    result = "You can't divide with 0"

print(result)