import random
from card import Card
from player import Player

class Deck():
    def __init__(self):
        self.cards = []
    
    def build(self):
        for suit in ["Spades","Clubs","Hearts","Diamonds"]:
            for value in range(1,14):
                self.cards.append(Card(suit,value))
    
    def setup(self):
        self.build()
        self.shuffle()
                
    def show(self):
        for c in self.cards:
            c.show()
            
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i) #always pick a random number from the left
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i] #swap 2 random cards
            
    def drawCard(self):
        return self.cards.pop()
    
    def drawTo(self,destination):
        card=self.drawCard()
        destination.append(card)
        
    
    def insert(self,card):
        self.cards.append(card)
        
    def combine(self, deck):
        for card in self.cards:
            deck.insert(card)
