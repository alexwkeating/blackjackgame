import random

suits = pass
ranks = pass
values = pass

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
                self.deck.append(str(card_now))
    
    def __str__(self):
        return str(self.deck)

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
        elif player_choice.upper() == "STAND":
            playing = False
        else:
            print("Invalid choice, available choices include 'hit' and 'stand'")
     return hand

def show_some(player,dealer):
    
    print(f'The player has the following cards: {player}')
    print(f'The dealer has a {dealer[1]} and a hidden card.')
    
def show_all(player,dealer):
    
    print(f'The player has the following cards:\n{player}')
    print(f'The dealer has the following cards:\n{dealer}')

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
    
def push(player, dealer):
    if player.value = dealer.value:
        print("Same value hands, PUSH")