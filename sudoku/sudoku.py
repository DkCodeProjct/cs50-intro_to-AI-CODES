from collections import deque

class SudokuSolver:
    def __init__(self):
        self.q = deque()
        self.hash1 = {}

    def domains(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    self.hash1[(row, col)] = set(range(1, 10))
                else:
                    self.hash1[(row, col)] = {board[row][col]}
        return self.hash1
    
    def isValid(self, x, y, X, Y):
        """
        If the cells X and Y are in the same row, column, or 3x3 box,
        then the values x and y must be different.
        """

        xRow, xCol = X
        yRow, yCol = Y

        if xRow == yRow:
            return x != y 
        
        elif xCol == yCol:
            return x != y 
        
        elif (xRow // 3,  xCol //3) == (yRow // 3,  yCol // 3):
            return x != y
        
        return True
    
    def revise(self, domains, X, Y):
        rvis = False
        xRow, xCol = X
        yRow, yCol = Y

        for x in list(domains[X]):
            if not any(self.isValid(x, y, X, Y) for y in domains[Y]):
                domains[X].remove(x)
                rvis = True
        return rvis
    
    def init_Q(self, board):
        for row in range(9):
            for col in range(9):
                
                if board[row][col] == 0:
                    for c in range(9):
                        if board[row][c] == 0 and col != c:
                            self.q.append(((row, col), (row, c)))
                    
                    for r in range(9):
                        if board[r][col] == 0 and row != r:
                            self.q.append(((row, col), (r, col)))

                    boxRow_3x3 = row - row % 3
                    boxCol_3x3 = col - col % 3
                    for i in range(3):
                        for j in range(3):
                            r = boxRow_3x3 + i
                            c = boxCol_3x3 + j

                            if (r, c) != (row, col) and board[r][c] == 0:
                                self.q.append(((row, col), (r, c)))
        
        return self.q
    
    def AC3(self, domains, board):
        q = self.init_Q(board)
        
        while q:
            X, Y = q.popleft()
            if self.revise(domains, X, Y):
                if not domains[X]:
                    return False
                for Z in domains:
                    if Z != Y and Z != X:
                        self.q.append((Z, X))
        
        return True 
    
    def selectUnassignedVar(self, domains):
        unasigndVar = [var for var in domains if len(domains[var]) > 1]
        if not unasigndVar:
            return None
        return min(unasigndVar, key=lambda var: len(domains[var]))
    
    def backTrackRecursive(self, board, domains):
        if all(len(domains[cell]) == 1 for cell in domains):
            return True
        
        cell = self.selectUnassignedVar(domains)
        for val in list(domains[cell]):
            originalDomain = {var: domains[var].copy() for var in domains}
            board[cell[0]][cell[1]] = val
            domains[cell] = {val}

            if self.AC3(domains, board) and self.backTrackRecursive(board, domains):
                return True

            board[cell[0]][cell[1]] = 0
            domains = originalDomain
        return False
    
    def backTrack(self, board):
        doms = self.domains(board)
        if self.AC3(doms, board):
            return self.backTrackRecursive(board, doms)
        return False


if __name__ == "__main__":
    
    sudokuBoard = [
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
    
    sudoku = SudokuSolver()

    if sudoku.backTrack(sudokuBoard):
        for row in sudokuBoard:
            print(row)
    else:
        print('No Solution has Found...!!')

    



        
    
