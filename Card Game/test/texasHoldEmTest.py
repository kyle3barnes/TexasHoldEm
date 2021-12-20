import unittest
from texasHoldEm import TexasHoldEm
from PlayingCard import PlayingCard
from ConsoleInput import ConsoleInput


class TexasHoldEmTest(unittest.TestCase):
    playingCard = PlayingCard()
    texas = TexasHoldEm()
    input = ConsoleInput()
    hands, table_cards = texas.deal_cards()

    def test_hands(self):
        self.assertEqual(2, len(self.hands))

    def test_initial_table_card(self):
        self.assertEqual(3, len(self.table_cards))

    def test_play_game(self):
        fold = self.texas.play_game(self.hands, self.table_cards)
        self.assertTrue(fold in ["F", "C"])

    def test_get_win_rank(self):
        self.assertEqual(int(self.input.get_string("leave blank for false or enter any character for true\nwin rank: ")),
                         self.texas.get_win_rank(
                             (bool(self.input.get_string("suit: "))),
                             (bool(self.input.get_string("straight: "))),
                             (bool(self.input.get_string("four pair: "))),
                             (bool(self.input.get_string("three pair: "))),
                             (bool(self.input.get_string("pair: "))),
                             (int(self.input.get_string("no of pairs: "))),
                         ))

    def test_determine_winner(self):



if __name__ == '__main__':
    unittest.main()
