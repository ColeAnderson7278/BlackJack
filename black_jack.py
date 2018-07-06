from random import shuffle


def card_total(hand):
    non_aces = []
    aces = 0
    for card in hand:
        if card == 'Ace':
            aces += 1
        else:
            non_aces.append(card)
    total = sum(non_aces)
    if aces == 0:
        return total
    elif aces == 1:
        if total == 10:
            return 21
        elif total < 10:
            return total + 11
        else:
            return total + 1
    elif aces == 2:
        if total == 9:
            return 21
        elif total < 9:
            return total + 12
        else:
            return total + 2
    elif aces == 3:
        if total == 8:
            return 21
        elif total < 8:
            return total + 13
        else:
            return total + 3
    else:
        if total == 7:
            return 21
        elif total < 7:
            return total + 14
        else:
            return total + 4


def dealer_decide(dealer, deck):
    while card_total(dealer) < 17:
        dealer.append(deck.pop())


def do_you_hit(player, deck):
    while True:
        choice = input('Would you like another card? Yes or no? ')
        choice = choice.lower().strip()
        if choice == 'yes':
            player.append(deck.pop())
            print(player)
            print('Your Total:', card_total(player))
            if card_total(player) == 21:
                print('Player Wins')
                break

            if card_total(player) > 21:
                print('Dealer Wins')
                break

        if choice == 'no':
            return card_total(player)


def who_won(player, dealer):
    if card_total(player) == 21 and card_total(dealer) == 21:
        print('Tie Game')

    elif card_total(player) > 21 and card_total(dealer) > 21:
        print('Tie Game')

    elif card_total(player) > 21:
        print('Dealer Wins')

    elif card_total(dealer) > 21:
        print('Player Wins')

    elif card_total(player) == 21:
        print('Player Wins')

    elif card_total(dealer) == 21:
        print('Dealer Wins')

    elif card_total(player) > card_total(dealer):
        print('Player Wins')

    elif card_total(player) < card_total(dealer):
        print('Dealer Wins')

    elif card_total(player) == card_total(dealer):
        print('Tie Game')


def blackjack():
    deck = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 'Ace', 'Ace', 'Ace', 'Ace'
    ]

    shuffle(deck)
    dealer = []
    player = []

    while True:
        dealer.append(deck.pop())
        dealer.append(deck.pop())
        player.append(deck.pop())
        player.append(deck.pop())
        break
    print('Dealer Shown Card:', dealer[0], 'Cards in Dealer\'s Hand:',
          len(dealer))
    print('Your Shown Card:', player[0], 'Your Hand:', player)

    do_you_hit(player, deck)
    dealer_decide(dealer, deck)
    print('Your Final Score:', card_total(player), '\nDealer\'s Final Score:',
          card_total(dealer))
    who_won(player, dealer)


def main():
    blackjack()


if __name__ == '__main__':
    main()
