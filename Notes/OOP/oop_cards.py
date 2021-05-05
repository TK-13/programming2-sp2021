SUITS = ['♥', '♦', '♠', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


class Card:  # The blueprint for a card object
    def __init__(self, rank, suit):  # everything after self is a customization.
        self.rank = rank  # The object's customization feature = what the user specifies.
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


def main():
    deck = Deck()
    deck.shuffle()
    deck.show()
    drawn_card = deck.draw_card()



if __name__ == "__main__":
    main()


