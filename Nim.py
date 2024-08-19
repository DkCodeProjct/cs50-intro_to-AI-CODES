# : Making the nim game
# : rulse-
#         | take nums untill piles are empty  

import random
import random

class Nim:
    def __init__(self):
        self.piles = [1, 3, 5, 7]
        self.lastMove = None
        self.choosePlay = int(input("Choose Play [1/2]: "))
        print(f'\nPILES: {self.piles}')
 
    def compRm(self, pile):
        while True:
            compPile = random.randint(0, 3)
            if pile[compPile] > 0:  
                rmNum = random.randint(1, pile[compPile])  # 1 to num in choose pile
                pile[compPile] -= rmNum
                print(f'\nComputer removed {rmNum} objects from pile {compPile + 1}')
                break
        return pile
    
    def validMove(self, prompt):
        while True:
            user = int(input(prompt))
            if user in [0, 1, 2, 3]:
                return user
            else:
                print('Invalid number, please choose a pile between 0 and 3.')
    
    def mainLoop(self):
        while True:
            if all(pile == 0 for pile in self.piles):  
                print('Game Over')
                
                if self.lastMove == 'user':
                    print('User Loose by rm last pile')
                
                else:
                    print('Computer Loose by rm last pile')
                
                break
                
            
            if self.choosePlay == 1:
                print('\nUser Turn:\n')
                userPile = self.validMove('Choose pile [0/1/2/3]: ')
                userRmNum = int(input('Choose how many to remove: '))
                
                if self.piles[userPile] > 0 and userRmNum <= self.piles[userPile]:
                    self.piles[userPile] -= userRmNum
                    self.lastMove = 'user'
                    print(f'\nUser removed {userRmNum} objects from pile {userPile + 1}.')
                    print(self.piles, '--> after user removes')
                else:
                    print('Invalid move. Try again.')
                    continue  
                
                self.choosePlay = 2  
            else:
                print('\nComputer Turn')
                self.piles = self.compRm(self.piles)  #
                print(self.piles, '--> after computer removes')
                self.lastMove = 'computer'
                
                self.choosePlay = 1  

game = Nim()
game.mainLoop()
