def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.
    If no possible path, returns None.
    """
     # tODO
    visited = []
    q = []
    parent = {}


    visited.append(source)
    q.append(source)

    while q:
        currnt = q.pop(0)
        if currnt == target:
            path = []
            
            while currnt != source:
                path.insert(0, currnt)
                currnt = parent[currnt]
            path.insert(0, source)
            return path
        for neigbour in people:
            if neigbour not in  visited:
                visited.append(neigbour)
                q.append(neigbour)
                parent[neigbour] = currnt
    
    
    print('no path found')
    return None
