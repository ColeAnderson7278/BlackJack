from random import shuffle


def war():
    deck = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12,
        13, 13, 13, 13, 14, 14, 14, 14
    ]

    shuffle(deck)
    deck_1 = deck[:26]
    deck_2 = deck[26:]
    pile_1 = []
    pile_2 = []
    war_deck = []
    while True:
        if len(deck_1) == 0:
            shuffle(pile_1)
            deck_1 = pile_1.copy()
            pile_1 = []

        if len(deck_1) == 0:
            print('\nPlayer Two Wins At Life!')
            break

        if len(deck_2) == 0:
            shuffle(pile_2)
            deck_2 = pile_2.copy()
            pile_2 = []

        if len(deck_2) == 0:
            print('\nPlayer One Wins At Life!')
            break

        x = deck_1.pop()
        y = deck_2.pop()

        print(
            'Player 1: Drew:{}\nCards in Hand:{}\nvs\nPlayer 2: Drew:{}\nCards in Hand:{}'.
            format(x, len(deck_1), y, len(deck_2)))
        if x == y:
            deck_1.extend(pile_1)
            pile_1 = []
            deck_2.extend(pile_2)
            pile_2 = []
            if len(deck_2) < 4:
                print('Player One Wins At Life!')
                break
            if len(deck_1) < 4:
                print('Player Two Wins At Life!')
                break
            else:
                war_deck.append(deck_1.pop())
                war_deck.append(deck_1.pop())
                war_deck.append(deck_1.pop())
                war_deck.append(deck_2.pop())
                war_deck.append(deck_2.pop())
                war_deck.append(deck_2.pop())
                x = deck_1.pop()
                y = deck_2.pop()
                if x > y:
                    print('Player 1 Won This Round\n')
                    pile_1.extend([x, y])
                if x < y:
                    print('Player 2 Won This Round\n')
                    pile_2.extend([x, y])

        elif x > y:
            print('Player 1 Won This Round\n')
            pile_1.extend([x, y])
        elif x < y:
            print('Player 2 Won This Round\n')
            pile_2.extend([x, y])


def main():
    war()


if __name__ == '__main__':
    main()
