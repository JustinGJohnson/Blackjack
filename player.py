# import random module
from random import*

# Player class definition
class Player:

  # Player class constructor
  # sets self.name to name parameter
  # sets self.hand to empty list
  # sets self.score to 0
  def __init__(self, name):
    self.name = name
    self.hand = []
    self.score = 0

  # Player first_deal method
  # store random values in value1, value2
  # assign card saccording to value
  # add true value of cards to score
  # append card1, card2 to hand list
  def first_deal(self):
    card1 = ""
    card2 = ""
    value1 = randint(2, 14)
    value2 = randint(2, 14)

    # logic for card1
    if value1 <= 10:
        card1 = str(value1)
        self.score+=value1
    elif value1 == 11:
        card1 = "J"
        self.score+=10
    elif value1 == 12:
        card1 = "Q"
        self.score+=10
    elif value1 == 13:
        card1 = "K"
        self.score+=10
    elif value1 == 14:
        card1 = "A"
        test = self.score+11
        if test > 21:
            self.score+=1
        else:
            self.score+=11

    self.hand.append(card1)

    # logic for card2
    if value2 <= 10:
        card2 = str(value2)
        self.score+=value2
    elif value2 == 11:
        card2 = "J"
        self.score+=10
    elif value2 == 12:
        card2 = "Q"
        self.score+=10
    elif value2 == 13:
        card2 = "K"
        self.score+=10
    elif value2 == 14:
        card2 = "A"
        test = self.score+11
        if test > 21:
            self.score+=1
        else:
            self.score+=11

    self.hand.append(card2)

  # Player hit method
  # get random value
  # assign card according to value
  # add true value of card to score
  # append card to hand list
  def hit(self):
    card = ""
    value = randint(2, 14)

    # logic for card
    if value <= 10:
        card = str(value)
        self.score+=value
    elif value == 11:
        card = "J"
        self.score+=10
    elif value == 12:
        card = "Q"
        self.score+=10
    elif value == 13:
        card = "K"
        self.score+=10
    elif value == 14:
        card = "A"
        test = self.score+11
        if test > 21:
            self.score+=1
        else:
            self.score+=11

    self.hand.append(card)

  # Player get_name accessor method
  def get_name(self):
    return self.name

  # Player get_hand accessor method
  def get_hand(self):
    return self.hand

  # Player get_score accessor method
  def get_score(self):
    return str(self.score)
