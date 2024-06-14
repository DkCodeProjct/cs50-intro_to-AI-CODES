"""
Tic Tac Toe Player
"""



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
            elif cell == O:
                o += 1

    
    if x > o:
        return O
    elif o == x:
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
    #print(action)
    i, j = action
    if i < 0 or j < 0 or i >= len(board) or j >= len(board):
        raise Exception('not an  empty cell')
    

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
            if row[0] is not None and all(cell == row[0] for cell in row):
                return row[0]
    
    # Check columns
    for i in range(3):
        if board[0][i] is not None and all(board[j][i] == board[0][i] for j in range(3)):
            return board[0][i]
    
    # Check diagonals
    if board[0][0] is not None and all(board[i][i] == board[0][0] for i in range(3)):
        return board[0][0]
    
    if board[0][2] is not None and all(board[i][2-i] == board[0][2] for i in range(3)):
        return board[0][2]
    
    return None
    
   
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
    return 0

def maxValue(board):
    if terminal(board):
        return utility(board), None
    value = -math.inf
    bestAction = None
    possibleActions = actions(board)
    for act in possibleActions:
        newValue, _ = minValue(result(board, act))
        if newValue > value:
            value = newValue
            bestAction = act
    return value, bestAction

def minValue(board):
    if terminal(board):
        return utility(board), None
    value = math.inf
    bestAction = None
    possibleActions = actions(board)
    for act in possibleActions:
        newValue, _ = maxValue(result(board, act))
        if newValue < value:
            value = newValue
            bestAction = act
    return value, bestAction

def bestActionForPlayer(board):
    if player(board) == X:
        _, action = maxValue(board)
    else:
        _, action = minValue(board)
    return action

def evaluate(board):
    if player(board) == X:
        value, _ = maxValue(board)
    else:
        value, _ = minValue(board)
    return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        _, action = maxValue(board)
    else:
        _, action = minValue(board)
    return action
