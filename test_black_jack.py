from black_jack import *


def test_who_won():
    assert who_won([10, 10], [9, 10]) == print('Player Wins')
    assert who_won(['Ace', 'Ace'], [2, 10]) == print('Tie Game')
    assert who_won(['Ace', 10, 10], [5, 5, 10]) == print('Player Wins')
    assert who_won([6, 7, 10], [10, 8]) == print('Dealer Wins')


def test_card_total():
    assert card_total([2, 2]) == (4)
    assert card_total(['Ace', 10]) == (21)
    assert card_total(['Ace', 10, 9]) == (20)
    assert card_total([5, 2, 3, 7, 4]) == (21)
    assert card_total([9, 3, 10]) == (22)


def test_is_digit():
    assert is_digit('2323') == True
    assert is_digit('Not A Number') == False
    assert is_digit('Nope3') == False

def test
