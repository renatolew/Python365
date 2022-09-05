# Let's practice using string representation method to represent the data in previous exercise in a much "classier" way, no pun intended!.
#
# __str__ function can be used to return a string representation for the class when needed.

class Nobel:

    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

    def __str__(self):
        return "{} was the winner of Nobel {} Prize in {}".format(self.winner, self.category, self.year)

np2005 = Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005)