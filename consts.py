from state import State

states = []

for player_usable_ace in [False, True]:
    for player_sum in range(12, 22):
        for dealer_card in range(2, 12):
            states.append(State(player_sum, player_usable_ace, dealer_card))
