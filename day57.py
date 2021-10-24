# Write a Python program to valid a IP address.

import socket


test_ip = '127.0.0.0'
test_ip2 = '127.0.0.3500'

try:
    socket.inet_aton(test_ip)
    print("Valid IP")
except socket.error:
    print("Invalid IP")

try:
    socket.inet_aton(test_ip2)
    print("Valid IP")
except socket.error:
    print("Invalid IP")