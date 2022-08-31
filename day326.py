# A class regarding an imaginary jet inventory is already defined for you. Also an instant of this Jet class is created and assigned to variable first_item.
#
# Print the name of the first_item.

class Jets:

    def __init__(self, name, country):
        self.name = name
        self.origin = country


first_item = Jets("F16", "USA")

a = first_item.name
print(a)
