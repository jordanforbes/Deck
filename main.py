import PySimpleGUI as sg 
from player import Player 
from deck import Deck 

d = Deck()
d.setup()
discard = Deck()
bob = Player("Bob")
# jim = Player("Jim")
bob.xDraw(d,5)
# jim.xDraw(d,5)
# print("show hand")
# print("$$$ bob's hand $$$")
# bob.showHand()
# print("$$$ Jim's hand $$$")
# jim.showHand()
# d.show()

sg.theme('DarkAmber')
layout = [
            [sg.Text('Deck Methods')],
            [sg.Button('Draw', k='-DRAW-')],
            [sg.Button('Discard', k='-DISCARD-')],
            [sg.Button('Show Hand', k="-SHOW-")],
            [sg.Button('Show Deck',k='-DECK-')],
            [sg.Button('Show Discard Pile',k='-PILE-')],
            [sg.Button('Shuffle',k='-SHUFFLE-')],
            [sg.Button('Combine',k='-COMBINE-')]
        ]

window = sg.Window(
    title="deck",
    layout= layout
    )

while True:
    e, v = window.read()
    if e == sg.WIN_CLOSED or e == 'Close':
        break 
    
    if e == '-DRAW-':
        print("$$$ DRAW $$$")
        bob.draw(d)
        bob.showHand()
        print("$$$ END OF HAND $$$")
        
    if e == '-SHOW-':
        print("$$$ HAND $$$")
        bob.showHand()
        print("$$$ END OF HAND $$$")
    
    if e == '-DISCARD-':
        print("$$$ DISCARD $$$")
        bob.discard(discard)
        bob.showHand()
        print("$$$ END OF HAND $$$")
        
    if e == '-DECK-':
        print("$$$ SHOW DECK $$$")
        d.show()
        print("$$$ END OF DECK $$$")
                
    if e == '-PILE-':
        print("$$$ DISCARD PILE $$$")
        discard.show()
        print("$$$ END OF DISCARD PILE $$$")
        
    if e == '-SHUFFLE-':
        print("$$$ SHUFFLE $$$")
        d.shuffle()
        
    if e == '-COMBINE-':
        print("$$$ COMBINE $$$")
        discard.combine(d)
        
window.close()