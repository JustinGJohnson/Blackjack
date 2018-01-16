# import Player class from player.py
from player import Player

# initiate game by getting name input from user
print("\nWelcome to Multi-deck Blackjack!\n")
name = input("What is your name?\n")
user = Player(name)
print("Hello, " + user.get_name() + ".\n")
cpu = Player("CPU")
user.first_deal()
cpu.first_deal()
print("Hand: ")
print(user.get_hand())
print("Score: \n" + user.get_score())
hit = input("\nWould you like a hit? (y/n)\n")
while hit=="y":
    user.hit()
    if user.score == 21:
        print("\nHand: ")
        print(user.get_hand())
        print("Score: \n" + user.get_score())
        print("\nCongratulations! You got a Blackjack!\n")
        exit(0)
    elif user.score > 21:
        print("\nHand: ")
        print(user.get_hand())
        print("Score: \n" + user.get_score())
        print("\nYou lose! Good day sir!\n")
        exit(0)
    elif user.score < 21:
        print("\nHand: ")
        print(user.get_hand())
        print("Score: \n" + user.get_score())
        hit = input("\nWould you like another hit? (y/n)\n")
else:
    print("\nHand: ")
    print(user.get_hand())
    print("Score: \n" + user.get_score())
