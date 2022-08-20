# From scratch create a new class named AJS37. Make it inherit from the parent class Jets. This jet should have an origin attribute of Sweden and name attribute of AJS37. The rest of the attributes doesn't need to be overwriten.
#
# Assign an instance of the new class to the variable b.

class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country

class AJS37(Jets):
    def __init__(self):
        self.name = "AJS37"
        self.origin = "Sweden"

b = AJS37()
print(b.name)
print(b.origin)