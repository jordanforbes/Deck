from utility import p
from random import randint as r, shuffle as shfl  

class Deck():
    hand= {'Hearts':[],
           'Diamonds':[],
           'Spades':[],
           'Clubs':[]
           }
    suits = ['Hearts','Diamonds','Spades','Clubs']
    cards = {
            'Hearts': [1,2,3,4,5,6,7,8,9,10,11,12,13],
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
        suit = self.getSuit(r(1,4))
        self.checkSuit(suit)
        card = self.cards[suit]
        p(suit)
        c = card.pop(0)
        self.hand[suit].append(c)
        p(f'hand: {self.hand}')
        c = self.getVal(c)
        
        p(card)
        print(f'{c} of {suit}')
        return c,suit
        
    @staticmethod
    def getVal(v):
        if v == 1:
            return "Ace"
        
        elif v == 11:
            return "Jack"
            
        elif v == 12:
            return "Queen"
            
        elif v == 13:
            return "King"  
            
        else:
            return v
        
    def checkSuit(self, k=0):
        p("checksuit")
        # p(self.suits[k])
        if self.suits[k]:
            p(f"nothing else in {self.suits[k]}")
            del self.suits[k]
            self.draw()
        
    @staticmethod 
    def getSuit(s):
        if s == 1:
            return "Hearts"
            
        elif s == 2: 
            return "Diamonds"
            
        elif s == 3:
            return "Spades"
            
        else: 
            return "Clubs"