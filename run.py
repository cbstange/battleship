import random
from random import randomint

SHIP_LENGTH = [2,3,3,4,5]
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