import random
import time

suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                card_now = Card(suit, rank)
                self.deck.append((card_now))
    
    def __str__(self):
        deck_cards = ''
        for card in self.deck:
            deck_cards += '\n' + card.__str__()
        return deck_cards

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        one_card = self.deck.pop()
        return one_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list
        self.value = 0   # start with zero value
        self.aces = 0    # keep track of aces
    
    def add_card(self,card): #card will be the dealt card from the Deck.deal()
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1
    
    def ace_adjustment(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet():
    while True:
        try:
            player_bet = int(input("Please enter the value of the bet you would like to place:"))
        except:
            print("An error has occurred, please ensure value entered is a valid number.")
        else:
            print(f"Thank you, your bet is {player_bet}")
            break
    return player_bet

def hit(deck,hand):
    hand.add_card(deck.deal())
    
    while hand.value > 21 and hand.aces > 0:
        hand.ace_adjustment()
    
    return hand

def hit_or_stand(deck,hand):
    global playing
    playing = True
    
    while playing:
        player_choice = input('Please choose if you would like to hit or stand')
        if player_choice.upper() == "HIT":
            hit(deck, hand)
            if hand.value > 21:
                playing = False
            print(hand.cards[-1])
        elif player_choice.upper() == "STAND":
            playing = False
        else:
            print("Invalid choice, available choices include 'hit' and 'stand'")
    return hand

def show_some(player,dealer):
    
    print('The player has the following cards:')
    for card in player.cards:
        print(card)
    print(f'The dealer has a {dealer.cards[1]} and a hidden card.')
    
def show_all(player,dealer):
    
    print('The player has the following cards:')
    for card in player.cards:
        print(card)
    print('The dealer has the following cards:')
    for card in dealer.cards:
        print(card)

def player_busts(player, chips):
    if player.value > 21:
        print("Player has busted")
        chips.lose_bet()
    
def player_wins(player, dealer, chips):
    if player.value > dealer.value:
        print("Player wins!")
        chips.win_bet()

def dealer_busts(dealer, chips):
    if dealer.value > 21:
        print("Dealer has busted")
        chips.win_bet()

    
def dealer_wins(player, dealer, chips):
    if dealer.value > player.value:
        print("Dealer wins!")
        chips.lose_bet()

    
def push(player, dealer, chips):
    if player.value == dealer.value:
        print("Same value hands, PUSH")



player_chips = Chips()

while True:
    playing = True
    print(f"Welcome to Blackjack! Current player chip amount: {player_chips.total}")
    
    # Create & shuffle the deck, deal two cards to player and dealer
    play_deck = Deck()
    play_deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand()
    
    player_hand.add_card(play_deck.deal())
    dealer_hand.add_card(play_deck.deal())
    player_hand.add_card(play_deck.deal())
    dealer_hand.add_card(play_deck.deal())
        
    # Set up the Player's chips

    player_chips.bet = take_bet()

    while playing:
        
        show_some(player_hand, dealer_hand)
        player_hand = hit_or_stand(play_deck, player_hand)
        print('\n'*100) # clean up command window

        if player_hand.value > 21:
            player_busts(player_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    show_all(player_hand, dealer_hand)

    if player_hand.value < 22:
        while dealer_hand.value < 17:
            print("Dealer chooses to HIT")
            time.sleep(2)                      # slight delay to seem like a more realistic hit
            dealer_hand = hit(play_deck, dealer_hand)
            print('\n'*100)                    # clean up command window
            show_all(player_hand, dealer_hand)
            
        if dealer_hand.value < 22:
            player_wins(player_hand, dealer_hand, player_chips) 
            dealer_wins(player_hand, dealer_hand, player_chips)
            push(player_hand, dealer_hand, player_chips)
        else:
            dealer_busts(dealer_hand, player_chips)

        
    
    # Inform player of their chips total 
    print(f"Player's current chip value is: {player_chips.total}")
    
    # Ask to play again
    play_again = 'placeholder'
    while play_again.upper() != 'YES' and play_again.upper() != 'NO':
        play_again = input("Would you like to play again, please answer 'yes' or 'no':")
    if play_again.upper() == 'YES':
        continue
    else:
        break