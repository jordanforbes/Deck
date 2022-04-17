# from utility import p 

# class Identify():

#     @staticmethod
#     def readCard(card):
#         suit=""
#         if card <=13:
#             suit="Hearts"
            
#         elif 13 < card <= 26:
#             suit="Diamonds"
#             card -= 13
            
#         elif 26 < card <=39:
#             suit="Spades"
#             card -= 13*2
            
#         elif 39 < card <=52:
#             suit="Clubs"
#             card -= 13*3

#         return(card,suit)
    
#     @staticmethod
#     def checkFace(val):
#         v = val
#         if v == 1:
#             return "Ace"
            
#         elif v == 11:
#             return "Jack"
            
#         elif v == 12:
#             return "Queen"
            
#         elif v == 13:
#             return "King"  
            
#         else:
#             return str(v)
        
#     @staticmethod 
#     def id(card):
#         card = Identify.readCard(card)
#         name = Identify.checkFace(card[0])
#         suit = card[1]
#         name=f"{name} of {suit}"
#         p("card ID'd")
#         p(name)
#         return name
    