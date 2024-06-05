from queue import PriorityQueue

class BestFirstSearch:
    def __init__(self):
        self.nodes = 7
        self.graph = [[] for _ in range(self.nodes)]
        self.pq = PriorityQueue()
    
    def bfs(self, startNode, targetNode):
        visited = [False] * self.nodes
        self.pq.put((0, startNode))
        visited[startNode] = True

        while not self.pq.empty():
            currentNode = self.pq.get()[1]
            print(currentNode, end=' ')

            if currentNode == targetNode:
                break

            for neighbor, cost in self.graph[currentNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    self.pq.put((cost, neighbor))
        print()
    
    def addEdge(self, x, y, cost):
        self.graph[x].append((y, cost))
        self.graph[y].append((x, cost))

# Create an instance of BestFirstSearch
bestfs = BestFirstSearch()

# Add edges to the graph
bestfs.addEdge(1, 3, 1)
bestfs.addEdge(1, 6, 1)
bestfs.addEdge(3, 4, 2)
bestfs.addEdge(6, 0, 4)
bestfs.addEdge(6, 2, 2)
bestfs.addEdge(4, 5, 1)
bestfs.addEdge(2, 0, 2)
bestfs.addEdge(2, 5, 1)

# Perform best first search
bestfs.bfs(1, 2)




"""
1 ↔ 3 with cost 1
1 ↔ 6 with cost 1
3 ↔ 4 with cost 2
6 ↔ 0 with cost 2  // Add more cost to the 6to0 not the uotPut |1 3 6 2 | instead |1 3 6 0 2|
6 ↔ 2 with cost 2
4 ↔ 5 with cost 1
2 ↔ 0 with cost 1
2 ↔ 5 with cost 1
    
 ------------
    
    1
   / \                                   
  /   \ 
 3     6
 |     |\
 4     2 \
 | \   |  \
 5  0--5---0

 ------------

 """