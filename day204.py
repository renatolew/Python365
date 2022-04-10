# Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)
tuple2 = (45, 25, 35, 45)


def check(tuple):
    return all(i == tuple[0] for i in tuple)

print(check(tuple1))
print(check(tuple2))