class Player():
    def __init__(self, name=""):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self #allows chaining
    
    def xDraw(self, deck, times):
        for c in range(times):
            self.draw(deck)
        
    def showHand(self):
        for card in self.hand:
            card.show()
    
    def discard(self,deck):
        card= self.hand.pop()
        deck.insert(card)
        return card 