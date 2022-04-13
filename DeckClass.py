from random import randint as r, shuffle as shfl  

class Deck():
    hand= {}
    suits = ['Hearts','Diamonds','Spades','Clubs']
    cards = {
            'Hearts': [1,2,3,4,5,6,7,8,9,10,11,12,13],
            'Diamonds': [1,2,3,4,5,6,7,8,9,10,11,12,13],
            'Spades': [1,2,3,4,5,6,7,8,9,10,11,12,13],
            'Clubs': [1,2,3,4,5,6,7,8,9,10,11,12,13]
         }

    def __init__(self):
        self.cards = cards
        self.shuffle()
        
    def shuffle(self):
        for x in range(4):
            shfl(self.cards[self.suits[x]])