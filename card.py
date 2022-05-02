class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = self.faceCheck(val)
        self.pointVal = self.pointVal(val)

    def show(self):
        return f"{self.value} of {self.suit}"
        # return(self.value)

    def faceCheck(self, val):
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

    def pointVal(self, val):
        if val > 10:
            return 10
        elif val == 1:
            return "A"
        else:
            return val
