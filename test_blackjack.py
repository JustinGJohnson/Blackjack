import Blackjack
import player
import ui
import unittest

class TestBlackJack(unittest.TestCase):

    def test_first_deal(self):

        # deal cards to player and cpu
        # test that they have a hand with a score of 21 or less
        user = player.Player("You")
        cpu = player.Player("CPU")
        user.first_deal()
        cpu.first_deal()

        # this method tests the first_deal() method within the Player class
        # I tested this one because the other first_deal() isn't actually dealing
        # but seems like it is, but all it does it print to deal to the user.
        # Instead of checking strings, I thought checking value would be more useful
        self.assertTrue(user.get_score() <= str(21))
        self.assertTrue(cpu.get_score() <= str(21))

    def test_final_logic(self):

        # simulate a game all the way to the end, test that the winner is correctly identified
        playa = player.Player("You")
        computa = player.Player("CPU")
        playa.first_deal()
        computa.first_deal()

        quit = "q"
        choice = None

        Blackjack.first_deal()

        while choice != "s":
            choice = ui.hit_menu()
            Blackjack.handle_choice(choice)

        Blackjack.cpu_hits()
        Blackjack.print_data()

        expected = Blackjack.final_logic()

        win = "You win!\n"
        lose = "You lose! Good day sir!\n"
        tie = "Tie!\n"

        if user.get_score() > cpu.get_score():
            self.assertEqual(expected, win)
        elif user.get_score() < cpu.get_score():
            self.assertEqual(expected, lose)
        elif user.get_score() == cpu.get_score():
            if len(user.get_hand()) < len(cpu.get_hand()):
                self.assertEqual(expected, lose)
            elif len(user.get_hand()) > len(cpu.get_hand()):
                self.assertEqual(expected, win)
            else:
                self.assertEqual(expected, tie)


if __name__ == '__main__':
    unittest.main()
