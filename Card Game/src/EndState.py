from PlayerState import PlayerState

class EndState(PlayerState):
    def set_state(self, game, deck, hand, action):
        game.output.display("End")