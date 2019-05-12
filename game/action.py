from enum import Enum


class Action(Enum):
    HIT = 0
    STAND = 1

    def __int__(self):
        return self.value
