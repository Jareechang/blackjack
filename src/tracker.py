import random
from card import Card

class Tracker:
    """
        Tracker:

            It should tracks the card being issued and handle re-shuffles of the deck if required

        Features:
            - Should issue cards in a random fashion
            - Should not issue cards given a suit (diamond, clubs, heart and spade) within (1-12)
            - Should not duplicate the cards
    """
    def __init__(self, suits):
        self.available_suits = suits
        self.unavailable_suits = []
        self.dealt_cards = {}
        for suit in suits:
            self.dealt_cards[suit] = []

    def cards_all_dealt_in_suit(self, suit):
        return len(self.dealt_cards[suit]) >= 12

    def reshuffle_deck(self):
        self.unavailable_suits = []
        self.dealt_cards = {}
        for suit in self.available_suits:
            self.dealt_cards[suit] = []

    def get_new_suit(self, available_suits):
        if len(available_suits) > 1:
            new_suit = available_suits[random.randint(0,3)]
        else:
            new_suit = available_suits[0]

        return new_suit

    def generate_card_suit(self):
        available_suits = list(
            set(self.available_suits)
            - set(self.unavailable_suits))

        if len(available_suits) == 0:
            self.reshuffle_deck()

        new_suit = self.get_new_suit(available_suits)

        while self.cards_all_dealt_in_suit(new_suit):
            new_suit = self.get_new_suit(available_suits)

        return new_suit

    def generate_card_number(self, suit):
        number = random.randint(1, 12) 
        while number in self.dealt_cards[suit]:
            number = random.randint(1, 12) 
        return number

    def generate_new_card(self):
        suit = self.generate_card_suit()
        number = self.generate_card_number(suit)
        return Card(suit, number)

