from PlayerState import PlayerState
from EndState import EndState


class FoldState(PlayerState):

    def set_state(self, game, deck, hand, action):
        state = EndState()
        game.set_player_state(state)
        state.set_state(game, deck, hand, action)
