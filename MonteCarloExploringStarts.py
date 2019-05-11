import consts
from action import Action
from player import Player
from dealer import Dealer
from state import State
import random

from statistics import mean
import numpy as np


class MonteCarloExploringStarts:

    policy = {k: Action.STAND if k.player_sum >=
              19 else Action.HIT for k in consts.states}
    returns = {(k, a): [] for k in consts.states for a in list(Action)}
    Q = {k: {} for k in consts.states}

    def calculate(self, number=1000000):
        for i in range(0, number):
            self.estimate_one()
        return self.policy

    def estimate_one(self):
        episode, reward = self.generate_episode()
        for state, action in episode:
            self.returns[(state, action)].append(reward)
            self.Q[state][action] = mean(self.returns[(state, action)])

        for state, _ in episode:
            self.policy[state] = max(self.Q[state], key=self.Q[state].get)

    def generate_episode(self):
        """Generate episode using current policy

        Returns:
            list(state, action) -- List of pairs(state, action)
            int -- reward (1 or 0)
        """
        player = Player()
        dealer = Dealer()
        # State(player.sum, player.usable_ace, dealer.sum)
        current_state = random.choice(consts.states)
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
