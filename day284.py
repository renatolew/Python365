# Write a function named "count_l" that counts the number of words that contain the letter: "l" in a given string.

string1 = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's... lobster!"

def count_l(a):
    c = 0
    for i in a.split():
        if "l" in i:
            c += 1
        else:
            pass

    return c


print(count_l(string1))
