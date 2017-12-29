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
        self.expected_dealt_cards = {}
        for suit in CARD_SUITS:
            self.expected_dealt_cards[suit] = []

    def test_tracker_has_properties(self):
        tracker = self.tracker
        self.assertIsNotNone(tracker.suits)
        self.assertIsNotNone(tracker.unavailable_suits)
        self.assertIsNotNone(tracker.dealt_cards)

    def test_generate_from_available_card_suit(self):
        # It only generates a suit from available list
        expected_suit = 'spade'
        new_tracker = Tracker(CARD_SUITS)
        # Make a list of already dealt suits
        new_tracker.unavailable_suits = [
            'diamond',
            'clubs',
            'heart'
        ]
        available_suits = new_tracker.available_suits()
        self.assertEqual(available_suits, [expected_suit])

    def test_generate_from_available_numbers(self):
        # It only generates a suit from available numbers
        expected_suit = 'spade'
        new_tracker = Tracker(CARD_SUITS)
        # Force Suit to be spade 
        new_tracker.unavailable_suits = [
            'diamond',
            'clubs',
            'heart'
        ]
        new_tracker.dealt_cards[expected_suit] = [1,2,3,4,5,6,7,8,9,10,11]
        number = new_tracker.generate_card_number(expected_suit)
        self.assertEqual(number, 12)

    def test_reshuffle(self):
        new_tracker = Tracker(CARD_SUITS)
        new_tracker.unavailable_suits = [
            'diamond',
            'club'
        ]
        new_tracker.dealt_cards['spade'] = [1,2,3,4]
        new_tracker.dealt_cards['diamond'] = [3,4,5]
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
