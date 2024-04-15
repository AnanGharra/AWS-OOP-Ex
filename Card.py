#!/usr/bin/env python3

import random

class Card:
    "A class representing a single playing card."
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    "A class representing a deck of cards."
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        "Shuffle the deck of cards."
        if len(self.cards) != 52:
            self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
        random.shuffle(self.cards)

    def deal(self):
        "Deal one card from the deck."
        return self.cards.pop() if self.cards else None
