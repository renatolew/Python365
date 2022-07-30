# Using map() function and lambda and count() function create a list consisted of the number of occurence of both letters: A and a.

list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

list2 = list(map(lambda x: x.lower().count("a"), list1))


print(list2)