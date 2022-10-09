# build a program that is able to print a variable inside of a function


balance = 0

def addAmount(x):
    global balance
    balance = balance + x

addAmount(5)
print(balance)