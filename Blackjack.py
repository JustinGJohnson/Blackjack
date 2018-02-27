# import Player class from player.py
from player import Player
import ui


# initiate game
user = Player("You")
cpu = Player("CPU")
user.first_deal()
cpu.first_deal()


def first_deal():
    # print first user deal
    # check for blackjack
    ui.message("\nHand: ")
    ui.message(user.get_user_string())
    ui.message("Score: \n" + user.get_score() + "\n")
    if int(user.get_score()) == 21:
        ui.message("\nCongratulations! You got a Blackjack!\n")
        exit(0)

    # print first cpu deal
    # check for blackjack
    if int(cpu.get_score()) == 21:
        ui.message(cpu.get_name() + "\n")
        ui.message("Hand: ")
        ui.message(cpu.get_user_string())
        ui.message("Score: \n" + cpu.get_score() + "\n")
        ui.message("\nThe dealer got Blackjack...Better luck next time.\n")
        exit(0)
    else:
        ui.message(cpu.get_name() + "\n")
        ui.message("Hand: ")
        ui.message(cpu.get_cpu_string())

def hit_sequence():
    # loop sequence for user hits
    user.hit()
    if user.score == 21:
        ui.message("\n" + user.get_name() + "\n")
        ui.message("Hand: ")
        ui.message(user.get_hand())
        ui.message("Score: \n" + user.get_score())
        ui.message("\nCongratulations! You got a Blackjack!\n")
        exit(0)
    elif user.score > 21:
        ui.message("\n" + user.get_name() + "\n")
        ui.message("Hand: ")
        ui.message(user.get_hand())
        ui.message("Score: \n" + user.get_score())
        ui.message("\nYou bust! The dealer wins!\n")
        exit(0)
    elif user.score < 21:
        ui.message("\n" + user.get_name() + "\n")
        ui.message("Hand: ")
        ui.message(user.get_hand())
        ui.message("Score: \n" + user.get_score())
        ui.message("\n")



def cpu_hits():
    while int(cpu.get_score()) <= 16:
        cpu.hit()

def print_data():
    # user data
    ui.message(user.get_name() + "\n")
    ui.message("Hand: ")
    ui.message(user.get_user_string())
    ui.message("Score: \n" + user.get_score() + "\n")

    # cpu data
    ui.message(cpu.get_name() + "\n")
    ui.message("Hand: ")
    ui.message(cpu.get_user_string())
    ui.message("Score: \n" + cpu.get_score() + "\n")

    #check for dealer bust
    if int(cpu.get_score()) > 21:
        ui.message("\nThe dealer busts! You win!\n")
        exit(0)

def final_logic():
    # final logic of game
    if user.get_score() > cpu.get_score():
        ui.message("You win!\n")
    elif user.get_score() < cpu.get_score():
        ui.message("You lose! Good day sir!\n")
    elif user.get_score() == cpu.get_score():
        ui.message("Tie!\n")


def handle_choice(choice):

    if choice == "h":
        hit_sequence()

    elif choice == "s":
        ui.message("You stay")

    else:
        ui.message("Either hit (h) or stay (s)")


def main():

    quit = "q"
    choice = None

    first_deal()

    while choice != "s":
        choice = ui.hit_menu()
        handle_choice(choice)

    cpu_hits()
    print_data()
    final_logic()


if __name__ == '__main__':
    main()
