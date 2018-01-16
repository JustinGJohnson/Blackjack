# import Player class from player.py
from player import Player

# initiate game by getting name input from user
print("\nWelcome to Multi-deck Blackjack!\n")
name = input("What is your name?\n")
user = Player(name)
cpu = Player("CPU")
user.first_deal()
cpu.first_deal()

# print first user deal
# check for blackjack
print("\nHand: ")
print(user.get_user_string())
print("Score: \n" + user.get_score() + "\n")
if int(user.get_score()) == 21:
    print("\nCongratulations! You got a Blackjack!\n")
    exit(0)

# print first cpu deal
# check for blackjack
if int(cpu.get_score()) == 21:
    print(cpu.get_name() + "\n")
    print("Hand: ")
    print(cpu.get_user_string())
    print("Score: \n" + cpu.get_score() + "\n")
    print("\nThe dealer got Blackjack...Better luck next time.\n")
    exit(0)
else:
    print(cpu.get_name() + "\n")
    print("Hand: ")
    print(cpu.get_cpu_string())

# loop sequence for user hits
hit = input("\nWould you like a hit? (y/n)\n")
while hit=="y":
    user.hit()
    if user.score == 21:
        print("\n" + user.get_name() + "\n")
        print("Hand: ")
        print(user.get_hand())
        print("Score: \n" + user.get_score())
        print("\nCongratulations! You got a Blackjack!\n")
        exit(0)
    elif user.score > 21:
        print("\n" + user.get_name() + "\n")
        print("Hand: ")
        print(user.get_hand())
        print("Score: \n" + user.get_score())
        print("\nYou bust! The dealer wins!\n")
        exit(0)
    elif user.score < 21:
        print("\n" + user.get_name() + "\n")
        print("Hand: ")
        print(user.get_hand())
        print("Score: \n" + user.get_score())
        hit = input("\nWould you like another hit? (y/n)\n")
else:
    print("\n")
    while int(cpu.get_score()) <= 16:
        cpu.hit()

    # user data
    print(user.get_name() + "\n")
    print("Hand: ")
    print(user.get_user_string())
    print("Score: \n" + user.get_score() + "\n")

    # cpu data
    print(cpu.get_name() + "\n")
    print("Hand: ")
    print(cpu.get_user_string())
    print("Score: \n" + cpu.get_score() + "\n")

    #check for dealer bust
    if int(cpu.get_score()) > 21:
        print("\nThe dealer busts! You win!\n")
        exit(0)

    # final logic of game
    if user.get_score() > cpu.get_score():
        print("You win!\n")
    elif user.get_score() < cpu.get_score():
        print("You lose! Good day sir!\n")
    elif user.get_score() == cpu.get_score():
        print("Tie!\n")
