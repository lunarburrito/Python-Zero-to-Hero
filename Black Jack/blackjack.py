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
        return(f"{self.rank} of {self.suit}")

class Deck:
    def __init__(self):
        self.deck = [] #starting with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card_dealt = self.deck.pop()
        return card_dealt

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        # card will be returned from Deck.deal meth
        self.cards.append(card)
        self.value += values[card.rank]

        #tracking aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces : #verything that is not 0 is TRUE
            self.value -= 10
            self.aces -=1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try :
            chips.bet = int(input("how much would you like to bet? "))
        except :
            print("that is not a number try again")
        else :
            if chips.bet > chips.total:
                print(f'you cannot bet more than {chips.total}')
            else :
                break


#Either player can take hits until they bust.
#This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17.
#It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand.
#You may want it to check for aces in the event that a player's hand exceeds 21.

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.
#If the Player Hits, employ the hit() function above.
#If the Player Stands, set the playing variable to False -
#this will control the behavior of a while loop later on in our code.

def hit_or_stand(deck,hand):
    global playing # to control an upcoming while loop
    while True:
        x = input('Hit or Stand ? enter h or s')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player Stands , Dealer\'s turn')
            playing = False
        else :
            print("didn't get that , please write h or s ")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("BUST PLAYER !")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player Wins !')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Player Wins ! Dealer BUSTED')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer Wins !")
    chips.lose_bet()

def push(player,dealer):
    print('dealer and player Tie ! PUSH')


while True:
    print ("Welcome to the black Jack game ! - Simplified version ")

    playing_deck = Deck()
    playing_deck.shuffle()

    player_hand = Hand()

    player_hand.add_card(playing_deck.deal())
    player_hand.add_card(playing_deck.deal())

    computer_hand = Hand()
    computer_hand.add_card(playing_deck.deal())
    computer_hand.add_card(playing_deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,computer_hand)

    while playing: # recall this variable from our hit_or_stand function
        hit_or_stand(playing_deck,player_hand)
        show_some(player_hand,computer_hand)
        if player_hand.value > 21 :
            player_busts(player_hand,computer_hand,player_chips)
            break
    if player_hand.value <= 21:
        while computer_hand.value > 17:
            hit(playing_deck,computer_hand)
        show_all(player_hand,computer_hand)

        if computer_hand.value > 21 :
            dealer_busts(player_hand,computer_hand,player_chips)
        elif computer_hand.value > player_hand.value :
            dealer_wins(player_hand,computer_hand,player_chips)
        elif computer_hand.value < player_hand.value :
            player_wins(player_hand,computer_hand,player_chips)

        else:
            push(player_hand,computer_hand)

        print (f"Player chips are at {player_chips.total}")

        play_again = input("Want to play again ? y or n  ?")

        if play_again[0].lower() == 'y':
            playing = True
            continue
        else :
            break
