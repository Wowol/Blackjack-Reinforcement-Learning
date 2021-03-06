from game.dealer import Dealer
from game.player import Player
import numpy as np
from statistics import mean
from utils.state import State, states
from .agent import Agent
from game.action import Action
import random


class MonteCarloExploringStarts(Agent):

    policy = {k: Action.STAND if k.player_sum >=
              19 else Action.HIT for k in states}
    returns = {(k, a): [] for k in states for a in list(Action)}
    Q = {k: {} for k in states}

    DELTA = 0.05
    TIMES_TESTED_SAME_STATE = 1000

    def __init__(self, improve = True, *_, **__):
        self.IMPROVE = improve

    def calculate(self, number=1000000):
        """Estimate many times

        Keyword Arguments:
            number {int} -- Number of times to estimate (default: {1000000})

        Returns:
            Dictionary -- Estimated policy
        """
        for i in range(0, number):
            self.estimate_one()

        if self.IMPROVE:
            for k, v in self.Q.items():
                if abs(v[Action.HIT] - v[Action.STAND]) < self.DELTA:
                    for i in range(0, self.TIMES_TESTED_SAME_STATE):
                        self.estimate_one(k)

        return self.policy

    def estimate_one(self, starting_state=None):
        episode, reward = self.generate_episode(starting_state)
        for state, action in episode:
            self.returns[(state, action)].append(reward)
            self.Q[state][action] = mean(self.returns[(state, action)])

        for state, _ in episode:
            self.policy[state] = max(self.Q[state], key=self.Q[state].get)

    def generate_episode(self, starting_state=None):
        """Generate episode using current policy

        Returns:
            list(state, action) -- List of pairs(state, action)
            int -- reward (1 or 0)
        """
        player = Player()
        dealer = Dealer()
        current_state = starting_state if starting_state is not None else random.choice(
            states)
        current_action = random.choice(list(Action))

        player.sum = current_state.player_sum
        player.usable_ace = current_state.player_usable_ace
        dealer.sum = current_state.dealer_card

        episode = [(current_state, current_action)]
        reward = 0

        while True:
            if current_action == Action.HIT:
                player.hit()
                if player.sum > 21:
                    reward = -1
                    break
                else:
                    current_state = State(
                        player.sum, player.usable_ace, dealer.sum)
                    current_action = self.policy[current_state]
                    episode.append((current_state, current_action))
            else:
                dealer.play_to_end()
                if dealer.sum > 21 or dealer.sum < player.sum:
                    reward = 1
                elif dealer.sum == player.sum:
                    reward = 0
                else:
                    reward = -1
                break

        return episode, reward
