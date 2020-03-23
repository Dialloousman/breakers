import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuit(self):
        return(self.suit)

    def getValue(self):
        return(self.value)

class Deck(Card):
    def __init__(self):
        self.suits = ["DIAMONDS", "SPADES", "HEARTS", "CLUBS"]
        self.values = ["ACE", "TWO" , "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]
        self.deck = []
        for suit in self.suits:
            for value in self.values:
                self.deck.append(["{} of {}".format(value, suit)])

    
    def num_cards (self):
        return (len(self.suits) * len(self.values))

    def shuffle(self):
        random.shuffle(self.deck)
        return ("Deck shuffled")

     # Returns the top Card in the deck, then puts it back.
    def peek(self):
        return self.deck[-1]
    
    # Draws and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self):
        return self.deck.pop()
    
    # Adds the input card to the deck. If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card):
        if len(self.deck) >= 52:
            return Exception
        self.deck.append(card)
    
    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self):
        print(self.deck)

if __name__ == '__main__':
    uno = Deck()
    
   


