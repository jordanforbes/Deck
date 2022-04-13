from random import randint as r, shuffle as shfl  


def p(x=""):
    print(x)

def s(x=0):
    return str(x)

def d(x):
    return r(0,x)+1
    

def cardVal(): 
    card = (d(12),d(3))
    return card
    
    
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
        return str(v)
        
        
def getSuit(s):
        if s == 1:
            return "Hearts"
            
        elif s == 2: 
            return "Diamonds"
            
        elif s == 3:
            return "Spades"
            
        else: 
            return "Clubs"

    
def cardName(v,s):
    return f"{getVal(v)} of {getSuit(s)}"
    

def drawCard():
    draw = cardVal()
    draw = cardName(draw[0], draw[1])
    return draw

cards = {'Hearts': [1,2,3,4,5,6,7,8,9,10,11,12,13],
         'Diamonds': [1,2,3,4,5,6,7,8,9,10,11,12,13],
         'Spades': [1,2,3,4,5,6,7,8,9,10,11,12,13],
         'Clubs': [1,2,3,4,5,6,7,8,9,10,11,12,13]
         }

class Deck():
    hand= {}
    suits = ['Hearts','Diamonds','Spades','Clubs']
    cards = {
            'Hearts': [1,2,3,4,5,6,7,8,9,10,11,12,13],
            'Diamonds': [1,2,3,4,5,6,7,8,9,10,11,12,13],
            'Spades': [1,2,3,4,5,6,7,8,9,10,11,12,13],
            'Clubs': [1,2,3,4,5,6,7,8,9,10,11,12,13]
         }

    def __init__(self):
        self.cards = cards
        self.shuffle()
        
    def shuffle(self):
        for x in range(4):
            shfl(cards[self.suits[x]])
d = Deck()
    
# p(drawCard())
p(d.cards)