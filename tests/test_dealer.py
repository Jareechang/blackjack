import unittest
from src import Dealer

class testCard(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer('Bob')

    def test_attributes(self):
        dealer = self.dealer
        self.assertIsNotNone(dealer.name, 'Bob')
        self.assertIsNotNone(dealer.player_response, 'stay')

    def test_analyze_response(self):
        pass

if __name__ == '__main__':
    unittest.main()
