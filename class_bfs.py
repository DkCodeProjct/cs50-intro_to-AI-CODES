class Maze:
    def __init__(self):
        self.visited = []
        self.q = []
        with open('maze.txt' ,'r') as file:
            self.maze = [list(line.strip()) for line in file]
        
    def bfs(self,start):
        navigation = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up,down,left,right

        if start not in self.visited:
            self.visited.append(start)
            self.q.append(start)

            while self.q:
                currentNode = self.q.pop(0)
                x,y = currentNode

                for nav in navigation:
                    newX = x + nav[0]
                    newY = y + nav[1]

                    if 0 <= newX < len(self.maze) and 0 <= newY < len(self.maze):
                        if self.maze[newX][newY] == ' ' or self.maze[newX][newY] == 'B':
                            newPosition = (newX, newY)

                            if newPosition not in self.visited:
                                self.visited.append(newPosition)
                                self.q.append(newPosition)

                                if self.maze[newX][newY] == 'B':
                                    print('goal')
                                    return
                                
maze = Maze()
startNode = (0,0)
maze.bfs(startNode)