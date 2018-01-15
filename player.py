# import random module
from random import*

# Player class definition
class Player:

  # Player class constructor
  # sets self.name to name parameter
  # sets self.hand to empty list
  def __init__(self, name):
    self.name = name
    self.hand = []

  # Player first_deal method
  # store random card values in card1, card2
  # append card1, card2 to hand list
  def first_deal(self):
    card1 = randint(2, 14)
    card2 = randint(2, 14)
    self.hand.append(card1)
    self.hand.append(card2)

  # Player hit method
  # store random card value in card
  # append card to hand list
  def hit(self):
    card = randint(2, 14)
    self.hand.append(card)

  # Player get_name accessor method
  def get_name(self):
    return self.name

  # Player get_hand accessor method
  def get_hand(self):
    return self.hand
