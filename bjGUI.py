import PySimpleGUI as sg


class BJGUI():
    def __init__(self, player, d, discard):
        sg.theme('DarkTanBlue')

        col1 = [
                        [sg.Text('Deck Methods')],
                        [sg.Button('Draw', k='-DRAW-')],
                        [sg.Button('Discard', k='-DISCARD-')],
                        [sg.Button('Show Hand', k="-SHOW-")],
                        [sg.Button('Show Deck', k='-DECK-')],
                        [sg.Button('Show Discard Pile', k='-PILE-')],
                        [sg.Button('Shuffle', k='-SHUFFLE-')],
                        [sg.Button('Combine', k='-COMBINE-')],
                    ]
        col2 = [
                    [sg.Output(size=(60, 15))]
            ]
        col3 = [
                    [sg.Text('BLACKJACK')],
                    [sg.Text('Chips: 0', k='-CHIPS-')],
                    [sg.Button('Stand', k='-STAND-')],
                    [sg.Button('Hit', k='-HIT-')],
                    [sg.Button('Double Down', k='-DOUBLE-')],
                    [sg.Button('Split', k='-SPLIT-')],
                    [sg.Button('Fold', k='-FOLD-')]
                ]
        layout = [
                    [sg.Column(col1, element_justification='c'),
                     sg.Column(col2, element_justification='c'),
                     sg.Column(col3, element_justification='c')]
                ]

        window = sg.Window(
            title="deck",
            layout=layout
            )

        while True:
            e, v = window.read()
            if e == sg.WIN_CLOSED or e == 'Close':
                break

            #blackjack
            if e == '-HIT-':
                print("HIT")

            if e == '-STAND-':
                print("STAND")

            #Basic methods
            if e == '-DRAW-':
                print("$$$ DRAW $$$")
                player.draw(d)
                player.showHand()
                print("$$$ END OF HAND $$$")

            if e == '-SHOW-':
                print("$$$ HAND $$$")
                player.showHand()
                print("$$$ END OF HAND $$$")

            if e == '-DISCARD-':
                print("$$$ DISCARD $$$")
                player.discard(discard)
                player.showHand()
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
