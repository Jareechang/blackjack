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
        self.suits = suits
        self.unavailable_suits = []
        self.dealt_cards = {}
        for suit in suits:
            self.dealt_cards[suit] = []

    def cards_all_dealt_in_suit(self, suit):
        return len(self.dealt_cards[suit]) >= 12

    def reshuffle_deck(self):
        self.unavailable_suits = []
        self.dealt_cards = {}
        for suit in self.suits:
            self.dealt_cards[suit] = []

    def available_suits(self):
        return list(set(self.suits)
            - set(self.unavailable_suits))

    def generate_card_number(self, suit):
        number = random.randint(1, 12) 
        while number in self.dealt_cards[suit]:
            number = random.randint(1, 12) 
        return number

    def track_card(self, suit, number):
        card_tracking_slot = self.dealt_cards[suit]
        card_tracking_slot.append(number)
        unavailable_suits = self.unavailable_suits
        if self.cards_all_dealt_in_suit(suit):
            unavailable_suits.append(suit)

