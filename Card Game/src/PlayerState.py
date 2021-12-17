from abc import ABC, abstractmethod


class PlayerState(ABC):
    def set_state(self, game, deck, hand, action):
        pass
