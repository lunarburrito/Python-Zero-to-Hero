##
#The game needs to have one player versus an automated dealer.
#The player can stand or hit.
#The player must be able to pick their betting amount.
#You need to keep track of the player's total money.
#You need to alert the player of wins, losses, or busts, etc...
#Steps :
#Create a deck of 52 cards
#Shuffle the deck
#Ask the Player for their bet
#Make sure that the Player's bet does not exceed their available chips
#Deal two cards to the Dealer and two cards to the Player
#Show only one of the Dealer's cards, the other remains hidden
#Show both of the Player's cards
#Ask the Player if they wish to Hit, and take another card
#If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
#If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
#Determine the winner and adjust the Player's chips accordingly
#Ask the Player if they'd like to play again

import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

#Card class where each Card object has a suit and a rank,
#Deck class to hold all 52 Card objects, and can be shuffled,
#Hand class that holds those Cards that have been dealt to each player from the Deck.

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        print(f"{self.rank} of self.suit")
