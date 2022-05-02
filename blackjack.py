from deck import Deck
from card import Card
from player import Player
class Field():
    def __init__(self):
        self.field=self.blank()
        self.pVals=self.emptyPoints()

    def drawToField(self,place="up"):
        card = d.drawCard()
        self.field[place].append(card)
        return self
    
    def custCard(self,place,suit,val):
        card = Card(suit,val)
        self.field[place].append(card)
        return self

    def showField(self,show="no"):
        # pVals=[]
        for card in self.field["up"]:
            if card.pointVal == "A":
                if self.pVals[0] == 10:
                    self.pVals.append(11)
                    print(card.show())
                else:
                    self.pVals.append(1)
                    print(card.show())
            else:
                self.pVals.append(card.pointVal)
                print(card.show())
                
        print("break")
        
        if show=="no":
            for card in self.field["down"]:
                print("unknown")                
        
        else:
            for card in self.field["down"]:
                print(card.show())
        
        value=0
        print(self.pVals)
    
    def blank(self):
        self.field={
            "up":[],
            "down":[]
        }
        return {"up":[],"down":[]}

    def emptyPoints(self):
        self.pVals=[]
        return []
    
    def reset(self):
        self.blank()
        self.emptyPoints()
    
d = Deck()
d.setup()
d.show()
f = Field()            
# f.drawToField().drawToField().drawToField("down").drawToField("down")
f.custCard("up","Spades",11).custCard("up","Hearts",1)
print("$$$ FIELD $$$")
f.showField()

f.reset()

f.custCard("up","Spades",9).custCard("up","Hearts",1)
print("$$$ FIELD $$$")
f.showField()

# print("$$$ actual field $$$")
# f.showField("yes")