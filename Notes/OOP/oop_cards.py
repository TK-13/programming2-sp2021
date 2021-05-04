SUITS = ['♥', '♦', '♠', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def flip(self):
        print(self.rank + " of " + self.suit)


class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(rank, suit))

    def show(self):
        for card in self.deck:
            card.flip()


def main():
    deck = Deck()
    deck.show()


if __name__ == "__main__":
    main()


