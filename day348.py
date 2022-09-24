#  This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
#
# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
#
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
#
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.


def print_horiz_line():
    print(" --- " * board_size)


def print_vert_line():
    print("|   " * (board_size + 1))


if __name__ == "__main__":
    board_size = int(input("What size of game board? "))

    for index in range(board_size):
        print_horiz_line()
        print_vert_line()
    print
