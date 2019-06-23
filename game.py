# importing "random" for random operations
import random
import time
# Needed for clear() function
from os import system, name
from time import sleep

# This will start the game
def start_game():
    # Initialize the board to be empty
    main_board = [' ']*10
    clear()
    display_board(main_board)
    player1_marker, player2_marker = player_input()

    # If user is X, they start first
    if player1_marker == 'X':
        # Keep prompting the player until they pick an open spot
        while True:
            p1spot = int(input("Your turn to mark a spot (1-9): "))
            # Check if their choice is available
            if space_check(main_board, p1spot):
                place_marker(main_board, player1_marker, p1spot)
                display_board(main_board)
                break
            else:
                print(f"{p1spot} is already taken. Look at the board for available spots.")
        # Keep assigning a random number until an available spot is chosen for the computer
        while True:
            # Assign p2spot to a random number between 1-9
            p2spot = random.randrange(1, 10)
            if space_check(main_board, p2spot):
                # Wait 1.5 seconds before updating the board
                time.sleep(1.5)
                print(f"The computer has placed their marker at position {p2spot}")
                place_marker(main_board, player2_marker, p2spot)
                display_board(main_board)
                break
            else:
                p2spot = random.randrange(1,10)

    # Else, the user is O and the computer will go first
    else:
        # Keep assigning a random number until an available spot is chosen for the computer
        while True:
            # Assign p2spot to a random number between 1-9
            p2spot = random.randrange(1, 10)
            if space_check(main_board, p2spot):
                print(f"The computer has placed their marker at {p2spot}")
                place_marker(main_board, player2_marker, p2spot)
                display_board(main_board)
                break
            else:
                p2spot = random.randrange(1,10)

        # Keep prompting the player until they pick an open spot
        while True:
            p1spot = int(input("Your turn to mark a spot (1-9): "))
            # Check if their choice is available
            if space_check(main_board, p1spot):
                place_marker(main_board, player1_marker, p1spot)
                display_board(main_board)
                break
            else:
                print(f"{p1spot} is already taken. Look at the board for available spots.")

# Introduces the game and displays the board with numbers to show the positions
def intro():
    clear()
    test_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(test_board)
    print("Welcome to Tic-Tac-Toe! Here is what the game board will look like.")
    input("Press Enter to continue...")

# Clears the terminal screen
def clear():
    # For windows
    if name == 'nt':
        _ = system('cls')
    # For mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Displays the tic-tac-toe board
def display_board(board):
    print("   |   |   ")
    print(' ' + board[0] + ' ' + '|' + ' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ')
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(' ' + board[3] + ' ' + '|' + ' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ')
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(' ' + board[6] + ' ' + '|' + ' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ')
    print("   |   |   ")

# Assigns the user a marker (X or O). Returns two character values
def player_input():
    # Take input from user if they want to be X or O
    # Keep asking until they pick X or O; Use a While True  + if statements to emulate do while() loop
    while True:
        p1marker = input("Do you want to be X or O? ")
        if p1marker.upper() == 'X':
            p1marker = p1marker.upper()
            p2marker = 'O'
            print(f"You will play as {p1marker} and the computer will play as {p2marker}.")
            break
        elif p1marker.upper() == 'O':
            p1marker = p1marker.upper()
            p2marker = 'X'
            print(f"You will play as {p1marker} and the computer will play as {p2marker}.")
            break
        else:
            print(f"{p1marker} is not a valid option!")

    return (p1marker, p2marker)

# Places the marker on the board given their marker and position selected
#def place_marker(board, marker, position):
    pass

# Checks whether the position in the board is open and returns a boolean value. True = open, false = taken
def space_check(board, position):
    # Needs to be position - 1 because the list starts at 0
    if board[position - 1] != ' ':
        return False
    else:
        return True

# Checks whether the board is full and returns a boolean value. True = full, false otherwise
def full_board_check(board):
    index = 0
    while index < len(board):
        if board[index] == ' ':
            return False
        else:
            index += 1

    return True

# Places the player's marker at the given position on the baord
def place_marker(board, marker, position):
    board[position - 1] = marker

# Checks to see if a mark has three in a row (horizontal, vertical, or diagonal) to win the game and returns a boolean value
def win_check(board, mark):
    # Check if there was three in a row horizontally
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == mark:
            return True
    # Check if there was three in a row vertically
    for i in range (0, 3):
        if board[i] == board[i + 3] == board[i + 6] == mark:
            return True
    # Check first diagonal
    if board[0] == board[4] == board[8] == mark:
        return True
    # Check second diagonal
    if board[2] == board[4] == board[6] == mark:
        return True

    return False

# This is where the game begins!
intro()
start_game()
