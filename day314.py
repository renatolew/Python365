# A new class named F14 is initated for you which inherits from the parent class Jets.
#
# Instead of taking parameters other than self such as name and country, initiate the new class so that name is always fixed to "F14" and origin is always fixed to "USA"
#
# Make sure the new class has its own initation method (constructor or __init__) which takes only one parameter:self and overrides name and origin attributes as those don't change for an F14 fighter jet.


class Jets:

    def __init__(self, name, country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country

class F14(Jets):

    def __init__(self):
        self.name = "F14"
        self.origin = "USA"


a = F14()
print(a.origin)
print(a.name)
