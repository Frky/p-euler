#-*- coding: utf-8 -*-

from p import Problem

class p17(Problem):

    """
        If the numbers 1 to 5 are written out in words: one, two, three, four, five, then 
        there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

        If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
        how many letters would be used?

        NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
        contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
        "and" when writing out numbers is in compliance with British usage.

    """

    def unit(self, i):
        """
            Retourne le nombre de lettres nécessaires à l'écriture d'un nombre compris entre 0 et 9.

        """
        # case where the unit is zero
        if (i == 0):
            return 0
        # one, two, six
        elif (i == 1 or i == 2 or i == 6):
            return 3
        # four, five, nine
        elif (i == 4 or i == 5 or i == 9):
            return 4
        # three, seven, eight
        elif (i == 3 or i == 7 or i == 8):
            return 5


    def dizain(self, i):
        """
            Retourne le nombre de lettres nécessaires à l'écriture d'un nombre compris entre 1 et 99

        """
        if (i > 99):
            print("Error.")
            return
        if (i >= 80):
            # ninety : 6 letters
            # eighty : 6 letters
            return 6 + self.unit(i % 10)
        elif (i >= 70):
            # seventy : 7 letters
            return 7 + self.unit(i % 10)
        elif (i >= 40):
            # sixty : 5 letters
            # fifty : 5 letters
            # forty : 5 letters
            return 5 + self.unit(i % 10)
        elif (i >= 20):
            # thirty : 6 letters
            # twenty : 6 letters
            return 6 + self.unit(i % 10)
        elif (i >= 10):
            if (i == 10):
                # ten : 3 letters
                return 3
            if (i == 11 or i == 12):
                # eleven : 6 letters
                # twelve : 6 letters
                return 6
            elif (i == 13 or i == 14 or i == 18 or i == 19):
                # thirteen : 8 letters
                # fourteen : 8 letters
                # eighteen : 8 letters
                # nineteen : 8 letters
                return 8 
            elif (i == 15 or i == 16):
                # fifteen : 7 letters
                # sixteen :  7 letters
                return 7
            else:
                # seventeen : 9 letters
                return 9
        else:
            return self.unit(i)


    def hundred(self, i):
        """
            Retourne le nombre de lettres nécessaires à l'écriture d'un nombre compris entre 1 et 999

        """
        # hundred : 7 letters
        if (i > 999):
            print("Error")
            return 
        if (i < 100):
            return self.dizain(i)
        elif (i % 100 == 0):
            return self.unit(i/100) + 7
        else:
            return self.unit(i/100) + 10 + self.dizain(i % 100)


    def nb_letters(self, i):
        """
            Retourne le nombre de lettres nécessaires à l'écriture d'un nombre quelconque

        """
        if (i > 1000):
            print("Error.")
            return
        if i == 1000:
            # one thousand : 11 letters
            return 11
        else:
            return self.hundred(i)


    def solve(self):
        return sum([self.nb_letters(i) for i in xrange(1001)])
