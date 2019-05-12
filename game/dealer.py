from .card import Card


class Dealer:
    sum = 0
    usable_ace = False

    def __init__(self):
        self.take_card()

    def take_card(self):
        """Take one card

        Returns:
            int -- value of card taken
        """
        c = Card().value
        if c == 11:
            self.usable_ace = True
        self.sum += c
        return c

    def play_to_end(self):
        """Play while sum < 17

        Returns:
            int -- sum of cards after playing
        """
        while (self.sum < 17):
            self.take_card()
            if self.sum > 21 and self.usable_ace:
                self.usable_ace = False
                self.sum -= 10
        return self.sum
