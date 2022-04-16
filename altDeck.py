import numpy as np
from numpy.random import default_rng

from utility import p

rng = default_rng()
vals = rng.standard_normal(10)
more_vals = rng.standard_normal(10)
hand = []


rng = np.random.default_rng()
deck = rng.choice(52, 52,replace=False)
p(deck)


def drawCard(deck=deck):
    card = deck[0]
    deck = deck[1:]
    return card

p(deck)
p(deck=drawCard(deck))
p(deck)


# def getVal(v):
#     if v == 1:
#         return "Ace"
        
#     elif v == 11:
#         return "Jack"
            
#     elif v == 12:
#         return "Queen"
            
#     elif v == 13:
#         return "King"  
            
#     else:
#         return v
        
# def checkSuit(self, k=0):
#     p("checksuit")
#     # p(self.suits[k])
#     if self.suits[k]:
#         p(f"nothing else in {self.suits[k]}")
#         del self.suits[k]
#         self.draw()
        
# def getSuit(s):
#     if s == 1:
#         return "Hearts"
            
#     elif s == 2: 
#         return "Diamonds"
            
#     elif s == 3:
#         return "Spades"
            
#     else: 
#         return "Clubs"
