import unittest
from texasHoldEm import TexasHoldEm
from PlayingCard import PlayingCard


class TexasHoldEmTest(unittest.TestCase):
    playingCard = PlayingCard()

    def test_hands(self):
        hands, table_cards = TexasHoldEm.dealCards(self)
        self.assertEqual(2, len(hands))

    def test_table_card(self):
        hands, table_cards = TexasHoldEm.dealCards(self)
        self.assertEqual(1, len(table_cards))

    def test_play_game(self):
        hands, table_cards = TexasHoldEm.dealCards(self)
        self.assertEqual("F", TexasHoldEm.playGame(self, hands, table_cards))


if __name__ == '__main__':
    unittest.main()