import PySimpleGUI as sg 
from player import Player 
from deck import Deck 

d = Deck()
bob = Player("Bob")
jim = Player("Jim")
bob.xDraw(d,5)
jim.xDraw(d,5)
print("show hand")
print("$$$ bob's hand $$$")
bob.showHand()
print("$$$ Jim's hand $$$")
jim.showHand()
d.show()

sg.theme('DarkAmber')
layout = [
    [sg.Text('Hello')]
]

window = sg.Window(
    title="deck",
    Layout = layout
    )

while True:
    e, v = window.read()
    if e == sg.WIN_CLOSED or e == 'Close':
        break 

window.close()