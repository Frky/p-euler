#-*- coding: utf-8 -*-

from src.p import Problem 

class Hand(object):
    """
        Object representing a poker hand (i.e. five cards)
        Contains methods to evaluate the hand and to compare to hands.

    """

    def __init__(self, hand):
        # a card is a tuple (value, color)
        self.hand = hand
        # set of possible values
        self.values = ['0', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 
                          'J', 'Q', 'K', 'A']
        # set of possible colors
        self.colors = ['S', 'H', 'C', 'D']
        # set of possible scores
        self.scores = ['H', 'P', 'TP', 'T', 'Fl', 'Fo', 'Fu', 'S', 'SFl', 'RFl']
        # sorting hand
        self.sort()
        self.highest = self.hand[0]
        self.lowest = self.hand[1]
        # definition of some fields for more info about the value
        self.full_cards = list()
        self.four_of = ''
        self.three_of = ''
        self.two_pairs_of = list()
        self.pair_of = list()
        return
    
    def highest_value(self):
        return self.highest[0]

    def lowest_value(self):
        return self.lowest[0]

    def sort(self):
        self.hand = sorted(self.hand, key=lambda a: -self.values.index(a[0]))

    def is_pair(self):
        for card in self.values:
            if [c[0] for c in self.hand].count(card) == 2:
                self.pair_of = card
                return True
        return False

    def is_two_pairs(self):
        pairs = list()
        for card in self.values:
            if [c[0] for c in self.hand].count(card) == 2:
                pairs.append(card)
        if len(pairs) == 2:
            self.two_pairs_of = sorted(pairs, key=lambda a: self.values.index(a))
            return True
        else:
            return False

    def is_three(self):
        for card in self.values:
            if len([c for c in self.hand if c[0] == card]) == 3:
                self.three_of = card
                return True
        return False

    def is_flush(self):
        return [color for card, color in self.hand].count(self.hand[0][1]) == len(self.hand)

    def is_four(self):
        for card in self.values:
            if [c[0] for c in self.hand].count(card) == 4:
                self.four_of = card
                return True
        return False

    def is_full(self):
        for card in self.values:
            if [c[0] for c in self.hand].count(card) == 3:
                second_card = [c[0] for c in self.hand if c[0] != card][0]
                if [c[0] for c in self.hand].count(second_card) == 2:
                    self.full_cards = [card, second_card]
                    return True
        return False

    def is_straight(self):
        ref_ind = self.values.index(self.hand[0][0])
        for k, card in enumerate(self.hand):
            if -k != self.values.index(card[0]) - ref_ind:
                return False
        return True
        # it is a straight if all values are different and there is a gap of 4 values between the highest and the lowest value
        return (len(list(set([c[0] for c in self.hand]))) == len(self.hand) and 
                    self.values.index(self.highest_value()) - self.values.index(self.lowest_value()) == 4)

    def is_straight_flush(self):
        # it is a straight flush if it is a flush and all colors are the same
        return self.is_straight() and len([c for c in self.hand if c == self.hand[0][1]]) == len(self.hand)

    def is_royal_flush(self):
        # it is a royal flush if it is a flush and the highest card is an A
        return self.is_straight_flush() and self.highest_value() == self.values[-1]
    
    def evaluate(self):
        if self.is_royal_flush():
            return 'RFl'
        elif self.is_straight_flush():
            return 'SFl'
        elif self.is_straight():
            return 'S'
        elif self.is_full():
            return 'Fu'
        elif self.is_four():
            return 'Fo'
        elif self.is_flush():
            return 'Fl'
        elif self.is_three():
            return 'T'
        elif self.is_two_pairs():
            return 'TP'
        elif self.is_pair():
            return 'P'
        else:
            return 'H'

    def __lt__(self, other_hand):
        hand_values = (self.scores.index(self.evaluate()), 
                            self.scores.index(other_hand.evaluate()))
        if hand_values[0] < hand_values[1]:
            return True
        elif hand_values[0] > hand_values[1]:
            return False
        else:
            if hand_values[0] == 0:
                return self.values.index(self.highest_value()) < self.values.index(other_hand.highest_value())
            elif hand_values[0] == 1:
                if self.values.index(self.pair_of) < self.values.index(other_hand.pair_of):
                    return True
                if self.values.index(self.pair_of) > self.values.index(other_hand.pair_of):
                    return False
                elif self.highest_value() != self.pair_of:
                    return self.values.index(self.highest_value()) < self.values.index(other_hand.highest_value())
                else:
                    raise NotImplemented
            else:
                raise NotImplemented

class p54(Problem):

        """
            In the card game poker, a hand consists of five cards and are 
            ranked, from lowest to highest, in the following way:
            
                High Card: Highest value card.
                One Pair: Two cards of the same value.
                Two Pairs: Two different pairs.
                Three of a Kind: Three cards of the same value.
                Straight: All cards are consecutive values.
                Flush: All cards of the same suit.
                Full House: Three of a kind and a pair.
                Four of a Kind: Four cards of the same value.
                Straight Flush: All cards are consecutive values of same suit.
                Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

            The cards are valued in the order:
            2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
            
            If two players have the same ranked hands then the rank made up of 
            the highest value wins; for example, a pair of eights beats a pair 
            of fives (see example 1 below). But if two ranks tie, for example, 
            both players have a pair of queens, then highest cards in each hand
            are compared (see example 4 below); if the highest cards tie then 
            the next highest cards are compared, and so on.
            
            Consider the following five hands dealt to two players:
            
                Hand    Player 1                Player 2            Winner
    
                1       5H 5C 6S 7S KD          2C 3S 8S 8D TD      2
                        Pair of Fives           Pair of Eights
                   
                2       5D 8C 9S JS AC          2C 5C 7D 8S QH      1
                        Highest card Ace        Highest card Queen
    
                3       2D 9C AS AH AC          3D 6D 7D TD QD      2
                        Three Aces              Flush with Diamonds
    
                4       4D 6S 9H QH QC          3D 6D 7H QD QS      1
                        Pair of Queens          Pair of Queens
                        Highest card Nine       Highest card Seven
    
                5       2H 2D 4C 4D 4S          3C 3D 3S 9S 9D      1
                        Full House              Full House
                        With Three Fours        With Three Threes
    
            The file, poker.txt, contains one-thousand random hands dealt to two 
            players. Each line of the file contains ten cards (separated by a 
            single space): the first five are Player 1's cards and the last five 
            are Player 2's cards. You can assume that all hands are valid (no 
            invalid characters or repeated cards), each player's hand is in no 
            specific order, and in each hand there is a clear winner.
            
            How many hands does Player 1 win?

        """

        def __init__(self, id):
            self.data = list()
            return super(p54, self).__init__(id)

        def parse_file(self, file_path):
            with open(file_path, 'r') as f:
                for line in f.readlines():
                    cards = line[:-1].split(" ")
                    hand_p1 = list()
                    hand_p2 = list()
                    for i, card_colored in enumerate(cards):
                        card = card_colored[0]
                        color = card_colored[1]
                        if i < 5:
                            hand_p1.append((card, color))
                        else:
                            hand_p2.append((card, color))
                    self.data.append((hand_p1, hand_p2))


        def solve(self):
            self.parse_file("data/p54.txt")
            res = 0
            for nround in self.data:
                hand_p1 = Hand(nround[0])
                hand_p2 = Hand(nround[1])
                if hand_p1 > hand_p2:
                    res += 1
            return res
            
