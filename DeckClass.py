from utility import p
from random import randint as r, shuffle as shfl  

class Deck():
    hand= {}
    suits = ['Hearts','Diamonds','Spades','Clubs']
    cards = {
            'Hearts': ['A',2,3,4,5,6,7,8,9,10,11,12,13],
            'Diamonds': [1,2,3,4,5,6,7,8,9,10,11,12,13],
            'Spades': [1,2,3,4,5,6,7,8,9,10,11,12,13],
            'Clubs': [1,2,3,4,5,6,7,8,9,10,11,12,13]
         }

    def __init__(self):
        self.shuffle()
        self.draw()
        
    def shuffle(self):
        for x in range(4):
            shfl(self.cards[self.suits[x]])
    
    def draw(self):
        suit = self.suits[r(0,3)]
        suit = self.cards[suit]
        # v = r(1,len(suit))
        v = self.cards['Hearts'][0]
        p(f"val: {v}")
        