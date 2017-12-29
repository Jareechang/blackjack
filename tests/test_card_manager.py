import unittest
from src import CardManager

class testCard(unittest.TestCase):
    def setUp(self):
        self.cardManager = CardManager()

    def test_card_has_properties(self):
        cardManager = self.cardManager
        card = cardManager.generate_new_card()
        self.assertTrue(cardManager.contains_card(card))

if __name__ == '__main__':
    unittest.main()
