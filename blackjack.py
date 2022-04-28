from deck import Deck
from player import Player

d = Deck()
d.setup()
d.show()

carda,cardib,c,ddd= d.drawCard().show(),d.drawCard().show(),d.drawCard().show(),d.drawCard().show()    

field={
    "up":[],
    "down":[]
    }

def drawToField(place="up"):
    card = d.drawCard()
    field[place].append(card)


drawToField()
drawToField("down")

def showField(field=field,show="no"):
    for card in field["up"]:
        print(card.show())
    print("break")

    if show=="no":
        for card in field["down"]:
            print("unknown")
    else:
        for card in field["down"]:
            print(card.show())
        
print("$$$ FIELD $$$")
showField()

print("$$$ actual field $$$")
showField(field,"yes")