import random

#        0    1    2    3
#       +----+----+----+----+
#    0 |  0 | 10 | 15 | 20 |
#       +----+----+----+----+
#    1 | 10 |  0 | 35 | 25 |
#       +----+----+----+----+
#    2 | 15 | 35 |  0 | 30 |
#       +----+----+----+----+
#    3 | 20 | 25 | 30 |  0 |
#       +----+----+----+----+
#
#     Solution: [1, 0, 2, 3]
#     Total Distance: 80
#   
#    --  Distance from city 0 to city 1: 10
#        Distance from city 1 to city 2: 10
#        Distance from city 2 to city 3: 35
#        Distance from city 3 to city 0: 20  --
# # #

class HillClibing:
    def __init__(self):
        self.distanceMatrix = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]
        self.maxIterations = 10000

    def totalDistace(self, path):
        total = 0
        
        for i in range(len(path) - 1):
            total += self.distanceMatrix[path[i]][path[i + 1]]
        total += self.distanceMatrix[path[-1]][path[0]] 
        
        return total
    
    def hillClibing(self, numCiteis):
        currentPath = list(range(numCiteis)) 
        random.shuffle(currentPath)  
        currentDistance = self.totalDistace(currentPath)

        for _ in range(self.maxIterations):
          
            neighbourPath = currentPath.copy()
            i, j = random.sample(range(numCiteis), 2)
            neighbourPath[i], neighbourPath[j] = neighbourPath[j], neighbourPath[i]
            neighbourDistance = self.totalDistace(neighbourPath)

            # If the neighbor solution is better, move to it
            if neighbourDistance < currentDistance:
                currentPath = neighbourPath
                currentDistance = neighbourDistance

        return currentPath
    
def main():
    numCities = 4
    sol = HillClibing()
    solution = sol.hillClibing(numCities)
    totalDistance = sol.totalDistace(solution)
    print('Solution:', solution)
    print('Total Distance:', totalDistance)

if __name__ == "__main__":
    main()
