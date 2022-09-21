# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
#     Ask the user how strong they want their password to be.


# generate a password with length "passlen" with no duplicate characters in the password

import random

characs = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input("Type the lenght of the password you want to be generated: "))

random_password =  "".join(random.sample(characs,passlen ))
print(random_password)