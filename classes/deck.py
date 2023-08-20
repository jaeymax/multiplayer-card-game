import random
from typing import List
from card import Card
#from .card import Card

class Deck:
    """This class represent a deck of cards"""
    NUMBER_OF_CARDS = 32
    NAMES_OF_CARDS = [
        'eight of club','eight of diamond','eight of heart','eight of spade',
        'king of club','king of diamond','king of heart','king of spade',
        'jack of club','jack of diamond','jack of heart','jack of spade',
        'nine of club','nine of diamond','nine of heart','nine of spade',
        'queen of club','queen of diamond','queen of heart','queen of spade',
        'seven of club','seven of diamond', 'seven of heart','seven of spade',
        'six of club','six of diamond', 'six of heart','six of spade',
        'ten of club', 'ten of diamond', 'ten of heart', 'ten of spade',
        
    ]

    def __init__(self) -> None:
        self.cards = []
        self.create_cards()
        assert len(self.cards) == Deck.NUMBER_OF_CARDS


    def shuffle(self)->None:
        random.shuffle(self.cards)

    def __iter__(self):
        for card in self.cards:
            yield card

    def create_cards(self):
        for card_name in Deck.NAMES_OF_CARDS:
            kind, value = card_name.split(' ')[2], card_name.split(' ')[0]
            image_url = value+'of'+kind+'.png'

            match value:
                case 'king':
                    value = 13
                case 'queen':
                    value = 12
                case 'jack':
                    value = 11
                case 'ten':
                    value = 10
                case 'nine':
                    value = 9
                case 'eight':
                    value = 8
                case 'seven':
                    value = 7
                case 'six':
                    value = 6

            card = Card(kind, value, image_url)
            self.cards.append(card)

deck1 = Deck()
deck1.shuffle()

for card in deck1:
    print(card)