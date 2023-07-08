##### Blackjack Project #######

#Difficulty Normal: Use all Hints below to complete the project.
#Difficulty Hard: Use only hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard: only use Hints 1 & 2 to complete the project.
#Difficulty Expert: Only use Hint 1 to complete the project.
########## Our Blackjack House Rules ##########
## The deck is unlimited in size.
##There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of card:
cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
##The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
########## Hints ##########
# Hint 1: Go to this website and try out the Blackjack game:
# https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
# https://blackjack-final.appbrewery.reply

import random
from typing import List, Any
def deal_card():
     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
     card = random.choice(cards)
     return card
def calculate_score(cards):
      user_cards = []
      computer_cards = []
      is_game_over = False
for _ in  range(2):
     computer_cards = []
     new_card = deal_card()
     #user_cards.append(deal_card())
     computer_cards.append(deal_card())
     user_score = calculate_score(deal_card())
     computer_score = calculate_score(computer_cards)
     print(f"your cards: {deal_card()}, current score: {user_score}")
     print(f"computer first card: {computer_cards[0]}")
#

