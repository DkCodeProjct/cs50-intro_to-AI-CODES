# // input:
        ####
        # A#
        #  #
        #B##
        ####
# // outPut:
"""
        visiting:(1, 2)
        queing:(2, 2)
        queing:(1, 1)
        visiting:(2, 2)
        queing:(2, 1)
        visiting:(1, 1)
        visiting:(2, 1)
        queing:(3, 1)
        goal

      //~  Path: down -> left -> down
"""


class Maze:
    def __init__(self):
        self.visited = []
        self.q = []
        with open('maze.txt', 'r') as file:
            self.maze = [list(line.strip()) for line in file]
        
        for row in self.maze:
            print(' '.join(row))
        print()
    
    def findStartNode(self, node_A="A"):
        for j in range(len(self.maze)):
            for k in range(len(self.maze[j])):
                if self.maze[j][k] == node_A:
                    return (j, k)
        return None
    
    def bfs(self, start):
        navigation = [(-1, 0, 'up'), (1, 0, 'down'),(0, -1, 'left'), (0,  1, 'right')] 
        path = []
        parent = {start:(None, None)}
        if start not in self.visited:
            self.visited.append(start)
            self.q.append(start)

            while self.q:
                current = self.q.pop(0)
                x,y = current
                print(f'visiting:{current}')

                for nav in navigation:
                    newX = x + nav[0]
                    newY = y + nav[1]
                    direction = nav[2]

                    if 0 <= newX < len(self.maze) and 0 <= newX < len(self.maze):
                        if self.maze[newX][newY] == ' ' or self.maze[newX][newY] == 'B':
                            newNode = (newX, newY)

                            if newNode not in self.visited:
                                self.visited.append(newNode)
                                self.q.append(newNode)
                                parent[newNode] = (current, direction)
                                print(f'queing:{newNode}')

                                if self.maze[newX][newY] == 'B':
                                    print('goal')
                                    
                                    while newNode in parent and parent[newNode][1] is not None:
                                        path.append(parent[newNode][1])
                                        newNode = parent[newNode][0]
                                    
                                    path.reverse()
                                    print('Path:', ' -> '.join(path))
                                    return
        print('no path to follow')

    
maze = Maze()
startNode = maze.findStartNode('A')
if startNode:
    maze.bfs(startNode)
else:
    print("Start node 'A' not found in the maze")
             