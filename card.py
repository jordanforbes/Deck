class Card():
    def __init__(self,suit,val):
        self.suit = suit
        self.value = self.faceCheck(val) 
        
    def show(self):
        print(f"{self.value} of {self.suit}")
    
    def faceCheck(self,val):
        if val == 1:
            return "Ace"
        elif val == 11:
            return "Jack"
        elif val == 12:
            return "Queen"
        elif val == 13:
            return "King"
        else: 
            return val