from utility import p


class Card():
    def __init__(self,num):
        p("$$$ card drawn $$$")
        self.num=num
        cardName=self.idCard()
        self.val=cardName[0]
        self.suit=cardName[1]
        p(self.showCard())
        
    def showCard(self):
        name=self.getVal(self.val)
        name=f"{name} of {self.suit}"
        p(name)
        return name
    
    def getNum(self):
        return self.num
        

    def idCard(self):
        c = self.getNum()
        p("$$$ ID $$$")
        p(c)
        suit=""
        if c <=13:
            suit="Hearts"
            
        elif 13 < c <= 26:
            suit="Diamonds"
            c -= 13
            
        elif 26 < c <=39:
            suit="Spades"
            c -= 13*2
            
        elif 39 < c <=52:
            suit="Clubs"
            c -= 13*3

        return(c,suit)
    
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