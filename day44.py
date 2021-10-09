# Write a Python class to get all possible unique subsets from a set of distinct integers.

class set_subsets:
    def sub_sets(self, sub_set):
        return self.subsetsRecur([], sorted(sub_set))

    def subsetsRecur(self, current, sub_set):
        if sub_set:
            return self.subsetsRecur(current, sub_set[1:]) + self.subsetsRecur(current + [sub_set[0]], sub_set[1:])
        return [current]


print(set_subsets().sub_sets([1, 2, 3]))

print(set_subsets().sub_sets([1, 2, 3, 4, 5, 6]))