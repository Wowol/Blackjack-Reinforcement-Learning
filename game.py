from player import Player
from dealer import Dealer
from state import State
from action import Action
from MonteCarloExploringStarts import MonteCarloExploringStarts
from OnPolicyMonteCarlo import OnPolicyMonteCarlo


def play(policy, win=1, tie=0, lose=-1):
    player = Player()
    dealer = Dealer()

    state = State(player.sum, player.usable_ace, dealer.sum)
    current_action = policy[state]

    while True:
        if current_action == Action.HIT:
            player.hit()
            if player.sum > 21:
                return lose
                break
            else:
                current_state = State(
                    player.sum, player.usable_ace, dealer.sum)
                current_action = policy[current_state]
        else:
            dealer.play_to_end()
            if dealer.sum > 21 or dealer.sum < player.sum:
                return win
            elif dealer.sum == player.sum:
                return tie
            else:
                return lose
            break


def play_many_times(policy, times=10000):
    times_won = 0
    all = 0
    for i in range(0, times):
        result = play(policy)
        if result != 0:
            all += 1
        if result == 1:
            times_won += 1
    return times_won / all * 100


agent = OnPolicyMonteCarlo()
policy = agent.calculate(100000)
for state, action in policy.items():
    print(state.dealer_card, state.player_sum, state.player_usable_ace, action)


print(play_many_times(policy))
