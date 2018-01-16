# import Player class from player.py
from player import Player

# initiate game by getting name input from user
playerName = input("What is your name?\n")
# create Player object for user
player1 = Player(playerName)
# game opening dialogue
print("\nHello " + player1.get_name() + "! Welcome to Blackjack\n")
print("Dealing cards...")
print("................\n")
print("................\n")
print("................\n")
# test first_deal method
player1.first_deal()
print(player1.get_hand())
print(player1.get_score())
# test hit method
player1.hit()
print(player1.get_hand())
print(player1.get_score())
