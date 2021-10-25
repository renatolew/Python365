# Write a Python program to access and print a URL's content to the console.

from http.client import HTTPConnection


conn = HTTPConnection("renatolew.github.io")

conn.request("GET", "/")
result = conn.getresponse()

contents = result.read()

print(contents)