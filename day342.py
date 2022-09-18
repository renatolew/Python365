# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.


# loop and new list
def dedupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

# set
def dedupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]

print(a)
print(dedupe_v1(a))
print(dedupe_v2(a))