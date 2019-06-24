import random
import time
# Needed for clear() function
from os import system, name
from time import sleep

# Global variables
# Set the board to be an empty list
main_board = [' ']*9
# Game is on by default
status = True
announcement = marker1 = marker2 = ''

# Starts the game
def start_game():
    global announcement, marker1, marker2
    reset_board()

    # Randomly assign marker1 and marker2 X or O
    marker1, marker2 = first_turn()

    while True:
        # Show the board
        clear()
        display_board()

        # If marker1 is X, they go first
        if marker1 == 'X':
            # Player X
            announcement, status = check_player(marker1)
            print(announcement)
            if status == False:
                break

            # Player O
            announcement, status = check_computer(marker2)
            print(announcement)
            if status == False:
                break
        # Else they are O, and go second
        else:
            # Player X
            announcement, status = check_computer(marker2)
            print(announcement)
            if status == False:
                break

            # Player O
            announcement, status = check_player(marker1)
            print(announcement)
            if status == False:
                break

# Introduces the game and displays the board with numbers to show the positions
def intro():
    global main_board
    # Clear the current screen
    clear()
    main_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board()
    print("Welcome to Tic-Tac-Toe!")
    print("Choose a number between 1-9 to place your marker on the board above")
    input("Press Enter to continue...")

# Clears the terminal screen
def clear():
    # For windows
    if name == 'nt':
        _ = system('cls')
    # For mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Resets the board to be empty and status = True
def reset_board():
    global main_board, status
    main_board = [' ']*9
    game_state = True

# Displays the tic-tac-toe board
def display_board():
    global main_board, marker1, marker2
    print(f"Player 1: {marker1}             Computer: {marker2}")
    print("   |   |   ")
    print(' ' + main_board[0] + ' ' + '|' + ' ' + main_board[1] + ' ' + '|' + ' ' + main_board[2] + ' ')
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(' ' + main_board[3] + ' ' + '|' + ' ' + main_board[4] + ' ' + '|' + ' ' + main_board[5] + ' ')
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(' ' + main_board[6] + ' ' + '|' + ' ' + main_board[7] + ' ' + '|' + ' ' + main_board[8] + ' ')
    print("   |   |   ")

# Randomly ssigns the user a marker (X or O). Returns marker1 and marker2
def first_turn():
    flip = random.randint(0, 1)

    if flip == 0:
        marker1 = 'X'
        marker2 = 'O'
    else:
        marker1 = 'O'
        marker2 = 'X'

    return (marker1, marker2)

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
def ask_player(mark):
    global main_board

    question = mark + "'s turn. Choose where to place your marker: "
    while True:
        try:
            choice = int(input(question))
        except ValueError:
            print("Sorry. Choose a number between 1-9")
            continue

        if main_board[choice - 1] == " ":
            main_board[choice - 1] = mark
            break
        else:
            print(f"{choice} is taken. Look at the board for available spots")
            continue

# Randomly assigns the computer a position between 1-9 if it is open
def ask_computer(mark):
    global main_board

    # Randomly choose a number between 1-9
    choice = random.randrange(1, 10)

    # The computer has to "think" for 1.5 seconds
    print("Computer is thinking...")
    time.sleep(1.5)
    while True:
        if main_board[choice - 1] == " ":
            main_board[choice - 1] = mark
            break
        else:
            choice = random.randrange(1, 10)
            continue

# Checks whether the player won or if there is a tie and returns the game state and result
def check_player(mark):
    global main_board, status, announcement
    # Set the results of the game to be blank
    announcement = ''
    # Validate input
    ask_player(mark)

    # Check for win
    if win_check(main_board, mark):
        clear()
        display_board()
        announcement = mark + " won the game!"
        status = False
    # Show the baord
    clear()
    display_board()

    # Check for a tie
    if full_board_check(main_board):
        clear()
        display_board()
        announcement = "It was a TIE!"
        status = False

    return announcement, status

# Checks whether the computer won or if there is a tie and returns the game state and result
def check_computer(mark):
    global main_board, status, announcement
    # Set the results of the game to be blank
    announcement = ''
    # Validate input
    ask_computer(mark)

    # Check for win
    if win_check(main_board, mark):
        clear()
        display_board()
        announcement = mark + " won the game!"
        status = False
    # Show the baord
    clear()
    display_board()

    # Check for a tie
    if full_board_check(main_board):
        clear()
        display_board()
        announcement = "It was a TIE!"
        status = False

    return announcement, status

# Checks whether the game wants to be played again
def replay():
    ans = input("Do you want to play again? y/n: ")
    if ans == 'y' or ans == 'Y':
        return True
    else:
        return False

# This is the where the game begins!
intro()

while True:
    start_game()
    # If they want to play again, start a new game
    if replay():
        continue
    # Otherwise, break out of the loop
    else:
        break
