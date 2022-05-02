from player import Player
from deck import Deck
from bjGUI import BJGUI
d = Deck()
d.setup()
discard = Deck()
p1 = Player("Player1")
p2 = Player("Dealer")
print(p1.draw(d))
# p1.draw(d)
BJGUI(p1, d, discard)
