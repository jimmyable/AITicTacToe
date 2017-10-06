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

start=drawBoard(['X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O'])