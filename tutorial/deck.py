import random as rand

class Card():
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val 
        
    def show(self):
        print(f"{self.value} of {self.suit}")
        
class Deck():
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()
    
    def build(self):
        for s in ["Spades","Clubs","Hearts","Diamonds"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))
                
    def show(self):
        for c in self.cards:
            c.show()
            
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = rand.randint(0, i) #always pick a random number from the left
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i] #swap 2 random cards
            
    def drawCard(self):
        return self.cards.pop()
    
class Player():
    def __init__(self, name=""):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self #allows chaining
        
    def showHand(self):
        for card in self.hand:
            card.show()
    
    def discard(self):
        return self.hand.pop()

d = Deck()
# # d.show()
# card= d.draw()
# print("$$$ shown card $$$")
# card.show()
# print("$$$ next deck $$$")
# # d.show()
bob = Player("Bob")
bob.draw(d).draw(d).draw(d).draw(d).draw(d)
bob.showHand()
