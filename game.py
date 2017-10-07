# Tic Tac Toe

import random

def drawBoard(board):
    #This function prints out the board that it was passed.

    #"board" is a list of 10 strings representing the baord (ignore index 0)
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |')
    print('----------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |')
    print('----------------')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |')

def PlayerLetter():
    #Let the player type which letter they want to be
    #Returns a list with the players letter as the first item and the computer as second
    letter = ""
    while not (letter == 'X' or letter == 'O'):
        print('Are you an X or an O?')
        letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def FirstPlayer():
    #randomly chooses the 1st PlayerLetter
    if random.randint(0, 1) == 0:
        return 'AI'
    else:
        return 'You'

def playAgain():
    #This function returns True if the player wants to play again
    print('One more game! (Y or N)')
    return input().upper().startswith('Y')

def makeMove(board, letter, move):
    board[move] = letter



start=drawBoard(['X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O'])
