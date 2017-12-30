from dealer import Dealer
from player import Player

OPTIONS = 'o'
HIT = 'hit'
STAY = 'stay'
QUIT = 'q'

class GameLogic:

    def __init__(self):
        pass

    def start_game(self):
        print("Welcome to BlackJack")
        print("================ \n")
        print("Options:")
        print("{} - options".format(OPTIONS))
        print("{} - deal another card".format(HIT))
        print("{} - stay at current card".format(STAY))
        print("{} - stay at current card".format(QUIT))

        print("\n")
        print("Game Started...\n")

        dealer_name = "George"
        dealer = Dealer(dealer_name)
        print("A wild {} appeared (your dealer) \n".format(dealer_name))

        player_name = raw_input("What is your name ? \n")
        player = Player(player_name)

        print("{dealer}: Hello, {player_name}. Lets Play! \n".format(dealer=dealer_name, player_name=player_name))

        players_hand = []
        dealers_hand = []

        players_hand.append(dealer.deal_card())
        dealers_hand.append(dealer.deal_card())
        players_hand.append(dealer.deal_card())
        dealers_hand.append(dealer.deal_card())

        dealers_second_hand = dealers_hand[1]
        print("Dealers hand: \n")
        print("Card 1: x x")
        print("Card 2: {suit}, {number} \n".format(suit=dealers_second_hand.suit, number=dealers_second_hand.number))

        players_first_hand = players_hand[0]
        players_second_hand = players_hand[1]
        print("Your hand: \n")
        print("Card 1: {suit}, {number} ".format(suit=players_first_hand.suit, number=players_first_hand.number))
        print("Card 2: {suit}, {number} \n".format(suit=players_second_hand.suit, number=players_second_hand.number))

        nth_card = 2

        player_response = raw_input("Cards have been dealt, would you like to hit or stay ? \n")

        while player_response != STAY:
            players_hand.append(dealer.deal_card())
            nth_card += 1
            next_card = players_hand[nth_card - 1]
            print("Card {nth_card}: {suit}, {number} \n".format(nth_card=nth_card, suit=players_second_hand.suit, number=players_second_hand.number))
            player_response = raw_input("Cards have been dealt, would you like to hit or stay ? \n")

