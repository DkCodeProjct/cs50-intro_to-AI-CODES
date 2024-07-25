
"""
  
     Lecture Uncertanty , Quiz 2
  
     """



# Consider a standard 52-card deck of cards with 13 card values 
# (Ace, King, Queen, Jack, and 2-10) 
# in each of the four suits (clubs, diamonds, hearts, spades). 
# If a card is drawn at random, 
# what is the probability that it is a spade or a two?


# Note that “or” in this question refers to inclusive, not exclusive, or.

""" Inclusion-Exclusion Rule in Prob """
# -- P(a ∨ b) = P(a) + P(b) - P(a ∧ b) -- 

probOfSades = 13/52
probOfNumCards = 4/52
probOfTwoOfSpades = 1/52
totalProb = probOfSades + probOfNumCards - (probOfTwoOfSpades)
print(f'totalProb {totalProb:.3f}', )


#                                         \
# -------------------------------------- | \
# -------------------------------------- |  \
# -------------------------------------- |  /
# -------------------------------------- | /
#                                         /  


#  Imagine flipping two fair coins, 
#  where each coin has a Heads side and a Tails side, 
#  with Heads coming up 50% of the time and Tails coming up 50% of the time. 
#  What is probability that after flipping those two coins, 
#  one of them lands heads and the other lands tails?


"""
Probability of the first coin landing heads and the second coin landing tails:
P(heads on 1st and tails on 2nd)=12×12=14P(heads on 1st and tails on 2nd)=2/1​×2/1 ​= 4/1​

Probability of the first coin landing tails and the second coin landing heads:
P(tails on 1st and heads on 2nd)=12×12=14P(tails on 1st and heads on 2nd)=2/1​×2/1​ = 4/1​
"""

c1 = 1/2
c2 = 1/2

headTail = c1 * c2 + c1 * c2
print(f'headOrTail: {headTail}')




#                                         \
# -------------------------------------- | \
# -------------------------------------- |  \
# -------------------------------------- |  /
# -------------------------------------- | /
#                                         /  

#  Two factories — Factory A and Factory B — design batteries to be used in mobile phones.
#  Factory A produces 60% of all batteries,
#  and Factory B produces the other 40%. 
#  2% of Factory A’s batteries have defects, 
#  and 4% of Factory B’s batteries have defects.
#  What is the probability that a battery is both made by Factory A and defective?


""" Inclusion-Exclusion Rule in Prob """
# -- P(a ∨ b) = P(a) + P(b) - P(a ∧ b) -- 

factryA = 0.6
defectA = 0.02

outPut =  factryA * defectA
print('output: ',outPut)