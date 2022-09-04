# Try building a simple class from the ground up.
# An instance is already created for you and instance attributes are included inside the print.
# Take those clues and try to reverse engineer the class.

class Nobel:

    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

np2005 = Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005.category, np2005.year, np2005.winner)