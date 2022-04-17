import numpy as np
import numpy.random as npr
from numpy.random import default_rng

from card import Card
from utility import p
        
rng = npr.default_rng()
vals = rng.standard_normal(10)
more_vals = rng.standard_normal(10)


class Deck():
    def __init__(self):
        p("$$$ built deck $$$")
        self.deck = self.build()
    
    def build(self):
        deck = rng.choice(52,52,replace=False)
        deck = np.where(deck == 0, 52,deck)
        return deck
    
    def draw(self,hand):
        card, self.deck = Card(self.deck[0]), self.deck[1:]
        hand.add(card)
        return card
    
    def show(self):
        p(self.deck)
        
def chk(name,var):
    # p("CHECK")
    p(f"{name}:")
    p(var)
    p()
    