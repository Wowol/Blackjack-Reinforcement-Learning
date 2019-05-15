from utils.state import State, states
from game.player import Player
from game.dealer import Dealer
from game.action import Action
from agents.monteCarloExploringStarts import MonteCarloExploringStarts
from agents.onPolicyMonteCarlo import OnPolicyMonteCarlo
from agents.deterministic import Deterministic
from agents.sarsa import Sarsa


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


def play_many_times(policy, times=30000):
    times_won = 0
    all = 0
    for i in range(0, times):
        result = play(policy)
        if result != 0:
            all += 1
        if result == 1:
            times_won += 1
    return times_won / all * 100

def print_differences(first_policy, second_policy):
    number = 0
    for k, v in first_policy.items():
        if second_policy[k] != v:
            number +=1
            print(k)
            print("FIRST POLICY: ", v)
            print("SECOND POLICY: ", second_policy[k])
            print()

    print ("Number of diffrences: ", number)
    print()


# Biore najlepsza akcje z duzym prawodpdobosniewm
deterministic_agent = Deterministic()
agent = MonteCarloExploringStarts()
agent = OnPolicyMonteCarlo(0.2)
# agent =  Deterministic()# Sarsa()#OnPolicyMonteCarlo(0.1)
policy = agent.calculate(100000)

print_differences(deterministic_agent.calculate(), policy)

# for state, action in policy.items():
#     print(state.dealer_card, state.player_sum, state.player_usable_ace, action)


print(play_many_times(policy))
