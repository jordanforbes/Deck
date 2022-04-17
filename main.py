from utility import p

from deck import Deck
from card import Card
from hand import Hand
from identify import Identify as I

class Field():
    def __init__(self):
        self.cards = 0
        
    def add(self,n=1):
        self.cards += n


d1 = Deck()
field = Field()
p("start")
h1 = Hand()
d1.show()

def drawCard():
    h1.draw(d1)
    
for x in range(5):
    drawCard()
d1.show()
h1.show()
p("cutoff")
# I.id(h1.hand[0].val)
