from random import*

class Player:

  def __init__(self, name):
    self.name = name
    self.hand = []

  def first_deal(self):
    card1 = randint(2, 14)
    card2 = randint(2, 14)
    self.hand.append(card1)
    self.hand.append(card2)

  def hit(self):
    card = randint(2, 14)
    self.hand.append(card)

  def get_name(self):
    return self.name

  def get_hand(self):
    return self.hand
