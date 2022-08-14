# .get() is not a list method. Place pass keyword to the right line so that program doesn't throw an error.


a = [1, 3, 5]

try:
    a.get()
except:
    pass

print(a)