# Write a similar function to the previous exercise which returns the number of words that start with letter "A" in a string.
# (Make sure it counts lower case a's as well).

str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's. Amem!"

def count_a(string):
    c = 0
    for i in string.split():
        if i[0].lower() == 'a':
            c = c + 1
        else:
            pass

    return c

print(count_a(str))