# This will start the game
def start_game():
    # Initialize the board to be empty
    main_board = ['']*10
    display_board(main_board)
    player1_marker, player2_marker = player_input()

# Introduces the game and displays the board with numbers to show the positions
def intro():
    print("Welcome to Tic-Tac-Toe! Here is what the game board will look like:")
    test_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(test_board)
    input("Press Enter to continue...")

# Clears the screen
from os import system, name
from time import sleep
def clear():
    # For windows
    if name == 'nt':
        _ = system('cls')
    # For mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Displays the tic-tac-toe board
def display_board(board):
    clear()
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

# Assigns the user a marker (X or O)
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
#def place_marker(board, marker, position:


# This is where the game begins!
intro()
start_game()
