class Card:

    #defining suits and ranks
    suits = {'c':'Clubs', 'd':'Diamonds', 'h':'Hearts', 's':'Spades'}
    ranks = ['none', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, rank, suit):

        if not isinstance(rank, int):
            raise TypeError ('Please, enter an integer')

        if not isinstance (suit, str):
            raise TypeError ('Please, enter a string')

        if rank not in range (1,13):
            raise ValueError ("the value of the first parameter is not in the range 1..13 inclusive")

        if suit not in ('d','h','c','s'):
            raise ValueError('suit not in dhcs')
        self.rank = rank
        self.suit = suit



    def getRank(self):
        return Card.ranks[self.rank]


    def getSuit(self):
        return Card.suits[self.suit]

    def bjValue(self):
        if Card.ranks[self.rank] == 'Ace':
            return 1
        elif Card.ranks[self.rank] == 'none':
            return 0
        elif Card.ranks[self.rank] == 'Jack':
            return 10
        elif Card.ranks[self.rank] == 'Queen':
            return 10
        elif Card.ranks[self.rank] == 'King':
            return 10
        else:
            return Card.ranks[self.rank]


    def __str__(self):
        return '%s of %s' % (Card.ranks[self.rank],
                                   Card.suits[self.suit])

#objects of card
card1 = Card(5,"s")


print(card1)

print(card1.getRank())
print(card1.getSuit())
print (card1.bjValue())