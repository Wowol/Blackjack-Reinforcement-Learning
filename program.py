from utils.state import State, states
from game.player import Player
from game.dealer import Dealer
from game.action import Action
from agents.monteCarloExploringStarts import MonteCarloExploringStarts
from agents.onPolicyMonteCarlo import OnPolicyMonteCarlo
from agents.qLearning import QLearning
from agents.deterministic import Deterministic
from agents.sarsa import Sarsa
from utils.tests import *
import argparse
import sys
import time


algos = {"deterministic": Deterministic, "monteCarloExploringStarts": MonteCarloExploringStarts,
         "onPolicyMonteCarlo": OnPolicyMonteCarlo, "qlearning": QLearning, "sarsa": Sarsa}

parser = argparse.ArgumentParser(
    description='Blackjack reinforcement learning')
parser.add_argument('-n', '--number', type=int, default=10000,
                    help='Number of times to repeat algorithms')
parser.add_argument('-e', '--epsilon', type=int, default=0.2,
                    help='Epsilon value for algorithms')
parser.add_argument('-a', '--alpha', type=int, default=0.02,
                    help='Alpha')
parser.add_argument('-i', '--improve', type=bool, default=True,
                    help='Try to improve results by repeat to learn starting with states with nearly expected reward')
parser.add_argument('algorithm', type=str, help='Algorithm to learn (' +
                    ', '.join([name for name in algos.keys()]) + ')')
args = parser.parse_args()

algo = None
for name, cls in algos.items():
    if name.lower().startswith(args.algorithm.lower()):
        algo = cls
if algo is None:
    parser.print_help()
    sys.exit(1)

deterministic_agent = Deterministic()


agent = algo(epsilon=args.epsilon, alpha=args.alpha, improve=args.improve)

start_time = time.time()
policy = agent.calculate(args.number)
elapsed_time = print("TIME: ", time.time() - start_time)

print_differences(deterministic_agent.calculate(), policy)
print(play_many_times(policy, times=1000000))