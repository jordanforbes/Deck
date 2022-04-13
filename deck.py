from utility import p,s,d
from random import randint as r, shuffle as shfl  

from DeckClass import Deck 
    

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


d = Deck()
    
# p(drawCard())
p(d.cards)
d.draw()