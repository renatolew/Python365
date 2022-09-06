# We have seen multiple examples of class usage in Python. Let's build something from ground up.
#
# In this exercise create a class named myfunc and inside it place a very simple function named "fifth" which takes x and returns fifth power of x. No __init__ or class attributes needed.
#
# Finally call your function with number 5 and assign it to variable ans.


class myfunc:

    def fifth(x):
        return x ** 5

ans = myfunc.fifth(5)

print(ans)