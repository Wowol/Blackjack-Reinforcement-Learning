class State:
    player_sum = 0  # between 12 and 21
    player_usable_ace = False

    dealer_card = 0  # between 2 and 11

    def __init__(self, player_sum, player_usable_ace, dealer_card):
        """Initialize state

        Arguments:
            player_sum {int} -- Player sum
            player_usable_ace {bool} -- Does player have usable ace
            dealer_card {int} -- Dealer card value (11 if ace)
        """
        self.player_sum = player_sum
        self.player_usable_ace = player_usable_ace
        self.dealer_card = dealer_card

    def __eq__(self, other):
        return (self.player_sum, self.player_usable_ace, self.dealer_card) == (other.player_sum, other.player_usable_ace, other.dealer_card)

    def __hash__(self):
        return hash((self.player_sum, self.player_usable_ace, self.dealer_card))

    def __ne__(self, other):
        return not(self == other)