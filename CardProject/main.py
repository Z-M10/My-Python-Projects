### Card shuffler
from itertools import product
import random
from random import shuffle

ranks = ["2", "3", "4", "5", "6", "7",
         "8", "9", "10", "Jack", "Queen",
         "King", "Ace"]

suites = ["Hearts", "Diamonds", "Clubs", "Spades"]



def ranks_suites(r, s):
    deck = []
    for i in product(r, s):
       deck.append(i)
    return deck

my_deck = ranks_suites(ranks, suites)
shuffle(my_deck)

hands = {
    "Player 1": [],
    "Player 2": [],
    "Player 3": [],
    "Player 4": []

}
for player in range(1,5):
    for _ in range(0, 5):
        card = my_deck.pop()
        hands[f"Player {player}"].append(card) ## Loops through all players in dictionary and assigns a card

for player, hand in hands.items():
    print(player, "hand: ")

    for i, card in enumerate(hand):
        print(f"{card[0]} of {card[1]}", end="" if i == len(hand)-1 else ", ")
    print()
















