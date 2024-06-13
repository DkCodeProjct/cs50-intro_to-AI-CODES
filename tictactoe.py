"""
Tic Tac Toe Player
"""

#
#
#  ...//// BUGGY CODE FIRST TRY \\\...
#    //////// ~~~~~~~~~~~~~~~~~\\\\\\\
#

import math
import copy


X = "X" 
O = "O" 
EMPTY = None 


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0

    for row in board:
        for cell in row:
            if cell == X:
                x += 1
            else:
                o += 1
    
    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is None:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copyBoard = copy.deepcopy(board)
    i, j = action
    if copyBoard[i][j] is not None:
        raise Exception('not empty')
    
    else: 
        if player(board) == X:
           copyBoard[i][j] = X
        else:
            copyBoard[i][j] = O
    return copyBoard



    
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if all(element== X and element is not None for element in  row ):
            return X
        if all(element== O and element is not None for element in  row ):
            return O
    
    for i in range(0, 3):
        col = [[row[i]] for row in board]
        
        if all(element == X  for element  in col):
            return X
        
        if all(element == O for element  in col):
            return O
    
    
    diagnalLeft = [board[i][i] for i in range(0, 3)]

    if all(element == X for element in diagnalLeft) and all(element is not None for element in diagnalLeft):
        return X
    if all(element == O for element in diagnalLeft) and all(element is not None for element in diagnalLeft):
        return O
    
    diagnalRight =[board[i][3 - 1 - i] for i in range(0, 3)]

    if all(element == X for element in diagnalRight) and all(element is not None for element in diagnalRight):
        return X
    if all(element == O for element in diagnalRight) and all(element is not None for element in diagnalRight):
        return O

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    if winner(board) is not None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return utility(board)
    
    action = actions(board)

    if player(board) == X:
        return max(minimax(result(board,action)))
    if player(board) == O:
        return min(minimax(result(board,action)))
