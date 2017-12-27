import unittest
from src import Card

class testCard(unittest.TestCase):
    def setUp(self):
        self.card = Card('diamond', 10)

    def test_card_has_properties(self):
        self.assertEqual(self.card.suit, 'diamond')
        self.assertEqual(self.card.number, 10)

if __name__ == '__main__':
    unittest.main()
