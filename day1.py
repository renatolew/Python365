# Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for
# Santa! Create a function that accepts a Date object and returns True if it's Christmas Eve
# (December 24th) and False otherwise.

print('Welcome to the Santa cookie maker test! Lets see if today is the day we make some cookies for Santa Claus.')

year = input('What year is it? \n')
month = input('What month is it? (Use numbers from 1 to 12) \n')
day = input('What day is it? (Use numbers from 1 to 31) \n')

def xmas_eve_checker(month,day):
    if int(month) == 12 and int(day) == 24:
        return True
    else:
        return False

if xmas_eve_checker(month,day) == True:
    print('Today is christmas eve!! Lets make Santa some cookies!')
else:
    print('It is not christmas eve yet. Santa will have to wait some more for his cookies!')