'''
Leta Zeng
CS8 Homework 2
This code allows a user and the computer to play a game of tic-tac-toe
This code also includes extra credit: the user can keep playing games until
they decide to exit and it keeps track of wins by the computer and user
'''

import random
        
def main():
    turn = 1
    game_number = 0
    user_win = 0
    cpu_win = 0
    while turn == 1:
        game_number += 1
        symbol = input('Which player would you like to be?(X or O) ').upper()

        """This accounts for if the user does not input a valid symbol"""
        while symbol != 'X' and symbol != 'O':
            print('Please enter a valid answer')
            symbol = input('Which player would you like to be?(X or O) ').upper()

        """This assigns the user and the computer the role they will be in the game"""
        if symbol == 'X':
            computer = 'O'
        elif symbol == 'O':
            computer = 'X'
        
        # Basic game board initialization.
        game_board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

        print('User has {} and will go first...'.format(symbol))
        while not is_draw(game_board) and not has_player_won(game_board, symbol):
            # This goes through the user's turn
            print("It's your turn...")
            game_board = get_user_move(game_board, symbol)
            display_board(game_board)

            #Checks if the user has won
            if has_player_won(game_board, symbol):
                user_win += 1
                print('Congrats, you won!')
                print('=' * 45)
                break
            #Checks if the game is a draw
            if is_draw(game_board):
                print("It's a draw!")
                print('=' * 45)
                break
            else:
                print('=' * 45)
            # This goes through the computer's turn
            print("Computer's turn...")
            game_board = get_computer_move(game_board, computer)
            display_board(game_board)

            #Checks if the computer has won
            if has_player_won(game_board, computer):
                cpu_win += 1
                print('Sorry, you lost!')
                print('=' * 45)
                break
            #Checks if the game is a draw
            if is_draw(game_board):
                print("It's a draw!")
                print('=' * 45)
                break
            else:
                print('=' * 45)
        print('Thanks for playing!')
        more_games = input('Do you want to continue (Y/N)? ')
        if more_games.upper() != 'Y':
            turn = -1
    print("{} games were played, and user won {} games and computer won {} games".format(game_number, user_win, cpu_win))
    
def display_board(game_board):
    """This function prints the game board for the user to see its state."""
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == (''):
                #Checks to see if the iteration is at the end of a row to remove the '|' symbol
                if col == 2:
                    print('_ _', end = '')
                else:
                    print('_ _|', end = '')
            else:
                #Checks to see if the iteration is at the end of a row to remove the '|' symbol
                if col == 2:
                    print('_{}_'.format(game_board[row][col]), end = '')
                else:
                    print('_{}_|'.format(game_board[row][col]), end = '')
        print('')  
    pass

def get_user_move(game_board, symbol):
    """This function asks the user for their row and column move and sets the game_board with
       their symbol."""
    row = input('What row do you want to play? (0-2) ')
    col = input('What column do you want to play? (0-2) ')
    """Checks to see if the row and col input are valid inputs. Otherwise, it continues to ask the user
       for a valid input"""
    while not is_legal_move(game_board, row, col):
        print('Please enter a valid answer')
        row = input('What row do you want to play? (0-2) ')
        col = input('What column do you want to play? (0-2) ')
    """This converts row and col into an int value after being validated in is_legal_move"""
    row = int(row)
    col = int(col)
    """This sets the game_board at the user's desired coordinates with their symbol"""
    game_board[row][col] = symbol
    return game_board
    pass

def get_computer_move(game_board, computer):
    """This function generates random number coordinates for the computer to place their
    symbol."""
    row = random.randint(0,2)
    col = random.randint(0,2)
    """Checks to see if the row and col input are valid inputs. Otherwise, the computer
       must continue to generate random number coordinates"""
    while not is_legal_move(game_board, row, col):
        row = random.randint(0,2)
        col = random.randint(0,2)
    """This sets the game_board at the computer's randomly generated coordinates with its symbol"""
    game_board[row][col] = computer
    return game_board
    pass
    
def is_legal_move(game_board, row, col):
    """This function checks to see if the row and col provided are within the boundaries of 
       the board and if the space is unoccupied."""
    """This converts row and col, which are strings, into integers. If the inputed row and col
       cannot be converted into an integer, the function returns False"""
    try:
        row = int(row)
        col = int(col)
    except ValueError:
        return False
    if row >= 0 and row <= 2 and col >= 0 and col <= 2:
        if game_board[row][col] == (''):
            return True
    return False
    pass

def is_draw(game_board):
    """This function determines if a game is a draw by checking each space. If it finds at
       least one empty spot, it will return False since it's a playable spot."""
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == (''):
                return False
    return True
    pass

def has_player_won(game_board, symbol):
    """Check to see if the given symbol has won the game in any of the possible
       ways."""
    winner_sequence = symbol * 3 
    
    # Check for horizontal wins
    for r in range(len(game_board)):
        row_symbols = ''
        for c in range(len(game_board[r])):
            row_symbols += game_board[r][c]
        if row_symbols == winner_sequence:
            return True
        
    # Check for vertical wins
    for c in range(len(game_board[0])):
        col_symbols = ''
        for r in range(len(game_board)):
            col_symbols += game_board[r][c]
        if col_symbols == winner_sequence:
            return True
            
    # Check for the two diagonal wins
    diag_symbols = ''
    anti_diag_symbols = ''
    for rc in range(len(game_board)):
        diag_symbols += game_board[rc][rc]
        anti_diag_symbols += game_board[rc][len(game_board) - 1 - rc]
    if winner_sequence in (diag_symbols, anti_diag_symbols):
        return True
    
    # If we got here, nobody won yet
    return False

main()
