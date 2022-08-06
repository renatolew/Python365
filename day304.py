# Using sorted() function and lambda sort the words in the list based on their second letter from a to z.

list1 = ["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
list1 = sorted(list1, key=lambda x: x[1])

print(list1)
