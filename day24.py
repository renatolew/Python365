# Write a Python program to execute a string containing Python code.

string_with_code = """
def printing_hello(name):
    return print('Hello, {}!!'.format(name))

printing_hello('John')
"""

exec(string_with_code)