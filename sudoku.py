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


def constraints(board):
    # check row Constrain
    for row in range(9):
        rowSet = set()
        for nums in board[row]:
            if nums != 0:
                if nums in rowSet:
                    return False
                rowSet.add(nums)
    
    # check col Constrain
    for col in range(9):
        colSet = set()
        for row in range(9):
            nums = board[row][col]
            if nums != 0:
                if nums in colSet:
                    return False
                colSet.add(nums)

    # check 3x3 box Constrain
    for boxRow in range(3): # y:
        for boxCol in range(3): # x:  --- > x:y: loop over over each 3x3 box in the 9x9 grid.
            boxSet = set()
            for j in range(3): #w:
                for k in range(3): #z  ---- > w:z: loop over  over each cell within a single 3x3 box.
                    nums = board[boxRow * 3 + j][boxCol * 3 + k]
                    if nums != 0:
                        if nums in boxSet:
                            return False
                        boxSet.add(nums)
    return True


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
                """
                for i in range(3):
                    for j in range(3):
                        r = boxRow + i
                        c = boxCol + j
                        if (r, c) != (row, col) and board[r][c] == 0:
                            q.append(((row, col)), ((r, c)))
                """
                for i in range(3):
                    for j in range(3):
                        r = boxRow + i
                        c = boxCol + j
                        if (r, c) != (row, col) and board[r][c] == 0:
                            q.append(((row, col), (r, c)))
    return q 


def isValid(x, y, X, Y):
    xRow, xCol = X
    yRow, yCol = Y

    if xRow == yRow:
        return x != y
    elif xCol  == yCol:
        return x != y 
    elif (xRow // 3, xCol // 3) == (yRow // 3, xCol // 3):
        return x != y 
    return True

 

def revise(domain ,X, Y):
    rvis = False
    xRow, xCol = X
    yRow, yCol = Y

    for x in list(domain[X]):
        if not any(isValid(x, y,X, Y) for y in domain[Y]):
            domain[x].remove(x)
            rvis = True
    return rvis



def AC3(domain, board):
    q = init_Q(board)

    while q:
        x, y = q.popleft()

        if revise(domain, x, y):
            if not domain[x]:
                return False
            for z in domain:
                if z != y and z != x and isValid(domain, x, z):
                    q.append((z,x))
    return True

def selectUnAssignedVar(domains):
    unAsingVar = [var for var in domains if len(domains[var]) > 1]
    if not unAsingVar:
        return None
    return min(unAsingVar, key=lambda var: len(domains[var]))


def backTrackRecursive(board, domains):
    if all(len(domains[cell]) == 1 for cell in domains):
        return True

    cell = selectUnAssignedVar(domain)
    for val in list(domain[cell]):
        originalDomain = {var: domain[var].copy() for var in domain}
        board[cell[0]][cell[1]] = val
        domain[cell] = {val}

        if AC3(domain, board) and backTrackRecursive(board, domain):
            return True
        
        board[cell[0]][cell[1]] = 0
        domain = originalDomain
    return False

def backTrack(board):
    doms = domains(board)
    if AC3(doms, board):
        return backTrackRecursive(board, doms)
    return False



sudokuBoard = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]

if backTrack(sudokuBoard):
    for row in sudokuBoard:
        print(row)
else:
    print("No solution exists")
    



