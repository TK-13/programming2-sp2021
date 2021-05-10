import random

SUITS = ['♥', '♦', '♠', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


class Card:  # The blueprint for a card object
    def __init__(self, rank, suit):  # everything after self is a customization.
        self.rank = rank  # The object's customization feature = what the user specifies.
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
        selection = self.deck.pop(0)
        selection.flip()
        return selection


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, source):
        drawn_card = source.draw_card()
        self.hand.append(drawn_card)

    # From Alex and Aaron
    def draw_better(self, deck, amount=1):
        for i in range(amount):
            self.hand.append(deck.draw_card())

    def show_hand(self):
        print(self.name + " has:\n")
        for card in self.hand:
            card.flip()

    # From Alex and Aaron
    def show_hand_better(self):
        card_names = [card.flip() for card in self.hand]
        print("{0}: {1}".format(self.name, ", ".join(card_names)))


def main():
    deck = Deck()
    deck.shuffle()
    deck.show()
    drawn_card = deck.draw_card()

    bob = Player("Bob")
    bob.draw(deck, 3)
    bob.show_hand()

    lucy = Player("Lucy")
    lucy.draw(deck, 49)
    lucy.show_hand()


if __name__ == "__main__":
    main()


