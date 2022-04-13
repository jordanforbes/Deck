from random import randint as r 


def p(x=""):
    print(x)
    

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
    match s:
        case 1:
            return "Hearts"
            
        case 2: 
            return "Diamonds"
            
        case 3:
            return "Spades"
            
        case 4: 
            return "Clubs"

    
def cardName(v,s):
    return f"{getVal(v)} of {getSuit(s)}"
    

def drawCard():
    draw = cardVal()
    draw = cardName(draw[0], draw[1])
    return draw

def card(x):
    pass
    
    
p(drawCard())
    