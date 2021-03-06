import random
from tracker import Tracker
from card import Card

CARD_SUITS = [
    'diamond',
    'clubs',
    'heart',
    'spade'
]

class CardManager(object):
    """
        Card Manager

        Features:
            - Wrapper around Tracker and Card api to generate new card
    """
    def __init__(self):
        self.__tracker = Tracker(CARD_SUITS)

    def __get_new_card_suit(self):
        tracker = self.__tracker
        available_suits = tracker.available_suits()

        if len(available_suits) == 0:
            tracker.reshuffle_deck()

        if len(available_suits) > 1:
            new_suit = available_suits[random.randint(0,3)]
        else:
            new_suit = available_suits[0]

        return new_suit

    def __generate_card_suit(self):
        tracker = self.__tracker
        available_suits = tracker.available_suits()

        if len(available_suits) == 0:
            tracker.reshuffle_deck()

        new_suit = self.__get_new_card_suit()

        while tracker.cards_all_dealt_in_suit(new_suit):
            new_suit = self.__get_new_card_suit()

        return new_suit

    def __generate_card_number(self, suit):
        tracker = self.__tracker
        number = random.randint(1, 12) 
        while number in tracker.dealt_cards[suit]:
            number = random.randint(1, 12) 
        return number

    def contains_card(self, card):
        tracker = self.__tracker
        dealt_cards = tracker.dealt_cards
        suit = card.suit
        number = card.number
        if number in dealt_cards[suit]:
            return True
        return False

    def generate_new_card(self):
        tracker = self.__tracker
        suit = self.__generate_card_suit()
        number = self.__generate_card_number(suit)
        tracker.track_card(suit, number)
        return Card(suit, number)

