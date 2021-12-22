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
        int(self.input.get_string("leave blank for false or enter any character for true\nwin rank: ")),
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

    def test_game_rules(self):
        test_inputs = []
        hand = []
        table_cards = []
        rule_type_to_test = self.input.get_string(
            "Enter the rule type you would like to test ('SU' for same suit, 'S' for straight, 'F' for four pair, 'T' for three pair, and 'P' for pair: ")
        test_inputs.append(bool(self.input.get_string("Enter desired result (T for True or leave blank for False): ")))

        for i in range(2):
            hand.append(self.input.get_string("Enter card for test hand: "))

        counter = self.input.get_string("Enter how many cards for test table cards: ")
        for i in range(int(counter)):
            table_cards.append(self.input.get_string("Enter card for test table cards: "))

        test_inputs.append(hand)
        test_inputs.append(table_cards)

        self.test_input.set_test_inputs(test_inputs)

        desired_result = self.test_input.get_string()
        hand = self.test_input.get_string()
        table_cards = self.test_input.get_string()

        same_suit, straight, four_pair, three_pair, pair, number_of_pairs = self.texas.game_rules(hand, table_cards)
        if rule_type_to_test == "SU":
            self.assertEqual(desired_result, same_suit)
        elif rule_type_to_test == "S":
            self.assertEqual(desired_result, straight)
        elif rule_type_to_test == "F":
            self.assertEqual(desired_result, four_pair)
        elif rule_type_to_test == "T":
            self.assertEqual(desired_result, three_pair)
        elif rule_type_to_test == "P":
            self.assertEqual(desired_result, pair)

    def test_get_card_number_list(self):
        desired_list = []
        hand = []
        table_cards = []

        counter = self.input.get_string("Enter how many cards: ")
        for i in range(int(counter)):
            desired_list.append(int(self.input.get_string("Enter card number for desired list: ")))

        for i in range(2):
            hand.append(self.input.get_string("Enter card for test hand: "))

        for i in range(int(counter)-2):
            table_cards.append(self.input.get_string("Enter card for test table cards: "))

        self.assertEqual(desired_list, self.texas.get_card_number_list(hand, table_cards))

    def test_suit_check(self):
        test_inputs = []
        table_cards = []
        test_inputs.append(bool(self.input.get_string("Enter desired result (T for True or leave blank for False): ")))

        for i in range(2):
            test_inputs.append(self.input.get_string("Enter card: "))

        counter = int(self.input.get_string("Enter number of table cards: "))
        for i in range(counter):
            test_inputs.append(self.input.get_string("Enter table card: "))

        self.test_input.set_test_inputs(test_inputs)

        desired_result = self.test_input.get_string()
        card1 = self.test_input.get_string()
        card2 = self.test_input.get_string()
        for i in range(len(self.test_input.test_inputs)):
            table_cards.append(self.test_input.test_inputs[i])
        actual_result = self.texas.suit_check([card1, card2], table_cards)

        self.assertEqual(desired_result, actual_result)

    def test_straight_check(self):
        test_inputs = []
        straight_list = []
        test_inputs.append(bool(self.input.get_string("Enter desired result (T for True or leave blank for False): ")))

        counter = int(self.input.get_string("Enter how many card you would like to test with (MIN: 5, MAX: 7): "))
        for i in range(counter):
            test_inputs.append(int(self.input.get_string("Enter card number: ")))

        self.test_input.set_test_inputs(test_inputs)

        desired_result = self.test_input.get_string()
        for i in range(counter):
            straight_list.append(self.test_input.get_string())

        self.assertEqual(desired_result, self.texas.straight_check(straight_list))

    def test_pair_check(self):
        test_inputs = []
        number_list = []
        pair_type_to_test = self.input.get_string("Enter the pair type you would like to test ('F' for four pair, 'T' for three pair, and 'P' for pair: ")
        test_inputs.append(bool(self.input.get_string("Enter desired result (T for True or leave blank for False): ")))

        counter = int(self.input.get_string("Enter how many card you would like to test with (MIN: 5, MAX: 7): "))
        for i in range(counter):
            test_inputs.append(int(self.input.get_string("Enter card number: ")))

        self.test_input.set_test_inputs(test_inputs)

        desired_result = self.test_input.get_string()
        for i in range(counter):
            number_list.append(self.test_input.get_string())

        four_pair, three_pair, pair, number_of_pairs = self.texas.pair_check(number_list)

        if pair_type_to_test == "F":
            self.assertEqual(desired_result, four_pair)
        elif pair_type_to_test == "T":
            self.assertEqual(desired_result, three_pair)
        elif pair_type_to_test == "P":
            self.assertEqual(desired_result, pair)


if __name__ == '__main__':
    unittest.main()
