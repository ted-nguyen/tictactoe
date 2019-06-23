import random
import time
# Needed for clear() function
from os import system, name
from time import sleep

# Starts the game
def start_game():
    # Initialize the board to be empty
    main_board = [' ']*9
    marker1, marker2 = first_turn()
    status = True
    announcement = ''

    while True:
        # Show the board
        clear()
        display_board(main_board)


        status, announcement = check_conditions(main_board, marker1)
        print announcement
        if game

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

# Checks whether the board is full and returns a boolean value. True = full, false otherwise
def full_board_check(board):
    index = 0
    while index < len(board):
        if board[index] == ' ':
            return False
        else:
            index += 1

    return True

# Asks the player where they want to place their marker and whether that spot is open
def ask_player(board, mark):
    question = "Choose where to place your " + mark
    while True:
        try:
            choice = int(raw_input(question))
        except ValueError:
            print("Sorry. Choose a number between 1-9")
            continue

        if board[choice - 1] == " ":
            board[choice - 1] = mark
            break
        else:
            print(board[choice - 1] + " is taken. Look at the board for available spots")
            continue

# Checks whether the player won or if there is a tie and returns the game state and result
def check_conditions(board, mark):
    # Set the results of the game to be blank
    result = ''
    # Validate input
    ask_player(mark)

    if win_check(board, mark):
        clear()
        display_board(board)
        result = mark + " won the game!"
        game_state = False
    elif full_board_check(board):
        clear()
        display_board(board)
        result = "It was a TIE!"
        game_state = False

    return result, game_state

# This is the where the game begins!
intro()
start_game()
