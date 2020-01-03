import random

suits = pass
ranks = pass
values = pass

playing = True


class Card:
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass


class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                pass
    
    def __str__(self):
        pass

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        pass


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 
    
    def add_card(self,card):
        pass
    
    def ace_adjustment(self):
        pass


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
    global playing  # to control an upcoming while loop
    
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