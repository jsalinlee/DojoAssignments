import random
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    # def setCard(self, suit, value):
class Deck(object):
    def __init__(self):
        self.deck = []
        self.suits = ["spades", "hearts", "diamonds", "clubs"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q","K"]
        for i in self.values:
            for j in self.suits:
                self.deck.append(Card(j, i))
                # print self.deck[i].value
    def randomCard(suit, value):
        pass
    def deal(self):
        random.randrange(0, 5)
        print self.deck[random.randrange(0, 52)].value
        print self.deck[random.randrange(0, 52)].suit
        # for i in range(len(self.deck)):
            # print self.deck[i].value, self.deck[i].suit
deck = Deck()
deck.deal()
