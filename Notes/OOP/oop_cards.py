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
            card.flip(True)

    def shuffle(self):
        random.shuffle(self.deck)
        # self.deck = random.sample(self.deck, 52)

    def draw_card(self):
        # x = random.randint(1, 52)
        # listlist = []
        # for i in x:
        #     if i in listlist:
        #         i = random.randint(1, 52)

        selection = self.deck.pop(0)
        # self.deck.pop(0)
        # selection.flip()  # keep selection hidden (not shown in a game)
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

    print()
    bob = Player("Bob")
    bob.draw_better(deck,  3)
    bob.show_hand_better()

    print()
    lucy = Player("Lucy")
    lucy.draw_better(deck, 49)
    lucy.show_hand_better()


if __name__ == "__main__":
    main()
