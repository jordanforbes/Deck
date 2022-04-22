from player import Player 
from deck import Deck
from gui import Gui 

d = Deck()
d.setup()
discard = Deck()
bob = Player("Bob")
bob.xDraw(d,5)

Gui(bob,d,discard)
