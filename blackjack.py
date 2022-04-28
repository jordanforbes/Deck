from deck import Deck
from player import Player

d = Deck()
d.setup()
d.show()

carda,cardb,c,ddd= d.drawCard().show(),d.drawCard().show(),d.drawCard().show(),d.drawCard().show()    

field={
    "up":[],
    "down":[]
    }

def drawToField(place="up"):
    card = d.drawCard()
    field[place].append(card)


drawToField()
drawToField("down")

def showField(field=field):
    for card in field["up"]:
        print(card.show())
    for card in field["down"]:
        print("unknown")
        
print("$$$ FIELD $$$")
showField()
