# Now let's make some changes to the class we created in the previous Python exercise.
#
# First make your function so that it takes to parameters: x and y. x will be the number being raised and y will be the power. So, users can raise numbers to any power! Also let's change the function's name to power.
#
# Also let's add a string representation quickly, so that when a user prints the class they get a meaningful description.
#
# It can be something like: This class will consist of mathematical operations. We only have one function named power currently.

class myfunc:

    def power(x,y):
        return x ** y

    def __str__(self):
        return "Myfunc is a class which is capable of mathematical operations like raising a number to a power with power function."

ans1 = myfunc.power(5, 6)
ans2 = myfunc()

print(ans1)
print(ans2)