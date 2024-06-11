import csv
from utily import Node, QueueFrontier

class SixDegreesOfSeparation:
    def __init__(self):
        self.criminals = {}
        self.murders = {}
        self.connections = {}
        self.visited = set()
        self.q = QueueFrontier()
    
    def loadData(self):
        with open('criminals.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.connections[row['id']] = {
                    'name': row['name'],
                    'birth_date': row['birth_date'],
                    'murders': set()
                }
                if row['name'].lower() not in self.criminals:
                    self.criminals[row['name'].lower()] = {row['id']}
                else:
                    self.criminals[row['name'].lower()].add(row['id'])
            
        with open('murders.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.murders[row['id']] = {
                    'location': row['location'],
                    'date': row['date'],
                    'suspects': set()
                }

        with open('connections.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    self.connections[row['person_id']]['murders'].add(row['murder_id'])
                    self.murders[row['murder_id']]['suspects'].add(row['person_id'])
                except KeyError:
                    pass

    def main(self):
        source = self.person_id_for_name(input('Source Name: ').lower())
        if not source:
            print('No Source Name')
            return

        target_name = input('Target Name: ').lower()
        target = self.person_id_for_name(target_name)
        if not target:
            print('No Target Name')
            return
        
        print(f"Source ID: {source}")
        print(f"Target ID: {target}")

        path = self.shortestPath(source, target)

        if path is None:
            print('No connections between suspects.')
        else:
            degrees = len(path)
            print(f'{degrees} locations of Connections')
            path = [(None, source)] + path
            for i in range(degrees):
                criminal1 = self.connections[path[i][1]]['name']
                criminal2 = self.connections[path[i + 1][1]]['name']
                murder = self.murders[path[i + 1][0]]['location']
                print(f'{i + 1}: {criminal1} and {criminal2} have connections at {murder}')




    def shortestPath(self, source, target):
        startIds = self.criminals.get(source)
        target_ids = self.criminals.get(target)

        if not startIds or not target_ids:
            return None

        for start_id in startIds:
            start = Node(state=start_id, parent=None, action=None)
            self.q.add(start)

        while not self.q.empty():
            currentNode = self.q.remove()

            if currentNode.state in target_ids:
                path = []
                while currentNode.parent is not None:
                    path.append((currentNode.action, currentNode.state))
                    currentNode = currentNode.parent
                path.reverse()
                return path
            
            self.visited.add(currentNode.state)

            for murderId, criminalId in self.neighborsForPerson(currentNode.state):
                if not self.q.contains_state(criminalId) and criminalId not in self.visited:
                    child = Node(state=criminalId, parent=currentNode, action=murderId)
                    self.q.add(child)
        return None

    def neighborsForPerson(self, criminalId):
        murderIds = self.connections.get(criminalId, {}).get('murders', set())

        neighbors = set()
        for murderId in murderIds:
            for suspectId in self.murders[murderId]['suspects']:
                neighbors.add((murderId, suspectId))
        return neighbors
    
    
    
    def person_id_for_name(self, name):   
        """
        Returns the IMDB id for a person's name,
        resolving ambiguities as needed.
        """
        person_ids = list(self.criminals.get(name.lower(), set()))
        if len(person_ids) == 0:
            return None
        elif len(person_ids) > 1:
            print(f"Which '{name}'?")
            for person_id in person_ids:
                person = self.criminals[person_id]
                name = person["name"]
                birth = person["birth"]
                print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
            try:
                person_id = input("Intended Person ID: ")
                if person_id in person_ids:
                    return person_id
            except ValueError:
                pass
            return None
        else:
            return person_ids[0]

if __name__ == "__main__":
    sixds = SixDegreesOfSeparation()
    sixds.loadData()
    sixds.main()
