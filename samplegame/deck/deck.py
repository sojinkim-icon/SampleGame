from iconservice import json_dumps, sha3_256

from samplegame.deck.card.card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:

    def __init__(self, deck: list = None):
        self.deck = deck
        # If deck is empty list, fill the deck with cards
        if self.deck is None:
            self.deck = []
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))

    def deal(self):
        random_index = int.from_bytes(bytes(sha3_256("some unique things".encode())), 'big') % len(self.deck)
        single_card = self.deck.pop(random_index)
        return single_card

    def __str__(self):
        response = {
            'deck': self.deck
        }
        return json_dumps(response)
