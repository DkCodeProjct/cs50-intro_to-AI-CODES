import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
      
        #for var in self.crossword.variables:
        #    for word in self.crossword.variables.words:
        #        if len(var) != len(word):
        #            self.domains.pop(word)
        
        
        for var in self.crossword.variables:
            for word in  self.domains[var].copy():
                if len(word) != var.length:
                    self.domains[var].remove(word)

                    
    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        flag = False
        i, j = self.crossword.overlaps[x, y]
        for valx in self.domains[x].copy():
            satisfi = False
            for valy in self.domains[y]:
                if valx[i] == valy[j]:
                    satisfi = True
                    break
            #if satisfi == False:
            if not satisfi:
                self.domains[x].remove(valx)
                flag = True
        return flag


    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None:
            arcs = []
            for x in self.crossword.variables:
                for y in self.crossword.neighbors(x):
                    arcs.append((x, y))
        q = list(arcs)

        while q:
            x, y = q.pop()
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False

           
                for z in self.crossword.neighbors(x):
                    if z != y:
                       q.append((x, z))
        return True

            
    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for var in self.crossword.variables:
            if var not in assignment:
                return False
            if assignment[var] is None:
                return False
        return True
                


    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        for var in assignment:
            wordVar = assignment[var]

            for neigbour in self.crossword.neighbors(var):
                if neigbour in assignment:
                    wordNeighbour = assignment[neigbour]
                    i, j = self.crossword.overlaps[var, neigbour]

                    if i is not None and j is not None:
                        if wordVar[i] != wordNeighbour[j]:
                            return False
        return True


    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
         
        # valCounter = []
        # for valVar in self.domains(var):
        #    counter = 0
        #    for neigbour in var:
        #        if neigbour not in assignment:
        #            for valNeighbour in self.domains(neigbour):
        #                if valVar != valNeighbour:
        #                    counter += 1
        
        valCounter = []
        for valVar in self.domains[var]:
            counter = 0
            for neighbour in self.crossword.neighbors(var):
                if neighbour not in assignment:
                    for valNeighbour in self.domains[neighbour]:
                        if (var, neighbour) in self.crossword.overlaps:
                            i, j = self.crossword.overlaps[valVar, valNeighbour]

                            #if i is not None and j is not None:
                            if valVar != valNeighbour: 
                                counter += 1    
            valCounter.append((valVar, valNeighbour))
        
        valCounter.sort(key=lambda x: x[1])

        return [val[0] for val in valCounter]
    


    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        
        bestVar = None
        minRemainingVal = float('inf')
        maxDegree = -1
        
        for var in self.crossword.variables:
            if var not in assignment:
                numRemainingVal = len(self.domains[var])
                degree = len(self.crossword.neighbors(var))

                if  numRemainingVal < minRemainingVal:
                    bestVar = var
                    minRemainingVal = numRemainingVal
                    maxDegree = degree
                elif numRemainingVal == minRemainingVal:
                    if degree > maxDegree:
                        bestVar = var
                        maxDegree = degree
        return bestVar

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)

        for val in self.order_domain_values(var, assignment):
            assignment[var] = val

            if self.consistent(assignment):
                outPut = self.backtrack(assignment)
                if outPut is not None:
                    return outPut
            del assignment[var]
        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
