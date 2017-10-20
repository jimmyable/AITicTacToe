# Tic Tac Toe

import random

def drawBoard(board):
    #This function prints out the board that it was passed.

    #"board" is a list of 10 strings representing the baord (ignore index 0)
    print('     |     |')
    print('  ' + board[7] + '   |  ' + board[8] + '   |  ' + board[9])
    print('     |     |')
    print('----------------')
    print('     |     |')
    print('  ' + board[4] + '   |  ' + board[5] + '   |  ' + board[6])
    print('     |     |')
    print('----------------')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '   |  ' + board[3])
    print('     |     |')

def inputPlayerLetter():
    #Let the player type which letter they want to be
    #Returns a list with the players letter as the first item and the computer as second
    letter = ''
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
        return 'Player'

def playAgain():
    #This function returns True if the player wants to play again
    print('One more game! (Y or N)')
    return input().upper().startswith('Y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    #Function outputs true if player has a winning board letter combination
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
    #Make a duplicate of the board list and return it as the duplicate.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    #Return true if the passed move is free on the passed board
    return board[move] == ''

def getPlayerMove(board):
    #Let the player type in their move.
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Make your next move! (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    #Returns a valid move from the passes list on the passed board
    #Returns None if there is no valid.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

            if len(possibleMoves) !=0:
                return random.choice(possibleMoves)
            else:
                return None

def getComputerMove(board, computerLetter):
    #Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    #Here is our algorithm for out Tic Tac Toe AI
    #First we check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    #Check if the player can win in 1 move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
        if isWinner(copy, playerLetter):
            return i
    #Try to take one of the corners, if they are free
    move = chooseRandomMoveFromList(board,[1, 3, 7, 9])
    if move != None:
        return move
    #Try to take the center, if it is free
    if isSpaceFree(board, 5):
        return 5
    #Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6 ,8])

def isBoardFull(board):
    #Retrun True if every space on the board has been taken. Otherwise return False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

###########################
#Start of the game#
print('XO TicTacToe XO')
while True:
    #reset the board
    theBoard = ['']*10
    #Decide who goes first
    playerLetter, computerLetter = inputPlayerLetter()
    turn = FirstPlayer()
    print('The '+ turn +' will go first!')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hoooray!, You have won the game!!')
                makeMove(theBoard, playerLetter, move)
    
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('This game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            #Computer's turn
            move = getComputerMove(theBoard,computerLetter)
            makeMove(theBoard,computerLetter, move)
            if isWinner(theBoard,computerLetter):
                drawBoard(theBoard)
                print('The AI has beaten you! xD')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break

start=drawBoard(['X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O'])
