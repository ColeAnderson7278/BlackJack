from random import shuffle


def getting_in():
    while True:
        player_money = 100
        pot = 0
        print('Wallet:${}'.format(player_money))
        choice = input(
            'This game has a $20 entry fee. Would you like to play? ')
        if choice.strip().lower() == 'no':
            print('Thank you anyways. Maybe nex time.')
            exit()
        if choice.strip().lower() == 'yes':
            player_money = int(player_money) - 20
            pot = 40
            print('Wallet:${}'.format(player_money))
            return


def betting(player_money, pot):
    while True:
        choice = input('\nWould you like to raise your bet? ')
        if choice.strip().lower() == 'no':
            return
        if choice.strip().lower() == 'yes':
            betting_math(player_money, pot)
            return


def is_digit(amount):
    for char in amount:
        if char not in '0123456789':
            return False
        return True


def betting_math(player_money, pot):
    while True:
        amount = input('\nHow much would you like to bet? ')
        if is_digit(amount) == False:
            print('Please put in a number')
        elif int(amount) > int(player_money):
            print('It appears you don\'t have enough to make that bet.')
        elif int(amount) <= int(player_money):
            player_money = player_money - int(amount)
            pot = int(amount) * 2
            print('\nYour Wallet:${} Pot:${}\n'.format(player_money,
                                                       (pot + 40)))
            return


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


def do_you_hit(player, deck, pot):
    while True:
        choice = input('\nWould you like another card? Yes or no? ')
        choice = choice.lower().strip()
        if choice == 'yes':
            player.append(deck.pop())
            print(player)
            print('Your Total:', card_total(player))
            if card_total(player) == 21:
                print('\nPlayer Wins')
                exit()

            if card_total(player) > 21:
                print('\nDealer Wins')
                exit()
        if choice == 'no':
            return card_total(player)


def who_won(player, dealer):
    if card_total(player) == 21 and card_total(dealer) == 21:
        print('\nTie Game')

    elif card_total(player) > 21 and card_total(dealer) > 21:
        print('\nTie Game')

    elif card_total(player) > 21:
        print('\nDealer Wins')

    elif card_total(dealer) > 21:
        print('\nPlayer Wins')

    elif card_total(player) == 21:
        print('\nPlayer Wins')

    elif card_total(dealer) == 21:
        print('\nDealer Wins')

    elif card_total(player) > card_total(dealer):
        print('\nPlayer Wins')

    elif card_total(player) < card_total(dealer):
        print('\nDealer Wins')

    elif card_total(player) == card_total(dealer):
        print('\nTie Game')


def blackjack():
    getting_in()
    deck = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 'Ace', 'Ace', 'Ace', 'Ace'
    ]
    pot = 40
    player_money = 80
    shuffle(deck)
    dealer = []
    player = []
    while True:
        dealer.append(deck.pop())
        dealer.append(deck.pop())
        player.append(deck.pop())
        player.append(deck.pop())
        break
    print('\nDealer Shown Card:', dealer[0], 'Cards in Dealer\'s Hand:',
          len(dealer))
    print('Your Shown Card:', player[0], 'Your Hand:', player)
    do_you_hit(player, deck, pot)
    betting(player_money, pot)
    dealer_decide(dealer, deck)
    print('\nYour Final Score:', card_total(player),
          '\nDealer\'s Final Score:', card_total(dealer))
    who_won(player, dealer)


def main():
    blackjack()


if __name__ == '__main__':
    main()
