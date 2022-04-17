from utility import p


class Card():
    def __init__(self,num):
        p("$$$ card drawn $$$")
        self.num=num
        cardName=self.idCard(num)
        self.val=cardName[0]
        self.suit=cardName[1]
        p(self.showCard())
        
    def showCard(self):
        name=self.getVal(self.val)
        name=f"{name} of {self.suit}"
        p(name)
        return name
        

    def idCard(self,card):
        suit=""
        if card <=13:
            suit="Hearts"
            
        elif 13 < card <= 26:
            suit="Diamonds"
            card -= 13
            
        elif 26 < card <=39:
            suit="Spades"
            card -= 13*2
            
        elif 39 < card <=52:
            suit="Clubs"
            card -= 13*3

        return(card,suit)
    
    def getVal(self,v):
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