


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuit(self):
        return(self.suit)

    def getValue(self):
        return(self.value)

class Deck():
    def __init__(self):
        self.suits = ["DIAMONDS", "SPADES", "HEARTS", "CLUBS"]
        self.values = ["ACE", "TWO" , "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]
    
    def num_cards(self):
        return (len(self.suits) * len(self.values))

    #shuffles the deck
    def shuffle(self):




uno = Deck()

print(uno.num_cards())


