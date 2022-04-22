import PySimpleGUI as sg 
from player import Player 
from deck import Deck 
import subprocess 
import sys 

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

sg.theme('DarkTanBlue')

col1= [
                [sg.Text('Deck Methods')],
                [sg.Button('Draw', k='-DRAW-')],
                [sg.Button('Discard', k='-DISCARD-')],
                [sg.Button('Show Hand', k="-SHOW-")],
                [sg.Button('Show Deck',k='-DECK-')],
                [sg.Button('Show Discard Pile',k='-PILE-')],
                [sg.Button('Shuffle',k='-SHUFFLE-')],
                [sg.Button('Combine',k='-COMBINE-')],
            ]
col2= [ 
            [sg.Output(size=(60,15))]
       ]
layout = [
            [sg.Column(col1, element_justification='c'),
             sg.Column(col2, element_justification='c')]
        ]

window = sg.Window(
    title="deck",
    layout= layout
    )


# def runCommand(cmd, timeout=None, window=None):
#     p = subprocess.Popen(
#         cmd, 
#         shell=True, 
#         stdout=subprocess.PIPE, 
#         stderr=subprocess.STDOUT
#         )
#     output=''
#     for line in p.stdout:
#         line = line.decode(
#             errors='replace' if (sys.vewrsion_info) < (3,5) 
#             else 'backslashreplace'.rstrip())
#         output += line 
#         print(line) 
#         window.Refresh() if window else None 
#     retval = p.wait(timeout)
#     return (retval, output)
    
# def run(k):
#     runCommand(cmd=v[k], window=window)
    

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
