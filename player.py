# from deck import Deck
class Player():
    def __init__(self, name=""):
        self.name = name
        self.hand = []
        self.size = 0
        self.h = {}

    def draw(self, deck):
        # deck = Deck()
        card = deck.drawCard()
        print(card)
        self.hand.append(card)
        self.h.update({self.size: card})
        self.showSize(1)
        return self  # allows chaining

    def showSize(self, i=0):
        self.size += i
        print(f"size of hand: {self.size}")
        print("____________________")

    def xDraw(self, deck, times):
        for c in range(times):
            self.draw(deck)

    def showHand(self):
        self.showSize()
        # print(self.h.items())
        for card in self.hand:
            print(card.show())
        print("dict")
        for card in self.h:
            print(card)
        return self.hand

    def discard(self, deck):
        card = self.hand.pop()
        deck.insert(card)
        self.showSize(-1)
        return card
        self.showSize(-1)
        return card
