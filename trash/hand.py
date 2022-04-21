from utility import p


class Hand():
    def __init__(self):
        self.hand = []
    
    def add(self,card):
        self.hand.append(card)
    
    def show(self):
        hand = []
        for card in self.hand:
            hand.append(card.showCard())
        p(hand)
    
    def draw(self, deck):
        deck.draw(self)