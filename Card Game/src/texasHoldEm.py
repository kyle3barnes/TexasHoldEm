from ConsoleInput import ConsoleInput
from ConsoleOutput import ConsoleOutput
from PlayingCard import PlayingCard


class TexasHoldEm:
    playingCard = PlayingCard()
    input = ConsoleInput()
    output = ConsoleOutput()

    def set_input(self, input):
        self.input = input

    def deal_cards(self):
        deck = self.playingCard.generate_deck()
        deck = self.playingCard.shuffle_cards(deck)
        hands = self.playingCard.deal_cards(deck, 2, 2)
        table_cards = self.playingCard.deal_cards(deck, 5, 1)
        return hands, table_cards

    def play_game(self, hands, table_cards):
        fold = "F"
        print("Your hand: " + str(hands[0]) + "  " + "Computers hand: " + str(
            hands[1]))
        print()
        print("Card " + str(1) + ": " + table_cards[0][0])
        print("Card " + str(2) + ": " + table_cards[0][1])
        for i in range(2, len(table_cards[0])):
            print(
                "Card " + str(i + 1) + ": " + table_cards[0][i])
            if i == len(table_cards[0]) - 1:
                break
            fold = self.input.get_string("Would you like to (C)all or (F)old? ")
            while fold not in ["F", "f", "C", "c"]:
                fold = self.input.get_string("Error, enter 'C' for call or 'F' for fold: ")
            if fold == "F" or fold == "f":
                break
            print()
        return fold

    def determine_winner(self, hands, table_cards):
        user_hand = hands[0]
        comp_hand = hands[1]

        win_ranks = {1: "Straight Flush",
                     2: "Four of a Kind",
                     3: "Full House",
                     4: "Flush",
                     5: "Straight",
                     6: "Three of a Kind",
                     7: "Two Pair",
                     8: "Pair",
                     9: "Highest Card"}

        same_suit, straight, four_pair, three_pair, pair, number_of_pairs = self.game_rules(user_hand, table_cards)

        comp_win_rank = self.get_win_rank(same_suit, straight, four_pair, three_pair, pair,
                                          number_of_pairs)

        same_suit, straight, four_pair, three_pair, pair, number_of_pairs = self.game_rules(comp_hand, table_cards)

        user_win_rank = self.get_win_rank(same_suit, straight, four_pair, three_pair, pair,
                                          number_of_pairs)

        return user_win_rank, comp_win_rank, win_ranks

    @staticmethod
    def get_win_rank(same_suit, straight, four_pair, three_pair, pair, number_of_pairs):
        if same_suit and straight:
            win = 1
        elif four_pair:
            win = 2
        elif three_pair and pair:
            win = 3
        elif same_suit:
            win = 4
        elif straight:
            win = 5
        elif three_pair:
            win = 6
        elif pair and number_of_pairs == 2:
            win = 7
        elif pair:
            win = 8
        else:
            win = 9
        return win

    def game_rules(self, hand, table_cards):
        same_suit = self.suit_check(hand, table_cards)

        straight = self.straight_check(hand)

        four_pair, three_pair, pair, number_of_pairs = self.pair_check(hand)

        return same_suit, straight, four_pair, three_pair, pair, number_of_pairs

    def get_card_number_list(self, hand, table_cards):
        number_list = []

        for x in range(len(hand)):
            number_list.append(hand[x])
        for x in range(len(table_cards[0])):
            number_list.append(table_cards[0][x])

        self.playingCard.convert_faces_to_numbers(number_list)

        for i in range(len(number_list)):
            number_list[i] = int(number_list[i][1:len(number_list[i])])

        number_list.sort()

        return number_list

    @staticmethod
    def suit_check(hand, table_cards):
        suit_counter = 0
        same_suit = False
        for x in range(len(hand)):
            for i in range(len(table_cards[0])):
                if hand[x][0:1] == table_cards[0][i][0:1]:
                    suit_counter += 1
            if suit_counter == 5:
                same_suit = True

        return same_suit

    @staticmethod
    def straight_check(straight_list):
        num_counter = 0
        straight = False
        for i in range(len(straight_list) - 1):
            if straight_list[i + 1] == (straight_list[i]):
                num_counter += 1
        if num_counter >= 5:
            straight = True

        return straight

    @staticmethod
    def pair_check(number_list):
        pair = False
        four_pair = False
        three_pair = False

        pair_dict = {i: number_list.count(i) for i in number_list if number_list.count(
            i) != 1}

        pair_values = list(pair_dict.values())

        number_of_pairs = len(pair_values)

        if len(pair_dict) == 0:
            pair = False
        else:
            for pairNumber in pair_values:
                if pairNumber == 4:
                    four_pair = True
                elif pairNumber == 3:
                    three_pair = True
                else:
                    pair = True
        return four_pair, three_pair, pair, number_of_pairs

    def display_winner(self, user_win_rank, comp_win_rank, win_ranks):
        print(user_win_rank, comp_win_rank)
        if user_win_rank > comp_win_rank:
            self.output.display("Congratulations, you have won with a " + win_ranks.get(
                user_win_rank))
        elif user_win_rank < comp_win_rank:
            self.output.display("Sorry, the computer won with a " + win_ranks.get(comp_win_rank))
        else:
            self.output.display("Draw! You both have a " + win_ranks.get(user_win_rank))

    def main(self):
        play_again = "Y"
        while play_again == "Y" or play_again == "y":
            hands, table_cards = self.deal_cards()
            fold = self.play_game(hands, table_cards)
            if fold != "F" or fold != "f":
                user_win_rank, comp_win_rank, win_ranks = self.determine_winner(hands, table_cards)
                self.display_winner(user_win_rank, comp_win_rank, win_ranks)
            play_again = self.input.get_string("Would you like to play again? (Y)es or (N)o: ")


if __name__ == "__main__":
    texas_hold_em = TexasHoldEm()
    texas_hold_em.main()
