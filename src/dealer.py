from card_manager import CardManager

HIT = 'hit'
STAY = 'stay'

class Dealer(CardManager):
    def __init__(self, name):
        self.name = name
        self.player_response = STAY # default to stay
        super(Dealer, self).__init__()

    def __deal_card(self, player_response):
        return super(Dealer, self).generate_new_card()

    def analyze_response(self, player):
        if player == None:
            # todo: turn into a custom exception
            print "player instance is required for dealer to analyze response."
            return None

        name = player.name
        points = player.total_points
        response = player.response

        if response == HIT:
            return self.generate_new_card()
        elif response == STAY:
            print("{} stays at {}".format(name, points))

        return None

        # player_response = raw_input("{name}, do you wish to hit or stay ? \n".format(name=player_name))
        # while player_response not in [HIT, STAY]:
            # player_response = raw_input("{name}, do you wish to hit or stay ? \n".format(name=player_name))
        # print("player responded with {response}".format(response=player_response))
        # self.player_response = player_response
