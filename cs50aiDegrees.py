
def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # tODO
    numVisited = 0
    startNode = Node(state=source, parent=None, action=None)
    q = QueueFrontier()
    q.add(startNode)

    visited = set()

    while True:
        if q.empty():
            raise Exception ('No Separation Found')
        
        currentNode = q.remove()
        numVisited += 1

        visited.add(currentNode.state)

        for moiveId, personId in neighbors_for_person(currentNode.state):
            if q.contains_state(personId) and personId not in visited:
                childNode = Node(state=personId, parent=currentNode, action=moiveId)
                
                if childNode.state == target:
                    movies = []
                    ppl = []

                    while childNode.parent is not None:
                        movies.append(childNode.action)
                        ppl.append(childNode.state)
                        childNode = childNode.parent

                    movies.reverse()
                    ppl.reverse()
                    sol = []
                    tpl = zip(movies,ppl) 
                    
                    for movie, star in tpl:
                        sol.append((movie,star))

                    return sol
                
                q.add(childNode)




