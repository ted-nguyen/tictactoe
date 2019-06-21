# This will start the game
def start_game():
    # Take input from user if they want to be X or O
    player1 = input("Do you want to be X or O? ").upper()
    if player1 == 'X':
        player2 = 'O'
        print(f"You will play as {player1} and the computer will play as {player2}.")
    elif player1 == 'O':
        player2 = 'X'
        print(f"You will play as {player1} and the computer will play as {player2}.")
    else:
        print(f"{player1} is not a valid option!")

def intro():
    print("Welcome to Tic-Tac-Toe! Here is what the game board will look like:")
    print("   |   |   ")
    print(" 1 | 2 | 3 ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" 4 | 5 | 6 ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" 7 | 8 | 9 ")
    print("   |   |   ")
    print(end='\n')

intro()
start_game()
