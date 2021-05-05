import random

SUITS = ['♥', '♦', '♠', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def flip(self, to_print=False):
        if to_print:
            print(self.rank + " of " + self.suit)
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(rank, suit))

    def show(self):
        for card in self.deck:
            card.flip(to_print=True)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)


class Player:

    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck, amount=1):
        for i in range(amount):
            self.hand.append(deck.draw_card())

    def show_hand(self):
        card_names = [card.flip() for card in self.hand]
        print("{0}: {1}".format(self.name, ", ".join(card_names)))


def main():
    deck = Deck()
    deck.shuffle()
    deck.show()

    bob = Player("Bob")
    bob.draw(deck, 3)
    bob.show_hand()

    lucy = Player("Lucy")
    lucy.draw(deck, 49)
    lucy.show_hand()


if __name__ == "__main__":
    main()
