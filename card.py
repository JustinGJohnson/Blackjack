import random

class Card:
  def __init__(self):
    self.rank = random.choice(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
    self.suit = random.choice(["c", "d", "h", "s"])
    self.instance = self.rank + self.suit

  def get_instance(self):
    return self.instance
