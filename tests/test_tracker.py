import unittest
from src import Tracker

CARD_SUITS = [
    'diamond',
    'clubs',
    'heart',
    'spade'
]

class testTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = Tracker(CARD_SUITS) 
        self.card = self.tracker.generate_new_card()

        self.expected_dealt_cards = {}
        for suit in CARD_SUITS:
            self.expected_dealt_cards[suit] = []

    def test_tracker_has_properties(self):
        self.assertIsNotNone(self.card.suit)
        self.assertIsNotNone(self.card.number)

    def test_generate_from_available_card_suit(self):
        """
            it only generates a suit from available list
        """
        new_tracker = Tracker(CARD_SUITS)
        # Make a list of already dealt suits
        new_tracker.unavailable_suits = [
            'diamond',
            'clubs',
            'heart'
        ]
        card = new_tracker.generate_new_card()
        self.assertEqual(card.suit, 'spade')

    def test_generate_from_available_numbers(self):

        """
            it only generates a suit from available numbers
        """
        new_tracker = Tracker(CARD_SUITS)
        # Force Suit to be spade 
        new_tracker.unavailable_suits = [
            'diamond',
            'clubs',
            'heart'
        ]
        new_tracker.dealt_cards['spade'] = [1,2,3,4,5,6,7,8,9,10,11]
        card = new_tracker.generate_new_card()
        self.assertEqual(card.suit, 'spade')
        self.assertEqual(card.number, 12)

    def test_generate_single_card_suit(self):
        expected_suit = 'spade'
        new_suit = self.tracker.get_new_suit([expected_suit])
        self.assertEqual(new_suit, expected_suit)

    def test_reshuffle(self):
        new_tracker = Tracker(CARD_SUITS)
        new_tracker.generate_new_card()
        new_tracker.generate_new_card()
        new_tracker.generate_new_card()
        new_tracker.reshuffle_deck()
        self.assertEqual(new_tracker.unavailable_suits, [])
        self.assertEqual(new_tracker.dealt_cards, self.expected_dealt_cards)

    def test_cards_all_in_suit(self):
        test_suit = 'spade'
        new_tracker = Tracker(CARD_SUITS)
        # Force Suit to be spade 
        new_tracker.unavailable_suits = [
            'diamond',
            'clubs',
            'heart'
        ]
        new_tracker.dealt_cards[test_suit] = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.assertTrue(new_tracker.cards_all_dealt_in_suit(test_suit))


if __name__ == '__main__':
    unittest.main()
