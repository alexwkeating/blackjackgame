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
        self.card.append(card)
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
        pass
    
    def lose_bet(self):
        pass


def take_bet():
    
    pass

def hit(deck,hand):
    
    pass

def hit_or_stand(deck,hand):
    global playing  
    
    pass

def show_some(player,dealer):
    
    pass
    
def show_all(player,dealer):
    
    pass

def player_bust():
    pass

def player_win():
    pass

def dealer_bust():
    pass
    
def dealer_win():
    pass
    
def push():
    pass