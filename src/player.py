HIT = 'hit'
STAY = 'stay'

class Player:

    def __init__(self, name):
        self.name = name
        self.response = STAY
        self.__total_points = 0

    # todo - Should update points based on card given
    def update_points(card):
        pass

    @property
    def total_points(self):
        return self.__total_points

    # todo - Should return raw_input from prompt to 'hit' or 'stay'
    def respond_to_dealer(self):
        pass
