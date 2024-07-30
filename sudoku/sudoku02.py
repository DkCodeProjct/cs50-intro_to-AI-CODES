from collections import deque


def domains(board):
    h1 = {}
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                h1[(row, col)] = set(range(1, 10))
            else:
                h1[(row, col)] = {board[row][col]}
    return h1

def isValid(x, y, X, Y):
    # if the [x,y] in the same [row,col] value should be x!=y 
    xRow, xCol = X
    yRow, yCol = Y

    if xRow == yRow:
        return x != y
    elif xCol == yCol:
        return x != y 
    elif (xRow // 3, xCol // 3) == (yRow // 3, yCol // 3):
        return x != y 
    return True

def revise(domains, X, Y):
    rvis = False
    xRow, xCol = X
    yRow, yCol = Y

    for x in list(domains[X]):
        if not any(isValid(x, y, X, Y) for y in domains[Y]):
            domains[X].remove(x)
            rvis = True
    return rvis

def init_Q(board):
    q = deque()
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for c in range(9):
                    if board[row][c] == 0:
                        q.append(((row, col), (row, c)))
                for r in range(9):
                    if board[r][col] == 0:
                        q.append(((row, col), (r, col)))
                
                boxRow = row - row % 3
                boxCol = col - col % 3
                for i in range(3):
                    for j in range(3):
                        r = boxRow + i
                        c = boxCol + j
                        if (r, c) != (row, col) and board[r][c] == 0:
                            q.append(((row, col), (r, c)))
    return q 

def AC3(domains, board):
    q = init_Q(board)

    while q:
        X, Y = q.popleft()
        if revise(domains, X, Y):
            if not domains[X]:
                return False
            for Z in domains:
                if Z != Y and Z != X and isValid(domains, X, Z):
                    q.append((Z, X))
    return True

def select_unassigned_variable(domains):
    unassigned_vars = [var for var in domains if len(domains[var]) > 1]
    if not unassigned_vars:
        return None
    return min(unassigned_vars, key=lambda var: len(domains[var]))

def backtrack(board):
    doms = domains(board)   
    if AC3(doms, board):
        return backtrack_recursive(board, doms)
    return False

def backtrack_recursive(board, domains):
    if all(len(domains[cell]) == 1 for cell in domains):
        return True

    cell = select_unassigned_variable(domains)
    for value in list(domains[cell]):
        original_domains = {var: domains[var].copy() for var in domains}
        board[cell[0]][cell[1]] = value
        domains[cell] = {value}

        if AC3(domains, board) and backtrack_recursive(board, domains):
            return True

        board[cell[0]][cell[1]] = 0
        domains = original_domains

    return False

# Example usage
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if backtrack(board):
    for row in board:
        print(row)
else:
    print("No solution exists")
