# Using map() function and lambda and count() function create a list which consists of the number of occurence of letter: a.

list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

list2 = list(map(lambda x: x.count("a"), list1))


print(list2)