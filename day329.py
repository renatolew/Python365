# Add another attribute called "quantity" to the initialization method (usually referred to as constructor or __init__). Then define assign this attribute to self.quantity attribute inside the constructor.
#
# Then create 2 instances for: F14 and Mirage2000 with quantities 87 and 35.


class Jets:
    model = None
    country = 0

    def __init__(self, name, country, quantity):
        self.name = name
        self.origin = country
        self.quantity = quantity



first_item = Jets("F14", "USA", 87)
second_item = Jets("Mirage2000","France", 35)

total = first_item.quantity + second_item.quantity
print(total)
