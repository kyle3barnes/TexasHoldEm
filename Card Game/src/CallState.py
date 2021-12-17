from PlayerState import PlayerState
from EndState import EndState
from FoldState import FoldState
from TexasAction import TexasAction


class CallState(PlayerState):

    def set_state(self, game, deck, hand, action):
        game.deal_to_player(deck, hand)
        game.output.display(hand)
        if game.score_hand(hand) > game.winning_score:
            state = EndState()
        action = game.valid_deal_input()
        if action == TexasAction.CALL[0]:
            state = CallState()
        elif action == TexasAction.FOLD[0]:
            state = FoldState()
        game.set_player_state(state)
        state.set_state(game, deck, hand, action)