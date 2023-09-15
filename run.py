import random
from random import randomint

LENGTH_OF_SHIPS = [2,3,3,4,5]
PLAYER_BRD = [[" "] * 8 for i in range(8)]
COM_BRD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BRD = [[" "] * 8 for i in range(8)]
COM_GUESS_BRD = [[" "] * 8 for i in range(8)]
LET_TO_NUM = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, "G": 6, 'H': 7}

def display_board(board):
    """
    Display initial board play area starting at 1 
    then iterating through row length.
    """
    print("  A B C D E F G H")
    print(" -----------------")
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1

def place_ships(board):
    """
    Function loops through the different ship lengths until
    a ship fits in its orientation and does not overlap or
    go outside of the board boundry.
    """
    for ship_length in LENGTH_OF_SHIPS:
        while True:
            if board == COM_BRD:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                if ship_fit_check(ship_length, row, column, orientation):
                    # check for overlaping
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                    board[i][column] = "X"
                        break
            else:
                place_ship = True
                print(f"Place ship with a length of {ship_length}.\n")
                row, column, orientation = user_input(place_ship)
                if ship_fit_check(ship_length, row, column, orientation):
                        if ship_overlaps(board, row, column, orientation, ship_length) == False:
                            if orientation == "H":
                                for i in range(column, column + ship_length):
                                    board[row][i] = "X"
                            else:
                                for i in range(row, row + ship_length):
                                    board[i][column] = "X"
                            print_board(PLAYER_BOARD)
                            break 

def ship_fit_check(SHIP_LENGTH, row, column, orientation):
    """
    Verifies if ship will fit based on its orientation, 
    length and position within the board.
    """
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True