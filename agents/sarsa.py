from game.dealer import Dealer
from game.player import Player
import numpy as np
from statistics import mean
from utils.state import State, states
from .agent import Agent
from game.action import Action
import random


class Sarsa(Agent):

    policy = {k: Action.STAND if k.player_sum >=
              19 else Action.HIT for k in states}
    returns = {(k, a): [] for k in states for a in list(Action)}
    Q = {k: {} for k in states}
    ALPHA = 0.1

    def __init__(self):
        for k in states:
            for a in list(Action):
                self.Q[k][a] = 0.0

    def calculate(self, number=1000000):
        """Estimate many times

        Keyword Arguments:
            number {int} -- Number of times to estimate (default: {1000000})

        Returns:
            Dictionary -- Estimated policy
        """
        for i in range(0, number):
            self.estimate_one()
        return self.policy

    def get_best_action(self, state, from_where=None):
        if from_where is None:
            from_where = self.Q
        return max(self.Q[state], key=self.Q[state].get)


    def estimate_one(self):
        episode, reward = self.generate_episode()
        for i in range(0, len(episode)-1):
            current_state = episode[i][0]
            current_action = episode[i][1]

            next_state = episode[i+1][0]
            next_action = episode[i+1][1]

            # print(self.Q[current_state][current_action])
            # print(self.Q[next_state][next_action])

            diff = self.Q[current_state][current_action] - \
                self.Q[next_state][next_action]

            self.Q[current_state][current_action] += self.ALPHA*((reward if i == len(episode) - 2 else 0) +
                                                                 diff)

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

        current_state = random.choice(states)
        current_action = self.get_best_action(current_state)

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
