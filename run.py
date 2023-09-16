import random
from random import randint

LENGTH_OF_SHIPS = [2, 3, 3, 4, 5]
PLAYER_BRD = [[" "] * 8 for i in range(8)]
COM_BRD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BRD = [[" "] * 8 for i in range(8)]
COM_GUESS_BRD = [[" "] * 8 for i in range(8)]
LET_TO_NUM = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

def welcome():
    """
    Welcome message with simple game play instructions
    and request for user to start game.
    """
    print("Welcome to Battleship!")
    print("----------------------------------")
    print("The rules are simple.")
    print("You and the computer will place")
    print("five ships on your board.")
    print("Sink all the ships and you win!")
    print("----------------------------------\n")
    input("Press 'enter' to start the game!\n")

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
                orientation, row, column = (
                    random.choice(["H", "V"]),
                    random.randint(0, 7),
                    random.randint(0, 7),
                )
                if ship_fit_check(ship_length, row, column, orientation):
                    # check for overlaping
                    if (
                        ship_overlaps(board, row, column, orientation, ship_length)
                        == False
                    ):
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
                    if (
                        ship_overlaps(board, row, column, orientation, ship_length)
                        == False
                    ):
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        display_board(PLAYER_BRD)
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

def ship_overlaps(board, row, column, orientation, ship_length):
    """
    Verifies position of ships do not overlap.
    """
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False

# Try/except code used from Knowledge Mavens. See README for credit.
def user_input(place_ship):
    """
    Try and except statements to verify that user
    input is valid and to raise an error requesting
    valid imput from user.
    """
    if place_ship == True:
        while True:
            try:
                orientation = input(
                    "Enter ship orientation: 'H' for horizontal or 'V' for vertical.\n "
                ).upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print(
                    "Invalid entry. Please enter ship orientation: 'H' for horizontal or 'V' for vertical.\n "
                )
        while True:
            try:
                row = input("Enter row 1-8 for the ship. \n")
                if row in "12345678":
                    row = int(row) - 1
                    break
            except ValueError:
                print("Please enter a valid number between 1-8.\n")
        while True:
            try:
                column = input("Enter the column of the ship between A-H.\n").upper()
                if column in "ABCDEFGH":
                    column = LET_TO_NUM[column]
                    break
            except KeyError:
                print(
                    "Invalid entry. Please enter a letter between A-H for the column.\n"
                )
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter row 1-8 for the ship.\n")
                if row in "12345678":
                    row = int(row) - 1
                    break
            except ValueError:
                print("Invalid entry. Please enter a number between 1-8.\n")
        while True:
            try:
                column = input("Enter the column of the ship between A-H.\n").upper()
                if column in "ABCDEFGH":
                    column = LET_TO_NUM[column]
                    break
            except KeyError:
                print(
                    "Invalid entry. Please enter a letter between A-H for the column.\n"
                )
        return row, column

def hit_ships_count(board):
    """
    Verifies if all ships have been hit.
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

def take_turn(board):
    """
    Function for both player and computer to take a turn.
    Player is prompted to make a choice, while computer
    generates rondom choices.
    """
    if board == PLAYER_GUESS_BRD:
        row, column = user_input(PLAYER_GUESS_BRD)
        if board[row][column] == "-":
            take_turn(board)
        elif board[row][column] == "X":
            take_turn(board)
        elif COM_BRD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "-":
            take_turn(board)
        elif board[row][column] == "X":
            take_turn(board)
        elif PLAYER_BRD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"

welcome()
place_ships(COM_BRD)
display_board(PLAYER_BRD)
place_ships(PLAYER_BRD)

# Game play: Player & computer taking turns.
while True:
    # Player takes turn
    while True:
        print("Guess a ship location.\n")
        display_board(PLAYER_GUESS_BRD)
        take_turn(PLAYER_GUESS_BRD)
        break
    if hit_ships_count(PLAYER_GUESS_BRD) == 17:
        print("Congratulations! You win!\n")
        break
    # Computer takes turn
    while True:
        take_turn(COM_GUESS_BRD)
        break
    display_board(COM_GUESS_BRD)
    if hit_ships_count(COM_GUESS_BRD) == 17:
        print("Bummer! The computer won.\n")
        break