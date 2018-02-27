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

        self.assertTrue(user.get_score() <= str(21))
        self.assertTrue(cpu.get_score() <= str(21))



if __name__ == '__main__':
    unittest.main()
