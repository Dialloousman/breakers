class Routine:
    def __init__(self, person):
        self.person = person

    def morning(self):
        print('good morning' + ' ' + self.person)
    
    def afternoon (self):
        print('Hey {}, are you hungry yet?'.format(self.person))

    def evening (self):
        print('{}, its time for bed!'.format(self.person))


SUITS = ["DIAMONDS", "SPADES", "HEARTS", "CLUBS"]
VALUES = ["ACE", "TWO" , "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuit(self):
        print(self.suit)

    def getValue(self):
        print(self.value)


# inhertiance example
class Schedule(Routine):
    def greeting():
        pass

monday = Card("ace", "diamonds", )

monday.getValue()


