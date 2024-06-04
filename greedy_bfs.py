from queue import PriorityQueue

nodes = 7
graph = [[] for none in range(nodes)]

def bestFirstSearch(startNode,targetNode,nodes):
    visited = [False] * nodes
    pq = PriorityQueue()
    pq.put((0, startNode))

    while not pq.empty():
        currentNode = pq.get()[1]
        print(currentNode, end=' ')
        
        if currentNode == targetNode:
            break
            
        for neigbour, cost in graph[currentNode]:
            if not visited[neigbour]:
                visited[neigbour] = True
                pq.put((neigbour,cost))
    print()

def addEdge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


addEdge(1, 3, 1)
addEdge(1, 6, 1)
addEdge(3, 4, 2)
addEdge(6, 0, 2)
addEdge(6, 2, 2)
addEdge(4, 5, 1)
addEdge(2, 0, 2)
addEdge(2, 5, 1)

bestFirstSearch(1, 4, nodes)


"""
1 ↔ 3 with cost 1
1 ↔ 6 with cost 1
3 ↔ 4 with cost 2
6 ↔ 0 with cost 2
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