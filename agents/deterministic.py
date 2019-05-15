from utils.state import State, states
from game.action import Action
from .agent import Agent


class Deterministic(Agent):

    def __init__(self,  *_, **__):
        pass

    def calculate(self, _=0):
        policy = {}
        for s in states:
            if s.player_usable_ace:
                if s.player_sum <= 17:
                    policy[s] = Action.HIT
                elif s.player_sum == 18 and s.dealer_card >= 9:
                    policy[s] = Action.HIT
                else:
                    policy[s] = Action.STAND
            else:
                if s.player_sum <= 16 and s.dealer_card >= 7:
                    policy[s] = Action.HIT
                elif s.player_sum <= 12 and s.dealer_card <= 3:
                    policy[s] = Action.HIT
                else:
                    policy[s] = Action.STAND
        return policy
