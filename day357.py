# If we have a list of persons who like to eat at restaurants, can we make every one of them eat a certain restaurant?

persons = [ "John", "Marissa", "Pete", "Dayton" ]
restaurants = [ "Japanese", "American", "Mexican", "French" ]

for person in persons:
    for restaurant in restaurants:
        print(person + " eats " + restaurant)