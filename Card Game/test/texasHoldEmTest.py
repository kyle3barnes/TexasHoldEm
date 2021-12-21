import unittest
from texasHoldEm import TexasHoldEm
from PlayingCard import PlayingCard
from ConsoleInput import ConsoleInput
from TestInput import TestInput


class TexasHoldEmTest(unittest.TestCase):
    playingCard = PlayingCard()
    texas = TexasHoldEm()
    input = ConsoleInput()
    hands, table_cards = texas.deal_cards()
    test_input = TestInput()

    def test_hands(self):
        self.assertEqual(2, len(self.hands))

    def test_initial_table_card(self):
        self.assertEqual(3, len(self.table_cards))

    def test_play_game(self):
        fold = self.texas.play_game(self.hands, self.table_cards)
        self.assertTrue(fold in ["F", "C"])

    def test_get_win_rank(self):
        self.assertEqual(
            int(self.test_input.get_string("leave blank for false or enter any character for true\nwin rank: ")),
            self.texas.get_win_rank(
                (bool(self.input.get_string("suit: "))),
                (bool(self.input.get_string("straight: "))),
                (bool(self.input.get_string("four pair: "))),
                (bool(self.input.get_string("three pair: "))),
                (bool(self.input.get_string("pair: "))),
                (int(self.input.get_string("no of pairs: "))),
            ))

    def test_determine_winner(self):
        win_rank_to_test = self.input.get_string("Enter win rank to test: ")
        hands = []
        table_cards = []

        for i in range(2):
            hand = self.input.get_string("Enter card for hand: ")
            hands.append(hand)

        counter = self.input.get_string("Enter how many table cards: ")
        for i in range(int(counter)):
            tab_card = self.input.get_string("Enter card for table cards: ")
            table_cards.append(tab_card)

        user_win_rank, comp_win_rank, win_ranks = self.texas.determine_winner([hands, ["HK", "C2"]], table_cards)

        self.assertEqual(int(win_rank_to_test), user_win_rank)

    def test_suit_check(self):
        test_inputs = []
        table_cards = []
        win_rank = bool(self.input.get_string("Enter desired result (T for True or leave blank for False): "))
        test_inputs.append(win_rank)

        for i in range(2):
            card = self.input.get_string("Enter card: ")
            test_inputs.append(card)

        counter = int(self.input.get_string("Enter number of table cards: "))
        for i in range(counter):
            table_card = self.input.get_string("Enter table card: ")
            test_inputs.append(table_card)

        self.test_input.set_test_inputs(test_inputs)

        for i in range(len(self.test_input.test_inputs)):
            table_cards.append(self.test_input.test_inputs[i])

        self.assertEqual(self.test_input.get_string(), self.texas.suit_check([self.test_input.get_string(), self.test_input.get_string()], table_cards))


if __name__ == '__main__':
    unittest.main()
