import unittest
from src import Dealer, Player, Card

class testDealer(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer('Bob')

    def test_attributes(self):
        dealer = self.dealer
        self.assertIsNotNone(dealer.name, 'Bob')
        self.assertIsNotNone(dealer.player_response, 'stay')

    def test_analyze_response_hit_response(self):
        dealer = self.dealer
        player = Player('George')
        player.response = 'hit'
        response = dealer.analyze_response(player)
        self.assertIsInstance(response, Card)

    def test_analyze_response_stay_response(self):
        dealer = self.dealer
        player = Player('George')
        player.response = 'stay'
        response = dealer.analyze_response(player)
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
